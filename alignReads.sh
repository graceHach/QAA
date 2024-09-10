#!/bin/bash

#SBATCH --account=bgmp
#SBATCH --partition=bgmp
#SBATCH --cpus-per-task=8
#SBATCH --output=LOG/alignment_%j.out
#SBATCH --error=LOG/alignment_%j.err
#SBATCH --job-name=alignment

set -e

mamba activate QAA

/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
--outFilterMultimapNmax 3 \
--outSAMunmapped Within KeepPairs \
--alignIntronMax 1000000 --alignMatesGapMax 1000000 \
--readFilesCommand zcat \
--readFilesIn 17_R1_adapters_removed_paired.fq.gz 17_R2_adapters_removed_paired.fq.gz \
--genomeDir mouse_GENOME_INDEX \
--outFileNamePrefix lib_17_ALIGNMENT/

/usr/bin/time -v STAR --runThreadN 8 --runMode alignReads \
--outFilterMultimapNmax 3 \
--outSAMunmapped Within KeepPairs \
--alignIntronMax 1000000 --alignMatesGapMax 1000000 \
--readFilesCommand zcat \
--readFilesIn 15_R1_adapters_removed_paired.fq.gz 15_R2_adapters_removed_paired.fq.gz \
--genomeDir mouse_GENOME_INDEX \
--outFileNamePrefix lib_15_ALIGNMENT/
