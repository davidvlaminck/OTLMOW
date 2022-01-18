# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KlKabelmofType import KlKabelmofType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kabelmof(AIMNaamObject, AttributeInfo):
    """Een verbindingsgreep die aansluitingen van kabels rondom afsluit."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kabelmof'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)

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
