import requests
from bs4 import BeautifulSoup
from utils import HelpUtils
from utils import SeleniumUtils
from urlManager import URLManager
from selenium.webdriver.common.by import By
#构造分页列表
page_indexs=range(175,250,25)
hs=HelpUtils()
#获取Top250的电影的所有列表页面
def download_all_htmls():
    global  hs
    htmls=[]
    for start in page_indexs:
        url=f"https://movie.douban.com/top250?start={start}&filter="
        res=requests.get(url,headers=hs.get_my_headers(),proxies=hs.get_my_proxies())
        if(res.status_code!=200):
            raise Exception("html列表页面爬取错误")
        htmls.append(res.text)
        res.close()
    return htmls
#传入一个页面，解析页面得到数据
def parse_single_html(html):
    soup=BeautifulSoup(html,'html.parser')
    article_items=(
        soup.find("div",class_="article").find("ol",class_='grid_view').find_all("div",class_="item")
    )
    #用来存放取到的数据
    datas={"rank":[],"cover":[],"title":[],"rating_star":[],"rating_num":[],"grade":[]}
    for article_item in article_items:
        #电影排名
        rank=article_item.find("div",class_="pic").find("em").get_text()
        #电影封面
        cover=article_item.find("div",class_="pic").find("a").find("img")['src']
        '''
        电影的相关信息，包括电影名称，别名，发行地区，发行时间，导演，主演，电影类型，评分，评分人数，电影简短引用
        '''
        info=article_item.find("div",class_="info")
        title=info.find("div",class_="hd").find("span",class_="title").get_text()

        stars=(
            info.find("div",class_="bd")
            .find("div",class_="star")
            .find_all("span")
        )
        rating_star=stars[0]["class"][0]
        rating_num=stars[1].get_text()
        grade=stars[3].get_text()
        datas["rank"].append(rank)
        datas["cover"].append(cover)
        datas["title"].append(title)
        datas["rating_star"].append(rating_star.replace("rating","".replace("-t","")))
        datas["rating_num"].append(rating_num)
        datas["grade"].append(grade.replace("人评价",""))
    return datas
def download_detailed_single_page(url):
    global hs
    htmlText=""
    res=requests.get(url,headers=hs.get_my_headers(),proxies=hs.get_my_proxies())
    if(res.status_code!=200):
        raise Exception("html单个电影页面爬取错误")
    htmlText+=res.text
    res.close()
    return htmlText
def get_single_page_info(url,browser):
    global  hs
    html=download_detailed_single_page(url)
    soup=BeautifulSoup(html,'html.parser')
    #获取电影排名
    rankId=soup.select_one(".top250-no").get_text()[3:]
    # 存放数据
    store = {"rank":[rankId],"actor": [], "adaptors": [], "actors": [], "types": [], "product": [], "language": [], "release": [],"time": []}
    #获取相关信息
    data=soup.find("div",id="info").get_text()
    data=data.split("\n")
    arr=[]
    for index in range(len(data)):
        s=data[index][3:]
        if(index==5):
            s=data[index][9:]
        items=s.split("/")
        items=[item.strip() for item in items if (len(item)>0 and item.strip()!="")]
        if(index>=1 and index<=8):
            arr.append(items)
    start=0
    #arr是一个二维数组
    for key in store.keys():
        if(key!="rank"):
            store[key].append(" ".join(arr[start]))
            start += 1
    print(store)
    hs.storage_movies(store,"DouBanSingleDetailedPage.xlsx")
#获取单个电影详细页面的信息
def download_detailed_singles():
    #url管理器
    urlDB=URLManager()
    for count in page_indexs:
        url = f"https://movie.douban.com/top250?start={count}&filter="
        urlDB.add_new_url(url)
        while urlDB.has_new_url():
            newURl=urlDB.get_url()
            for i in range(0,25):
                #因为每次跳转一次页面之后，所引用的元素从DOM结构上移除了，所以需要重新生成一个webdriver
                s1= SeleniumUtils()
                elements = s1.find_all_Elements(newURl, "a>.title:first-child", By.CSS_SELECTOR)
                elements[i].click()
                #获取当前页面地址的url
                current_url=s1.get_current_url()
                #通过url去获取这个页面的数据
                get_single_page_info(current_url,s1)
                s1.history_change(-1)
                s1.close_browser()
if __name__=="__main__":
    #获取豆瓣top250列表页面的数据(第一部分注释)
   '''
    htmls=download_all_htmls()
    for html in htmls:
        data=parse_single_html(html)
        #将获取的数据存入到excel表中
        hs.storage_movies(data)
   '''
   #获取豆瓣top250的每个电影的单个页面信息(第二部分注释)
   '''
    download_detailed_singles()
   '''






