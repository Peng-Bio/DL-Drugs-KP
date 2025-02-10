#!/bin/bash

# this script is using ESMExtract model to convert drug target data(fasta) to embedded vector
FILES=/path/to/drugbank_target/*
echo ${#FILES[@]}

INDEX=0

# for each file, extract file name, create target file name and use ESMExtract to save the result to target file name
for f in $FILES
do
  filename=$(echo "$f" | sed -r "s/.+\/(.+)\..+/\1/")
  targetfile=/path/to/drugbank_pytorch/"$filename".pt
  if [ ! -f "$targetfile" ]; then
    echo "#""$INDEX"
    ((INDEX+=1))
    echo "$filename"
    python esm/scripts/extract.py esm2_t33_650M_UR50D "$f" drugbank_pytorch --repr_layers 33 --include mean
  fi
done