# Selenium-car-project🚗

## How it works
This app gets data from https://www.olx.pl/motoryzacja/samochody/bialystok/?search%5Border%5D=filter_float_price%3Adesc&page=1 and next pages of this site.

Then it writes offer name and price to Dataframe and retuns it.

In next step program outputs car count where price is bigger than 700.000, 

or the price is between 700.000 and 300.000, or price is less than 300.000.

At the end it displays a chart with all prices.

## Setup

First of all you need to install `driver` for your website.

Check this link for drivers:

https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

I am using chromedriver here.
To start the program go to the project folder.
 ```
C:\Users\user> cd Selenium-car-projekt
```
Then just run `car_data_downloader.py` file:
 ```
C:\Users\user\Selenium-car-projekt> python car_data_downloader.py
```

## Note
It could not work correctly for many pages.
