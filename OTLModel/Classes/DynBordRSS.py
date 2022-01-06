# coding=utf-8
from OTLModel.Classes.LEDBord import LEDBord
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDynBordRSSMerk import KlDynBordRSSMerk
from OTLModel.Datatypes.KlDynBordRSSModelnaam import KlDynBordRSSModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordRSS(LEDBord):
    """Dynamisch verkeersbord voor rijstrooksignalisatie (RSS)."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRSS"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlDynBordRSSMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRSS.merk",
                                    definition="Merk van het dynamische bord.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk van het dynamische bord."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlDynBordRSSModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordRSS.modelnaam",
                                         definition="Modelnaam van het RSS-bord.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam van het RSS-bord."""
