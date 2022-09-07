# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AndereLaag import AndereLaag
from OTLMOW.OTLModel.Datatypes.KlScheurremmendeLaagType import KlScheurremmendeLaagType
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ScheurremmendeLaag(AndereLaag, VlakGeometrie):
    """Een scheurremmende laag is een laag onder andere bitumineuze lagen om reflectiescheurvorming tegen te gaan of een wegstructuur te versterken (asfaltwapening)."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ScheurremmendeLaag'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereLaag.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Fundering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Markering')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SelNietSelLus')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Straatmeubilair')

        self._type = OTLAttribuut(field=KlScheurremmendeLaagType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ScheurremmendeLaag.type',
                                  definition='Het type scheurremmende laag.',
                                  owner=self)

    @property
    def type(self):
        """Het type scheurremmende laag."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
