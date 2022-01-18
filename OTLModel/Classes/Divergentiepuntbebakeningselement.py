# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Signalisatie import Signalisatie
from OTLModel.Datatypes.KlDivergentiepuntbebakeningselementType import KlDivergentiepuntbebakeningselementType
from OTLModel.Datatypes.KlFolieType import KlFolieType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Divergentiepuntbebakeningselement(AIMObject, Signalisatie, AttributeInfo):
    """Een constructie met als doel de zichtbaarheid van het divergentiepunt te vergroten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)
        Signalisatie.__init__(self)

        self._folietype = OTLAttribuut(field=KlFolieType,
                                       naam='folietype',
                                       label='folietype',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement.folietype',
                                       definition='Het type folie dat bevestigd is aan het Divergentiepuntbebakeningselement.')

        self._type = OTLAttribuut(field=KlDivergentiepuntbebakeningselementType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement.type',
                                  definition='De vormen van het divergentiepuntbebakeningselement.')

    @property
    def folietype(self):
        """Het type folie dat bevestigd is aan het Divergentiepuntbebakeningselement."""
        return self._folietype.waarde

    @folietype.setter
    def folietype(self, value):
        self._folietype.set_waarde(value, owner=self)

    @property
    def type(self):
        """De vormen van het divergentiepuntbebakeningselement."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
