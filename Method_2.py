import requests
from bs4 import BeautifulSoup

url = 'https://www.mohfw.gov.in/'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
urls = soup.find('div', attrs={"class" : "tab-content"})
a_tags = urls.find_all('a')
for atag in a_tags:
    link = atag['href']
    title = atag.get_text().strip()
    try:
        with open(title.replace(' ', "_") + '.pdf', 'wb') as f:
            get_res = requests.get(link)
            f.write(get_res.content)
            print(title)
    except:
        pass
