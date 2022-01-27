# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlEcoAfschermingtype import KlEcoAfschermingtype


# Generated with OTLClassCreator. To modify: extend, do not edit
class Afscherming(AIMObject):
    """Schermen of wallen op de rand van het ecoduct die ervoor zorgen dat dieren op de brug niet afgeschrikt worden door de lichten van voorbijrijdende voertuigen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afscherming'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlEcoAfschermingtype,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Afscherming.type',
                                  definition='Het type van afscherming.')

    @property
    def type(self):
        """Het type van afscherming."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
