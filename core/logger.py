import logging

class ColoredFormatter(logging.Formatter):
    COLORS = {
        'INFO': '\033[94m',      # Blue
        'WARNING': '\033[93m',   # Yellow
        'ERROR': '\033[91m',     # Red
        'CRITICAL': '\033[95m',  # Magenta
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, '')
        message = super().format(record)
        reset = '\033[0m'  # Reset color
        return f"{color}{message}{reset}"

def setup_logger():
    """Setup logger with colored formatter."""
    logging.basicConfig(level=logging.INFO)
    formatter = ColoredFormatter(fmt='%(asctime)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)
    logging.getLogger().handlers.clear()
    logging.getLogger().addHandler(handler)
