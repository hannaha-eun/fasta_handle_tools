''' Create a reverse complemented fasta file from input fasta file '''

import sys
from Bio import SeqIO

input_file=sys.argv[1]
output_file=sys.argv[2]

def get_reverse_complement(input_file, output_file):
    sequences = {}

    for record in SeqIO.parse(input_file, "fasta"):
        entry_name = record.description
        sequences[entry_name] = record.seq.reverse_complement()

    with open(output_file, "w") as file:
        for entry_name, rc_sequence in sequences.items():
            file.write(f">{entry_name}\n{rc_sequence}\n")


get_reverse_complement(input_file, output_file)