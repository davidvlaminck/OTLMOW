from abc import ABC, abstractmethod


class AbstractAttributeSetter(ABC):
    @abstractmethod
    def set_attribute(self, value):
        pass