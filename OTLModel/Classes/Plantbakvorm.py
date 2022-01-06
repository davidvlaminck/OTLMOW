# coding=utf-8
from OTLModel.Classes.VegetatieElement import VegetatieElement
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Plantbakvorm(VegetatieElement):
    """Beplanting die niet in volle grond werd aangebracht, maar in bakvorm."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plantbakvorm"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.isBereikbaar = BooleanField(naam="isBereikbaar",
                                         label="is bereikbaar",
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plantbakvorm.isBereikbaar",
                                         definition="Duidt aan of de plantbakvorm door de mens fysiek bereikbaar is zonder hulpmiddelen.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Duidt aan of de plantbakvorm door de mens fysiek bereikbaar is zonder hulpmiddelen."""

        self.isVerplaatsbaar = BooleanField(naam="isVerplaatsbaar",
                                            label="is verplaatsbaar",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plantbakvorm.isVerplaatsbaar",
                                            definition="Duidt aan of de plantbakvorm al dan niet verplaatsbaar is en dus niet permanent verankerd werd met het aardoppervlak.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Duidt aan of de plantbakvorm al dan niet verplaatsbaar is en dus niet permanent verankerd werd met het aardoppervlak."""

        self.oppervlakteBak = KwantWrdInVierkanteMeter()
        """De afmetingen van de plantbak in vierkante meter."""
        self.oppervlakteBak.naam = "oppervlakteBak"
        self.oppervlakteBak.label = "oppervlakte"
        self.oppervlakteBak.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plantbakvorm.oppervlakteBak"
        self.oppervlakteBak.definition = "De afmetingen van de plantbak in vierkante meter."
        self.oppervlakteBak.constraints = ""
        self.oppervlakteBak.usagenote = ""
        self.oppervlakteBak.deprecated_version = ""

        self.volume = KwantWrdInKubiekeMeter()
        """De inhoud of grootte van de plantbakvorm in de ruimte in kubieke meter."""
        self.volume.naam = "volume"
        self.volume.label = "volume"
        self.volume.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Plantbakvorm.volume"
        self.volume.definition = "De inhoud of grootte van de plantbakvorm in de ruimte in kubieke meter."
        self.volume.constraints = ""
        self.volume.usagenote = ""
        self.volume.deprecated_version = ""
