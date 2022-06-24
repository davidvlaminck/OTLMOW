# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AndereVerharding import AndereVerharding
from OTLMOW.OTLModel.Datatypes.KlDolomietType import KlDolomietType


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
                                  definition='Het type dolomiet.',
                                  owner=self)

    @property
    def type(self):
        """Het type dolomiet."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
