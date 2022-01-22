import webbrowser, sys, time, pyperclip, requests, bs4, urllib, os, logging, random

os.chdir('C:\\Users\\haesh\\Documents\\pythonProj\\Scraping')
logging.basicConfig(filename='sorting_log_xkcdScrapeParse.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('start of program\n\n\n')


urlhome = 'https://xkcd.com/'
path = 'C:\\Users\\haesh\\Documents\\pythonProj\\Scraping\\scrapeOutput' #path for output


#randomises the comic
def createRandomSite():
    rand = random.randint(1,9999)
    print("random is:  " +str(rand))
    urlhome = 'https://xkcd.com/' + str(rand)+'/'
    print("url is:  "+str(urlhome))
    logging.debug('\n\ncreated random url:  '+str(urlhome))
    return urlhome

def createSpecificSite(i=1):
    print("number is:  " +str(i))
    urlhome = 'https://xkcd.com/' + str(i) +'/'
    print("url is:  "+str(urlhome))
    logging.debug('\n\ncreated specific url:  '+str(urlhome))
    return urlhome


#returns every img in website
def getComic(url):
    try:
        data3 = requests.get(url)
        data3.raise_for_status()
    except: return
    soup1 = bs4.BeautifulSoup(data3.text, 'html.parser')
    imgs = soup1.find_all('img')
    srcs = []
    for a in imgs:
        srcs.append(a['src'])
        print(srcs)
    logging.debug('built array of img src:  {}'.format(srcs))
    return srcs

#checks for https: and adds if not
def checkIfHTTPS(add=''):
    try:
        print(add)
        if(add[:2]=='//'):
            print("no https")
            add='https:' + add
    except: print("not a string")
    return add

#takes imgs sources, saves to path
def saveToFile(arr=[], path1=''):
    if(type(arr) is not list):          #if nothing in website
        return
    for i in range(len(arr)):
        try:
            name =arr[i].rsplit('/', 2)[-1]
            print("test name   " + name)
            if(os.path.exists(path+"\\"+name)==True):
                print("exist=True")
                if(os.path.getsize(path+"\\"+name)>0):
                    print("size>0")
                    continue
                else:
                    imgfile = open(path1 + "\\" + name, 'wb')
                    arri = checkIfHTTPS(arr[i])
                    imgfile.write(urllib.request.urlopen(arr[i]).read())
                    logging.debug('saved to file (updated):  {}'.format(arr[i]))
                    imgfile.close()
            else:
                imgfile = open(path1 + "\\" + name, 'wb')
                print(arr[i])
                if(arr[i][:2]=='//'):
                    print("no https")
                    arr[i]='https:' + arr[i]
                imgfile.write(urllib.request.urlopen(arr[i]).read())
                logging.debug('saved to file (new):  {}\n\n'.format(arr[i]))
                imgfile.close()

        except: print("exception")

#run
def randomComic():
    logging.debug('started randomComic')
    while(True):
        saveToFile(getComic(str(createRandomSite())), path)

def runFromZero():
    logging.debug('started runFromZero')
    for i in range(9999):
        saveToFile(getComic(str(createSpecificSite(i))), path)
        logging.debug('run from zero index:  {}'.format(i))
        print("\n")

def runSpecificIndex(i=1):
    if(i>0):
        if(i<10000):
            saveToFile(getComic(str(createSpecificSite(i))), path)
        else: print("index must be smaller than 10000")
    else: print("index must be larger than 0")

def main():
    logging.debug('started main()')
    inp = input("scrape random, by order or specific index?\n\nr/o/s?   ")
    logging.debug('input is:  {}  '.format(inp))
    if(inp=='r'):
        randomComic()
    elif(inp=='o'):
        runFromZero()
    elif(inp=='s'):
        i = int(input("what index?  "))
        runSpecificIndex(i)
    else:
        logging.debug('input {} is not valid'.format(inp))
        print("not valid input!")
    time.sleep(4)

if(__name__=="__main__"):
    main()

#saveToFile(getComic(str(createSpecificSite(260))), path)
