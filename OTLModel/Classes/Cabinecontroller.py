# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Controller import Controller
from OTLModel.Datatypes.KlControllerBeveiligingssleutel import KlControllerBeveiligingssleutel
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Cabinecontroller(Controller, AttributeInfo):
    """Controller die zorgt voor de bewaking en bediening van de geschakelde verlichtingsaftakkingen en voor bewaking van de voedingsinstallatie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Controller.__init__(self)

        self._beveiligingssleutel = OTLAttribuut(field=KlControllerBeveiligingssleutel,
                                                 naam='beveiligingssleutel',
                                                 label='beveiligingssleutel',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller.beveiligingssleutel',
                                                 definition='De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen.')

        self._merk = OTLAttribuut(field=StringField,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller.merk',
                                  definition='Merk van de cabinecontroller.')

        self._modelnaam = OTLAttribuut(field=StringField,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller.modelnaam',
                                       definition='Modelnaam van de cabinecontroller.')

    @property
    def beveiligingssleutel(self):
        """De encryptie die wordt toegepast om de verbinding tussen lokaal en centraal te beveiligen."""
        return self._beveiligingssleutel.waarde

    @beveiligingssleutel.setter
    def beveiligingssleutel(self, value):
        self._beveiligingssleutel.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merk van de cabinecontroller."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van de cabinecontroller."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
