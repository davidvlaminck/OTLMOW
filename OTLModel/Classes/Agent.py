# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.DtcContactinfo import DtcContactinfo
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Agent:(AttributeInfo)
    """Iemand die of iets dat kan handelen of een effect kan teweeg brengen."""

    typeURI = 'http://purl.org/dc/terms/Agent'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._agentId = OTLAttribuut(field=DtcIdentificator,
                                     naam='agentId',
                                     label='agent identificatie',
                                     objectUri='http://purl.org/dc/terms/Agent.agentId',
                                     definition='Identificatie van de agent volgens een bepaalde bron.')

        self._contactinfo = OTLAttribuut(field=DtcContactinfo,
                                         naam='contactinfo',
                                         label='Contactinfo',
                                         objectUri='http://purl.org/dc/terms/Agent.contactinfo',
                                         kardinaliteit_max='*',
                                         definition='Algemene contactgegevens voor de agent.')

        self._naam = OTLAttribuut(field=StringField,
                                  naam='naam',
                                  label='naam',
                                  objectUri='http://purl.org/dc/terms/Agent.naam',
                                  definition='De naam waarmee de agent doorgaans benoemd wordt.')

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
