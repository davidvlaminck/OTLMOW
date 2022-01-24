# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.Fundering import Fundering
from OTLModel.Datatypes.DtcAfmetingBxlInM import DtcAfmetingBxlInM
from OTLModel.Datatypes.KlFunderingBetonkwaliteit import KlFunderingBetonkwaliteit


# Generated with OTLClassCreator. To modify: extend, do not edit
class Betonfundering(Fundering):
    """Abstracte voor funderingen in beton."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._afmetingGrondvlak = OTLAttribuut(field=DtcAfmetingBxlInM,
                                               naam='afmetingGrondvlak',
                                               label='afmeting grondvlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering.afmetingGrondvlak',
                                               usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                               deprecated_version='2.0.0',
                                               definition='De maximale lengte en breedte van bovenkant van de fundering.')

        self._betonkwaliteit = OTLAttribuut(field=KlFunderingBetonkwaliteit,
                                            naam='betonkwaliteit',
                                            label='betonkwaliteit',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering.betonkwaliteit',
                                            usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                            deprecated_version='2.0.0',
                                            definition='Kwaliteit van het beton gebruikt voor de fundering volgens een vaste lijst van mogelijke waarden.')

    @property
    def afmetingGrondvlak(self):
        """De maximale lengte en breedte van bovenkant van de fundering."""
        return self._afmetingGrondvlak.waarde

    @afmetingGrondvlak.setter
    def afmetingGrondvlak(self, value):
        self._afmetingGrondvlak.set_waarde(value, owner=self)

    @property
    def betonkwaliteit(self):
        """Kwaliteit van het beton gebruikt voor de fundering volgens een vaste lijst van mogelijke waarden."""
        return self._betonkwaliteit.waarde

    @betonkwaliteit.setter
    def betonkwaliteit(self, value):
        self._betonkwaliteit.set_waarde(value, owner=self)
