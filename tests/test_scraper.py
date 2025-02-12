# tests/test_scraper.py
import unittest
from src.scraper import parse_jobs

class TestScraper(unittest.TestCase):
    
    def test_parse_jobs_with_empty_html(self):
        """
        Test that parse_jobs returns an empty list when no job listings are present.
        """
        html = "<html><head></head><body><div>No job listings here.</div></body></html>"
        jobs = parse_jobs(html)
        self.assertEqual(jobs, [])
        
    def test_parse_jobs_with_sample_html(self):
        """
        Test that parse_jobs correctly extracts job details from sample Indeed-style HTML.
        """
        sample_html = """
        <html>
            <head><title>Job Listings</title></head>
            <body>
                <div class="job_seen_beacon">
                    <h2 class="jobTitle">
                        <span title="Python Developer">Python Developer</span>
                    </h2>
                    <span class="companyName">Tech Corp</span>
                    <div class="companyLocation">Toronto, ON</div>
                </div>
                <div class="job_seen_beacon">
                    <h2 class="jobTitle">
                        <span title="Data Scientist">Data Scientist</span>
                    </h2>
                    <span class="companyName">Data Inc.</span>
                    <div class="companyLocation">Vancouver, BC</div>
                </div>
            </body>
        </html>
        """
        jobs = parse_jobs(sample_html)
        self.assertEqual(len(jobs), 2)
        self.assertEqual(jobs[0]["title"], "Python Developer")
        self.assertEqual(jobs[0]["company"], "Tech Corp")
        self.assertEqual(jobs[0]["location"], "Toronto, ON")
        self.assertEqual(jobs[1]["title"], "Data Scientist")
        self.assertEqual(jobs[1]["company"], "Data Inc.")
        self.assertEqual(jobs[1]["location"], "Vancouver, BC")

if __name__ == '__main__':
    unittest.main()
