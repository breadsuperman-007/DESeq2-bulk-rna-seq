import pandas as pd
#——————————————step1:把六个文件里的count合并成一个dataframe——————————————
files = [
    "Control_1.txt",
    "Control_2.txt",
    "Control_3.txt",
    "Treated_1.txt",
    "Treated_2.txt",
    "Treated_3.txt"
]

dfs = []
for f in files:
    df = pd.read_csv(f, sep='\t')
    df = df[['Symbol', df.columns[1]]]  # 取基因和count列
    df.columns = ['Gene', f]
    dfs.append(df)

# 以第一个文件为基准，依次合并
count_df = dfs[0]
for df in dfs[1:]:
    count_df = pd.merge(count_df, df, on='Gene', how='outer')

count_df = count_df.fillna(0)  # 缺失值填0
count_df = count_df.set_index('Gene')

print(count_df.head())

count_df.to_csv("counts.csv")

