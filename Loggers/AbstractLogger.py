from abc import ABC, abstractmethod

from Loggers.LogType import LogType


class AbstractLogger(ABC):
    @abstractmethod
    def log(self, message: str, logType: LogType):
        pass
