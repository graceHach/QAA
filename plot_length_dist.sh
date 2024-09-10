#!/bin/bash

python plot_length_dist.py -color1 "darkgreen" -color2 "limegreen" -color3 "k" -color4 "darkgray" \
 -title "17 3E Fox Trimmed Read Lengths Distribution" -f_out "17_trimmed_lengths" \
 -r1_paired_in "17_R1_adapters_removed_paired.fq.gz"  -r1_unpaired_in "17_R1_adapters_removed_unpaired.fq.gz" \
 -r2_paired_in "17_R2_adapters_removed_paired.fq.gz"  -r2_unpaired_in "17_R2_adapters_removed_unpaired.fq.gz" 

# Running with defaults gives plot for lib 15
python plot_length_dist.py -color1 "blue" -color2 "cornflowerblue" -color3 "k" -color4 "darkgray"


