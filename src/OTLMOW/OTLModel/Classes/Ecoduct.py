# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Datatypes.KlEcoEcoductType import KlEcoEcoductType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ecoduct(AIMObject):
    """Ecoducten of natuurbruggen zorgen ervoor dat dieren veilig de weg kunnen oversteken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduct'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlEcoEcoductType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Ecoduct.type',
                                  definition='Het type van ecoduct, zoals bv ecoveloduct, bermbrug,….')

    @property
    def type(self):
        """Het type van ecoduct, zoals bv ecoveloduct, bermbrug,…."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
