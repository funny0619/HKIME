# get a list of characters from dictionary to match frequency

import requests
from bs4 import BeautifulSoup
import math
from time import sleep
total_levels = 5
page = 0
count = 0
for level in range(1, total_levels+1):
    URL = "http://www.cantonese.sheik.co.uk/scripts/wordlist.htm?action=&wordtype=0&level=" + \
        str(level)+"&page="+str(page)
    # page is 0 indexed
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
    h3 = soup.find('h3')
    total_chars = int(h3.text.split()[3])
    total_pages = math.ceil(total_chars/20)
    for page in range(total_pages):
        URL = "http://www.cantonese.sheik.co.uk/scripts/wordlist.htm?action=&wordtype=0&level=" + \
            str(level)+"&page="+str(page)
        # page is 0 indexed
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser', from_encoding='utf-8')
        table = soup.find_all('a', attrs={'class': 'wordlink'})
        for word in table:
            dataFile = open("dictionary_list.txt", "a", encoding="utf-8")
            dataFile.write(word.text + '\n')
            count += 1
        print("level " + str(level) + " page " + str(page))
        page += 1
        sleep(5)
    print(str(count)+" words in level " + str(level))
    count = 0
    page = 0

dataFile.close()
