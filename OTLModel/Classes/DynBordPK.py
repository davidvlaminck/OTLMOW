# coding=utf-8
from OTLModel.Classes.LEDBord import LEDBord
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDynBordPKMerk import KlDynBordPKMerk
from OTLModel.Datatypes.KlDynBordPKModelnaam import KlDynBordPKModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordPK(LEDBord):
    """Dynamisch verkeersbord dat een Pijl of Kruis verkeersteken kan afbeelden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlDynBordPKMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK.merk",
                                    definition="Merk van het dynamische bord.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk van het dynamische bord."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlDynBordPKModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordPK.modelnaam",
                                         definition="Modelnaam van het PK-bord.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam van het PK-bord."""
