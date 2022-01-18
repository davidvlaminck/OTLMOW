# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AndereLaag import AndereLaag
from OTLModel.Datatypes.KlScheurremmendeLaagType import KlScheurremmendeLaagType


# Generated with OTLClassCreator. To modify: extend, do not edit
class ScheurremmendeLaag(AndereLaag, AttributeInfo):
    """Een scheurremmende laag is een laag onder andere bitumineuze lagen om reflectiescheurvorming tegen te gaan of een wegstructuur te versterken (asfaltwapening)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ScheurremmendeLaag'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereLaag.__init__(self)
        AttributeInfo.__init__(self)

        self._type = OTLAttribuut(field=KlScheurremmendeLaagType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ScheurremmendeLaag.type',
                                  definition='Het type scheurremmende laag.')

    @property
    def type(self):
        """Het type scheurremmende laag."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
