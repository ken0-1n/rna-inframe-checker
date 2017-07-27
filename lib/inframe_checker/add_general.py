#! /usr/bin/env python

import re
import sys

r = re.compile("[A-Za-z0-9]+:[\+-][0-9]+")

class AddGeneral:

    def add_inframe_info(self, input_file, in_inframe, output ):

        inframe_hash = {}
        hResult = open(output, 'w')
        with open(in_inframe,"r") as hin:
            for line in hin:
                line = line.rstrip('\n').rstrip('\r')
                F = line.split('\t')
                m = r.findall(F[0])
                vals = m[0].split(":")
                bp1 = vals[0] +"\t"+ vals[1][1:] +"\t"+ vals[1][0:1]
                vals = m[1].split(":")
                bp2 = vals[0] +"\t"+ vals[1][1:] +"\t"+ vals[1][0:1]
                inframe_hash[bp1 +"\t"+ bp2] = F[1]
        
        with open(input_file,"r") as hin:
            for line in hin:
                line = line.rstrip('\n').rstrip('\r')
                F = line.split('\t')
                key = "\t".join(F[0:6])
                if key in inframe_hash:
                    print >> hResult, line +"\t"+ inframe_hash[key]
                else:
                    print >> hResult, line +"\t"

        hResult.close()
        
    
