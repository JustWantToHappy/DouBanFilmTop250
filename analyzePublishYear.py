from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd
#豆瓣top250年份与电影数量之间的关系
if __name__=="__main__":
    df=pd.read_excel("DouBanSingleDetailedPage.xlsx",sheet_name=0)
    arr={}
    dic=df.to_dict();count=0
    for data in dic['release'].values():
        s=data[3:7]
        try:
            year=int(s)
            arr[year]=arr.get(year,0)+1
        except:
            pass
    arr=dict(sorted(arr.items(),key=lambda x:x[0]))
    bar = (
        Bar(init_opts=opts.InitOpts(page_title="豆瓣评分top250之年份分析"))
            .add_xaxis(list(arr.keys()))
            .add_yaxis("",list(arr.values()))
            .set_global_opts(visualmap_opts=opts.VisualMapOpts(is_show=True))
            .set_global_opts(xaxis_opts=opts.AxisOpts(name="年份"))
            .set_global_opts(yaxis_opts=opts.AxisOpts(name="电影数量"))
            .set_global_opts(title_opts=opts.TitleOpts(title="豆瓣top250电影上映年份分布情况",pos_left="center"))
    )
    bar.render("years.html")
