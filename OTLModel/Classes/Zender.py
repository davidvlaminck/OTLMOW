from OTLModel.Classes.ZenderOntvangerToegang import ZenderOntvangerToegang
from OTLModel.Datatypes.DteTekstblok import DteTekstblok
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlZenderMerk import KlZenderMerk
from OTLModel.Datatypes.KlZenderModelnaam import KlZenderModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Zender(ZenderOntvangerToegang):
    """Een apparaat dat signalen uitzendt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zender"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlZenderMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zender.merk",
                                    definition="Het merk van een zender.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van een zender."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlZenderModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zender.modelnaam",
                                         definition="De modelnaam/product range van een zender.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van een zender."""

        self.toepassing = DteTekstblok()
        """De techniek of standaard waarmee signalen over het netwerk verstuurd worden. Mogelijke waarden zijn onder andere: KAR,  wifi, GPRS of GSM.."""
        self.toepassing.naam = "toepassing"
        self.toepassing.label = "toepassing"
        self.toepassing.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Zender.toepassing"
        self.toepassing.definition = "De techniek of standaard waarmee signalen over het netwerk verstuurd worden. Mogelijke waarden zijn onder andere: KAR,  wifi, GPRS of GSM.."
        self.toepassing.constraints = ""
        self.toepassing.usagenote = ""
        self.toepassing.deprecated_version = ""
