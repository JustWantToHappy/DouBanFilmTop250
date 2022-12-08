from pyecharts.charts import Pie
from pyecharts import options as opts
import pandas as pd
#豆瓣top250电影类型统计
if __name__=="__main__":
    df = pd.read_excel("DouBanSingleDetailedPage.xlsx", sheet_name=0)
    dic= df.to_dict()
    data={}
    for item in dic["types"].items():
        arr=item[1].split(" ")
        for type in arr:
            data[type]=data.get(type,0)+1
    pie=(
        Pie(init_opts=opts.InitOpts(page_title="豆瓣评分top250之类型分析"))
        .add(data_pair=list(data.items()),series_name="电影类型",color="skyblue",center=["600","300"])
        .set_global_opts(title_opts=opts.TitleOpts(title="豆瓣top250电影类型标签分布情况",pos_bottom="0px"))
    )
    pie.render("types.html")