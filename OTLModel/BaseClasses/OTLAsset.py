import warnings
from abc import abstractmethod, ABC
from collections import namedtuple

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

    def create_dict_from_asset(self, object=None):
        d = {}
        for k, v in vars(object).items():
            if v.waarde is not None and v.waarde != []:
                if isinstance(v.waarde, list) and not isinstance(v.waarde, dict):
                    pass
                if v.field.waardeObject is not None:
                    if v.field._uses_waarde_object:
                        d[k[1:]] = self.create_dict_from_asset(object=v.waarde)
                    else:
                        d[k[1:]] = v.waarde.waarde
                else:
                    d[k[1:]] = v.waarde
        return self.clean_dict(d)

    def clean_dict(self, d):
        """Recursively remove None values and empty dicts from input dict"""
        for k in list(d):
            v = d[k]
            if isinstance(v, dict):
                self.clean_dict(v)
                if len(v.items()) == 0:
                    del d[k]
            if v is None:
                del d[k]
        return d

    def __str__(self):
        return f'information about {self.__class__.__name__} {self.__hash__()}:\n' + self.build_string_version(indent=4)

    def build_string_version(self, indent=4) -> str:
        lines = []
        asset_dict = self.create_dict_from_asset(object=self)
        lines.extend(
            self.make_string_version_from_dict(
                d=asset_dict,
                level=1,
                indent=4))

        return '\n'.join(lines)

    def make_string_version_from_dict(self, d, level=0, indent=4) -> []:
        lines = []
        for key in sorted(d.keys()):
            value = d[key]
            if isinstance(value, dict):
                lines.append(' ' * indent * level + f'{key} :')
                lines.extend(self.make_string_version_from_dict(value, level=level+1, indent=indent))
            else:
                lines.append(' ' * indent * level + f'{key} : {value}')
        return lines


