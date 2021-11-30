from abc import ABC, abstractmethod

from OTLClasses.Verification.OTLAsset import OTLAsset


class StringField:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f'expecting string in {self.name}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class IntField:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'expecting integer in {self.name}')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


# inherit from ABC to create abstract class
class NaampadObject(OTLAsset, ABC):
    """Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad."""
    uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject"
    naampad = StringField()
    """Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra)."""

    @abstractmethod
    def __init__(self):
        raise TypeError("Can't instantiate abstract class " + self.__class__.__name__)

