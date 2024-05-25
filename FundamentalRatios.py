from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Create a new Chrome session
driver = webdriver.Chrome()

# Navigate to the financial ratios page
def scrape(q):
            """
    Scrapes financial ratios data from Mubasher Egypt for the specified quarter.

    Args:
        quarter (str): The quarter to scrape data for (e.g., "First Quarter").

    Returns:
        pandas.DataFrame: A DataFrame containing the scraped data.
    """
        driver.get("https://english.mubasher.info/analysis-tools/financial-ratios/EGX")
        time.sleep(5)
        # Select the "Fourth Quarter" option from the drop-down menu
        quarter_dropdown = driver.find_element(By.CSS_SELECTOR, "select[st-search='quarter']")
        time.sleep(5)
        quarter_dropdown.click()
        time.sleep(5)
        quarter_dropdown.send_keys(q)
        time.sleep(5)
        quarter_dropdown.send_keys(Keys.ENTER)
        # Save the table to a CSV file
        table = driver.find_element(By.CSS_SELECTOR, 'tbody[class="mi-table__tbody"]')
        time.sleep(5)
        rows = table.find_elements(By.TAG_NAME, 'tr')
        time.sleep(5)
        data = []
        for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                if len(cells) > 0:
                        print(cells[6].text)
                        data.append({

                                'Company': cells[0].text,
                                'EPS': cells[1].text,
                                'Dividend Per Share': cells[2].text,
                                'BVPS': cells[3].text,
                                'P/E': cells[4].text,
                                'P/B': cells[5].text,
                                'ROE': cells[6].text
                        })
                        
        time.sleep(5)      
        df = pd.DataFrame.from_dict(data)

        df.to_csv(r'D:\my stuff\LSTM Papers\Scraper\Scrapers\FundamentalData' + f'{q}'  + '.csv')


scrape('First Quarter')
