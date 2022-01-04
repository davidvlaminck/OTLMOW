from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType


class TxtLogger(AbstractLogger):

    def __init__(self, path):
        self.path = path
        open(path, 'w').close()

    def log(self, message, logType: LogType):
        file = open(self.path, 'a')
        file.write(logType.name + ":" + message + '\n')
        file.close()
