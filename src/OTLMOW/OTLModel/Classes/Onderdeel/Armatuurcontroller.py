# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Communicatieapparatuur import Communicatieapparatuur
from OTLMOW.OTLModel.Classes.Abstracten.FirmwareObject import FirmwareObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Armatuurcontroller(Communicatieapparatuur, FirmwareObject):
    """Controller die op het verlichtingstoestel wordt gemonteerd en die één verlichtingstoestel aanstuurt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Communicatieapparatuur.__init__(self)
        FirmwareObject.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Verlichtingstoestel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver', deprecated='2.4.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast', deprecated='2.4.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorschakelapparaat')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVOpvoertransformator')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VoedtAangestuurd', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#LEDDriver')

        self._ipAdres = OTLAttribuut(field=DteIPv4Adres,
                                     naam='ipAdres',
                                     label='IP-adres',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.ipAdres',
                                     definition='Het IP-adres van de armatuurcontroller.',
                                     owner=self)

        self._isDummydot = OTLAttribuut(field=BooleanField,
                                        naam='isDummydot',
                                        label='is dummydot',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.isDummydot',
                                        definition='Geeft aan of er in de toekomst een armatuurcontroller kan aangesloten worden op het verlichtingstoestel, maar dat het toestel voorlopig voorzien is van een kortsluitmodule (ook wel dummydot genoemd).',
                                        owner=self)

        self._merk = OTLAttribuut(field=StringField,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.merk',
                                  definition='Merk van de armatuurcontroller.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=StringField,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.modelnaam',
                                       definition='Modelnaam van de armatuurcontroller.',
                                       owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Armatuurcontroller.serienummer',
                                         definition='Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.',
                                         owner=self)

    @property
    def ipAdres(self):
        """Het IP-adres van de armatuurcontroller."""
        return self._ipAdres.get_waarde()

    @ipAdres.setter
    def ipAdres(self, value):
        self._ipAdres.set_waarde(value, owner=self)

    @property
    def isDummydot(self):
        """Geeft aan of er in de toekomst een armatuurcontroller kan aangesloten worden op het verlichtingstoestel, maar dat het toestel voorlopig voorzien is van een kortsluitmodule (ook wel dummydot genoemd)."""
        return self._isDummydot.get_waarde()

    @isDummydot.setter
    def isDummydot(self, value):
        self._isDummydot.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merk van de armatuurcontroller."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van de armatuurcontroller."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def serienummer(self):
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)
