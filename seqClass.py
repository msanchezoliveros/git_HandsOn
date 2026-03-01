#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA') # Create parser
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") # Required sequence argument
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif") # Required sequence argument

if len(sys.argv) == 1:
    parser.print_help() # Show help if no arguments provided 
    sys.exit(1) # Exit

args = parser.parse_args() # Parse command-line arguments
args.seq = args.seq.upper() # Sequence to uppercase

if re.search('^[ACGTU]+$', args.seq): # Search nucleotide letters
    if re.search('T', args.seq) and not re.search('U', args.seq):
        print ('The sequence is DNA') # Contains T and not U -> DNA
    elif re.search('U', args.seq) and not re.search('T', args.seq):
        print ('The sequence is RNA') # Contains U and not T -> RNA
    else:
        print ('The sequence can be DNA or RNA') # Not T or U
else:
    print ('The sequence is not DNA nor RNA') # Contains invalid characters

if args.motif: # If mtif argument is provided
    args.motif = args.motif.upper() # Motif to uppercase
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq): # Motif detected
        print("Found")
    else: # Not detected
        print("Not found")
