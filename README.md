# 使用的第三方库
- requests(用于爬虫)
- bs4(用于解析下载好的html页面)
- selenium(用于爬虫自动化)
- pyecharts(用于生成可视化图表)
# 使用说明
1. 运行app文件爬取网页信息，两部分注释分别用于生成两个excel表
2. 如果爬虫已经获取到数据了(每张excel工作表中的数据都是250条),这时候分别运行analyze开头的文件就可以生成不同的html文件了(有的是生成一张图)