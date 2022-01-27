# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AndereVerharding import AndereVerharding
from src.OTLMOW.OTLModel.Datatypes.KlDolomietType import KlDolomietType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dolomietverharding(AndereVerharding):
    """Bedekking van een onverharde zone die opgebouwd is uit een niet-gecompacteerde groep van individuele componenten die voldoen aan de volgende specificaties: dolomiet (gele kleur, gemiddelde korrelgrootte), onregelmatige vorm, onregelmatig verband."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dolomietverharding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlDolomietType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dolomietverharding.type',
                                  definition='Het type dolomiet.')

    @property
    def type(self):
        """Het type dolomiet."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
