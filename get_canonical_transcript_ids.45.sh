#!/bin/sh

# Extract transcript IDs.
# Input: the gff3 annotation file from GENCODE, gzipped.
# Filters: 
# - Require "Ensembl_canonical" i.e. the one best transcript to represent this gene
# - Require column 3 say "transcript (to exclude "gene" and "exon")
# - These filters also exclude comment lines, which start with #
# Parse column 9
# - Expect a list of tag=value pairs, delimited by semi-colon
# - Expect "transcript_id" is not the last tag, so is followed by semi-colon
# - Extract just the "transcript_id" tag and its value
# - Extract just the value
# Output: write one ID per line to a text file

gunzip -c gencode.v45.long_noncoding_RNAs.gff3.gz | \
    grep Ensembl_canonical | \
    awk '{if ($3=="transcript") print $9;}' | \
    grep -o "transcript_id=.*;" | \
    cut -c 1-29 | \
    sed 's/transcript_id=//' \
	> gencode.v45.long_noncoding_RNAs.canonical_transcripts.txt

echo Done
