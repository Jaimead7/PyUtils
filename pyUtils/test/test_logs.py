import logging

from pytest import LogCaptureFixture, fixture, mark

from ..src.logs import MyLogger

LOGGER_NAME = 'TestLogger'

@fixture(autouse= True)
def setCaplogLvl(caplog: LogCaptureFixture) -> None:
    caplog.set_level(logging.DEBUG)
    caplog.clear()

@fixture()
def myLogger() -> MyLogger:
    return MyLogger(LOGGER_NAME, logging.DEBUG)


class TestLogs:
    @mark.parametrize('msg', [
        'Debug test message',
    ])
    def test_debug(self, msg: str, caplog: LogCaptureFixture, myLogger: MyLogger) -> None:
        myLogger.debugLog(msg)
        record: logging.LogRecord = caplog.records[0]
        assert record.message == msg
        assert record.levelno == logging.DEBUG
        assert record.name == LOGGER_NAME

    @mark.parametrize('msg', [
        'Info test message',
    ])
    def test_info(self, msg: str, caplog: LogCaptureFixture, myLogger: MyLogger) -> None:
        myLogger.infoLog(msg)
        record: logging.LogRecord = caplog.records[0]
        assert record.message == msg
        assert record.levelno == logging.INFO
        assert record.name == LOGGER_NAME

    @mark.parametrize('msg', [
        'Warning test message',
    ])
    def test_warning(self, msg: str, caplog: LogCaptureFixture, myLogger: MyLogger) -> None:
        myLogger.warningLog(msg)
        record: logging.LogRecord = caplog.records[0]
        assert record.message == msg
        assert record.levelno == logging.WARNING
        assert record.name == LOGGER_NAME

    @mark.parametrize('msg', [
        'Error test message',
    ])
    def test_error(self, msg: str, caplog: LogCaptureFixture, myLogger: MyLogger) -> None:
        myLogger.errorLog(msg)
        record: logging.LogRecord = caplog.records[0]
        assert record.message == msg
        assert record.levelno == logging.ERROR
        assert record.name == LOGGER_NAME

    @mark.parametrize('msg', [
        'Critical test message',
    ])
    def test_critical(self, msg: str, caplog: LogCaptureFixture, myLogger: MyLogger) -> None:
        myLogger.criticalLog(msg)
        record: logging.LogRecord = caplog.records[0]
        assert record.message == msg
        assert record.levelno == logging.CRITICAL
        assert record.name == LOGGER_NAME

    @mark.parametrize('lvl, nMessages', [
        (logging.DEBUG, 5),
        (logging.INFO, 4),
        (logging.WARNING, 3),
        (logging.ERROR, 2),
        (logging.CRITICAL, 1),
    ])
    def test_setLoggingLevel(self, lvl: int, nMessages: int,  caplog: LogCaptureFixture, myLogger: MyLogger) -> None:
        myLogger.setLoggingLevel(lvl)
        myLogger.debugLog('Debug test message')
        myLogger.infoLog('Info test message')
        myLogger.warningLog('Warning test message')
        myLogger.errorLog('Error test message')
        myLogger.criticalLog('Critical test message')
        assert len(caplog.records) == nMessages
