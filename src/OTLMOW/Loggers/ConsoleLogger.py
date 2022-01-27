from src.OTLMOW.Loggers.AbstractLogger import AbstractLogger
from src.OTLMOW.Loggers.LogType import LogType


class ConsoleLogger(AbstractLogger):
    def log(self, message, logType: LogType):
        print(logType.name + ":" + message)

