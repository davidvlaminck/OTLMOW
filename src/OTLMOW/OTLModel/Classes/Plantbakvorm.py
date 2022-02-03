# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.VegetatieElement import VegetatieElement
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Plantbakvorm(VegetatieElement, VlakGeometrie):
    """Beplanting die niet in volle grond werd aangebracht, maar in bakvorm."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plantbakvorm'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        VegetatieElement.__init__(self)
        VlakGeometrie.__init__(self)

        self._isBereikbaar = OTLAttribuut(field=BooleanField,
                                          naam='isBereikbaar',
                                          label='is bereikbaar',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plantbakvorm.isBereikbaar',
                                          definition='Duidt aan of de plantbakvorm door de mens fysiek bereikbaar is zonder hulpmiddelen.',
                                          owner=self)

        self._isVerplaatsbaar = OTLAttribuut(field=BooleanField,
                                             naam='isVerplaatsbaar',
                                             label='is verplaatsbaar',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plantbakvorm.isVerplaatsbaar',
                                             definition='Duidt aan of de plantbakvorm al dan niet verplaatsbaar is en dus niet permanent verankerd werd met het aardoppervlak.',
                                             owner=self)

        self._oppervlakteBak = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                            naam='oppervlakteBak',
                                            label='oppervlakte',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plantbakvorm.oppervlakteBak',
                                            definition='De afmetingen van de plantbak in vierkante meter.',
                                            owner=self)

        self._volume = OTLAttribuut(field=KwantWrdInKubiekeMeter,
                                    naam='volume',
                                    label='volume',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plantbakvorm.volume',
                                    definition='De inhoud of grootte van de plantbakvorm in de ruimte in kubieke meter.',
                                    owner=self)

    @property
    def isBereikbaar(self):
        """Duidt aan of de plantbakvorm door de mens fysiek bereikbaar is zonder hulpmiddelen."""
        return self._isBereikbaar.waarde

    @isBereikbaar.setter
    def isBereikbaar(self, value):
        self._isBereikbaar.set_waarde(value, owner=self)

    @property
    def isVerplaatsbaar(self):
        """Duidt aan of de plantbakvorm al dan niet verplaatsbaar is en dus niet permanent verankerd werd met het aardoppervlak."""
        return self._isVerplaatsbaar.waarde

    @isVerplaatsbaar.setter
    def isVerplaatsbaar(self, value):
        self._isVerplaatsbaar.set_waarde(value, owner=self)

    @property
    def oppervlakteBak(self):
        """De afmetingen van de plantbak in vierkante meter."""
        return self._oppervlakteBak.waarde

    @oppervlakteBak.setter
    def oppervlakteBak(self, value):
        self._oppervlakteBak.set_waarde(value, owner=self)

    @property
    def volume(self):
        """De inhoud of grootte van de plantbakvorm in de ruimte in kubieke meter."""
        return self._volume.waarde

    @volume.setter
    def volume(self, value):
        self._volume.set_waarde(value, owner=self)
