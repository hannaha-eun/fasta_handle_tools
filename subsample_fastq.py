import argparse
import os
import random
import subprocess

def downsample_fastq(input_prefix, output_prefix, samples , percentage):
    for sample in samples:
        random_seed = random.randint(1, 2**32 - 1)

        input_R1 = f"{sample}_{input_prefix}.1.fastq.gz" # eg Sample1_RUN1_20240311_025210.L001.1.fastq.gz
        input_R2 = f"{sample}_{input_prefix}.2.fastq.gz" # eg Sample1_RUN1_20240311_025210.L001.2.fastq.gz

        output_R1 = f"{sample}_{output_prefix}.1.fastq.gz"
        output_R2 = f"{sample}_{output_prefix}.2.fastq.gz"

        subprocess.run(f"seqtk sample -s{random_seed} {input_R1} {percentage} | gzip > {output_R1}", shell=True)
        subprocess.run(f"seqtk sample -s{random_seed} {input_R2} {percentage} | gzip > {output_R2}", shell=True)

        print(f"Downsampled {input_R1} and {input_R2} with seed {random_seed}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Downsample FASTQ files")
    parser.add_argument("--input_prefix", required=True, help="Input file prefix")
    parser.add_argument("--output_prefix", required=True, help="Output file prefix")
    parser.add_argument("--percentage", required=True, help="Fraction of reads to subsample")

    args = parser.parse_args()

    samples = ["Sample1", "Sample2", "Sample3", "Sample4"]  # List of sample names

    downsample_fastq(args.input_prefix, args.output_prefix, samples , args.percentage)

# example usage 
# python subsample_fastq.py --input_prefix RUN1_20240311_025210.L001 --output_prefix downsampled_run --percentage 0.3
