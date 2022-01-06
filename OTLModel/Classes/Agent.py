# coding=utf-8
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcContactinfo import DtcContactinfo
from OTLModel.Datatypes.DtcIdentificator import DtcIdentificator
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Agent:
    """Iemand die of iets dat kan handelen of een effect kan teweeg brengen."""

    typeURI = "http://purl.org/dc/terms/Agent"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        self.agentId = DtcIdentificator()
        """Identificatie van de agent volgens een bepaalde bron."""
        self.agentId.naam = "agentId"
        self.agentId.label = "agent identificatie"
        self.agentId.uri = "http://purl.org/dc/terms/Agent.agentId"
        self.agentId.definition = "Identificatie van de agent volgens een bepaalde bron."
        self.agentId.constraints = ""
        self.agentId.usagenote = ""
        self.agentId.deprecated_version = ""

        contactinfoField = DtcContactinfo()
        contactinfoField.naam = "contactinfo"
        contactinfoField.label = "Contactinfo"
        contactinfoField.uri = "http://purl.org/dc/terms/Agent.contactinfo"
        contactinfoField.definition = "Algemene contactgegevens voor de agent."
        contactinfoField.constraints = ""
        contactinfoField.usagenote = ""
        contactinfoField.deprecated_version = ""
        self.contactinfo = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=contactinfoField)
        """Algemene contactgegevens voor de agent."""

        self.naam = StringField(naam="naam",
                                label="naam",
                                uri="http://purl.org/dc/terms/Agent.naam",
                                definition="De naam waarmee de agent doorgaans benoemd wordt.",
                                constraints="",
                                usagenote="",
                                deprecated_version="")
        """De naam waarmee de agent doorgaans benoemd wordt."""
