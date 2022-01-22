import webbrowser, sys, time, pyperclip, requests, bs4, urllib, logging, os

os.chdir('C:\\Users\\haesh\\Documents\\pythonProj\\Scraping')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

logging.basicConfig(filename='sorting_log_scrapeRubiks.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)
logging.debug('start of program\n\n\n')


url = "https://scrapethissite.com/lessons/sign-up/"
response = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(response.text, "html.parser")
aas = soup.find_all('img')
logging.debug('created aas')

print(aas)
#print(aas)

image_srcs = []
for a in aas:
    try:
        image_srcs.append(a['src'])
    except: print("exception")
logging.debug('finished for a in aas')
logging.debug(image_srcs)

url = url.rsplit('/', 3)[0]
address = url + image_srcs[2]
print(address)
header = image_srcs[2].rsplit('/', 3)[-1]
print('header:   '+header)
imgfile = open(header, 'wb')
imgfile.write(urllib.request.urlopen("https://imgs.xkcd.com/comics/thermometer.png").read())
imgfile.close()


print("\n\n\nimage srcs ending:  {}\n\n".format(image_srcs))
