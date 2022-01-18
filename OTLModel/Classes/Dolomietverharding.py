# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AndereVerharding import AndereVerharding
from OTLModel.Datatypes.KlDolomietType import KlDolomietType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dolomietverharding(AndereVerharding, AttributeInfo):
    """Bedekking van een onverharde zone die opgebouwd is uit een niet-gecompacteerde groep van individuele componenten die voldoen aan de volgende specificaties: dolomiet (gele kleur, gemiddelde korrelgrootte), onregelmatige vorm, onregelmatig verband."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dolomietverharding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereVerharding.__init__(self)
        AttributeInfo.__init__(self)

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
