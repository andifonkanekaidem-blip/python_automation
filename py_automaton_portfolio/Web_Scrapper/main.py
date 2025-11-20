import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import pandas as pd
import time
import re
import logging
logging.basicConfig(
    filename="app.log",
    filemode='a',
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def clean_text(t):
    return re.sub(r'[“”]',"",t).strip()

# ---------------------------------------------------
# 1. Setup Edge driver
# ---------------------------------------------------
def setup():
    try:
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080')
        try:
            service = Service(executable_path=r"\EdgeDriver\msedgedriver.exe")
            driver = webdriver.Edge(service=service,options=options)
        except:
            logging.error("Driver couldn't be found")
            print("Driver couldn't be found")
            sys.exit(1)
        driver.get("https://quotes.toscrape.com/login") #A site which contains quotes and allows scrapping using selenium

        time.sleep(2)  # Let page load
        return driver
    except Exception as w:
        et = f"Failed to start driver: {w}"
        if "net::ERR_INTERNET_DISCONNECTED" in et:
            logging.error(f"Failed to start driver: Check Network connection")
        print("Something went wrong check logs")
        driver.quit()
        sys.exit(1)
# ---------------------------------------------------
# 2. Open login page
# ---------------------------------------------------

# ---------------------------------------------------
# 3. Enter login details
# ---------------------------------------------------
def login(driver,username,password):
    try:
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        username_input.send_keys(username)
        password_input.send_keys(password)  # Demo site accepts any login

        login_button = driver.find_element(By.CSS_SELECTOR, "input[type=submit]")
        login_button.click()

        time.sleep(2)
    except Exception as e:
        et = f"Failed to start driver: {e}"
        if "no such element" in et:
            logging.error(f"Couldn't find an element. Check selectors")
        print("An Element was not found")
        driver.quit()
        sys.exit(0)
# ---------------------------------------------------
# 4. Scrape quotes from all pages
# ---------------------------------------------------


def scrape(driver,number_of_pages):
    all_quotes = []
    b = 0
    while b < number_of_pages:
        try:
            quotes = driver.find_elements(By.CLASS_NAME, "quote")

            for q in quotes:
                text = q.find_element(By.CLASS_NAME, "text").text
                cleaned_text = clean_text(text)
                author = q.find_element(By.CLASS_NAME, "author").text
                tags = [tag.text for tag in q.find_elements(By.CLASS_NAME, "tag")]

                all_quotes.append({
                    "Quote": cleaned_text,
                    "Author": author,
                    "Tags": ", ".join(tags)
                })

                b+=1 #Increment 'b'
                # Check for "Next" button
            try:
                next_btn = driver.find_element(By.CSS_SELECTOR, "li.next a")
                next_btn.click()
                time.sleep(2)
            except:
                print("Number of pages required is more than available")
                break
        except Exception as e:
            logging.error(f"Something went wrong: {e}")
            driver.quit()
            sys.exit(1)
    return all_quotes


# ---------------------------------------------------
# 5. Save to CSV
# ---------------------------------------------------
def save(filepath,list_):
    try:
        df = pd.DataFrame(list_)
        df.to_csv(filepath, index=False)
    except FileExistsError:
        logging.error(f"File exists")
    except Exception as e_:
        logging.error(f"Something went wrong: {e_}")
        sys.exit(0)
    print(f"Scraping complete. Data saved to {filepath}")

if __name__ == "__main__":
    """Modify these as needed"""
    d = setup()
    login(d,"Andifonkan","pass")
    l = scrape(d,2)
    save("res.csv",l)
