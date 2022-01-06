from OTLModel.Classes.AndereVerharding import AndereVerharding
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlSchanskorfVorm import KlSchanskorfVorm
from OTLModel.Datatypes.KlStortsteenKaliber import KlStortsteenKaliber
from OTLModel.Datatypes.KlStortsteenType import KlStortsteenType
from OTLModel.Datatypes.KlTypeSchanskorf import KlTypeSchanskorf


# Generated with OTLClassCreator. To modify: extend, do not edit
class Schanskorf(AndereVerharding):
    """Een schanskorf bestaat uit een metalen gaasnet dat wordt gevuld met steenachtige materialen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.heeftVerankeringspalen = BooleanField(naam="heeftVerankeringspalen",
                                                   label="heeft verankeringspalen",
                                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.heeftVerankeringspalen",
                                                   definition="Aanduiding of de palen de functie hebben om een schanskorf te verankeren.",
                                                   constraints="",
                                                   usagenote="",
                                                   deprecated_version="")
        """Aanduiding of de palen de functie hebben om een schanskorf te verankeren."""

        self.isGegalvaniseerd = BooleanField(naam="isGegalvaniseerd",
                                             label="is gegalvaniseerd",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.isGegalvaniseerd",
                                             definition="Aanduiding of de schanskorf gegalvaniseerd is.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Aanduiding of de schanskorf gegalvaniseerd is."""

        self.isGelast = BooleanField(naam="isGelast",
                                     label="is gelast",
                                     uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.isGelast",
                                     definition="Aanduiding of de schanskorf gelast is.",
                                     constraints="",
                                     usagenote="",
                                     deprecated_version="")
        """Aanduiding of de schanskorf gelast is."""

        self.kaliber = KeuzelijstField(naam="kaliber",
                                       label="kaliber",
                                       lijst=KlStortsteenKaliber(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.kaliber",
                                       definition="Het kaliber of gemiddelde diameter van de stenen in de schanskorf.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Het kaliber of gemiddelde diameter van de stenen in de schanskorf."""

        self.materiaalVulling = KeuzelijstField(naam="materiaalVulling",
                                                label="materiaalvulling",
                                                lijst=KlStortsteenType(),
                                                uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.materiaalVulling",
                                                definition="Het soort stenen waaruit de opvulling van een schanskorf bestaat.",
                                                constraints="",
                                                usagenote="",
                                                deprecated_version="")
        """Het soort stenen waaruit de opvulling van een schanskorf bestaat."""

        technischeFicheField = DtcDocument()
        technischeFicheField.naam = "technischeFiche"
        technischeFicheField.label = "technische fiche"
        technischeFicheField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.technischeFiche"
        technischeFicheField.definition = "De technische fiche van de schanskorven als bijlage."
        technischeFicheField.constraints = ""
        technischeFicheField.usagenote = ""
        technischeFicheField.deprecated_version = ""
        self.technischeFiche = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=technischeFicheField)
        """De technische fiche van de schanskorven als bijlage."""

        self.type = KeuzelijstField(naam="type",
                                    label="type",
                                    lijst=KlTypeSchanskorf(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.type",
                                    definition="Duidt het type schanskorf aan.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Duidt het type schanskorf aan."""

        self.vorm = KeuzelijstField(naam="vorm",
                                    label="vorm",
                                    lijst=KlSchanskorfVorm(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schanskorf.vorm",
                                    definition="De gebruikte vorm van de schanskorf.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """De gebruikte vorm van de schanskorf."""
