#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --output=LOG/fastqc_prelimplotting_%j.out
#SBATCH --error=LOG/fastqc_prelimplotting_%j.err
#SBATCH --job-name=fastqc_prelimplotting
#SBATCH --mail-type=ALL
#SBATCH --mail-user=ghach@uoregon.edu

conda activate QAA

mkdir -p 15_output
mkdir -p 17_output
/usr/bin/time -v fastqc /projects/bgmp/shared/2017_sequencing/demultiplexed/15_3C_mbnl_S11_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/15_3C_mbnl_S11_L008_R2_001.fastq.gz -o 15_output --svg --extract --delete
/usr/bin/time -v fastqc /projects/bgmp/shared/2017_sequencing/demultiplexed/17_3E_fox_S13_L008_R1_001.fastq.gz /projects/bgmp/shared/2017_sequencing/demultiplexed/17_3E_fox_S13_L008_R2_001.fastq.gz -o 17_output --svg --extract --delete