# this script is used to pull drug target fasta from uniprot.org
import pandas as pd
import math

data = pd.read_csv("drug_info.csv")
targets = data['target'].tolist()
target_set = set()

for target in targets:
    if isinstance(target, str):
        ts = target.split('|')
        for t in ts:
            target_set.add(t)
            
#print(len(target_set))
#print(target_set)

import requests as r
from Bio import SeqIO
from io import StringIO
import msvcrt
import os

baseUrl="http://www.uniprot.org/uniprot/"
ct = 0
for cID in target_set:
    ct += 1
    if os.path.exists("drugbank_target/"+cID+".fasta"):
        continue
    currentUrl=baseUrl+cID+".fasta"
    response = r.post(currentUrl)
    cData=''.join(response.text)
    #print(cData)
    Seq=StringIO(cData)
    #print(Seq)
    pSeq=list(SeqIO.parse(Seq,'fasta'))
    #print(pSeq[0])
    #print(pSeq[0].id)
    #print(pSeq[0].seq)
    if len(pSeq) > 1:
        print("WARN: long pSeq")
        print(pSeq)
        #msvcrt.getch()
    if len(pSeq) == 0:
        continue

    print(str(ct) + " " + cID)
    with open("drugbank_target/"+cID+".fasta", "w+") as f:
        try:
            if cID != pSeq[0].id.split('|')[1]:
                print("ERROR: mismatch in cID")
                print(cID)
                print(pSeq[0])
                #msvcrt.getch()
        except IndexError:
            print("ERROR: pSeq cID wrong pattern")
            print(pSeq)
            continue
            #msvcrt.getch()
        f.write(">"+cID+"\n")
        f.write(str(pSeq[0].seq))