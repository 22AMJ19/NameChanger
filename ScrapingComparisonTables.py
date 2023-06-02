# url取得
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36" #おまじない

# HTMLの取得
def GetHtml():
    url = 'http://gigadict.com/JxCsCode.htm'
    
    headers = {'User-Agent': USER_AGENT}
    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as res:
        body = res.read()
        return body

def kensaku():
    
    html = GetHtml()
    soup = BeautifulSoup(html, 'html.parser')

    title_text = soup.find('pre', attrs={ 'class': 'b1' }).get_text()
    all_list = []
    text_list = []
    all_list = title_text.splitlines()
    jpn = ""
    chs = ""
    for text in all_list:
        if text != "":
            text_list.append(text.replace('　', '').replace(' ', ''))
    for text in text_list:
        jpn = jpn + text[16]
        chs = chs + text[-1]
    return jpn, chs

if __name__ == "__main__":
    jpn, chs = kensaku()
    jpn = "　" + jpn[98:]
    print (jpn + "\n" + chs[97:])
    f = open("ComparisonTable.txt", "w", encoding='UTF-8')
    f.write(jpn + "\n" + chs[97:])