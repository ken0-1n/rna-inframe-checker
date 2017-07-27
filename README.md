# rna-inrame-checker 

## Introduction

## Dependency

### Python
Python (>= 2.7) , pyfasta packages.

### Software
[blat](https://genome.ucsc.edu/FAQ/FAQblat.html)

## Install

type the following command
```
git clone https://github.com/ken0-1n/rna-inframe-checker.git
python setup.py install
```

Then, install the package by standard python package protocol (https://docs.python.org/2/install/)
```
cd rna-inframe-checker
python setup.py build install
```

## Preparation

-input junction file
1. chromosome for the 1st breakpoint
1. coordinate for the 1st breakpoint
1. direction of the 1st breakpoint
1. chromosome for the 2nd breakpoint
1. coordinate for the 2nd breakpoint
1. direction of the 2nd breakpoint

## Commands

```
usage: inframe_checker inframe [-h] -a ALL_GENE -r REF_GENE -c CODING_INFO -b BLAT_PATH [-p BLAT_PARAMS] -i INPUT_JUNC -o OUTPUT_DIR
```


## Results
