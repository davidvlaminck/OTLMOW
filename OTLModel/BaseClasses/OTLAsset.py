import warnings
from abc import abstractmethod, ABC

from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.BaseClasses.WKTField import WKTField


class OTLAsset(ABC):
    @abstractmethod
    def __init__(self):
        self._geometry = OTLAttribuut(field=WKTField,
                                      naam='geometry',
                                      label='geometry',
                                      objectUri='https://loc.data.wegenenverkeer.be/ns/implementatieelement#Locatie.geometrie',
                                      definition='geometry voor DAVIE')

        if hasattr(self, 'deprecated_version'):
            if self.deprecated_version is not None:
                if hasattr(self, 'typeURI'):
                    warnings.warn(message=f'{self.typeURI} is deprecated since version {self.deprecated_version}',
                                  category=DeprecationWarning)
                else:
                    warnings.warn(message=f'used a class that is deprecated since version {self.deprecated_version}',
                                  category=DeprecationWarning)

    @property
    def geometry(self):
        """geometry voor DAVIE"""
        return self._geometry.waarde

    @geometry.setter
    def geometry(self, value):
        self._geometry.set_waarde(value, owner=self)

    def __str__(self):
        return f'information about {self.__class__.__name__} {self.__hash__()}:\n' + self.make_string_version(self, level=0)

    def make_string_version(self, object, level, indent=4) -> str:
        level += 1
        s = ''
        for k, v in vars(object).items():
            if v.waarde is not None and v.waarde != []:
                if isinstance(v.waarde, list) and not v.waarde is dict:
                    pass
                if v.field.waardeObject is not None:
                    if v.field._uses_waarde_object:
                        s = s + ' ' * indent * level + f'{k[1:]} :\n'
                        s = s + self.make_string_version(v.waarde, level, indent)
                    else:
                        s = s + ' ' * indent * level + f'{k[1:]} : {v.waarde.waarde}\n'
                else:
                    s = s + ' ' * indent * level + f'{k[1:]} : {v.waarde}\n'
        level -= 1
        return s
