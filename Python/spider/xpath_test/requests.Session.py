import requests
import urllib,urllib.request
import lxml
import lxml.html as HTML
import lxml.etree as etree

url ='http://www.baidu.com'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1 '}
# data1 = urllib.request.Request(url, headers=headers)
# data = urllib.request.urlopen(data1).read()
# print(urllib.request.urlopen(url).getcode())
MAX_RETRIES = 20
# url ='http://eutils.ncbi.nlm.nih.gov/entrez/eutils/einfo.fcgi'

session = requests.Session()
adapter = requests.adapters.HTTPAdapter(max_retries=MAX_RETRIES)
# session.mount('https://', adapter)
# session.mount('http://', adapter)

r = session.get(url)
print(r.content.decode('utf-8'))
