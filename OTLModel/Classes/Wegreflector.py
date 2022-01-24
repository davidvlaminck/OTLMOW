# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Bebakening import Bebakening
from OTLModel.Datatypes.KlWegreflectorType import KlWegreflectorType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wegreflector(Bebakening):
    """Heeft als doel de zichtbaarheid van verkeerseilanden te verhogen en geleiding van de weggebruiker langs de weg."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegreflector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlWegreflectorType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Wegreflector.type',
                                  definition='De vorm van wegreflector.')

    @property
    def type(self):
        """De vorm van wegreflector."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
