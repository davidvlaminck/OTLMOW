# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AndereLaag import AndereLaag
from OTLMOW.OTLModel.Datatypes.KlBeschermingWapeningType import KlBeschermingWapeningType


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeschermingWapening(AndereLaag):
    """De bescherming of de wapening van de onderfundering, fundering of grondmassief."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BeschermingWapening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlBeschermingWapeningType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BeschermingWapening.type',
                                  definition='Het type bescherming of wapening.')

    @property
    def type(self):
        """Het type bescherming of wapening."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
