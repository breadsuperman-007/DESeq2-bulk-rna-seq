# 读取count矩阵，第一列作为行名
count_data <- read.csv("/Users/zhanghuitian/Desktop/GSE183657_counts.csv", row.names = 1)
# 查看前几行是否正确读取
head(count_data)
# 样本条件信息
col_data <- data.frame(
  row.names = colnames(count_data),
  condition = c("Control", "Control","Control", "Treated", "Treated","Treated")
)    
dds <- DESeqDataSetFromMatrix(countData = count_data,
                              colData = col_data,
                              design = ~ condition)
dds <- DESeq(dds)     
res <- results(dds)
head(res)
write.csv(res, file = "GSE183657_counts_DESeq2_results.csv", row.names = TRUE)
# 获取 rlog 变换后的表达量（更适合画图）
rld <- rlog(dds)

# 提取表达矩阵
rld_mat <- assay(rld)

# 保存为CSV文件
write.csv(rld_mat, file = "GSE183657_rlog_matrix.csv")
