#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --output=LOG/python_plotting_%j.out
#SBATCH --error=LOG/python_plotting_%j.err
#SBATCH --job-name=python_plotting
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ghach@uoregon.edu

set -e

/usr/bin/time -v python quality_hist.py -f_in "/projects/bgmp/shared/2017_sequencing/demultiplexed/15_3C_mbnl_S11_L008_R1_001.fastq.gz" \
-title "15_3C_mbnl R1" \
-color "navy" \
-f_out "plot_15_3C_mbnl_R1"

/usr/bin/time -v python quality_hist.py -f_in "/projects/bgmp/shared/2017_sequencing/demultiplexed/15_3C_mbnl_S11_L008_R2_001.fastq.gz" \
-title "15_3C_mbnl R2" \
-color "mediumblue" \
-f_out "plot_15_3C_mbnl_R2"

/usr/bin/time -v python quality_hist.py -f_in "/projects/bgmp/shared/2017_sequencing/demultiplexed/17_3E_fox_S13_L008_R2_001.fastq.gz" \
-title "17_3E_fox R2" \
-color "purple" \
-f_out "plot_17_3E_fox_R2"

/usr/bin/time -v python quality_hist.py -f_in "/projects/bgmp/shared/2017_sequencing/demultiplexed/17_3E_fox_S13_L008_R1_001.fastq.gz" \
-title "17_3E_fox R1" \
-color "darkorchid" \
-f_out "plot_17_3E_fox_R1"