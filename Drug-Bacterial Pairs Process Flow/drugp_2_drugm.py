################
# This script is used to calculate similarity for each pair of drug metric and bacteria metric,
# and use a min heap to cut off the pairs that have top 0.01% similarity for statistical analysis 
################

import os
import torch
import numpy
import tensorflow as tf

from dataclasses import dataclass
from heapq import heappush, heappushpop

@dataclass
class PytorchFile:
    label: str
    tensor: torch.FloatTensor

@dataclass(order=True)
class TensorPair:
    diff: numpy.float32
    label_drug: str
    label_bacteria: str


# read in drugbank data
path = '/path/to/drugbank_pytorch'
drugbank_tensor_list = []
for filename in os.listdir(path):
    filepath=os.path.join(path, filename)
    pt_file = torch.load(filepath)
    pf = PytorchFile(pt_file['label'], pt_file['mean_representations'][33])
    drugbank_tensor_list.append(pf)


# read in bacteria data, per strain
geno1_path = '/path/to/geno1_pytorch/'
geno1_name_list = os.listdir(geno1_path)
geno1_name_list.sort()

stat = [0]*101
HEAPSIZE = 15

for geno1_name in geno1_name_list:
    print(geno1_name)
    path = geno1_path + geno1_name
    geno1_tensor_list = []
    for filename in os.listdir(path):
        filepath=os.path.join(path, filename)
        # read in the pytorch file, get label and last round of mean_representations
        pt_file = torch.load(filepath)
        pf = PytorchFile(pt_file['label'], pt_file['mean_representations'][33])
        geno1_tensor_list.append(pf)

    # use min heap to maintain top cut of drug-bacteria pairs
    pq = []
    HEAPSIZE = max(15, int(len(geno1_tensor_list) * len(drugbank_tensor_list) * 0.0001))

    # calculate cosine similarity between two tensors
    for geno in geno1_tensor_list:
        for drug in drugbank_tensor_list:
            diff =  tf.keras.metrics.CosineSimilarity()(geno.tensor, drug.tensor)
            stat[int(diff.numpy()*100)]+= 1
            if len(pq) < HEAPSIZE:
                heappush(pq, TensorPair(diff.numpy(), drug.label, geno.label))
            else:
                if diff.numpy() > pq[0].diff:
                    heappushpop(pq, TensorPair(diff.numpy(), drug.label, geno.label))

    for pair in pq:
        print(pair)
print(stat)
