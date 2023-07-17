import requests
from bs4 import BeautifulSoup


def Samsung_mobiles_list ():
    URL1="https://www.whatmobile.com.pk/Samsung_Mobiles_Prices" #URL For Samsung
    page_for_Samsung=requests.get(URL1)
    soup_for_samsung=BeautifulSoup(page_for_Samsung.content,"html.parser")

    rows_for_samsung=soup_for_samsung.findAll("div",class_="mobiles")
    for i in rows_for_samsung:
        print(i.text)

def SamsungMobile1():
    URL_for_samsung1_mobile="https://m.whatmobile.com.pk/Samsung_Galaxy-Z-Fold-4-12GB"
    page1=requests.get(URL_for_samsung1_mobile)
    soup1=BeautifulSoup(page1.content,"html.parser")
    rows1=soup1.findAll("div",class_="specs_box")
    for i in rows1:
        print(i.text)

def SamsungMobile2():
    URL_for_samsung2_mobile="https://m.whatmobile.com.pk/Samsung_Galaxy-S23-Ultra"
    page2=requests.get(URL_for_samsung2_mobile)
    soup2=BeautifulSoup(page2.content,"html.parser")
    rows2=soup2.findAll("div",class_="specs_box")
    for i in rows2:
        print(i.text)


def SamsungMobile3():
    URL_for_samsung3_mobile="https://m.whatmobile.com.pk/Samsung_Galaxy-Z-Flip-4"
    page3=requests.get(URL_for_samsung3_mobile)
    soup3=BeautifulSoup(page3.content,"html.parser")
    rows3=soup3.findAll("div",class_="specs_box")
    for i in rows3:
        print(i.text)


def HuaweiMobile():
    URL1="https://www.whatmobile.com.pk/Huawei_Mobiles_Prices" #URL For Huawei
    page_for_Huawei=requests.get(URL1)
    soup_for_Huawei=BeautifulSoup(page_for_Huawei.content,"html.parser")

    rows_for_Huawei=soup_for_Huawei.findAll("div",class_="mobiles")
    for i in rows_for_Huawei:
        print(i.text)

def Huawei_P30_Pro():
    URL_for_huawei1_mobile="https://www.whatmobile.com.pk/Huawei_P30-Pro"
    page1=requests.get(URL_for_huawei1_mobile)
    soup1=BeautifulSoup(page1.content,"html.parser")
    rows_for_p30_pro=soup1.findAll("table",class_="specs")
    for i in rows_for_p30_pro:
        print(i.text)

def Huawei_Mate_20_pro():
    URL_for_huawei2_mobile="https://www.whatmobile.com.pk/Huawei_Mate-20-Pro"
    page2=requests.get(URL_for_huawei2_mobile)
    soup2=BeautifulSoup(page2.content,"html.parser")
    rows_for_Mate_20_Pro=soup2.findAll("table",class_="specs")
    for i in rows_for_Mate_20_Pro:
        print(i.text)

def Vivo_Phones():
    URL_for_Vivo_Phones="https://www.whatmobile.com.pk/Vivo_Mobiles_Prices"
    page_for_Vivo_prices=requests.get(URL_for_Vivo_Phones)
    soup_for_Vivo=BeautifulSoup(page_for_Vivo_prices.content,"html.parser")
    rows_for_Vivo_phones=soup_for_Vivo.findAll("div",class_="mobiles")
    for i in rows_for_Vivo_phones:
        print(i.text)

def Vivo_X_80():
    URL_for_Vivi_X_80="https://www.whatmobile.com.pk/Vivo_X80"
    page_for_Vivo_X_80=requests.get(URL_for_Vivi_X_80)
    soup_for_Vivo_X_80=BeautifulSoup(page_for_Vivo_X_80.content,"html.parser")
    rows_for_Vivo_X_80=soup_for_Vivo_X_80.findAll("table",class_="specs")
    for i in rows_for_Vivo_X_80:
        print(i.text)

def Vivo_V25():
    URL_for_Vivo_V25="https://www.whatmobile.com.pk/Vivo_V25"
    page_for_Vivo_V25=requests.get(URL_for_Vivo_V25)
    soup_for_Vivo_V25=BeautifulSoup(page_for_Vivo_V25.content,"html.parser")
    rows_for_Vivo_V25=soup_for_Vivo_V25.findAll("table",class_="specs")
    for i in rows_for_Vivo_V25:
        print(i.text)


while (1):
    print("\nFollowing Are The Mobiles List")
    print("\n1-Samsung Phones")
    print("\n2-Huawei Phones")
    print("\n3-Vivo Phones")
    ch=int(input("Enter Option"))
    if ch == 1:
        Samsung_mobiles_list()
        print("\nThis is the List for Samsung Mobiles")
        print("\nCheck Specifications of 3 Mobiles")
        print("\n1-Samsung Galaxy Z Fold 4 ")
        print("\n2-Samsung Galaxy S-23 Ultra")
        print("\n3-Samsung Galaxy Z Flip 4")
        ch2=int(input("Enter choice for check specifications"))

        if ch2 == 1:
            SamsungMobile1()
        elif ch2==2:
            SamsungMobile2()
        elif ch2==3:
            SamsungMobile3()
        else:
            print("Wrong Option")

    elif ch == 2:
        HuaweiMobile()
        print("\nThis is the List for Huawei Mobiles")
        print("\nCheck Specifications of 2 Mobiles")
        print("\n1-Huawei P30-Pro ")
        print("\n2-Huawei Mate 20 Pro")
        ch3=int(input("Enter Mobile ID to check Specifications"))

        if ch3 == 1:
            Huawei_P30_Pro()
        elif ch3 == 2:
            Huawei_Mate_20_pro()
        else:
            print("Back to Main Menu")

    elif ch == 3:
        Vivo_Phones()
        print("\nThis is the List for Vivo Mobiles")
        print("\nCheck Specifications of 2 Mobiles")
        print("\n1-Vivo V-80 ")
        print("\n2-Vivo V-25")
        ch4=int(input("Enter Mobile ID to check Specifications"))

        if ch4 == 1:
            Vivo_X_80()
        elif ch4 == 2:
            Vivo_V25()
        else:
            print("Back to Main Menu")

