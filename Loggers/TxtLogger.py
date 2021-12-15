from AbstractLogger import AbstractLogger
from LogType import LogType


class TxtLogger(AbstractLogger):

    def __init__(self, path):
        self.path = path

    def log(self, message, logType: LogType):
        file = open(self.path, 'a')
        file.write(logType.name + ":" + message)
        file.close()
