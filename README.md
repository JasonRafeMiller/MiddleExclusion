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

## Part 4: lncLocator2
* [lncLocator2](https://github.com/Yang-J-LIN/lncLocator2) - repo
* [lncLocator2](http://www.csbio.sjtu.edu.cn/bioinf/lncLocator2/) - webserver
* [data](http://www.csbio.sjtu.edu.cn/bioinf/lncLocator2/Data.htm) - benchmark
* LL2_H1_YY.ipynb - extreme genes run
* LL2_H1_YY.log - extreme genes output
* LL2_H1_middle.ipynb - middle genes run
* LL2_H1_middle.csv - extreme genes output

## Part 5: TACOS
* [TACOS](https://balalab-skku.org/TACOS) - webserver
* TACOS_101.ipynb - one cell line
* TACOS_102.ipynb - one cell line
* TACOS_103.ipynb - one cell line
* TACOS_104.ipynb - one cell line
* TACOS_105.ipynb - one cell line
* TACOS_106.ipynb - one cell line
* TACOS_107.ipynb - one cell line
* TACOS_108.ipynb - one cell line
* TACOS_109.ipynb - one cell line
* TACOS_110.ipynb - one cell line
