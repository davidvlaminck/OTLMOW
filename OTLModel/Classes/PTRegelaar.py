# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPTRegelaarMerk import KlPTRegelaarMerk
from OTLModel.Datatypes.KlPTRegelaarModelnaam import KlPTRegelaarModelnaam
from OTLModel.Datatypes.KlPtRegelaarCommunicatiewijze import KlPtRegelaarCommunicatiewijze
from OTLModel.Datatypes.KlPtRegelaarProtocol import KlPtRegelaarProtocol
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class PTRegelaar(AIMNaamObject):
    """Deze PT-module staat in voor het ontvangen en bewerken van telegrammen van voertuigen van het openbaar vervoer (bussen, trams)."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.communicatiewijze = KeuzelijstField(naam="communicatiewijze",
                                                 label="communicatiewijze",
                                                 lijst=KlPtRegelaarCommunicatiewijze(),
                                                 objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.communicatiewijze",
                                                 definition="De manier waarop de PT-regelaar communiceert met de verkeersregelaar.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """De manier waarop de PT-regelaar communiceert met de verkeersregelaar."""

        lijnnummersField = DtcDocument()
        lijnnummersField.naam = "lijnnummers"
        lijnnummersField.label = "lijnnummers"
        lijnnummersField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.lijnnummers"
        lijnnummersField.definition = "Nummers van de PT lijnen die connecteren met de PT regelaar."
        lijnnummersField.constraints = ""
        lijnnummersField.usagenote = ""
        lijnnummersField.deprecated_version = ""
        self.lijnnummers = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=lijnnummersField)
        """Nummers van de PT lijnen die connecteren met de PT regelaar."""

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlPTRegelaarMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.merk",
                                    definition="Het merk van een PT regelaar.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van een PT regelaar."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlPTRegelaarModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.modelnaam",
                                         definition="De modelnaam/product range van een PT regelaar.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van een PT regelaar."""

        self.protocol = KeuzelijstField(naam="protocol",
                                        label="protocol",
                                        lijst=KlPtRegelaarProtocol(),
                                        objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.protocol",
                                        definition="Naam van het protocol waarmee gecommuniceerd wordt tussen PT-regelaar en verkeersregelaar.",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Naam van het protocol waarmee gecommuniceerd wordt tussen PT-regelaar en verkeersregelaar."""

        voertuignummersField = StringField(naam="voertuignummers",
                                           label="voertuignummers",
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PTRegelaar.voertuignummers",
                                           definition="Nummers van de voertuigen die connecteren met de PT regelaar.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.voertuignummers = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=voertuignummersField)
        """Nummers van de voertuigen die connecteren met de PT regelaar."""
