from bs4 import BeautifulSoup
import requests,re,json
class covdata():
    @classmethod
    def daily(self) -> str:
        r=requests.get("https://covid19.saglik.gov.tr/")
        soup=BeautifulSoup(r.content,"html.parser")
        scriptlist=soup.find_all("script")
        for i in scriptlist:
            if "//<![CDATA" in str(i.string) and "sondurumjson" in str(i.string):
                output=str(i.string)
                output=re.findall(r'{.+?}',output)
                return output
    @classmethod
    def weekly(self) -> list:
        '''Get last 7 days data. Output is an array which contains each days data.'''
        r=requests.get("https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html")
        soup=BeautifulSoup(r.content,"html.parser")
        scriptlist=soup.find_all("script")
        for i in scriptlist:
            if "//<![CDATA" in str(i.string) and "geneldurumjson" in str(i.string):
                output=str(i.string)
                output=re.findall(r'{.+?}',output)
                output=output[:7]
                return output
    @classmethod
    def range(self,start: int, end : int) -> list:
        '''Get data between specified days. Output is an array which contains each days data.\n
        Example :  range(0,30) Fetches last 30 days data.
        '''
        r=requests.get("https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html")
        soup=BeautifulSoup(r.content,"html.parser")
        scriptlist=soup.find_all("script")
        for i in scriptlist:
            if "//<![CDATA" in str(i.string) and "geneldurumjson" in str(i.string):
                output=str(i.string)
                output=re.findall(r'{.+?}',output)
                output=output[start:end]
                return output
    @classmethod
    def vaccination(self) -> str:
        '''String that contains current vaccination data of all provinces.'''
        r=requests.get("https://covid19.saglik.gov.tr/")
        soup=BeautifulSoup(r.content,"html.parser")
        data=soup.find('g',id="turkiye-tamamlanan")
        provinces=data.find_all("g")
        datadict={}
        for province in provinces:
            provincename=str(province["data-adi"]).upper().replace("İ","i").replace("Ş","S").replace("Ç","C").replace("Ğ","G").replace("Ü","U").replace("Ö","O").lower().capitalize() # converting turkish characters to english
            datadict[provincename]=str(province["data-yuzde"]).replace("% ","")
        output=json.dumps(datadict)
        return output
if __name__ == "__main__":
    today=covdata.daily()
    print(today)