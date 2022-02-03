# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Classes.Signalisatie import Signalisatie
from OTLMOW.OTLModel.Datatypes.KlDivergentiepuntbebakeningselementType import KlDivergentiepuntbebakeningselementType
from OTLMOW.OTLModel.Datatypes.KlFolieType import KlFolieType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Divergentiepuntbebakeningselement(AIMObject, Signalisatie, PuntGeometrie):
    """Een constructie met als doel de zichtbaarheid van het divergentiepunt te vergroten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)
        PuntGeometrie.__init__(self)

        self._folietype = OTLAttribuut(field=KlFolieType,
                                       naam='folietype',
                                       label='folietype',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement.folietype',
                                       definition='Het type folie dat bevestigd is aan het Divergentiepuntbebakeningselement.',
                                       owner=self)

        self._type = OTLAttribuut(field=KlDivergentiepuntbebakeningselementType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Divergentiepuntbebakeningselement.type',
                                  definition='De vormen van het divergentiepuntbebakeningselement.',
                                  owner=self)

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
