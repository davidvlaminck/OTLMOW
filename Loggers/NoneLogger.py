from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType


class NoneLogger(AbstractLogger):
    def log(self, message: str, logType: LogType):
        pass
