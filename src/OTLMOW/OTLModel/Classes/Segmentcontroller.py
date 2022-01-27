# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Controller import Controller
from OTLMOW.OTLModel.Datatypes.KlControllerBeveiligingssleutel import KlControllerBeveiligingssleutel
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Segmentcontroller(Controller):
    """Controller die zorgt voor de bewaking en bediening van verlichtingssegmenten per paal en aldus zorgt voor de communicatie tussen de cabine en de armatuurcontrollers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._beveil?igingssleutel = OTLAttribuut(field=KlControllerBeveiligingssleutel,
                                                  naam='beveil?igingssleutel',
                                                  label='beveiligingssleutel',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.beveil?igingssleutel',
                                                  usagenote='Attribuut uit gebruik sinds versie 2.0.0 ',
                                                  deprecated_version='2.0.0',
                                                  definition='De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen.')

        self._beveiligingssleutel = OTLAttribuut(field=KlControllerBeveiligingssleutel,
                                                 naam='beveiligingssleutel',
                                                 label='beveiligingssleutel',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.beveiligingssleutel',
                                                 definition='De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen.')

        self._merk = OTLAttribuut(field=StringField,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.merk',
                                  definition='Merk van de segmentcontroller.')

        self._modelnaam = OTLAttribuut(field=StringField,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller.modelnaam',
                                       definition='Modelnaam van de segmentcontroller.')

    @property
    def beveil?igingssleutel(self):
        """De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen."""
        return self._beveil?igingssleutel.waarde

    @beveil?igingssleutel.setter
    def beveil?igingssleutel(self, value):
        self._beveil?igingssleutel.set_waarde(value, owner=self)

    @property
    def beveiligingssleutel(self):
        """De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen."""
        return self._beveiligingssleutel.waarde

    @beveiligingssleutel.setter
    def beveiligingssleutel(self, value):
        self._beveiligingssleutel.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merk van de segmentcontroller."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van de segmentcontroller."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
