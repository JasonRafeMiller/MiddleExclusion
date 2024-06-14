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
* RNAlight_122.ipynb - grid search for LightGBM hyperparameters
* RNAlight_123.ipynb - lncATLAS lncRNA data prep
* RNAlight_133.ipynb - lncATLAS mRNA data prep
* RNAlight_125.ipynb - examine RNAlight optimized params
* [LightGBM](https://github.com/microsoft/LightGBM) - repo
* RNAlight_127.ipynb - LightGBM, defaults, lncRNA, all or no middle exclusion
* RNAlight_128.ipynb - LightGBM, defaults, lncRNA, train or test middle exclusion
* RNAlight_137.ipynb - LightGBM, defaults, mRNA, all or no middle exclusion
* RNAlight_138.ipynb - LightGBM, defaults, mRNA, train or test middle exclusion

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
* TACOS_201.ipynb - sample genes for submission to server
* TACOS_202.ipynb - compute accuracy from server results

## Part 6: DeepLncRNA
No files.

## Part 7: RF, GBM, SVM, MLP
* RF_201.ipynb - random forest
* GBM_201.ipynb - gradient boosting machine
* SVM_201.ipynb - support vector machine
* MLP_201.ipynb - multi-layer perceptron, lncRNA, all or no middle exclusion
* MLP_201.ipynb - multi-layer perceptron, lncRNA, train or test middle exclusion
* MLP_203.ipynb - multi-layer perceptron, mRNA, all or no middle exclusion
* MLP_204.ipynb - multi-layer perceptron, mRNA, train or test middle exclusion

## Part 8: Benchmark
* Benchmark_101.ipynb - data
* Benchmark_101.ipynb - model
