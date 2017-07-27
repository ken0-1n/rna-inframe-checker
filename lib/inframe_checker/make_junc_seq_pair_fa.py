#
# Copyright Human Genome Center, Institute of Medical Science, the University of Tokyo
# @since 2012
#

# use List::Util qw(min max);
# use strict;

import sys
from pyfasta import Fasta

class MakeJuncSeq:
    
    def reverse_complement(self, dna):
        complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
        return ''.join([complement[base] for base in dna[::-1]])
    
    def get_seq(self,chrom,pos,strand,f):
        start = 0
        end = 0
        if strand == "+":
            start = pos-48
            end = pos
        elif strand == "-":
            start = pos-1
            end = pos+47
        seq = f[chrom][start:end]
        return seq
    
    def main(self, input_junc, ref_fasta, output):
        hResult = open(output, 'w')
        f = Fasta(ref_fasta)
        with open(input_junc,"r") as hin:
            for line in hin:
                line = line.rstrip('\n').rstrip('\r')
                F = line.split('\t')
                chr1 = F[0]
                pos1 = int(F[1])
                strand1 = F[2]
                seq1 = self.get_seq(chr1,pos1,strand1,f)
                if strand1 == "-":
                  seq1 = self.reverse_complement(seq1)
        
                chr2 = F[3]
                pos2 = int(F[4])
                strand2 = F[5]
                seq2 = self.get_seq(chr2,pos2,strand2,f)
                if strand2 == "+":
                    seq2 = self.reverse_complement(seq2)
        
                name = chr1+":"+strand1+str(pos1)+"-"+chr2+":"+strand2+str(pos2)
                print >> hResult, ">"+name+"_contig1"
                print >> hResult, seq1
                print >> hResult, ">"+name+"_contig2"
                print >> hResult, seq2
        hResult.close()
        
