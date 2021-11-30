from abc import ABC, abstractmethod


class OTLAsset:
    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)


# inherit from ABC to create abstract class
class NaampadObject(OTLAsset, ABC):
    uri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__ )

