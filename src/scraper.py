# src/scraper.py
import requests
from bs4 import BeautifulSoup
import config

def fetch_page(url):
    """
    Fetch the HTML content of the given URL.
    """
    try:
        response = requests.get(url, headers=config.HEADERS)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
        return None

def parse_jobs(html):
    """
    Parse the HTML content and extract job listings.
    Returns a list of dictionaries containing job details.
    """
    soup = BeautifulSoup(html, "lxml")
    job_elements = soup.select(config.JOB_LISTING_SELECTOR)
    jobs = []
    
    for job_elem in job_elements:
        title_elem = job_elem.select_one(config.JOB_TITLE_SELECTOR)
        company_elem = job_elem.select_one(config.JOB_COMPANY_SELECTOR)
        location_elem = job_elem.select_one(config.JOB_LOCATION_SELECTOR)
        
        title = title_elem.get_text(strip=True) if title_elem else "No title"
        company = company_elem.get_text(strip=True) if company_elem else "No company"
        location = location_elem.get_text(strip=True) if location_elem else "No location"
        
        jobs.append({
            "title": title,
            "company": company,
            "location": location
        })
    
    return jobs

def scrape_jobs(url=config.JOB_SITE_URL):
    """
    Main function to scrape jobs from the specified URL.
    """
    html = fetch_page(url)
    if html:
        jobs = parse_jobs(html)
        return jobs
    else:
        return []
