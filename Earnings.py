from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from time import sleep
# Set up the Selenium driver
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the URL

# Extract the table data
data = []
driver.get('https://english.mubasher.info/countries/eg/earnings')
for i in range(1000):
    while True:
        try:
            table = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                        'tbody[class="mi-table__tbody"]'
                                                                                        )))
            rows = table.find_elements(By.TAG_NAME, 'tr')
            for row in rows:
                cells = row.find_elements(By.TAG_NAME, 'td')
                if len(cells) > 0:
                    data.append({
                            'Currency': cells[6].text,
                            'Company': cells[0].text,
                            'Announced': cells[2].text,
                            'Compared': cells[3].text,
                            'Budget Status': cells[5].text
                    })
            next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Next')))
            next_button.click()
            sleep(2)
        except: 
            print('Error Occured at {}; Retrying'.format(i+1))
            sleep(2)
            continue
        else:
            print('Success at {}; Proceeding onto next'.format(i+1))
            df = pd.DataFrame(data)
            df.to_csv('InsiderTrades.csv')
            break

