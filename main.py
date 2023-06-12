from bs4 import BeautifulSoup
import requests, openpyxl

excel = openpyxl.Workbook()
sheet=excel.active
sheet.title="shows_list"
sheet.append(['Rank','Show_name','Year of release','IMDB Rating '])

try:
    response = requests.get("https://www.imdb.com/chart/toptv/")
    soup = BeautifulSoup(response.text,'html.parser')
    shows = soup.find('tbody',class_="lister-list").find_all("tr")

    for show in shows:
        rank = show.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        show_name = show.find('td',class_="titleColumn").a.text
        rate = show.find('td', class_="ratingColumn").strong.text
        year = show.find('td', class_="titleColumn").span.text.replace('(',"")
        year = year.replace(')',"")
        sheet.append([rank,show_name,year,rate])
except Exception as e:
    print(e)

excel.save("scraped_data.xls")