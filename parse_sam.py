#!/usr/bin/env python

import argparse

def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("-filename",type=str, help="Name of sam file", default="../Danio_rerio.GRCz11.dna.ens112.STAR_2.7.11b_ALIGNMENT/sorted.sam")
    return parser.parse_args()


args = parse()
mapped = set()
unmapped = set()
with open(args.filename, 'r') as fh:
    for line in fh:
        line=line.strip()
        if line[0]=="@":
            continue
        else:
            line_split = line.split()
            # flag is index 1, qname is index 0
            flag = int(line_split[1])
            if((flag & 4) != 4):
                # mapped 
                if ((flag&256)!=256):
                    # Primary alignment only
                    # Original code used qname, but these are the same between r1 and r2, so creating altered qname
                    appended = "_R2" if flag&16==16 else "_R1"
                    q_name_plus_r = line_split[0] + appended
                    # Adds to string label whether reverse complimented or not, making R1 and R2 unique
                    mapped.add(q_name_plus_r)
            else:
                # unmapped
                appended = "_R2" if flag&16==16 else "_R1"
                q_name_plus_r = line_split[0] + appended
                unmapped.add(q_name_plus_r)

print("RESULTS for",args.filename)
print("Number of reads mapped:",len(mapped))
print("Number of reads unmapped:",len(unmapped))