# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.StringField import StringField


class DtcToezichterWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='https://tz.data.wegenenverkeer.be/ns/implementatieelement#DtcToezichter.naam',
                                  definition='De naam van de toezichter.')

        self._email = OTLAttribuut(field=StringField,
                                        naam='email',
                                        label='email',
                                        objectUri="https://tz.data.wegenenverkeer.be/ns/implementatieelement#DtcToezichter.email",
                                        definition='Het email adres van de toezichter.')

        self._gebruikersnaam = OTLAttribuut(field=StringField,
                                  naam='gebruikersnaam',
                                  label='gebruikersnaam',
                                  objectUri='https://tz.data.wegenenverkeer.be/ns/implementatieelement#DtcToezichter.gebruikersnaam',
                                  definition='De unieke gebruikersnaam van de toezichter.')

        self._voornaam = OTLAttribuut(field=StringField,
                                            naam='voornaam',
                                            label='voornaam',
                                            objectUri='https://tz.data.wegenenverkeer.be/ns/implementatieelement#DtcToezichter.voornaam',
                                            definition='De voornaam van de toezichtgroep.')

    @property
    def voornaam(self):
        """De voornaam van de toezichtgroep."""
        return self._voornaam.waarde

    @voornaam.setter
    def voornaam(self, value):
        self._voornaam.set_waarde(value, owner=self._parent)

    @property
    def gebruikersnaam(self):
        """De unieke gebruikersnaam van de toezichter."""
        return self._gebruikersnaam.waarde

    @gebruikersnaam.setter
    def gebruikersnaam(self, value):
        self._gebruikersnaam.set_waarde(value, owner=self._parent)

    @property
    def naam(self):
        """De naam van de toezichter."""
        return self._naam.waarde

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self._parent)

    @property
    def email(self):
        """Het email adres van de toezichter."""
        return self._email.waarde

    @email.setter
    def email(self, value):
        self._email.set_waarde(value, owner=self._parent)


class DtcToezichter(ComplexField, AttributeInfo):
    """De toezichter van een asset."""
    naam = 'DtcToezichter'
    label = 'Toezichter'
    objectUri = 'https://tz.data.wegenenverkeer.be/ns/dt#DtcToezichter'
    definition = 'De toezichter van een asset..'
    waardeObject = DtcToezichterWaarden

    def __str__(self):
        return ComplexField.__str__(self)
