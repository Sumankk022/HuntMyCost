import logging

from colorama import Fore, Style, init

init(autoreset=True)

class ColoredLogFormatter(logging.Formatter):
    COLORS = {
        "DEBUG": Fore.CYAN,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED,
        "CRITICAL": Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        log_message = super().format(record)
        return (
            f"{self.COLORS.get(record.levelname, Fore.RESET)}"
            f"{log_message}{Style.RESET_ALL}"
        )
    

logging.basicConfig(level=logging.DEBUG)
console_handler = logging.StreamHandler()
console_handler.setFormatter(
    ColoredLogFormatter("%(asctime)s - %(levelname)s - %(module)s - %(message)s")
)

logging.getLogger().addHandler(console_handler)