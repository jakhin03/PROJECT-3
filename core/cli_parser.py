import argparse

def parse_args():
    """Parse command-line arguments for the fuzzing tool."""
    parser = argparse.ArgumentParser(description="Project 3: Fuzzing Tool for Excessive Data Exposure")
    parser.add_argument("-u", "--url", help="Target URL to test", required=True)
    parser.add_argument("-c", "--config", help="Path to configuration file", default="config/settings.ini")
    parser.add_argument("--headless", action="store_true", help="Run in headless mode")
    parser.add_argument("--mode", choices=["fuzz"], default="dom", help="Mode of operation: Fuzzing only")
    return parser.parse_args()
