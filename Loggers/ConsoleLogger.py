from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType


class ConsoleLogger(AbstractLogger):
    def log(self, message, logType: LogType):
        print(logType.name + ":" + message)

