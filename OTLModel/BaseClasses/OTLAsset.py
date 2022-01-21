from abc import abstractmethod, ABC

from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.BaseClasses.OTLObject import OTLObject
from OTLModel.BaseClasses.WKTField import WKTField


class OTLAsset(ABC, OTLObject):
    @abstractmethod
    def __init__(self):
        super().__init__()
        self._geometry = OTLAttribuut(field=WKTField,
                                      naam='geometry',
                                      label='geometry',
                                      objectUri='https://loc.data.wegenenverkeer.be/ns/implementatieelement#Locatie.geometrie',
                                      definition='geometry voor DAVIE')

    @property
    def geometry(self):
        """geometry voor DAVIE"""
        return self._geometry.waarde

    @geometry.setter
    def geometry(self, value):
        self._geometry.set_waarde(value, owner=self)
