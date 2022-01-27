from OTLMOW.Loggers.AbstractLogger import AbstractLogger
from OTLMOW.Loggers.LogType import LogType


class NoneLogger(AbstractLogger):
    def log(self, message: str, logType: LogType):
        pass
