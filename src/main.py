# src/main.py
from scraper import scrape_jobs

def main():
    print("Starting Job Listing Aggregator & Scraper for Indeed...\n")
    jobs = scrape_jobs()
    if jobs:
        print(f"Found {len(jobs)} job listing(s):\n")
        for idx, job in enumerate(jobs, 1):
            print(f"{idx}. {job['title']} at {job['company']} - {job['location']}")
    else:
        print("No jobs found or there was an error fetching the page.")

if __name__ == "__main__":
    main()
