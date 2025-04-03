import logging

from .config import cfg


class Styles:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEBUG = '\033[94m'
    INFO = '\033[0m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    CRITICAL = '\033[101m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'


class _MyFormatter(logging.Formatter):
    FORMATS: dict = {
        logging.DEBUG: Styles.DEBUG + '%(levelname)s -----> %(asctime)s:' + Styles.ENDC + ' %(message)s',
        logging.INFO: Styles.INFO + '%(levelname)s ------> %(asctime)s:' + Styles.ENDC + ' %(message)s',
        logging.WARNING: Styles.WARNING + '%(levelname)s ---> %(asctime)s:' + Styles.ENDC + ' %(message)s',
        logging.ERROR: Styles.ERROR + '%(levelname)s -----> %(asctime)s:' + Styles.ENDC + ' %(message)s',
        logging.CRITICAL: Styles.CRITICAL + '%(levelname)s --> %(asctime)s:' + Styles.ENDC + ' %(message)s',
    }

    def format(self, record) -> str:
        log_fmt: str = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%d/%m/%Y %H:%M:%S')
        return formatter.format(record)


def _getLoggingLevel() -> int:
    try:
        return logging.__dict__[cfg.app.loggingLevel.upper()]
    except (KeyError, AttributeError):
        return logging.DEBUG

def setLoggingLevel(lvl: int = _getLoggingLevel()) -> int:
    _logger.setLevel(lvl)
print(__name__)
_logger: logging.Logger = logging.getLogger(__file__)
setLoggingLevel()
_streamHandler = logging.StreamHandler()
_streamHandler.setFormatter(_MyFormatter())
_logger.addHandler(_streamHandler)

def debugLog(msg: str, style: Styles = Styles.ENDC) -> None:
    _logger.debug(f'{style}{msg}{Styles.ENDC}')

def infoLog(msg: str, style: Styles = Styles.ENDC) -> None:
    _logger.info(f'{style}{msg}{Styles.ENDC}')

def warningLog(msg: str, style: Styles = Styles.ENDC) -> None:
    _logger.warning(f'{style}{msg}{Styles.ENDC}')

def errorLog(msg: str, style: Styles = Styles.ENDC) -> None:
    _logger.error(f'{style}{msg}{Styles.ENDC}')

def criticalLog(msg: str, style: Styles = Styles.ENDC) -> None:
    _logger.critical(f'{style}{msg}{Styles.ENDC}')
