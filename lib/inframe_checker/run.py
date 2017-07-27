#! /usr/bin/env python

import os, sys
import argparse
import subprocess
from psl2inframe_pair import Psl2inframe
from make_junc_seq_pair_fa import MakeJuncSeq
from add_general import AddGeneral

def inframe_main(arg):

    blat_path = arg.blat_path
    blat_params = arg.blat_params
    all_gene = arg.all_gene
    input_junc = arg.input_junc
    output_dir = arg.output_dir
    coding_info = arg.coding_info
    ref_gene = arg.ref_gene

    output_fa = output_dir+"/juncContig.fa"
    mjs = MakeJuncSeq()
    mjs.main(input_junc, ref_gene, output_fa)

    output_psl = output_dir+"/juncContig_allGene_cuff.psl"
    blat_params_list = blat_params.split(" ")
    cmd_list = [blat_path]
    cmd_list.extend(blat_params_list)
    cmd_list.extend([all_gene])
    cmd_list.extend([output_fa])
    cmd_list.extend([output_psl])

    FNULL = open(os.devnull, 'w')
    subprocess.check_call(cmd_list, stdout = FNULL, stderr = subprocess.STDOUT)
    
    output_inframe = output_dir+"/comb2inframe.txt"
    pti = Psl2inframe()
    pti.set_gene_dict(coding_info)
    pti.set_key_dict(output_psl)
    pti.print_inframe(output_inframe)

    base_file = os.path.basename(input_junc)
    output_base, ext = name, ext = os.path.splitext(base_file)
    result_file = output_dir+"/"+output_base+"_inframe.txt"
    ag = AddGeneral()
    ag.add_inframe_info(input_junc, output_inframe, result_file)


