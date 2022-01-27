from src.OTLMOW.Loggers.AbstractLogger import AbstractLogger
from src.OTLMOW.Loggers.LogType import LogType


class NoneLogger(AbstractLogger):
    def log(self, message: str, logType: LogType):
        pass
