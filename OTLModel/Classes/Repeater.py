# coding=utf-8
from OTLModel.Classes.ZenderOntvangerToegang import ZenderOntvangerToegang
from OTLModel.Datatypes.DteTekstblok import DteTekstblok
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlRepeaterMerk import KlRepeaterMerk
from OTLModel.Datatypes.KlRepeaterModelnaam import KlRepeaterModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class Repeater(ZenderOntvangerToegang):
    """Apparatuur die het ontvangen signaal versterkt doorgeeft."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Repeater"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlRepeaterMerk(),
                                    objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Repeater.merk",
                                    definition="Het merk van de repeater.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van de repeater."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlRepeaterModelnaam(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Repeater.modelnaam",
                                         definition="De modelnaam/product range van een repeater.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van een repeater."""

        self.toepassing = DteTekstblok()
        """De techniek of standaard waarmee signalen over het netwerk verstuurd worden. Mogelijke waarden zijn onder andere: KAR,  wifi, GPRS of GSM.."""
        self.toepassing.naam = "toepassing"
        self.toepassing.label = "toepassing"
        self.toepassing.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Repeater.toepassing"
        self.toepassing.definition = "De techniek of standaard waarmee signalen over het netwerk verstuurd worden. Mogelijke waarden zijn onder andere: KAR,  wifi, GPRS of GSM.."
        self.toepassing.constraints = ""
        self.toepassing.usagenote = ""
        self.toepassing.deprecated_version = ""
