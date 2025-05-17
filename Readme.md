# 🏛️ Department Of Government Efficiency (DOGE) Webscraper 💰

This repository contains a web scraper designed to extract savings data from the Department Of Government Efficiency website (https://doge.gov/savings). The scraper collects information about government contracts, grants, and leases, including savings achieved through efficiency measures.

## 📊 Overview

The DOGE Webscraper automates the collection of publicly available data about government efficiency initiatives. It extracts data from three main sections:

1. **Contracts** - Government contracts and associated savings
2. **Grants** - Government grants and associated savings
3. **Leases** - Government real estate leases and associated savings

The script navigates through multiple pages in each section, extracts the relevant data, and saves it to CSV files for further analysis.

## ✨ Features

- Automatic navigation through paginated data tables
- Comprehensive data extraction from all three sections (contracts, grants, leases)
- Clean data processing and formatting
- Detailed logging of the scraping process
- Error handling to ensure robustness
- Output in both raw and cleaned CSV formats

## 🔍 Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/Department_Of_Government_Efficiency_Webscraper.git
   cd Department_Of_Government_Efficiency_Webscraper
   ```

2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install required packages:
   ```
   pip install -r requirements.txt
   ```

4. Install ChromeDriver:
   - Download the appropriate version of ChromeDriver from [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)
   - Make sure the ChromeDriver executable is in your system PATH or in the project directory

## 🚀 Usage

To run the scraper:

```
python Doge_Scraper.py
```

The script will:
1. Open a Chrome browser window
2. Navigate to the DOGE savings webpage
3. Scrape data from all three sections (contracts, grants, leases)
4. Process and clean the collected data
5. Save the data to two CSV files:
   - `doge_savings_raw.csv`: Raw data as collected
   - `doge_savings_cleaned.csv`: Processed data with proper formatting

## 📋 Output Files

### doge_savings_raw.csv
Contains the raw data as scraped from the website, with minimal processing.

### doge_savings_cleaned.csv
Contains the processed and cleaned data:
- Numeric values converted to appropriate types
- Dates formatted consistently
- Missing values handled
- Data sorted by date

## 📊 Data Structure

The collected data includes:

For Contracts:
- Agency name
- Vendor name
- Description
- Date
- Type (always "Contract")
- Savings amount

For Grants:
- Agency name
- Recipient name
- Description
- Date
- Type (always "Grant")
- Savings amount

For Leases:
- Agency name
- Location
- Description
- Date
- Square footage
- Type (always "Lease")
- Savings amount

## ⚠️ Troubleshooting

### Common Issues:

1. **ChromeDriver version mismatch**:
   - Error: `SessionNotCreatedException: Message: session not created: This version of ChromeDriver only supports Chrome version XX`
   - Solution: Download and install the version of ChromeDriver that matches your Chrome browser version

2. **Element not found errors**:
   - Error: `NoSuchElementException: Message: no such element: Unable to locate element`
   - Solution: The website structure may have changed. Check the XPath selectors in the code and update them if necessary.

3. **Timeout errors**:
   - Error: `TimeoutException: Message: timeout: Timed out receiving message from renderer`
   - Solution: Increase the timeout values in the `WebDriverWait` calls or check your internet connection

## 📝 Logging

The script creates detailed logs of the scraping process. By default, logs are output to the console, but you can modify the logging configuration in the script to save logs to a file if needed.

## ⚖️ Disclaimer

This tool is designed for educational and research purposes only. Always respect the website's terms of service and robots.txt file. Be considerate about the frequency and volume of requests to avoid unnecessary load on the server. Be careful when you run the code as it may not work as the website is dynamic and the website code may change. 

## 📜 License

[MIT License](LICENSE)
