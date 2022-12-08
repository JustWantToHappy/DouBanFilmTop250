from pyecharts.charts import Scatter
from pyecharts import options as opts
import pandas as pd
#豆瓣top250电影排名&评分&评分人数情况
if __name__=="__main__":
    df = pd.read_excel("DouBanListPage.xlsx", sheet_name=0)
    dic = df.to_dict()
    rank=list(dic["rank"].values())
    grade=sorted(list(dic["grade"].values()))
    title="豆瓣评分top250电影排名&评分&评分人数情况"
    print(grade)#x轴
    print(rank)#y轴
    print(len(rank)==len(grade))
    scatter=(
        Scatter(init_opts=opts.InitOpts(page_title=title,width="1200px", height="500px"))
        #自变量x
        .add_xaxis(xaxis_data=grade)
        #因变量y
        .add_yaxis("", y_axis=rank)
        #坐标轴配置项
        .set_global_opts(xaxis_opts=opts.AxisOpts(name="评分人数",max_=2500000,min_=0,interval=500000),yaxis_opts=opts.AxisOpts(name="豆瓣排名",name_gap="40",min_=0,max_=250))
        .set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=True,pos_right="0",pos_bottom="center",precision="1",min_=8,max_=10,range_text=['高分','低分'],split_number=100,range_color=['#ffffff','blue']))
    )
    scatter.render("rank.html")
