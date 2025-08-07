import logging
import re

from pytest import LogCaptureFixture, fixture, mark

from ..src.logs import MyLogger
from ..src.timing import timeMe

LOGGER_NAME = 'TestLogger'

@fixture(autouse= True)
def setCaplogLvl(caplog: LogCaptureFixture) -> None:
    caplog.set_level(logging.DEBUG)
    caplog.clear()

@fixture()
def myLogger() -> MyLogger:
    return MyLogger(LOGGER_NAME, logging.DEBUG)


class TestTiming:
    def test_timing_normal(self, caplog: LogCaptureFixture, myLogger: MyLogger) -> None:
        @timeMe
        def test_func() -> None:
            [_ for _ in range(90000)]
        test_func()
        record: logging.LogRecord = caplog.records[0]
        assert record.levelno == logging.DEBUG
        print(record.message)
        assert bool(re.fullmatch(r'.* execution time: .*s\.$', record.message))

    def test_timing_called(self, caplog: LogCaptureFixture, myLogger: MyLogger) -> None:
        @timeMe()
        def test_func() -> None:
            [_ for _ in range(90000)]
        test_func()
        record: logging.LogRecord = caplog.records[0]
        assert record.levelno == logging.DEBUG
        print(record.message)
        assert bool(re.fullmatch(r'.* execution time: .*s\.$', record.message))

    def test_timing_muted(self, caplog: LogCaptureFixture, myLogger: MyLogger) -> None:
        @timeMe(debug= False)
        def test_func() -> None:
            [_ for _ in range(90000)]
        test_func()
        assert len(caplog.records) == 0
