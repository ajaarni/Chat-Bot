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

        page = requests.get(url)

        soup = BeautifulSoup(page.content, 'lxml')

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
            file.write(data.get_text(separator='\n').strip() + '- \n')

        for data2 in soup.find_all("li"):
            line = "{0}: {1}".format(data2.name, data2.text)
            if line != "*Search Session*":
                file.write("{0}: {1}".format(data2.name, data2.text) + '\n')

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
