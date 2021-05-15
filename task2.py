from requests_html import HTMLSession
import csv

session = HTMLSession()
result = []
url = 'https://www.mohfw.gov.in/'
response = session.get(url)
container = response.html.find('.tab-content', first=True)
pdfs = container.find('li')
for pdf in pdfs:
    try:
        link = pdf.links
    except:
        break
    try:
        text = pdf.text.replace(' ', '_')
    except:
        break
    result.append([text, link])
    print(result)

with open('results.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(result)
