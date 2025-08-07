import logging


class Styles:
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    DEBUG = '\033[0m'
    INFO = '\033[94m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    CRITICAL = '\033[101m'
    SUCCEED = '\033[92m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'


class _MyFormatter(logging.Formatter):
    def format(self, record) -> str:
        customStyle: str = str(record.customStyle) if hasattr(record, 'customStyle') else Styles.ENDC
        arrow: str = '-' * (30 - len(record.levelname + f"[{record.name}]")) + '>'
        log_fmt: str = f'{customStyle}{record.levelname}[{record.name}] {arrow} %(asctime)s:{Styles.ENDC} {record.msg}'
        formatter = logging.Formatter(log_fmt, datefmt='%d/%m/%Y %H:%M:%S')
        return formatter.format(record)


class MyLogger():
    def __init__(
        self,
        loggerName: str,
        loggingLevel: int = logging.DEBUG
    ) -> None:
        if loggerName not in logging.Logger.manager.loggerDict.keys():
            self._logger: logging.Logger = logging.getLogger(loggerName)
            self.setLoggingLevel(loggingLevel)
            _streamHandler: logging.StreamHandler  = logging.StreamHandler()
            _streamHandler.setFormatter(_MyFormatter())
            self._logger.addHandler(_streamHandler)
        else:
            self._logger: logging.Logger = logging.getLogger(loggerName)
            self.setLoggingLevel(loggingLevel)

    def setLoggingLevel(self, lvl: int = logging.DEBUG) -> int:
        self._logger.setLevel(lvl)

    def debugLog(self, msg: str, style: Styles = Styles.DEBUG) -> None:
        self._logger.debug(f'{msg}', extra= {'customStyle': style})

    def infoLog(self, msg: str, style: Styles = Styles.INFO) -> None:
        self._logger.info(f'{msg}', extra= {'customStyle': style})

    def warningLog(self, msg: str, style: Styles = Styles.WARNING) -> None:
        self._logger.warning(f'{msg}', extra= {'customStyle': style})

    def errorLog(self, msg: str, style: Styles = Styles.ERROR) -> None:
        self._logger.error(f'{msg}', extra= {'customStyle': style})

    def criticalLog(self, msg: str, style: Styles = Styles.CRITICAL) -> None:
        self._logger.critical(f'{msg}', extra= {'customStyle': style})
