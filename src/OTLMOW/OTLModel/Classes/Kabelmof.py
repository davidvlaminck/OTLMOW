# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.KlKabelmofType import KlKabelmofType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelmof(AIMNaamObject):
    """Een verbindingsgreep die aansluitingen van kabels rondom afsluit."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlKabelmofType,
                                  naam='type',
                                  label='type kabelmof',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof.type',
                                  definition='Soort mof volgens een lijst van types.')

    @property
    def type(self):
        """Soort mof volgens een lijst van types."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
