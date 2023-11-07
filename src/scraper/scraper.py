import requests
from bs4 import BeautifulSoup

# url = "https://www.yahoo.com"

class Scraper:
    def __init__(self,URL) -> None:
        self.url = URL
        self.pageData = []

                                    #Sending a request to the URL and getting a response
    def getResponse(self, maxtimeout):
        try:
            response = requests.get(self.url, timeout=maxtimeout)
            print(response.elapsed) #time to download a page
            # print(response.content)
            print(response.status_code)
            print(len(response.content))
            self.pageData.append(f'URL : {self.url}')
            self.pageData.append(f'Status Code : {response.status_code}')
            self.pageData.append(f'Download Time : {response.elapsed}')
            self.pageData.append(f'HTML Size : {len(response.content)}B')
            return response.text    # return response in text format
        except:
            return None
                                   #Get all possible URLs in the Response. Parsing and Scraping
    def parseContents(self, contents):
        soup = BeautifulSoup(contents,'html.parser')
        tags = soup.find_all("a")
        URLlist = []
        for item in tags:
            try:
                URLlist.append(item['href'])
                # print(item)
                print(item['href'])
        # print(URLlist)
            except KeyError:
                print("No HREF in tag")
        return URLlist
    
                                    #To extract Title, H1, H2 text from the page
    def saveInfo(self, contents):
        soup = BeautifulSoup(contents,'html.parser')
        title = soup.find("title")
        h1  = soup.find("h1")
        h2  = soup.find("h2")
        if title:
            self.pageData.append(f'Title : {title.text}')
        if h1:
            self.pageData.append(f'H1 : {h1.text}')
        if h2:
            self.pageData.append(f'H2 : {h2.text}')
        # print(title, h1, h2)
        return self.pageData
    

# scrape = Scraper('https://www.yellowpages.com')
# contents = scrape.getResponse(2)
# urls = scrape.parseContents(contents)
# print(scrape.saveInfo(contents))
