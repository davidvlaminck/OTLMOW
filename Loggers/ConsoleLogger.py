from AbstractLogger import AbstractLogger
from LogType import LogType


class ConsoleLogger(AbstractLogger):
    def log(self, message, logType: LogType):
        print(logType.name + ":" + message)

