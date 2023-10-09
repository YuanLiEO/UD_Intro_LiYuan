
import requests
from bs4 import BeautifulSoup
if __name__ == "__main__":


    headers={"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}

    content = requests.get("https://movie.douban.com/top250", headers=headers)
    HTML= content.text

    soup= BeautifulSoup(HTML,"html.parser")
    all_title= soup.findAll("span", attrs={"class": "title"})
    for t in all_title:
        print(t)

    print("helloworld")