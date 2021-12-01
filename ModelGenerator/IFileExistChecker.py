from abc import ABC, abstractmethod


class IFileExistChecker(ABC):
    path: str

    def __init__(self, path):
        self.path = path

    @abstractmethod
    def fileFound(self) -> bool:
        pass
