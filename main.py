import logging
from core.logger import setup_logger
from core.cacher import Cacher
from core.cli_parser import parse_args
from configparser import ConfigParser

def load_config(config_file):
    """Load configuration from the given file."""
    config = ConfigParser()
    config.read(config_file)
    return config

def main():
    # Setup logging
    setup_logger()

    # Parse arguments
    args = parse_args()

    # Load configuration
    config = load_config(args.config)

    # Display banner
    print(r"""
                    ██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    ██████╗ 
                    ██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝    ╚════██╗
                    ██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║        █████╔╝
                    ██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║        ╚═══██╗
                    ██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║       ██████╔╝
                    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       ╚═════╝ 
    """)

    # Initialize fuzzer
    cacher = Cacher(config)

    # Handle headless mode
    if args.headless:
        cacher.driver.options.headless = True

    # Select mode of operation
    if args.mode == "fuzz":
        logging.info("Running in DOM comparison mode...")
        cacher.run(args.url)

if __name__ == "__main__":
    main()
