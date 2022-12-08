from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import pandas as pd
class SeleniumUtils():
    def __init__(self):
        # 实例化一个浏览器对象
        service = Service("D:\Python\Scripts\chromedriver.exe")
        self.browser = webdriver.Chrome(service=service)
    #返回当前页面的url
    def get_current_url(self):
        return self.browser.current_url
    #回退到浏览记录上一个页面,下一个页面，以及页面刷新
    def history_change(self,num):
        if(num==1):
            self.browser.forward()
        elif(num==-1):
            self.browser.back()
        elif(num==0):
            self.browser.refresh()
        else:
            return
    def browser_wait(self,time):
        sleep(time)
    # 使用完之后关闭浏览器
    def close_browser(self):
        self.browser.quit()
    '''
    获取准确元素(通过ID,className,属性值等)
    '''
    def find_one_Element(self,url,key,by=By.ID):
        self.browser.get(url)
        try:
            print('test1')
            element=self.browser.find_element(by=by,value=key)
            print("test2")
            return element
        except:
            return None
        '''
        获取多个元素，通过css复合选择器获取
        '''
    def find_all_Elements(self,url,key,by=By.CSS_SELECTOR):
        self.browser.get(url)
        try:
            elements=self.browser.find_elements(by=by,value=key)
            return elements
        except:
            return []
class HelpUtils():
    def __init__(self):
        pass
    def get_my_cookies(self):
        return {"cookie":'bid=Y3wWfAgDTag; ll="118280"; push_noty_num=0; push_doumail_num=0; __utmz=223695111.1670310670.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __gads=ID=5b686d39e8e42eca-2274a644c2d800c8:T=1670310670:RT=1670310670:S=ALNI_MYVB0ELHtFnri-nxDOF1WLLgQDf0w; _vwo_uuid_v2=DA83D74F9C761628D0FE0E347336FD34A|69d3a142dfb24695c1e6fa518d60dbe4; __yadk_uid=t25x7rloiXgvBY7WwxdVAk0CZhX70GVm; __utmz=30149280.1670321364.3.2.utmcsr=movie.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/top250; __utmv=30149280.26511; ct=y; _pk_ses.100001.4cf6=*; ap_v=0,6.0; __utma=30149280.1798088384.1670310670.1670338524.1670381066.7; __utmb=30149280.0.10.1670381066; __utmc=30149280; __utma=223695111.1288569568.1670310670.1670338524.1670381066.7; __utmb=223695111.0.10.1670381066; __utmc=223695111; __gpi=UID=00000b8ab20654a5:T=1670310670:RT=1670381068:S=ALNI_MalKkjVHIjyyfduG4EwFYij_1jx2g; ck=iA93; _pk_id.100001.4cf6=1ce760962b43a86c.1670286570.11.1670381824.1670338529.'}
    def get_my_headers(self):
        return {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
                }
    def get_my_proxies(self):
        return {"http":None,"https":None}
    # 将获取的数据转换为excel表
    def storage_movies(self, data,fileURL="DouBanListPage.xlsx"):
        original_data = pd.read_excel(fileURL)
        data1 = pd.DataFrame(data)
        save_data = pd.concat([original_data, data1], ignore_index=True)
        save_data.to_excel(fileURL, index=False)
