# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KlBinnenverlichtingstoestelSoortLamp import KlBinnenverlichtingstoestelSoortLamp


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aanstraalverlichting(AIMObject):
    """Lamp met fel gebundeld licht die het verlicht gebied duidelijk zichtbaar maakt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aanstraalverlichting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlBinnenverlichtingstoestelSoortLamp,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aanstraalverlichting.type',
                                  definition='Geeft het soort lamp mee dat voor de verlichting zorgt.')

    @property
    def type(self):
        """Geeft het soort lamp mee dat voor de verlichting zorgt."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
