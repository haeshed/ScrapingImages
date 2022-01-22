import webbrowser, sys, time, pyperclip, requests, bs4, urllib

urlhome = 'https://www.freeimages.com/popular'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def getImages(url):
    data1 = requests.get(url, headers=headers)      #html content
    data1.raise_for_status()        #check for problems
    soup1 = bs4.BeautifulSoup(data1.text, 'html.parser')        #parse the data
    #print(soup1.prettify())
    aas = soup1.find_all('img')
    print('aas  {}'.format(aas[0].text))
"""
    image_info = []
    for a in aas:
        image_tag = a.findChildren("img")
        image_info.append((image_tag[0]["src"], image_tag[0]["alt"]))
"""

"""
    img1 = soup1.select('#istock_thumb_333550673 > span > img')
    #get images parsing
    print(img1[0].text)
    src1 = img1[0].get('src')       #get source from image parsing
    header1 = img1[0].get('alt')        #get headers from image parsing
    print("title:  {}".format(header1.strip()))
    print("img1: {}".format(img1[0]))
    print('src1  {}'.format(src1))
    webbrowser.open(src1)
    pyperclip.copy(src1)
    return img1[0].text
"""

"""
    imgfile = open(header1[0].text.strip() + ".jpeg", 'wb')
    imgfile.write(urllib.request.urlopen(src1).read())
    imgfile.close()
"""


getImages(urlhome)
