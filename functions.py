from datetime import datetime
from lxml import html
from bs4 import BeautifulSoup
from sys import exit


def isUpdated(a, b):
    try:
        return_value = b.index([x for x in b if x not in a][0])
    except IndexError:
        return_value = 69

    matching = True

    if return_value == 69:
        matching = False

    return matching, return_value


def getTime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %I:%M:%S %p")


def initializeClasses(a, b):
    class1 = 0
    try:
        class1 = str(a[0])
        class1 = class1[116:121]
    except IndexError:
        print("Enter a valid six digit Student ID and password!")
        exit(0)

    class2 = 0
    try:
        class2 = str(a[1])
        class2 = class2[116:121]
        if class2 == "":
            class2 = 0
    except IndexError:
        pass

    class3 = 0
    try:
        class3 = str(a[2])
        class3 = class3[116:121]
        if class3 == "":
            class3 = 0
    except IndexError:
        pass

    class4 = 0
    try:
        class4 = str(a[3])
        class4 = class4[116:121]
        if class4 == "":
            class4 = 0
    except IndexError:
        pass

    class5 = 0
    try:
        class5 = str(a[4])
        class5 = class5[116:121]
        if class5 == "":
            class5 = 0
    except IndexError:
        pass

    class6 = 0
    try:
        class6 = str(a[5])
        class6 = class6[116:121]
        if class6 == "":
            class6 = 0
    except IndexError:
        pass

    class7 = 0
    try:
        class7 = str(a[6])
        class7 = class7[116:121]
        if class7 == "":
            class7 = 0
    except IndexError:
        pass

    class8 = 0
    try:
        class8 = str(a[7])
        class8 = class8[116:121]
        if class8 == "":
            class8 = 0
    except IndexError:
        pass

    class_name_1 = "No class"
    try:
        class_name_1 = (str(b[0].text)).strip()
        index_of_deletion = class_name_1.index("-")
        class_name_1 = (class_name_1[index_of_deletion + 4:]).strip()
    except IndexError:
        pass

    class_name_2 = "No class"
    try:
        class_name_2 = (str(b[1].text)).strip()
        index_of_deletion = class_name_2.index("-")
        class_name_2 = (class_name_2[index_of_deletion + 4:]).strip()
    except IndexError:
        pass

    class_name_3 = "No class"
    try:
        class_name_3 = (str(b[2].text)).strip()
        index_of_deletion = class_name_3.index("-")
        class_name_3 = (class_name_3[index_of_deletion + 4:]).strip()
    except IndexError:
        pass

    class_name_4 = "No class"
    try:
        class_name_4 = (str(b[3].text)).strip()
        index_of_deletion = class_name_4.index("-")
        class_name_4 = (class_name_4[index_of_deletion + 4:]).strip()
    except IndexError:
        pass
    class_name_5 = "No class"
    try:
        class_name_5 = (str(b[4].text)).strip()
        dash_index = class_name_5.index("-")
        class_name_5 = (class_name_5[dash_index + 4:]).strip()
    except IndexError:
        pass

    class_name_6 = "No class"
    try:
        class_name_6 = (str(b[5].text)).strip()
        dash_index = class_name_6.index("-")
        class_name_6 = (class_name_6[dash_index + 4:]).strip()
    except IndexError:
        pass

    class_name_7 = "No class"
    try:
        class_name_7 = (str(b[6].text)).strip()
        dash_index = class_name_7.index("-")
        class_name_7 = (class_name_7[dash_index + 4:]).strip()
    except IndexError:
        pass

    class_name_8 = "No class"
    try:
        class_name_8 = (str(b[7].text)).strip()
        dash_index = class_name_8.index("-")
        class_name_8 = (class_name_8[dash_index + 4:]).strip()
    except IndexError:
        pass

    return [class_name_1, class_name_2, class_name_3, class_name_4, class_name_5, class_name_6, class_name_7,
            class_name_8], [class1, class2, class3, class4, class5, class6, class7, class8]


def login(session_requests, login_url, password, username):
    urls = "https://hac.friscoisd.org/HomeAccess/Content/Student/Assignments.aspx"
    result = session_requests.get(login_url)
    print(result)
    tree = html.fromstring(result.text)
    authenticity_token = list(set(tree.xpath("//input[@name='__RequestVerificationToken']/@value")))[0]

    payload = {
        "VerificationOption": "UsernamePassword",
        "Database": "10",
        "LogOnDetails.Password": password,
        "__RequestVerificationToken": authenticity_token,
        "LogOnDetails.UserName": username
    }
    session_requests.post(
        login_url,
        data=payload,
        headers=dict(referer=login_url)
    )

    result = session_requests.get(urls, headers=dict(referer=urls))

    soup = BeautifulSoup(result.text, "html.parser")

    h1 = soup.find_all(class_="sg-header-heading sg-right")

    h2 = soup.findAll('a', {"class": ["sg-header-heading"]})
    return h1, h2


def userInput():
    minutes_per_check = None
    try:
        minutes_per_check = float(input("Per how many minutes should the program check your grades >>> "))
    except ValueError:
        print("Enter a number without any spaces or letters!")
        exit(0)

    print()

    username = input("Enter your Student ID >>> ")
    password = input("Enter your password >>> ")
    spacing = ""

    for i in range(30):
        spacing += "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print(spacing)

    return username, password, minutes_per_check
