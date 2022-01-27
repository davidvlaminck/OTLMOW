from abc import ABC, abstractmethod

from src.OTLMOW.Loggers.LogType import LogType


class AbstractLogger(ABC):
    @abstractmethod
    def log(self, message: str, logType: LogType):
        pass
