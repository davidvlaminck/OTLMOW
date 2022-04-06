# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AbstracteAanvullendeGeometrie import AbstracteAanvullendeGeometrie
from OTLMOW.OTLModel.Datatypes.KlBijlageMetGeometrieType import KlBijlageMetGeometrieType
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class AanvullendeGeometrie(AbstracteAanvullendeGeometrie, VlakGeometrie):
    """Beschrijft een geometrie die aanvullend is bij de de werking van een asset maar beschrijft niet de asset zelf, bv. een detailplan of een werkingsgebied met een specifieke locatie, enz...De aanvullende geometrie kan al dan niet een bijlage bevatten."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AanvullendeGeometrie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AbstracteAanvullendeGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._type = OTLAttribuut(field=KlBijlageMetGeometrieType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AanvullendeGeometrie.type',
                                  definition='Het type van aanvullende geometrie.',
                                  owner=self)

    @property
    def type(self):
        """Het type van aanvullende geometrie."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
