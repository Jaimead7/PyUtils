import logging
from pathlib import Path

from .src.config import ConfigDict, ConfigFileManager, ProjectPathsDict
from .src.logs import MyLogger, Styles, my_logger
from .src.no_instantiable import NoInstantiable
from .src.timing import time_me
from .src.validation import ValidationClass


def set_pyutils_logs_path(new_path: Path | str) -> None:
    my_logger.logs_file_path = new_path

def save_pyutils_logs(value: bool) -> None:
    my_logger.save_logs = value

def set_pyutils_logging_level(lvl: int = logging.DEBUG) -> None:
    my_logger.set_logging_level(lvl)

my_logger.debug(f'Package loaded: pyUtils', Styles.SUCCEED)
