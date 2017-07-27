#
# Copyright Human Genome Center, Institute of Medical Science, the University of Tokyo
# @since 2012
#

# use List::Util qw(min max);
# use strict;

import sys

class Psl2inframe:

    def __init__(self):
        self.gene2coding_start = {}
        self.gene2coding_end = {}
        self.gene2coding_strand = {}
        self.key2score1 = {}
        self.key2line1 = {}
        self.key2score2 = {}
        self.key2line2 = {}


    def set_gene_dict(self, input_coding):

        with open(input_coding,'r') as hin:
            for line in hin:
                line = line.rstrip('\n').rstrip('\r')
                F = line.split('\t')
                self.gene2coding_start[F[3]] = F[1]
                self.gene2coding_end[F[3]] = F[2]
                self.gene2coding_strand[F[3]] = F[5]


    def set_key_dict(self, input_psl):

        with open(input_psl,"r") as hin:
            for line in hin:
                line = line.rstrip('\n').rstrip('\r')
                F = line.split('\t')

                if not F[0].isdigit(): continue

                line_out = ""
                if F[9].endswith("contig1") and (int(F[10]) - int(F[12])) < 5:
                    
                    if F[8] == "+":
                        line_out = F[13] + ":" + "+" + str(int(F[16]) + int(F[10]) - int(F[12]))
                    else:
                        line_out = F[13] + ":" + "-" + str(int(F[15]) + int(F[10]) - int(F[12]) + 1)

                elif F[9].endswith("contig2") and int(F[11]) < 5:

                    if F[8] == "+":
                        line_out = F[13] + ":" + "-" + str(int(F[15]) + int(F[11]) + 1)
                    else:
                        line_out = F[13] + ":" + "+" + str(int(F[16]) + int(F[11]))

                else:
                    continue
                

                if F[9].endswith("contig1"):
                    replaced_name = F[9].replace('_contig1', '')
                    
                    if not replaced_name in self.key2score1 or int(F[0]) > int(self.key2score1[replaced_name]):
                        self.key2score1[replaced_name] = F[0]
                        if replaced_name in self.key2line1:
                            del self.key2line1[replaced_name]

                    if not replaced_name in self.key2line1:
                        self.key2line1[replaced_name] = line_out
                    else:
                        self.key2line1[replaced_name] = self.key2line1[replaced_name] + ";" + line_out

                if F[9].endswith("contig2"):
                    replaced_name = F[9].replace('_contig2', '')
                
                    if not replaced_name in self.key2score2 or int(F[0]) > int(self.key2score2[replaced_name]):
                        self.key2score2[replaced_name] = F[0]
                        if replaced_name in self.key2line2:
                            del self.key2line2[replaced_name]
                
                    if not replaced_name in self.key2line2:
                        self.key2line2[replaced_name] = line_out
                    else:
                        self.key2line2[replaced_name] = self.key2line2[replaced_name] + ";" + line_out


    def print_inframe(self, output):
        comb2inframe = {}
        for key, value in sorted(self.key2line1.items()):
        
            if key not in self.key2line2: continue
        
            self.key2line1values = self.key2line1[key].split(';')
            self.key2line2values = self.key2line2[key].split(';')
            for value1 in self.key2line1values:
                for value2 in self.key2line2values:
        
                    values1 = value1.split(':')
                    gene1 = values1[0]
                    dir1  = values1[1][0:1]
                    pos1  = values1[1][1:]
        
                    values2 = value2.split(':')
                    gene2 = values2[0]
                    dir2  = values2[1][0:1]
                    pos2  = values2[1][1:]
        
                    if (self.gene2coding_start[gene1] == self.gene2coding_end[gene1]): continue 
                    if (self.gene2coding_start[gene2] == self.gene2coding_end[gene2]): continue
                    
                    cdir1 = "+" if dir1 == self.gene2coding_strand[gene1] else "-"
                    cpos1 = 0
                    if self.gene2coding_strand[gene1] == "+":
                        cpos1 = int(pos1) - int(self.gene2coding_start[gene1])
                    else:
                        cpos1 = int(self.gene2coding_end[gene1]) - int(pos1)
        
                    cdir2 = "+" if dir2 == self.gene2coding_strand[gene2] else "-"
                    cpos2 = 0
                    if self.gene2coding_strand[gene2] == "+":
                        cpos2 = int(pos2) - int(self.gene2coding_start[gene2])
                    else:
                        cpos2 = int(self.gene2coding_end[gene2]) - int(pos2)
                    
                    cpos1 = cpos1 + 1 if cdir1 == "+" else cpos1
                    cpos2 = cpos2 + 1 if cdir2 == "+" else cpos2
        
                    if cpos1 >= 0 and cpos2 >= 0 and cdir1 != cdir2 and cpos1 % 3 == cpos2 % 3:
                        if key in comb2inframe:
                            comb2inframe[key] = comb2inframe[key] + "," + gene1 + "-" + gene2
                        else:
                            comb2inframe[key] = gene1 + "-" + gene2
        
        
        hResult = open(output, 'w')
        for key, value in sorted(comb2inframe.items()):
            print >> hResult, key +"\t"+ value
        hResult.close()
    
    
