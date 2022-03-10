from re import search
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import matplotlib.pyplot as plt

# INSTALL CHROMEDRIVER.EXE
PATH = r'C:/Users/am/selenium/chromedriver.exe'

driver = webdriver.Chrome(PATH)

print("START")

names_tab = []
prices_tab = []
car_count = 0
count_bigger_than_700 = 0
count_700_300 = 0
count_less_than_300 = 0

driver.get("https://www.olx.pl/motoryzacja/samochody/bialystok/?search%5Border%5D=filter_float_price%3Adesc&page=1")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "onetrust-accept-btn-handler"))
    )
    element.click()
finally:
    for i in range(1, 6):
        driver.get(f"https://www.olx.pl/motoryzacja/samochody/bialystok/?search%5Border%5D=filter_float_price%3Adesc&page={i}")

        offers = driver.find_elements_by_class_name("offer")
        for offer in offers:
            if "promoted" in offer.get_attribute("class"):
                continue
            offer = offer.text.split("\n")
            names_tab.append(offer[0])
            price = offer[1].replace(" ", "")
            price = price[:-2] #zl removed
            if "," in price:    #grosze removed
                price = price[:-3]
            price = int(price)  #to int
            prices_tab.append(price)

            car_count += 1
            if price > 700000:
                count_bigger_than_700 += 1
            if price < 700000 and price > 300000:
                count_700_300 += 1
            if price < 300000 :
                count_less_than_300 += 1

    driver.close()

    data = {'Name':names_tab, 'Price':prices_tab}
    df = pd.DataFrame(data)
    print(df)
    df.to_csv('cars_df', index=False)

    print(f"Car count: {car_count}")
    print(f"Car price bigger than 700 000: {count_bigger_than_700}")
    print(f"Car price between 700 000 - 300 000: {count_700_300}")
    print(f"Car price less than 300 000: {count_less_than_300}")

    plt.hist(df['Price'], car_count)
    plt.title("Prices")
    plt.show()
