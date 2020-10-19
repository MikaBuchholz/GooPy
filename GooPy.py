import requests
import urllib

class GooPy():
    def __init__(self, url = None, keyWords = []):
        self.url = url
        self.keyWords = keyWords
        self.bytePageContent = None
    
    def connectToPage(self):
        try:
            connectData = requests.get(self.url)
            if connectData.status_code != 200:
                return False
            
            else:
                return connectData

        except:
            return False

    def checkWebpageForWords(self):
        data = self.connectToPage()
        dict = {}
      
        if data:
            wordCounter = 0
            for keyWord in self.keyWords:
                if keyWord in str(data.content):
                    wordCounter = str(data.content).count(keyWord)
                    dict[keyWord] = wordCounter

                else:
                    dict[keyWord] = 0

        return dict

if __name__ == "__main__":

    url1 = "https://www.w3schools.com/python/python_dictionaries.asp"
    acc = GooPy(url = url1, keyWords = ["thisdict", "Sex"])
    print(acc.checkWebpageForWords())