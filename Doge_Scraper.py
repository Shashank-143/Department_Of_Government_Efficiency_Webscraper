from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def initialize_driver(url):
    """Initialize and return a webdriver instance"""
    driver = webdriver.Chrome()
    driver.get(url)
    return driver

def get_page_count(driver, section_number):
    """Get the total number of pages for a specific section (table)"""
    xpath = f'//*[@id="main-content"]/div/div/div[4]/div[{section_number}]/div[3]/div[2]/button[7]'
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    page_count = element.text
    logger.info(f"Section {section_number} has {page_count} pages")
    return int(page_count)

def scrape_contracts(driver, page_count):
    """Scrape contract data """
    agencies, vendors, descriptions, dates, savings = [], [], [], [], []
    
    for page in range(page_count):
        logger.info(f"Scraping contracts page {page+1}/{page_count}")
        # Wait for table to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/div/div/div/table/tbody')))
        
        # Extract data from current page
        try:
            extract_contract_page_data(driver, agencies, vendors, descriptions, dates, savings)
        except Exception as e:
            logger.error(f"Error scraping contracts page {page+1}: {e}")
        
        if page < page_count - 1:
            navigate_to_next_page(driver, 1)
    
    # Create and return DataFrame
    df = pd.DataFrame({
        'Agency': agencies,
        'Vendor': vendors,
        'Description': descriptions,
        'Date': dates,
        'Type': 'Contract',
        'Savings': savings
    })
    
    logger.info(f"Scraped {len(agencies)} contract records")
    return df

def extract_contract_page_data(driver, agencies, vendors, descriptions, dates, savings):
    """Extract data from the current contract page"""
    agency_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/div/div/div/table/tbody/tr/td[1]')
    vendor_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/div/div/div/table/tbody/tr/td[2]')
    desc_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/div/div/div/table/tbody/tr/td[3]')
    date_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/div/div/div/table/tbody/tr/td[4]')
    saving_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[1]/div[2]/div/div/div/table/tbody/tr/td[6]')
    
    for i in range(min(len(agency_elements), 10)):
        try:
            agencies.append(agency_elements[i].text)
            vendors.append(vendor_elements[i].text)
            descriptions.append(desc_elements[i].text)
            dates.append(date_elements[i].text)
            savings.append(saving_elements[i].text)
        except Exception as e:
            logger.error(f"Error extracting row {i+1} from contract page: {e}")

def scrape_grants(driver, page_count):
    """Scrape grant data """
    agencies, recipients, descriptions, dates, savings = [], [], [], [], []
    
    for page in range(page_count):
        logger.info(f"Scraping grants page {page+1}/{page_count}")
        # Wait for table to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[2]/div[2]/div/div/div/table/tbody')))
        
        # Extract data from current page
        try:
            extract_grant_page_data(driver, agencies, recipients, descriptions, dates, savings)
        except Exception as e:
            logger.error(f"Error scraping grants page {page+1}: {e}")
        
        if page < page_count - 1:
            navigate_to_next_page(driver, 2)
    
    # Create and return DataFrame
    df = pd.DataFrame({
        'Agency': agencies,
        'Recipient': recipients,
        'Description': descriptions,
        'Date': dates,
        'Type': 'Grant',
        'Savings': savings
    })
    
    logger.info(f"Scraped {len(agencies)} grant records")
    return df

def extract_grant_page_data(driver, agencies, recipients, descriptions, dates, savings):
    """Extract data from the current grant page."""
    agency_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[2]/div[2]/div/div/div/table/tbody/tr/td[1]')
    recipient_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[2]/div[2]/div/div/div/table/tbody/tr/td[2]')
    desc_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[2]/div[2]/div/div/div/table/tbody/tr/td[3]')
    date_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[2]/div[2]/div/div/div/table/tbody/tr/td[4]')
    saving_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[2]/div[2]/div/div/div/table/tbody/tr/td[5]')
    
    for i in range(min(len(agency_elements), 10)):
        try:
            agencies.append(agency_elements[i].text)
            recipients.append(recipient_elements[i].text)
            descriptions.append(desc_elements[i].text)
            dates.append(date_elements[i].text)
            savings.append(saving_elements[i].text)
        except Exception as e:
            logger.error(f"Error extracting row {i+1} from grant page: {e}")

