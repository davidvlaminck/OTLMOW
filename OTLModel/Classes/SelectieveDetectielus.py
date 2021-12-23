from OTLModel.Classes.SelNietSelLus import SelNietSelLus
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSelLusSoort import KlSelLusSoort
from OTLModel.Datatypes.KlSelLusVerbinding import KlSelLusVerbinding


# Generated with OTLClassCreator
class SelectieveDetectielus(SelNietSelLus):
    """De selectieve detectielussen moeten bepaalde voertuigen toelaten het kruispunt prioritair te dwarsen. Daarvoor zijn die prioritaire voertuigen uitgerust met een zendtoestel dat gecodeerd informatie doorstuurt naar een datalus in het wegdek. Deze lus is verbonden met een demodulator die de informatie decodeert en doorstuurt naar de verkeersregelaar van het te dwarsen kruispunt"""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.heeftMeerdereKruisingen = BooleanField(naam="heeftMeerdereKruisingen",
                                                    label="heeft meerdere kruisingen",
                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus.heeftMeerdereKruisingen",
                                                    definition="Aanduiding of de lus voor meerdere kruispunten wordt gebruikt.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        """Aanduiding of de lus voor meerdere kruispunten wordt gebruikt."""

        soortLusField = KeuzelijstField(naam="soortLus",
                                        label="soort lus",
                                        lijst=KlSelLusSoort(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus.soortLus",
                                        definition="Type detectielus vb bus, tram,...",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        self.soortLus = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=soortLusField)
        """Type detectielus vb bus, tram,..."""

        self.verbinding = KeuzelijstField(naam="verbinding",
                                          label="verbinding",
                                          lijst=KlSelLusVerbinding(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#SelectieveDetectielus.verbinding",
                                          definition="Soort verbinding (serieel of contact).",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Soort verbinding (serieel of contact)."""
