# Created by antonaarnink at 4/4/22
import requests
from bs4 import BeautifulSoup
from loadingAnimation import loading
import time
import os


def WebScraper():
    start = time.time()
    loading()
    path = path = os.getcwd().removesuffix("/src")
    with open(path + "/data/output.txt", "w") as file:
        file2 = open(path + "/data/stats.txt", "a")
        file2.truncate(0)

        url = "https://www.scstatehouse.gov/member.php?code=351704504"
        # url2 = "https://www.scstatehouse.gov/sponsorsearch.php"
        page = requests.get(url)
        # page2 = requests.get(url2)

        soup = BeautifulSoup(page.content, 'lxml')
        # soup2 = BeautifulSoup(page2.content, 'lxml')

        # data = []
        # table = soup2.find_all('table', style="text-align:right")
        # table_body = table.find('tbody')
        #
        # rows = table_body.find_all('tr')
        # for row in rows:
        #     cols = row.find_all('td')
        #     cols = [ele.text.strip() for ele in cols]
        #     data.append([ele for ele in cols if ele])  # Get rid of empty values

        # results = soup.find_all(id="contentsection", text=True)

        name = soup.find("h2", class_="barheader").get_text().strip()

        file.write(name + '\n')

        # removes unused html so results later do not include
        soup.find('div', id='menu').decompose()
        soup.find('div', id="search").decompose()
        soup.find('div', id="submenu").decompose()
        soup.find('div', id="sidebar").decompose()
        soup.find('div', id="footer").decompose()
        soup.find('div', id="printfooter").decompose()
        for dat in soup(['form', 'script']):
            # Remove tags
            dat.decompose()

        for data in soup.find_all("p"):
            # print(data.get_text())

            file.write(data.get_text(separator='\n').strip() + '- \n')

        for data2 in soup.find_all("li"):
            line = "{0}: {1}".format(data2.name, data2.text)
            if line != "*Search Session*":
                file.write("{0}: {1}".format(data2.name, data2.text) + '\n')
        # print(data2.get_text())

        # file.write(data2.get_text(separator='\n').strip() + '- \n')

        # print(map)
        # print(data)
        file.close()
        page.close()
        end = time.time()
        runtime = round(end - start, 2)
        str1 = "***It took"
        str2 = "seconds to get information from the internet.***"
        str3 = " ".join([str1, str(runtime), str2])
        file2.write(str3)
        file2.write("\n")
        file2.close()
