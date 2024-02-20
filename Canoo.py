from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

def scrape_canoo_info():
    url = "https://www.marketwatch.com/investing/stock/goev/company-profile?mod=mw_quote_tab"
    
    # Launch browser
    driver = webdriver.Chrome()  # Assuming you're using Chrome. You may need to download chromedriver.exe
    driver.get(url)
    
    # Wait for the page to fully load
    time.sleep(5)  # Adjust the sleep time as needed
    
    # Get page source
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    # Close the browser
    driver.quit()
    
    # Extracting the company name
    company_name_element = soup.find('h4', class_='heading')
    company_name = company_name_element.text.strip() if company_name_element else 'N/A'
    print("Company Name:", company_name)

    # Extracting the industry and sector information
    industry_element = soup.find('small', text='Industry').find_next('span', class_='primary')
    industry = industry_element.text.strip() if industry_element else 'N/A'
    print("Industry:", industry)

    sector_element = soup.find('small', text='Sector').find_next('span', class_='primary')
    sector = sector_element.text.strip() if sector_element else 'N/A'
    print("Sector:", sector)

    # Extracting other relevant details
    fiscal_year_end_element = soup.find('small', text='Fiscal Year-end').find_next('span', class_='primary')
    fiscal_year_end = fiscal_year_end_element.text.strip() if fiscal_year_end_element else 'N/A'
    print("Fiscal Year-end:", fiscal_year_end)

    revenue_element = soup.find('small', text='Revenue').find_next('span', class_='primary')
    revenue = revenue_element.text.strip() if revenue_element else 'N/A'
    print("Revenue:", revenue)

    net_income_element = soup.find('small', text='Net Income').find_next('span', class_='primary')
    net_income = net_income_element.text.strip() if net_income_element else 'N/A'
    print("Net Income:", net_income)

    sales_growth_element = soup.find('small', text='2022 Sales Growth').find_next('span', class_='primary')
    sales_growth = sales_growth_element.text.strip() if sales_growth_element else 'N/A'
    print("2022 Sales Growth:", sales_growth)

    employees_element = soup.find('small', text='Employees').find_next('span', class_='primary')
    employees = employees_element.text.strip() if employees_element else 'N/A'
    print("Employees:", employees)

    return {
        "Company Name": company_name,
        "Industry": industry,
        "Sector": sector,
        "Fiscal Year-end": fiscal_year_end,
        "Revenue": revenue,
        "Net Income": net_income,
        "2022 Sales Growth": sales_growth,
        "Employees": employees
    }

# Rest of the code remains the same...


def write_to_csv(data):
    with open('canoo_info.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

# Main function
def main():
    canoo_info = scrape_canoo_info()
    print("Canoo Information:")
    print(canoo_info)
    write_to_csv(canoo_info)
    print("Data written to canoo_info.csv")

if __name__ == "__main__":
    main()
