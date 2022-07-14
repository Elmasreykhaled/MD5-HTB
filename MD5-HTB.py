import requests
from bs4 import BeautifulSoup
import hashlib
url = "http://134.209.29.219:31496/"
#r = requests.sessions()
resp = requests.get(url)
soup = BeautifulSoup(resp.content)
string = soup.select('h3')[0].txt
hash_txt = hashlib.md5(string.encode('utf-8')).hexdigest()
sent = requests.post(url=url, data={'hash': hash_txt})
print(sent.txt)
