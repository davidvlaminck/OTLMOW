# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLObject import OTLObject
from OTLMOW.OTLModel.BaseClasses.RelatieInteractor import RelatieInteractor
from OTLMOW.OTLModel.Datatypes.DtcContactinfo import DtcContactinfo
from OTLMOW.OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Agent(AttributeInfo, OTLObject, RelatieInteractor):
    """Iemand die of iets dat kan handelen of een effect kan teweeg brengen."""

    typeURI = 'http://purl.org/dc/terms/Agent'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        OTLObject.__init__(self)
        RelatieInteractor.__init__(self)

        self._agentId = OTLAttribuut(field=DtcIdentificator,
                                     naam='agentId',
                                     label='agent identificatie',
                                     objectUri='http://purl.org/dc/terms/Agent.agentId',
                                     definition='Identificatie van de agent volgens een bepaalde bron.',
                                     owner=self)

        self._contactinfo = OTLAttribuut(field=DtcContactinfo,
                                         naam='contactinfo',
                                         label='Contactinfo',
                                         objectUri='http://purl.org/dc/terms/Agent.contactinfo',
                                         kardinaliteit_max='*',
                                         definition='Algemene contactgegevens voor de agent.',
                                         owner=self)

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='http://purl.org/dc/terms/Agent.naam',
                                  definition='De naam waarmee de agent doorgaans benoemd wordt.',
                                  owner=self)

    @property
    def agentId(self):
        """Identificatie van de agent volgens een bepaalde bron."""
        return self._agentId.waarde

    @agentId.setter
    def agentId(self, value):
        self._agentId.set_waarde(value, owner=self)

    @property
    def contactinfo(self):
        """Algemene contactgegevens voor de agent."""
        return self._contactinfo.waarde

    @contactinfo.setter
    def contactinfo(self, value):
        self._contactinfo.set_waarde(value, owner=self)

    @property
    def naam(self):
        """De naam waarmee de agent doorgaans benoemd wordt."""
        return self._naam.waarde

    @naam.setter
    def naam(self, value):
        self._naam.set_waarde(value, owner=self)
