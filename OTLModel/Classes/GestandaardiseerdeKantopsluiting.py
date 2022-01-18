# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.Kantopsluiting import Kantopsluiting
from OTLModel.Datatypes.KlLEKantopsluitingBijkomendeParameter import KlLEKantopsluitingBijkomendeParameter
from OTLModel.Datatypes.KlLEStandaardFabricageLengte import KlLEStandaardFabricageLengte


# Generated with OTLClassCreator. To modify: extend, do not edit
class GestandaardiseerdeKantopsluiting(Kantopsluiting, AttributeInfo):
    """Abstracte voor een kantopsluiting die voldoet aan een bepaalde standaard."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GestandaardiseerdeKantopsluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AttributeInfo.__init__(self)
        Kantopsluiting.__init__(self)

        self._bijkomendeParameter = OTLAttribuut(field=KlLEKantopsluitingBijkomendeParameter,
                                                 naam='bijkomendeParameter',
                                                 label='bijkomende parameter',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GestandaardiseerdeKantopsluiting.bijkomendeParameter',
                                                 definition='Detail typering van de kantopsluiting.')

        self._fabricageLengte = OTLAttribuut(field=KlLEStandaardFabricageLengte,
                                             naam='fabricageLengte',
                                             label='fabricagelengte',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#GestandaardiseerdeKantopsluiting.fabricageLengte',
                                             definition='De lengte van de individuele kantopsluiting volgens de norm.')

    @property
    def bijkomendeParameter(self):
        """Detail typering van de kantopsluiting."""
        return self._bijkomendeParameter.waarde

    @bijkomendeParameter.setter
    def bijkomendeParameter(self, value):
        self._bijkomendeParameter.set_waarde(value, owner=self)

    @property
    def fabricageLengte(self):
        """De lengte van de individuele kantopsluiting volgens de norm."""
        return self._fabricageLengte.waarde

    @fabricageLengte.setter
    def fabricageLengte(self, value):
        self._fabricageLengte.set_waarde(value, owner=self)
