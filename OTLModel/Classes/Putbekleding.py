# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KlPutbekledingType import KlPutbekledingType
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Putbekleding(AIMObject, AttributeInfo):
    """De soort afwerkingslaag waarmee een put bekleed is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Putbekleding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._laagdikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                       naam='laagdikte',
                                       label='laagdikte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Putbekleding.laagdikte',
                                       definition='De dikte van de bekledingslaag in millimeter.')

        self._type = OTLAttribuut(field=KlPutbekledingType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Putbekleding.type',
                                  definition='Bepaalt het type van de putbekleding.')

    @property
    def laagdikte(self):
        """De dikte van de bekledingslaag in millimeter."""
        return self._laagdikte.waarde

    @laagdikte.setter
    def laagdikte(self, value):
        self._laagdikte.set_waarde(value, owner=self)

    @property
    def type(self):
        """Bepaalt het type van de putbekleding."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
