#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA') # Create parser
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") # Required sequence argument

if len(sys.argv) == 1:
    parser.print_help() # Show help if no arguments provided 
    sys.exit(1) # Exit

args = parser.parse_args() # Parse command-line arguments
args.seq = args.seq.upper() # Sequence to uppercase

if not re.search('^[ACGTU]+$', args.seq): # Search nucleotide letters
   print ('The sequence is not DNA nor RNA') # Contains invalid characters
   sys.exit(1) # Exit

# Compute nucleotide percentages
seq_length = len(seq) # Get sequence length
nucleotides = ['A', 'C', 'G', 'T', 'U'] # All possible nucelotides

print(f"Sequence length: {seq_length}")
print("Nucleotide percentages:")

for nucleotide in nucleotides:
    count = seq.count(nt) # Count the number of each nucleotide
    percent = (count / seq_length) * 100 # Compute the percent
    print(f"{nt}: {percent:0.2f}%") # Display the results 
