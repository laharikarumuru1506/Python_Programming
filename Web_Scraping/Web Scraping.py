from bs4 import BeautifulSoup
import requests
import webbrowser

url='https://coreyms.com/'
r=requests.get(url).text
soup=BeautifulSoup(r,"html5lib")
#print(soup.prettify())
article=soup.find("article")
#print(article.prettify())

#headline=article.h2.a.text
#print(headline)
#print()

#summary=article.find("div",class_="entry-content").p.text
#print(summary)

vid_link=article.find("iframe",class_="youtube-player")["src"]
#print(vid_link.prettify())
#print(vid_link)

vid_id=vid_link.split('/')[4]
vid_id=vid_id.split('?')[0]
#print(vid_id)

yt_link="https://youtube.com/watch?v={}".format(vid_id)
#print(yt_link)

webbrowser.open_new_tab(yt_link)
