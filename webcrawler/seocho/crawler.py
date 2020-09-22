from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import re
import requests

def req(loc) :
    #move key to enviroment file
    r = requests.get(f'https://dapi.kakao.com/v2/local/search/keyword.json?page=1&size=10&query={loc}', headers = {'Authorization':'KakaoAK 26551b75cd4a559678e76802fd7981e4'})
    data = r.json()
    if len(data['documents']) != 0 :
        return (data['documents'][0]['x'], data['documents'][0]['y'])
    return (str('0.00'), str('0.00'))

def parser(str) :
    tmp = []
    items = re.findall("\d+/\d+|\d+[^(\\n]+\([^)]+[\d]", str)
    current = 0
    result = []
    for idx, element in enumerate(items) :
        x = re.split('[(]',element)
        if len(re.findall(r"\d+:\d+~[\d+:\d+|\d+]+", x[0])) != 0 :
            time = re.findall(r"\d+:\d+~[\d+:\d+|\d+]+",x[0])
            name = x[0][x[0].find(" ")+1:]
            (axisx, axisxy) = req(x[1])
            result.append([items[current], time[0], name, x[1], axisx, axisxy])
        elif len(re.findall(r"\d+/\d+",x[0])) != 0:
            current = idx
    return result


def doCrawling() :
    with urllib.request.urlopen("https://www.seocho.go.kr/html/notice/main.jsp") as response:
        result = []
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        target = soup.find('div',{'id':'con12'})
        detailed = target.find_all('td',{'class':'left'})
        for idx, item in enumerate(detailed) :
            if(idx != len(detailed) - 1) :
                result.append(parser(item.string))
        for element in result :
            for ele in element :
                print(ele)


#For Testing
doCrawling()