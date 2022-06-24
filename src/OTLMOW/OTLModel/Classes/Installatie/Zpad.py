# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.NaampadObject import NaampadObject
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.KlZpadType import KlZpadType
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zpad(NaampadObject, GeenGeometrie):
    """End-to-end gebruikersverbinding over het transport netwerk."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NaampadObject.__init__(self)
        GeenGeometrie.__init__(self)

        self._WANCapaciteit = OTLAttribuut(field=IntegerField,
                                           naam='WANCapaciteit',
                                           label='wan capaciteit',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.WANCapaciteit',
                                           definition='Capaciteit van de verbinding vanuit het standpunt van de gebruiker.',
                                           owner=self)

        self._netwerkklant = OTLAttribuut(field=StringField,
                                          naam='netwerkklant',
                                          label='netwerkklant',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.netwerkklant',
                                          definition='Naam van de organisatie van de gebruiker.',
                                          owner=self)

        self._omschrijving = OTLAttribuut(field=StringField,
                                          naam='omschrijving',
                                          label='omschrijving',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.omschrijving',
                                          definition='Beschrijving van de aard en/of doel van de verbinding.',
                                          owner=self)

        self._type = OTLAttribuut(field=KlZpadType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Zpad.type',
                                  definition='De soort verbinding, gebaseerd op het gebruikte protocol.',
                                  owner=self)

    @property
    def WANCapaciteit(self):
        """Capaciteit van de verbinding vanuit het standpunt van de gebruiker."""
        return self._WANCapaciteit.get_waarde()

    @WANCapaciteit.setter
    def WANCapaciteit(self, value):
        self._WANCapaciteit.set_waarde(value, owner=self)

    @property
    def netwerkklant(self):
        """Naam van de organisatie van de gebruiker."""
        return self._netwerkklant.get_waarde()

    @netwerkklant.setter
    def netwerkklant(self, value):
        self._netwerkklant.set_waarde(value, owner=self)

    @property
    def omschrijving(self):
        """Beschrijving van de aard en/of doel van de verbinding."""
        return self._omschrijving.get_waarde()

    @omschrijving.setter
    def omschrijving(self, value):
        self._omschrijving.set_waarde(value, owner=self)

    @property
    def type(self):
        """De soort verbinding, gebaseerd op het gebruikte protocol."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
