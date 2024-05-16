import requests
import pandas as pd


url = "https://english.mubasher.info/api/1/financial-ratios"
params = {
    "exchangeCode": "EGX",
    "desc": "false",
    "quarter": "14",
    "sort": "roe"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://english.mubasher.info/analysis-tools/financial-ratios/EGX",
    "Cookie": "logged_in=0; selected_country=EG; UUID=42dfd073-5b57-41fc-8cec-b7a192afc7b6; UserCountryCode=EG; TESTUUID=42dfd073-5b57-41fc-8cec-b7a192afc7b6",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    # write data to CSV file
    df = pd.DataFrame(data['rows'])
    print(df)
    df.to_csv(r"D:\my stuff\LSTM Papers\Scraper\Scrapers\finraats.csv", index=False)
else:
    print(f"Error: {response.status_code}")