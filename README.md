# DESeq2-bulk-rna-seq
1.在GEO上下载数据集（有多个分组单独的count，也有整合后的count）  
2.单独分组的count使用python中的bulk-rna-seq7.25合并成一个文件  
3.将count文件用r的deseq2进行分析，会生成normalization count，画图用的是rlog normalization counts  
4.将保存的rlog normalization counts文件用python画图  
最后使用的是GSE183657数据集，mouse BLM
