# 导入常用库
import warnings
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 图表可以显示中文
warnings.filterwarnings('ignore')

df = pd.read_excel("DouBanListPage.xlsx", sheet_name=0)
x=list(df["rank"].to_list())#电影排名
y=list(df["grade"].to_list())#电影评分人数
z=list(df["rating_num"].to_list())#电影评分
plt.figure(figsize=(12, 8))
plt.scatter(x=y,
            y=x,
            cmap='Blues',
            marker='o',
            c=z,   # 数字越大，颜色越深，评分越高
            alpha=0.8,
            linewidths=0.3,
            edgecolors='Black')

plt.title('豆瓣top250电影排名&评分&评分人数情况', fontsize=18)
plt.xlabel('评分人数', fontsize=14)
plt.ylabel('豆瓣排名', fontsize=14)
plt.xlim(0, 2500000)
plt.colorbar()
plt.show()