# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Fundering import Fundering
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlInM import DtcAfmetingBxlInM
from OTLMOW.OTLModel.Datatypes.KlFunderingBetonkwaliteit import KlFunderingBetonkwaliteit
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Betonfundering(Fundering, VlakGeometrie):
    """Abstracte voor funderingen in beton."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0-RC4'

    @abstractmethod
    def __init__(self):
        Fundering.__init__(self)
        VlakGeometrie.__init__(self)

        self._afmetingGrondvlak = OTLAttribuut(field=DtcAfmetingBxlInM,
                                               naam='afmetingGrondvlak',
                                               label='afmeting grondvlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering.afmetingGrondvlak',
                                               usagenote='Klasse uit gebruik sinds versie 2.0.0-RC4',
                                               deprecated_version='2.0.0-RC4',
                                               definition='De maximale lengte en breedte van bovenkant van de fundering.',
                                               owner=self)

        self._betonkwaliteit = OTLAttribuut(field=KlFunderingBetonkwaliteit,
                                            naam='betonkwaliteit',
                                            label='betonkwaliteit',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Betonfundering.betonkwaliteit',
                                            usagenote='Klasse uit gebruik sinds versie 2.0.0-RC4',
                                            deprecated_version='2.0.0-RC4',
                                            definition='Kwaliteit van het beton gebruikt voor de fundering volgens een vaste lijst van mogelijke waarden.',
                                            owner=self)

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
