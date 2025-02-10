#!/bin/bash

# this script is using ESMExtract model to convert bacteria target data(fasta) to embedded vector
FILES=/path/to/geno1_target/*
echo ${#FILES[@]}

INDEX=0

# for each strain, for each target data file, extract file name
# use strain name to create target directory name
# use ESMExtract to save the result to the same target file name
for f in $FILES
do
  filename=$(echo "$f" | sed -r "s/.+\/(.+)\..+/\1/")
  targetdir=/path/to/geno1_pytorch/"$filename"
  if [ ! -d "$targetdir" ]; then
    echo "#""$INDEX"
    ((INDEX+=1))
    echo "$filename"
    mkdir /path/to/geno1_pytorch/"$filename"
    python esm/scripts/extract.py esm2_t33_650M_UR50D "$f" geno1_pytorch/"$filename" --repr_layers 33 --include mean
  fi
done