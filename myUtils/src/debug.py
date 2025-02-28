from datetime import datetime

from .config import cfg


class Styles:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INFO = '\033[95m'


def debug(msg: str, style: Styles = Styles.ENDC) -> None:
    """Print a message with a timestam formated with style.
    Args:
        msg (str): Messge to display.
        style (Styles, optional): Color of the message. Defaults to Styles.ENDC.
    """
    if (cfg.app.debug):
        print(f'{style}{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}:{Styles.ENDC} {msg}')
