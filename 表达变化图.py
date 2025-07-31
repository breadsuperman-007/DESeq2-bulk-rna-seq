import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取 rlog 表达矩阵
df = pd.read_csv("/Users/zhanghuitian/Desktop/原始数据记录/bulk-RNA-seq/GSE183657_rlog_matrix.csv", index_col=0)

# 查看基因名
gene = "ENSMUSG00000033161"  # 替换为你感兴趣的基因名

# 转置使样本为行
df_T = df.T

# 加入分组信息
df_T['condition'] = ['Control', 'Control', 'Control', 'Treated', 'Treated', 'Treated']
group_name_map = {"Control": "Control", "Treated": "Bleomycin"}  # 你可以改成任何名称
df_T['Group'] = df_T['condition'].map(group_name_map)
# ========= 可调节参数区 =========
# 字体设置
xlabel_fontsize = 20
ylabel_fontsize = 20
tick_fontsize = 12
axis_color = 'black'
axis_linewidth = 1.2

# boxplot设置
box_width = 0.5
box_linewidth = 2
box_palette = {"Control": "#ED8C8C", "Bleomycin": "#005B8C"}

# stripplot设置（散点图）
show_strip = False
# dot_size = 7
# dot_color = "black"
# dot_alpha = 0.9
# dot_edgecolor = "white"
# dot_linewidth = 0.5

# errorbar设置（用于图例示意）
errorbar_linewidth = 2
legend_location = "upper right"

# ========= 开始绘图 ==========
sns.set(style="white")  # 不显示网格线
plt.figure(figsize=(6, 5))

# 绘制 boxplot
bp = sns.boxplot(
    data=df_T,
    x='Group',
    y=gene,
    width=box_width,
    linewidth=box_linewidth,
    fliersize=0,  # 不显示离群值
    palette=box_palette,
    boxprops=dict(alpha=0.9)  # 控制透明度
)



# 坐标轴样式设置
plt.xlabel("", fontsize=xlabel_fontsize)
plt.ylabel("rlog normalized counts", fontsize=20, color=axis_color)
plt.xticks(fontsize=20, color=axis_color)
plt.yticks(fontsize=20, color=axis_color)

# 去除边框外部线条，仅保留左/下
sns.despine()

# 设置坐标轴线条粗细
for axis in ['bottom', 'left']:
    plt.gca().spines[axis].set_linewidth(axis_linewidth)
    plt.gca().spines[axis].set_color(axis_color)

# 添加图例
if show_strip:
    plt.legend(loc=legend_location, frameon=False, fontsize=12)

# 添加标题（可选）
plt.title(f"Expression of Atp1a1", fontsize=20, weight='bold')

# 紧凑排版
plt.tight_layout()

# 展示图像
plt.show()
