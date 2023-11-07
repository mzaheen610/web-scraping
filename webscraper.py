import sys
import queue
from src.scraper.scraper import Scraper
from src.config.config import configurations
from src.saveData import Document
from src.findDomain import isValidURL, getDomainName
from concurrent.futures import ThreadPoolExecutor
import threading

# URL = sys.argv[1]
URL = "https://www.yahoo.com"
domain = getDomainName(URL)
pageNo = 0
pages = queue.Queue()
pages.put(URL)
lock = threading.Lock()


def webscraper():
    global pageNo
    while True:
        try:
            with lock:
                if pages.empty() or pageNo > int(configurations['totalPages']):
                    break
                scrape = Scraper(pages.get())
                pageNo += 1
            response = scrape.getResponse(int(configurations['maxTimeout']))
            urls = scrape.parseContents(response)
            data = scrape.saveInfo(response)
            writer = Document(domain,data)
            writer.update_document()
            for item in urls:
                if isValidURL(item,domain):
                    print("Valid url : ",item)
                    with lock:
                        pages.put(item)   
        except Exception as e:
            print(e)

executor = ThreadPoolExecutor(max_workers= 5)

for i in range(5):
    executor.submit(webscraper)

executor.shutdown()