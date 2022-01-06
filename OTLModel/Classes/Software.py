from OTLModel.Classes.SoftwareToegang import SoftwareToegang
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.DtcSoftwarePoortconfiguratie import DtcSoftwarePoortconfiguratie
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSoftwareLicentie import KlSoftwareLicentie
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Datatypes.URIField import URIField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Software(SoftwareToegang):
    """Geheel van computerprogramma's met bijbehorende data."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aangebodenServices = DtcDocument()
        """De endpoints van diensten."""
        self.aangebodenServices.naam = "aangebodenServices"
        self.aangebodenServices.label = "aangeboden services"
        self.aangebodenServices.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.aangebodenServices"
        self.aangebodenServices.definition = "De endpoints van diensten."
        self.aangebodenServices.constraints = ""
        self.aangebodenServices.usagenote = ""
        self.aangebodenServices.deprecated_version = ""

        self.buildnummer = StringField(naam="buildnummer",
                                       label="buildnummer",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.buildnummer",
                                       definition="De software build.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """De software build."""

        self.dependencies = DtcDocument()
        """Afhankelijkheden met andere diensten."""
        self.dependencies.naam = "dependencies"
        self.dependencies.label = "dependencies"
        self.dependencies.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.dependencies"
        self.dependencies.definition = "Afhankelijkheden met andere diensten."
        self.dependencies.constraints = ""
        self.dependencies.usagenote = ""
        self.dependencies.deprecated_version = ""

        self.licentie = KeuzelijstField(naam="licentie",
                                        label="licentie",
                                        lijst=KlSoftwareLicentie(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.licentie",
                                        definition="De licentievorm van de software (bv. commercieel, shareware, freeware, open source [BSD, Apache, GPL],...).",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """De licentievorm van de software (bv. commercieel, shareware, freeware, open source [BSD, Apache, GPL],...)."""

        self.onlineDocumentatie = URIField(naam="onlineDocumentatie",
                                           label="online documentatie",
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.onlineDocumentatie",
                                           definition="De url waarop documentatie over de software te vinden is.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """De url waarop documentatie over de software te vinden is."""

        poortenconfiguratieField = DtcSoftwarePoortconfiguratie()
        poortenconfiguratieField.naam = "poortenconfiguratie"
        poortenconfiguratieField.label = "poortenconfiguratie"
        poortenconfiguratieField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.poortenconfiguratie"
        poortenconfiguratieField.definition = "Beschrijft welke poort voor welke service gebruikt wordt."
        poortenconfiguratieField.constraints = ""
        poortenconfiguratieField.usagenote = ""
        poortenconfiguratieField.deprecated_version = ""
        self.poortenconfiguratie = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=poortenconfiguratieField)
        """Beschrijft welke poort voor welke service gebruikt wordt."""

        self.versie = StringField(naam="versie",
                                  label="versie",
                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software.versie",
                                  definition="Het versienummer van de software.",
                                  constraints="",
                                  usagenote="",
                                  deprecated_version="")
        """Het versienummer van de software."""
