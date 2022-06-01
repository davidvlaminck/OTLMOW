# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlTypeOplegging import KlTypeOplegging


# Generated with OTLClassCreator. To modify: extend, do not edit
class Oplegging(AIMObject):
    """Een oplegging of steunpunt is een element dat is vastgemaakt aan de vaste ondergrond (vb. aan het landhoofd) of aan een ander constructiedeel. Een oplegging beperkt hier de beweging van de bewegend lichaam (vb. van de brugklap). Een oplegging kan ook een dempend effect hebben bij het sluiten van een bewegend lichaam."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlTypeOplegging,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Oplegging.type',
                                  definition='De soort oplegging.',
                                  owner=self)

    @property
    def type(self):
        """De soort oplegging."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
