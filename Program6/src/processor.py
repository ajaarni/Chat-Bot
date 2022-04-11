# Created by antonaarnink at 4/4/22
import re
import sys
import os
from scraper import WebScraper

path = os.getcwd().removesuffix("/src")
with open(path + "/data/output.txt", "r+") as data:
    personal_info = []
    phone_numbers = []
    all_info = []
    addresses = []
    committee_assign = ""
    service_length = ""
    fullname = ""

    lines = data.readlines()
    fullname = lines[0]
    addresses = [lines[7], lines[8], lines[11], lines[12]]
    for line in lines:
        all_info.append(line)
    for line in lines:
        if "li:" in line:
            personal_info.append(line.strip().split(':')[1])
        if line.startswith(" (8"):
            phone_numbers.append(line.strip())

    committee_assign = personal_info[-2]
    service_length = personal_info[-1]


def process():
    with open(path + "/data/stats.txt", "a") as file:
        count = 0

        # promoting the user to as a question
        print("What would you like to know about the representative? You can quit at any time just say so.")
        ans = input().lower()

        # lists on known keywords to match user input to
        personal_info_list = ["info", "about", "from"]
        phone_info_list = ["phone", "number", "contact", "homephone"]
        name_list = ["name", "full name", "last name", "who"]
        committee_list = ["committee"]
        service_list = ["service", "record", "long", "served"]
        address_list = ["live", "where", "address"]
        quit_cases = ["q", "quit", "exit", "bye", "goodbye"]
        all_list = ["everything", "all"]

        # starting while loop while the users answer is not a quit case
        while ans not in quit_cases:
            # searching the users answer for keywords and returning the values while writing a history to the
            # stats.txt file
            for element in personal_info_list:
                if re.search(element, ans, re.IGNORECASE):
                    print(personal_info)
                    for el in personal_info:
                        file.write(el)
                        file.write("\n\n")
                    sys.stdout.flush()
                break

            for element in phone_info_list:
                if re.search(element, ans, re.IGNORECASE):
                    print(phone_numbers)
                    for el in phone_numbers:
                        file.write(el)
                        file.write("\n\n")
                    sys.stdout.flush()
                break

            for element in name_list:
                if re.search(element, ans, re.IGNORECASE):
                    print(fullname)
                    file.write(fullname)
                    file.write("\n")
                    sys.stdout.flush()
                break

            for element in committee_list:
                if re.search(element, ans, re.IGNORECASE):
                    print(committee_assign)
                    file.write(committee_assign)
                    file.write("\n\n")
                    sys.stdout.flush()
                break

            for element in service_list:
                if re.search(element, ans, re.IGNORECASE):
                    print(service_length)
                    file.write(service_length)
                    file.write("\n\n")
                    sys.stdout.flush()
                break

            for element in address_list:
                if re.search(element, ans, re.IGNORECASE):
                    print(addresses)
                    for el in addresses:
                        file.write(el)
                        file.write("\n\n")
                    sys.stdout.flush()
                break

            # if the question is not matched to a know keyword then we will track the number of times this has
            # occurred and write it to the stats.txt file

            # promoting the user to ask another question
            print("What would you like to know about the representative? You can quit at any time just say so.")
            ans = input().lower()

        print("Thank you for visiting the chat bot! Come again soon!")
        with open(path + "/data/stats.txt", "a") as stat:
            stat.write(str(count))
            stat.write(" queries that couldn't be answered")
            stat.write("\n")
        stat.close()
    file.close()
