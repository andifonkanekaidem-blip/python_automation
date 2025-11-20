Quotes Web Scraper (Python)

A Python script that scrapes quotes from [Quotes to Scrape](http://quotes.toscrape.com) and saves them into a CSV file.  
Built using **Selenium** with the **Edge WebDriver**.

## Features
- Scrapes quotes text and author name
- Handles multiple pages automatically
- Saves scraped data into a CSV file
- Easy to modify for other websites

## Requirements
- Python 3.x
- Selenium (`pip install selenium`)
- Microsoft Edge WebDriver (compatible with your Edge version)
- pandas (`pip install pandas`)

## How It Works
1. The script opens Edge using Selenium.
2. Navigates through pages on the website.
3. Extracts quotes and author information.
4. Stores data in a CSV file (`quotes.csv` by default).

## Usage
1. Download Edge WebDriver and ensure it’s in your PATH.
2. Place `web_scraper.py` in your project folder.
3. Run the script: python web_scraper.py

4. Check quotes.csv for the scraped data.

## WebDriver
To run this scrapper, download the correct Edge WebDriver version from Microsoft:
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

Place `msedgedriver.exe` inside the `EdgeDriver` folder


