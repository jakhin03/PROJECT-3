from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from utilities.helpers import is_valid_url
import logging

class Cacher:
    def __init__(self, config):
        """Initialize Cacher with configuration."""
        self.config = config
        self.driver = self.create_driver()
        self.wait = WebDriverWait(self.driver, 10)

    def create_driver(self):
        """Create Selenium WebDriver with options."""
        from core.driver_factory import create_driver
        return create_driver(self.config)

    def get_dom_tree(self, url):
        """Fetch DOM tree for the given URL."""
        if not is_valid_url(url):
            logging.error("Invalid URL: %s", url)
            return None

        self.driver.get(url)
        wait_time = self.config.getint('general', 'wait_time', fallback=5)
        self.driver.implicitly_wait(wait_time)
        return self.driver.page_source

    def run(self, url):
        """Run the caching and comparison logic."""
        logging.info("Getting original DOM tree...")
        dom_original = self.get_dom_tree(url)
        if not dom_original:
            return

        logging.info("Getting mutated DOM tree...")
        dom_mutated = self.get_dom_tree(url)

        logging.info("Comparing DOM trees...")
        if dom_original == dom_mutated:
            logging.info("No differences found in DOM.")
        else:
            logging.warning("DOM differences detected!")

        self.driver.quit()
