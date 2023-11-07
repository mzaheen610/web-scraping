
class Document:
    def __init__(self,domain,data) -> None:
        self.filename = domain + 'ScraperData.txt'
        self.data = data

    def update_document(self):
        with open(self.filename,"a") as fileObject:
            for i in range(len(self.data)):
                fileObject.write('\n')
                fileObject.write(self.data[i])
                # fileObject.write('\n')
                

# writer = Document('Google',["Title : Homepage", "Download time : 2s", "URL : https://www.google.com"])
# writer.update_document()
