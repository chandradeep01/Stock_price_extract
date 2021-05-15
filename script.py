import requests
from bs4 import BeautifulSoup

f_urls = open('urls.txt', 'r')
f_result = open('result.txt', 'w')
for data in f_urls.readlines():
    stock,url=data.split("|")
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='top')
    #print(results.prettify())
    job_elems = results.find_all('span', class_='number')
    stk_price=(str(job_elems[1]).split(">")[1].split("<")[0])
    print(stock,stk_price)
    f_result.writelines(stock+"|"+stk_price+"\n")


f_urls.close()
f_result.close()
