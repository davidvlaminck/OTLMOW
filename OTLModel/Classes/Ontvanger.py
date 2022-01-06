from OTLModel.Classes.ZenderOntvangerToegang import ZenderOntvangerToegang
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlOntvangerMerk import KlOntvangerMerk
from OTLModel.Datatypes.KlOntvangerModelnaam import KlOntvangerModelnaam
from OTLModel.Datatypes.KlOntvangerToepassing import KlOntvangerToepassing


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ontvanger(ZenderOntvangerToegang):
    """Toestel voor het opvangen van signalen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlOntvangerMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.merk",
                                    definition="Het merk van een ontvanger.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Het merk van een ontvanger."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlOntvangerModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.modelnaam",
                                         definition="De modelnaam/product range van een ontvanger.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam/product range van een ontvanger."""

        self.toepassing = KeuzelijstField(naam="toepassing",
                                          label="toepassing",
                                          lijst=KlOntvangerToepassing(),
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.toepassing",
                                          definition="De techniek of standaard waarmee signalen over het netwerk verstuurd worden.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """De techniek of standaard waarmee signalen over het netwerk verstuurd worden."""
