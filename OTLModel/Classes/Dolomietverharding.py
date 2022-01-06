# coding=utf-8
from OTLModel.Classes.AndereVerharding import AndereVerharding
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDolomietType import KlDolomietType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Dolomietverharding(AndereVerharding):
    """Bedekking van een onverharde zone die opgebouwd is uit een niet-gecompacteerde groep van individuele componenten die voldoen aan de volgende specificaties: dolomiet (gele kleur, gemiddelde korrelgrootte), onregelmatige vorm, onregelmatig verband."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dolomietverharding"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlDolomietType(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dolomietverharding.type",
                                    definition="Het type dolomiet.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het type dolomiet."""
