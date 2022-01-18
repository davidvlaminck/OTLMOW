# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KlIOBitSnelheid import KlIOBitSnelheid
from OTLModel.Datatypes.KlIOKaartMerk import KlIOKaartMerk
from OTLModel.Datatypes.KlIOKaartModelnaam import KlIOKaartModelnaam
from OTLModel.Datatypes.KlIORichting import KlIORichting
from OTLModel.Datatypes.KlIOSignaaltype import KlIOSignaaltype
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class IOKaart(AIMObject, AttributeInfo):
    """Een kaart of module die gebruikt wordt voor de ingang of uitgang van een verwerkingseenheid (bv. een PLC). Op de IO-kaart worden perifere toestellen en sensoren aangesloten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._bitsnelheid = OTLAttribuut(field=KlIOBitSnelheid,
                                         naam='bitsnelheid',
                                         label='bitsnelheid',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.bitsnelheid',
                                         definition='De snelheid (hoeveel bits per seconde) waarmee data doorgestuurd kan worden.')

        self._firmwareversie = OTLAttribuut(field=StringField,
                                            naam='firmwareversie',
                                            label='firmwareversie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.firmwareversie',
                                            definition='Versie van de firmware.')

        self._merk = OTLAttribuut(field=KlIOKaartMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.merk',
                                  definition='Het merk van de IO-kaart.')

        self._modelnaam = OTLAttribuut(field=KlIOKaartModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.modelnaam',
                                       definition='De modelnaam van de IO-kaart.')

        self._poortadres = OTLAttribuut(field=StringField,
                                        naam='poortadres',
                                        label='poortadres',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.poortadres',
                                        definition='Het IO-kaart poortadres wordt gebruikt om data uit te wisselen met een perifere component. Elke component krijgt een uniek poortadres toegekend, dit adres is een hexadecimaal getal.')

        self._richting = OTLAttribuut(field=KlIORichting,
                                      naam='richting',
                                      label='richting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.richting',
                                      definition='Geeft aan of de IO-kaart dient voor input of output.')

        self._signaalType = OTLAttribuut(field=KlIOSignaaltype,
                                         naam='signaalType',
                                         label='signaalType',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IOKaart.signaalType',
                                         definition='Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal.')

    @property
    def bitsnelheid(self):
        """De snelheid (hoeveel bits per seconde) waarmee data doorgestuurd kan worden."""
        return self._bitsnelheid.waarde

    @bitsnelheid.setter
    def bitsnelheid(self, value):
        self._bitsnelheid.set_waarde(value, owner=self)

    @property
    def firmwareversie(self):
        """Versie van de firmware."""
        return self._firmwareversie.waarde

    @firmwareversie.setter
    def firmwareversie(self, value):
        self._firmwareversie.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de IO-kaart."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de IO-kaart."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def poortadres(self):
        """Het IO-kaart poortadres wordt gebruikt om data uit te wisselen met een perifere component. Elke component krijgt een uniek poortadres toegekend, dit adres is een hexadecimaal getal."""
        return self._poortadres.waarde

    @poortadres.setter
    def poortadres(self, value):
        self._poortadres.set_waarde(value, owner=self)

    @property
    def richting(self):
        """Geeft aan of de IO-kaart dient voor input of output."""
        return self._richting.waarde

    @richting.setter
    def richting(self, value):
        self._richting.set_waarde(value, owner=self)

    @property
    def signaalType(self):
        """Geeft aan of de IO-kaart werkt met een digitaal of met een analoog signaal."""
        return self._signaalType.waarde

    @signaalType.setter
    def signaalType(self, value):
        self._signaalType.set_waarde(value, owner=self)
