# Google Maps Webscraper 
This is a web scraper program powered by Python, Selenium Webdriver, Pandas, CSV and Time library that provides the functions such as extracting the data found on every local from Google Maps, saving into the local storage and saving them as csv and xlsx formats.
I hope to implement it a simple UI using Tkinter library in the future to improve the program presentation. :ok_hand:	

## Setup of dependencies
To install the libraries needed for the program on Windows.
1. Selenium: `pip install selenium`. Also you will need to install the specific ChromeDriver for your navigator in the rute `C:\bin\chromedriver.exe` or you can change it on the line no. 68 of the main.py file.
2. Time: `pip install time`
3. CSV: `pip install csv`
4. Pandas: `pip install pandas`

## How do I use it?
1. Clone this repo to your desktop.
2. Install the dependencies and the chromedriver into the correct path.
3. Execute the main.py program.
4. Write down on the terminal program the type of business you are looking for and press Enter.
5. Finally digit the number of information you want (Integer only) and wait for the results.

## Which data does it extract?
The program extract the next information from every business found in case it's registered, otherwise the datacell will appear empty.
- Business name.
- Business title.
- Address.
- Phone.
- Amount starts.
- Amount of reviews.

### Warning :warning:
This program was created, tested and used specifically for the Colombian Google Maps webpage :colombia:. In case you will use it in other location the HTML tags, xpath and CSS selectors must be changed depending on the country.

Thank you! :heart:
