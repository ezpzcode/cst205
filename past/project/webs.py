import urllib.request
from bs4 import BeautifulSoup
 
print('Beginning file download with urllib2...')
 
url = http://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project_%28454045%29.jpg/220px-Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project_%28454045%29.jpg" decoding="async" width="220" height="278" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project_%28454045%29.jpg/330px-Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project_%28454045%29.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project_%28454045%29.jpg/440px-Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project_%28454045%29.jpg 2x"
req = urllib.request.Request(url)
res = urllib.request.urlopen(url).read()
 
soup = BeautifulSoup(res,'html.parser')
soup = soup.find("div",class_="poster")
#img의 경로를 받아온다
imgUrl = soup.find("img")["src"]
 
#urlretrieve는 다운로드 함수
#img.alt는 이미지 대체 텍스트 == 마약왕
urllib.request.urlretrieve(imgUrl, soup.find("img")["alt"]+'.jpg')


