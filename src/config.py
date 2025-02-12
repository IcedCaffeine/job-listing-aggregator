# src/config.py

# Base URL for scraping (this is a dummy URL for now; replace with a real job listing URL)
JOB_SITE_URL = "https://ca.indeed.com/jobs?q=python&l=Canada"

# HTTP headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/115.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://www.google.com",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

# CSS selectors for scraping elements (adjust based on your target website's HTML structure)
# CSS selectors based on Indeed's current structure:
# Each job card is contained in a div with the class "job_seen_beacon".
JOB_LISTING_SELECTOR = "div.job_seen_beacon"

# The job title is usually within an <h2> with the class "jobTitle", and the actual text is in a nested <span>.
JOB_TITLE_SELECTOR = "h2.jobTitle span"

# The company name is typically in a <span> with class "companyName".
JOB_COMPANY_SELECTOR = "span.companyName"

# The location is generally in a <div> with the class "companyLocation".
JOB_LOCATION_SELECTOR = "div.companyLocation"
