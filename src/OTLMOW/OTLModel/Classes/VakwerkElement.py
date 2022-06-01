# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject
from OTLMOW.OTLModel.Datatypes.KlTypeVakwerkElement import KlTypeVakwerkElement


# Generated with OTLClassCreator. To modify: extend, do not edit
class VakwerkElement(ConstructiefObject):
    """Element dat deel uitmaakt van een constructie waarbij balken en staven, volgens een stelsel van rechthoeken en/of driehoeken, aan de uiteinden en/of kruiselings verbonden worden tot een onwrikbaar geheel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VakwerkElement'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._typeVakwerkElement = OTLAttribuut(field=KlTypeVakwerkElement,
                                                naam='typeVakwerkElement',
                                                label='type vakwerkelement',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#VakwerkElement.typeVakwerkElement',
                                                definition='Het type van vakwerkelement.',
                                                owner=self)

    @property
    def typeVakwerkElement(self):
        """Het type van vakwerkelement."""
        return self._typeVakwerkElement.get_waarde()

    @typeVakwerkElement.setter
    def typeVakwerkElement(self, value):
        self._typeVakwerkElement.set_waarde(value, owner=self)