def scrape_leases(driver, page_count):
    """Scrape lease data from all pages."""
    agencies, locations, descriptions, dates, sq_ft, savings = [], [], [], [], [], []
    
    for page in range(page_count):
        logger.info(f"Scraping leases page {page+1}/{page_count}")
        
        # Wait for table to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[3]/div[2]/div/div/div/table/tbody')))
        
        # Extract data from current page
        try:
            extract_lease_page_data(driver, agencies, locations, descriptions, dates, sq_ft, savings)
        except Exception as e:
            logger.error(f"Error scraping leases page {page+1}: {e}")
        
        if page < page_count - 1:
            navigate_to_next_page(driver, 3)
    
    # Create and return DataFrame
    df = pd.DataFrame({
        'Agency': agencies,
        'Location': locations,
        'Description': descriptions,
        'Date': dates,
        'Sq Ft': sq_ft,
        'Type': 'Lease',
        'Savings': savings
    })
    
    logger.info(f"Scraped {len(agencies)} lease records")
    return df

def extract_lease_page_data(driver, agencies, locations, descriptions, dates, sq_ft, savings):
    """Extract data from the current lease page."""
    agency_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[3]/div[2]/div/div/div/table/tbody/tr/td[1]')
    location_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[3]/div[2]/div/div/div/table/tbody/tr/td[2]')
    desc_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[3]/div[2]/div/div/div/table/tbody/tr/td[3]')
    date_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[3]/div[2]/div/div/div/table/tbody/tr/td[4]')
    sq_ft_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[3]/div[2]/div/div/div/table/tbody/tr/td[5]')
    saving_elements = driver.find_elements(By.XPATH, '//*[@id="main-content"]/div/div/div[4]/div[3]/div[2]/div/div/div/table/tbody/tr/td[6]')
    
    for i in range(min(len(agency_elements), 10)):
        try:
            agencies.append(agency_elements[i].text)
            locations.append(location_elements[i].text)
            descriptions.append(desc_elements[i].text)
            dates.append(date_elements[i].text)
            sq_ft.append(sq_ft_elements[i].text)
            savings.append(saving_elements[i].text)
        except Exception as e:
            logger.error(f"Error extracting row {i+1} from lease page: {e}")

def navigate_to_next_page(driver, section_number):
    """Navigate to the next page in the given section."""
    xpath = f'//*[@id="main-content"]/div/div/div[4]/div[{section_number}]/div[3]/div[2]/button[8]'
    next_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
    next_btn.click()
    time.sleep(2)  

def clean_and_process_data(df):
    """Clean and process the combined DataFrame."""

    df['Savings'] = df['Savings'].replace('Unavailable', '0')
    df['Savings'] = df['Savings'].str.replace('$', '', regex=False)
    df['Savings'] = df['Savings'].str.replace(',', '', regex=False)
    df['Savings'] = pd.to_numeric(df['Savings'], errors='coerce')
    df['Savings'] = df['Savings'].fillna(0)
    
    if 'Sq Ft' in df.columns:
        df['Sq Ft'] = df['Sq Ft'].fillna('0')
        df['Sq Ft'] = df['Sq Ft'].astype(str).str.replace(',', '', regex=False)
        df['Sq Ft'] = pd.to_numeric(df['Sq Ft'], errors='coerce')
        df['Sq Ft'] = df['Sq Ft'].fillna(0)
    else:
        df['Sq Ft'] = 0
    
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.sort_values(by='Date')
    return df

def save_data(df, filename):
    """Save the DataFrame to a CSV file."""
    df.to_csv(filename, index=False)
    logger.info(f"Data saved to {filename}")

def main():
    """Main function to run the scraper."""
    try:
        url = "https://doge.gov/savings"
        driver = initialize_driver(url)
        # Scrape contracts
        contract_pages = get_page_count(driver, 1)
        contracts_df = scrape_contracts(driver, contract_pages)
        
        # Scrape grants
        grant_pages = get_page_count(driver, 2)
        grants_df = scrape_grants(driver, grant_pages)
        
        # Scrape leases
        lease_pages = get_page_count(driver, 3)
        leases_df = scrape_leases(driver, lease_pages)
        
        combined_df = pd.concat([contracts_df, grants_df, leases_df], ignore_index=True)
        logger.info(f"Combined data has {len(combined_df)} records")
        
        cleaned_df = clean_and_process_data(combined_df)
        save_data(combined_df, 'doge_savings_raw.csv')
        save_data(cleaned_df, 'doge_savings_cleaned.csv')
        
        driver.quit()                               # Close the driver
        return cleaned_df
    
    except Exception as e:
        logger.error(f"An error occurred in the main function: {e}")
        if 'driver' in locals():
            driver.quit()
        raise

if __name__ == "__main__":
    main()