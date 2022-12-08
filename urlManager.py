class URLManager():
    '''
    url管理器
    '''
    def __init__(self):
        self.new_urls=set()
        self.old_urls=set()
    #添加一个url
    def add_new_url(self,url):
        if url==None or len(url)==0:
            return
        if url in self.old_urls or url in self.new_urls:
            return
        self.new_urls.add(url)
    #添加多个url
    def add_new_urls(self,urls):
        if(urls==None or len(urls)==0):
            return
        for url in urls:
            self.new_urls.add(url)
    #从新的urls中获取url,如果有则返回并且加入到old_urls
    def get_url(self):
        if(self.has_new_url()):
            url=self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None
    #有没有待爬取的url
    def has_new_url(self):
        return len(self.new_urls)>0