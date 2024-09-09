import requests
from bs4 import BeautifulSoup

web=requests.get("https://quotes.toscrape.com/")
soup=BeautifulSoup(web.content,'html.parser')
quotes=soup.find_all('span',class_='text')
authors=soup.find_all('small',class_='author')
index=1
for quote, author in zip(quotes, authors):
    quote_text=quote.text
    author_text=author.text
    print(f"{index}> Quote :{quote_text}")
    print(f"Author: {author_text}\n")
    index+=1;
    
