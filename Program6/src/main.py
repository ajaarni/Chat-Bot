#######################################
# Created by antonaarnink at 4/4/22
# Version: 0.0.1
# Copyright: Copyright 2022©
#######################################
from scraper import WebScraper
from processor import process
import time
import os


def main():
    path = os.getcwd().removesuffix("/src")
    WebScraper()
    start = time.time()

    print("What district do you have questions about?")
    district = input()

    if district != "35":
        print("I do not have information on that district ?")
        exit()

    print("You have selected district: " + district)
    process()

    end = time.time()
    # writes the usage time to the stats.txt file
    with open(path + "/data/stats.txt", "a") as file:
        runtime = round(end - start, 2)
        str1 = "***You were on this chat for"
        str2 = "seconds. Thank you, and come again!***"
        str3 = " ".join([str1, str(runtime), str2])
        file.write(str3)
        file.write("\n")
        file.close()


if __name__ == '__main__':
    main()
