import webbrowser, sys, time, pyperclip, requests, bs4, urllib

#urlhome = 'https://xkcd.com/'
urlhome = 'https://xkcd.com/2292/'

def getComic(url):
    data3 = requests.get(url)
    data3.raise_for_status()
    soup1 = bs4.BeautifulSoup(data3.text, 'html.parser')
    img1 = soup1.select('#comic > img') 
    header1 = soup1.select('#ctitle')
    src1 = img1[0].get('src')
    if(src1[:2]=='//'):
        src1='https:' + src1
        print(src1)

    imgfile = open(header1[0].text.strip() + ".jpeg", 'wb')
    imgfile.write(urllib.request.urlopen(src1).read())
    imgfile.close()

    print("title:  {}".format(header1[0].text.strip()))
    print("img1: {}".format(img1[0]))
    print('src1  {}'.format(src1))
    time.sleep(3)
    webbrowser.open(src1)
    pyperclip.copy(src1)
    return img1[0].text

getComic(urlhome)
