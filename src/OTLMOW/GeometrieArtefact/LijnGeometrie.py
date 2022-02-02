from abc import abstractmethod, ABC

from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.WKTField import WKTField


class LijnGeometrie(ABC):
    @abstractmethod
    def __init__(self):
        self._geometry = OTLAttribuut(field=WKTField,
                                      naam='geometry',
                                      label='geometry',
                                      objectUri='https://loc.data.wegenenverkeer.be/ns/implementatieelement#Locatie.geometrie',
                                      definition='geometry voor DAVIE',
                                      constraints='LINESTRING Z')

    @property
    def geometry(self):
        """geometry voor DAVIE"""
        return self._geometry.waarde

    @geometry.setter
    def geometry(self, value):
        self._geometry.set_waarde(value, owner=self)