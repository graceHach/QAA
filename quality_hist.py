#!/usr/bin/env python

# This script has been massively paired down. Original script with four subplots and mins/maxes took 36 hours to run.
import argparse
import numpy as np
import bioinfo
import matplotlib.pyplot as plt
import gzip

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f_in', help="input fastq filename",type=str, default="mini.fq",)
    parser.add_argument('-length', help="length of reads in f_in",type=int, default=101)
    parser.add_argument('-title', help="plot title",type=str,default="hello!")
    parser.add_argument('-color', help="color of line in plot",type=str,default="navy")
    parser.add_argument('-f_out', help="Output filename. .png will be apended",type=str, default="",)

    # ADD ARGUMENT IF NOT USING PHRED + 33
    return parser.parse_args()

def get_mean(filename, length):
    """
    Gets np arrays of means
    """
    means = np.zeros([length])
    # open the file
    with gzip.open(filename, 'rt') as fh:
        for index, line in enumerate(fh):
            line=line.strip()
            if index%4==3: # q score lines
                for char_index, char in enumerate(line):
                    score = bioinfo.convert_phred(char)
                    if index==0:
                        means[char_index] = score 
                    else:
                        # new_mean = old_mean + (new_point - old_mean)/n (where n includes new_point)
                        # Here, our n is (index-3)/4+1 (1 based index of record)
                        n = (index-3)/4+1  # 
                        old_mean = means[char_index] # mean before current datapoint, score is added
                        means[char_index] = old_mean + (score - old_mean)/n
    return means

args = parse_args()

# calcualted as a running mean!
means = get_mean(args.f_in, args.length)

fig, ax = plt.subplots()
ax.plot(range(1,args.length+1,1),means,color='navy',label='Mean')
ax.set_title(args.title)
ax.set_ylabel("Phred quality score")
ax.set_xlabel("Base position")

fig.savefig(args.f_out+".png")
