# MiddleExclusion
## Part 1: lncATLAS
* [lncATLAS](https://lncatlas.crg.eu/) - Get lncATLAS_all_data_RCI.csv
* lncATLAS_100.ipynb - Extract database info.

## Part 2: GenCode
* [GenCode](https://www.gencodegenes.org/)
* [FTP](https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human) - release 45
* Sequences - gencode.v45.lncRNA_transcripts.fa.gz
* Annotations - gencode.v45.long_noncoding_RNAs.gff3.gz
* [Ensembl](https://useast.ensembl.org/info/genome/genebuild/canonical.html) - define canonical
* get_canonical_transcript_ids.45.sh - unix shell script

## Part 3: RNAlight
* [RNAlight](https://github.com/YangLab/RNAlight) - repo
* [predict.tsv](https://github.com/YangLab/RNAlight/blob/main/Light_score_diverse_RNA/lncRNA_whole_genome/Whole_genome_lncRNA_predict_df.tsv) - predictions file
* RNAlight_101.ipynb - analyze predictions
* RNAlight_123.ipynb - lncATLAS mean CNRCI without middle exclusion
* RNAlight_122.ipynb - grid search
* RNAlight_125.ipynb - optimized params
* [LightGBM](https://github.com/microsoft/LightGBM) - repo
* RNAlight_127.ipynb - default params
