#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import gzip

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r1_paired_in', help="input r1 filename, gzipped",type=str, default="15_R1_adapters_removed_paired.fq.gz")
    parser.add_argument('-r2_paired_in', help="input r2 filename, gzipped",type=str, default="15_R2_adapters_removed_paired.fq.gz")
    parser.add_argument('-r1_unpaired_in', help="other input r1 filename, gzipped",type=str, default="15_R1_adapters_removed_unpaired.fq.gz")
    parser.add_argument('-r2_unpaired_in', help="otherinput r2 filename, gzipped",type=str, default="15_R2_adapters_removed_unpaired.fq.gz")
    parser.add_argument('-color1', help="matplotlib named color, for r1, paired",type=str)
    parser.add_argument('-color2', help="matplotlib named color, for r1, unpaired",type=str)
    parser.add_argument('-color3', help="matplotlib named color, for R2, paired",type=str)
    parser.add_argument('-color4', help="matplotlib named color, for R2, unpaired",type=str)
    parser.add_argument('-title', help="plot_title",type=str, default="15 3C mbnl Trimmed Read Lengths Distribution")
    parser.add_argument('-f_out', help="Output filename. .png will be appended",type=str, default="15_trimmed_lengths")
    return parser.parse_args()

def get_lengths_dist(filename):
    """
    Gets length distribution, returns pair of lists 
    Input:
        filename - str, gzipped fastq filename
    Output:
        lengths - dict, keys are lengths, values are frequency
    """
    lengths = {} # keys are lengths, values are frequency
    with gzip.open(filename, 'rt') as fh:
        for index, line in enumerate(fh):
            if index%4==1:
                line = line.strip()
                if len(line) in lengths:
                    lengths[len(line)] += 1
                else:
                    lengths[len(line)] = 1
    x, y = [], []
    for len_ in lengths:
        x.append(len_)
        y.append(lengths[len_])
    return x, y

def comb_freq(x1, y1, x2, y2):
    """
    Combines two frequnecy 
    """
    

args = parse()
r1_x_paired, r1_y_paired = get_lengths_dist(args.r1_paired_in)
r2_x_paired, r2_y_paired = get_lengths_dist(args.r2_paired_in)
r1_x_unpaired, r1_y_unpaired = get_lengths_dist(args.r1_unpaired_in)
r2_x_unpaired, r2_y_unpaired = get_lengths_dist(args.r2_unpaired_in)

fig, ax = plt.subplots(figsize=[13,8])
ax.set_title(args.title)
# Get minimum of all datasets 
min_x = min(min(r1_x_paired), min(r2_x_paired), min(r1_x_unpaired), min(r2_x_unpaired))
offset = .25
ax.bar([x - offset*2 for x in r1_x_paired], r1_y_paired, color=args.color1, label="R1 paired", width = .25)
ax.bar([x - offset for x in r1_x_unpaired], r1_y_unpaired, color=args.color2, label="R1 unpaired", width = .25)
ax.bar([x + offset for x in r2_x_paired], r2_y_paired, color=args.color3, label="R2 paired", width = .25)
ax.bar([x + offset*2 for x in r2_x_unpaired], r2_y_unpaired, color=args.color4, label="R2 unpaired", log=True, width = .25)
ax.set_ylabel("Frequency")
ax.set_xlabel("Read length")
ax.legend()
ax.set_xlim(min_x-1, 104) # lil wiggle room
plt.savefig(args.f_out+".png")

