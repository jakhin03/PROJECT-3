from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

def create_driver(config):
    """Create a WebDriver instance."""
    options = Options()
    options.headless = config.getboolean('selenium', 'headless', fallback=True)

    # service = Service(config.get('selenium', 'driver_path', fallback='chromedriver'))
    return webdriver.Chrome(options=options)
