import webbrowser, sys, time, pyperclip, requests, bs4

"""
data = requests.get('http://automatetheboringstuff.com/files/rj.txt')
print(len(data.text))
print(data.text[:50])

dataFile = open('romeo&juliet.txt', 'wb')
for chunk in data.iter_content(100000):
    dataFile.write(chunk)
dataFile.close()

data2 = requests.get('http://automatetheboringstuff.com/2e/chapter6/')
data2.raise_for_status()
print(len(data2.text))
print(data2.text[:50])

dataFile2 = open('automatetheborintstuff.txt', 'wb')
for chunk in data2.iter_content(100000):
    dataFile2.write(chunk)
dataFile2.close()
"""
url1 = 'https://www.ebay.com/itm/Men-Boar-Hair-Bristle-Beard-Mustache-Brush-Military-Hard-Round-Wood-Handle-Comb/112561966555?ssPageName=STRK%3AMEBIDX%3AIT&_trksid=p2057872.m2749.l2649'
url2 = 'https://www.ebay.com/itm/Bristle-Brush-Boar-Comb-Natural-Anti-static-Oval-Hairdressing-Hair-Styling-Comb/362936056044?hash=item5480acb8ec:g:AeEAAOSwLxheYeQM'

def getEbayPrice(url):
    data3 = requests.get(url)
    data3.raise_for_status()
    soup1 = bs4.BeautifulSoup(data3.text, 'html.parser')
    price1 = soup1.select('#prcIsum')
    header1 = soup1.select('#itemTitle')
    print("header1:  {}".format(header1[0].text.strip()))
    print("price1: {}".format(price1[0]))
    print("price1 is: {}\n".format(price1[0].text))
    return price1[0].text

getEbayPrice(url1)
getEbayPrice(url2)
