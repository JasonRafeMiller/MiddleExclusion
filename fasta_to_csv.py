'''
Typical command line:
 python fasta_to_csv.py gencode.v45.lncRNA_transcripts.fa \
 gencode.v45.long_noncoding_RNAs.canonical_transcripts.txt \
 gencode_canonical_lncRNA.csv \
 --debug
'''

import argparse
import traceback
import os
import sys

class Fasta_Oneliner():
    def __init__(self,infile,outfile,debug=False):
        self.infile = infile
        self.outfile = outfile
        self.DEFLINE_PREFIX='>'
        self.debug=debug
        self.id_set = set()

    def restrict_IDs(self,txtfile):
        with open (txtfile, 'r') as infa:
            for line in infa:
                line = line.strip()
                self.id_set.add(line)
        
    def fix(self,verbose=True):
        build_seq=''
        defline=''
        seqs_in=0
        seqs_out=0
        gene_id = ''
        tran_id = ''
        with open(self.outfile, 'w') as outfa:
            with open(self.infile, 'r') as infa:
                for line in infa:
                    line=line.rstrip()
                    if line[0]==self.DEFLINE_PREFIX:
                        if seqs_in>0 and tran_id in self.id_set:
                            seqs_out += 1
                            outfa.write(",".join([tran_id,gene_id,build_seq]))
                            outfa.write('\n')
                        # Convert this: >ENST00000417334.1|ENSG00000231141.1|OTTHUMG0...
                        # To this: ENST00000417334,ENSG00000231141,GGTTGCCAC...
                        tokens = line[1:].split('|')
                        tran_id = tokens[0].split('.')[0]
                        gene_id = tokens[1].split('.')[0]
                        build_seq=''
                        seqs_in += 1
                    else:
                        build_seq += line
                # Last sequence is special case
                if seqs_in>0 and tran_id in self.id_set:
                    seqs_out += 1
                    outfa.write(",".join([tran_id,gene_id,build_seq]))
                    outfa.write('\n')
        if verbose:
            print("Sequences_input: ",seqs_in)
            print("Sequences_output: ",seqs_out)

def args_parse():
    global args
    parser = argparse.ArgumentParser(
        description='Make csv of GenCode lncRNA canonical transcripts.')
    parser.add_argument(
        'fasta_file', help='input sequence file', type=str)
    parser.add_argument(
        'txt_file', help='input transcript ID list', type=str)
    parser.add_argument(
        'csv_file', help='output sequencefile', type=str)
    parser.add_argument(
        '--debug', help='Print traceback after exception.',
        action='store_true')
    args = parser.parse_args()

if __name__ == "__main__":
    '''FASTA input multiliners output oneliners.'''
    try:
        args_parse()
        fixer = Fasta_Oneliner(args.fasta_file,args.csv_file,args.debug)
        fixer.restrict_IDs(args.txt_file)
        fixer.fix()
    except Exception:
        print()
        if args.debug:
            print(traceback.format_exc())
        else:
            print("There was an error.")
            print("Run with --debug for traceback.")
