#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH -c 8
#SBATCH --output=LOG/gen_genome_index_%j.out
#SBATCH --error=LOG/gen_genome_index_%j.err
#SBATCH --job-name=gen_genome_index

#stop on error
set -e

conda activate QAA

/usr/bin/time -v STAR --runThreadN 8 \
--runMode genomeGenerate \
--genomeDir mouse_GENOME_INDEX \
--genomeFastaFiles gtf_primary_assembly/Mus_musculus.GRCm39.dna_sm.primary_assembly.fa \
--sjdbGTFfile gtf_primary_assembly/Mus_musculus.GRCm39.112.gtf
