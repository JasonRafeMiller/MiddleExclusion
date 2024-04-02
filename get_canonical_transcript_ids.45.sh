#!/bin/sh

gunzip -c gencode.v45.long_noncoding_RNAs.gff3.gz | \
    grep Ensembl_canonical | \
    awk '{if ($3=="transcript") print $9;}' | \
    grep -o "transcript_id=.*;" | \
    cut -c 1-29 | \
    sed 's/transcript_id=//' \
	> gencode.v45.long_noncoding_RNAs.canonical_transcripts.txt

echo Done
