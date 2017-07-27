# rna-inrame-checker 

## Introduction

## Dependency

### Python
Python (>= 2.7) , pyfasta packages.

### Software
[blat](https://genome.ucsc.edu/FAQ/FAQblat.html)

### database
hg19.fasta
[refGene.txt, knownGene.txt and ensGene.txt](http://hgdownload.cse.ucsc.edu/goldenpath/hg19/database/)

## Install

Please, ｔype the following command
```
git clone https://github.com/ken0-1n/rna-inframe-checker.git
python setup.py install
```

Then, install the package by standard python package protocol
```
cd rna-inframe-checker
python setup.py build install
```

## Preparation

### input file
Prepare the list of fusion junctions (The command input file).
1. chromosome for the 1st breakpoint
1. coordinate for the 1st breakpoint
1. direction of the 1st breakpoint
1. chromosome for the 2nd breakpoint
1. coordinate for the 2nd breakpoint
1. direction of the 2nd breakpoint

### database
ALL_GENE
CODING_INFO

## Commands

```
usage: inframe_checker inframe [-h] -a ALL_GENE -r REF_GENE -c CODING_INFO -b BLAT_PATH [-p BLAT_PARAMS] -i INPUT_FILE -o OUTPUT_DIR
```

## Results
