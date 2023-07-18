import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys

def phone_data(URL, id):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    mobile_list = soup.findAll(attrs={"class": "p4 biggertext"})
    phone_names = mobile_list[id].text.replace("\n", "")

    mobile_price = soup.findAll(attrs={"class": "PriceFont"})
    phone_prices = mobile_price[id].text.replace("\n", "")

    data_set = [[phone_names, phone_prices]]
    df = pd.DataFrame(data_set, columns=["Names", "Prices"])
    return df

def main():
    if len(sys.argv) < 3:
        print("!!!!!WRONG INPUT")
        sys.exit(1)

    brand = sys.argv[1]
    phone_index = int(sys.argv[2])

    if brand.lower() == "samsung":
        URL = "https://www.whatmobile.com.pk/Samsung_Mobiles_Prices"
    elif brand.lower() == "apple":
        URL = "https://www.whatmobile.com.pk/Apple_Mobiles_Prices"
    elif brand.lower() == "huawei":
        URL = "https://www.whatmobile.com.pk/Huawei_Mobiles_Prices"
    else:
        print("Invalid brand name.")
        sys.exit(1)

    df = phone_data(URL, phone_index)
    CSV = f"{brand}_Phone_{phone_index}_Data.csv"
    df.to_csv(CSV, index=False)
    print("Data saved to", {CSV})

if __name__ == "__main__":
    main()

