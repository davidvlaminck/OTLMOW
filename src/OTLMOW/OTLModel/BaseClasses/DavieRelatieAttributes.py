# coding=utf-8
from abc import abstractmethod

from OTLMOW.OTLModel.BaseClasses.DteAssetType import DteAssetType
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut


class DavieRelatieAttributes:
    @abstractmethod
    def __init__(self):
        self._bron = OTLAttribuut(field=DteAssetType,
                                  naam='bron',
                                  label='bron',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DavieRelatieAttributes.bron',
                                  definition='De bron van een relatie, geformatteerd voor de Davie applicatie',
                                  owner=self)

        self._doel = OTLAttribuut(field=DteAssetType,
                                  naam='doel',
                                  label='doel',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DavieRelatieAttributes.doel',
                                  definition='Het doel van een relatie, geformatteerd voor de Davie applicatie',
                                  owner=self)

    @property
    def bron(self):
        """De bron van een relatie, geformatteerd voor de Davie applicatie"""
        return self._bron.get_waarde()

    @bron.setter
    def bron(self, value):
        self._bron.set_waarde(value, owner=self)
        
    @property
    def doel(self):
        """Het doel van een relatie, geformatteerd voor de Davie applicatie"""
        return self._doel.get_waarde()

    @doel.setter
    def doel(self, value):
        self._doel.set_waarde(value, owner=self)

    
