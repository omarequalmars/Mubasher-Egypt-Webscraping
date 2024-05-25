# Mubasher Egypt Web Scraping

This Python project consists of four scripts that scrape various data points from Mubasher Egypt.

## Functionality
- InsiderTrades.py: Scrapes insider trading data for all tickers on Mubasher Egypt. Data is collected until a predefined loop counter is reached. This script is designed to run daily to capture the latest insider trades.
- Earnings.py: Scrapes earnings announcements data from Mubasher Egypt. Similar to InsiderTrades.py, this script relies on a loop counter to determine the amount of data collected.
- FundamentalRatios.py: Scrapes fundamental data (P/E Ratio and P/B Ratio) for various stocks on Mubasher Egypt. This script requires a specific quarter as input to retrieve the relevant data.
- LiquidityRatios.py: Scrapes additional data for tickers on Mubasher Egypt, again requiring a specific quarter as input.

## Dependencies
This project requires the following Python libraries:

- Selenium
- BeautifulSoup

## Installation
```bash
pip install selenium beautifulsoup4
```
## Contribution
We welcome contributions to this project! If you have any improvements or suggestions, feel free to create a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
