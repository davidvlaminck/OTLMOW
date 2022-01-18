# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlPTRegelaarMerk import KlPTRegelaarMerk
from OTLModel.Datatypes.KlPTRegelaarModelnaam import KlPTRegelaarModelnaam
from OTLModel.Datatypes.KlPtRegelaarCommunicatiewijze import KlPtRegelaarCommunicatiewijze
from OTLModel.Datatypes.KlPtRegelaarProtocol import KlPtRegelaarProtocol
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTRegelaar(AIMNaamObject, AttributeInfo):
    """Deze PT-module staat in voor het ontvangen en bewerken van telegrammen van voertuigen van het openbaar vervoer (bussen, trams)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)

        self._communicatiewijze = OTLAttribuut(field=KlPtRegelaarCommunicatiewijze,
                                               naam='communicatiewijze',
                                               label='communicatiewijze',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.communicatiewijze',
                                               definition='De manier waarop de PT-regelaar communiceert met de verkeersregelaar.')

        self._lijnnummers = OTLAttribuut(field=DtcDocument,
                                         naam='lijnnummers',
                                         label='lijnnummers',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.lijnnummers',
                                         kardinaliteit_max='*',
                                         definition='Nummers van de PT lijnen die connecteren met de PT regelaar.')

        self._merk = OTLAttribuut(field=KlPTRegelaarMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.merk',
                                  definition='Het merk van een PT regelaar.')

        self._modelnaam = OTLAttribuut(field=KlPTRegelaarModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.modelnaam',
                                       definition='De modelnaam/product range van een PT regelaar.')

        self._protocol = OTLAttribuut(field=KlPtRegelaarProtocol,
                                      naam='protocol',
                                      label='protocol',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.protocol',
                                      definition='Naam van het protocol waarmee gecommuniceerd wordt tussen PT-regelaar en verkeersregelaar.')

        self._voertuignummers = OTLAttribuut(field=StringField,
                                             naam='voertuignummers',
                                             label='voertuignummers',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.voertuignummers',
                                             kardinaliteit_max='*',
                                             definition='Nummers van de voertuigen die connecteren met de PT regelaar.')

    @property
    def communicatiewijze(self):
        """De manier waarop de PT-regelaar communiceert met de verkeersregelaar."""
        return self._communicatiewijze.waarde

    @communicatiewijze.setter
    def communicatiewijze(self, value):
        self._communicatiewijze.set_waarde(value, owner=self)

    @property
    def lijnnummers(self):
        """Nummers van de PT lijnen die connecteren met de PT regelaar."""
        return self._lijnnummers.waarde

    @lijnnummers.setter
    def lijnnummers(self, value):
        self._lijnnummers.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van een PT regelaar."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van een PT regelaar."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def protocol(self):
        """Naam van het protocol waarmee gecommuniceerd wordt tussen PT-regelaar en verkeersregelaar."""
        return self._protocol.waarde

    @protocol.setter
    def protocol(self, value):
        self._protocol.set_waarde(value, owner=self)

    @property
    def voertuignummers(self):
        """Nummers van de voertuigen die connecteren met de PT regelaar."""
        return self._voertuignummers.waarde

    @voertuignummers.setter
    def voertuignummers(self, value):
        self._voertuignummers.set_waarde(value, owner=self)
