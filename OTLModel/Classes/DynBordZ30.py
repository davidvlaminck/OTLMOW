# coding=utf-8
from OTLModel.Classes.LEDBord import LEDBord
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDynBordZ30Merk import KlDynBordZ30Merk
from OTLModel.Datatypes.KlDynBordZ30Modelnaam import KlDynBordZ30Modelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordZ30(LEDBord):
    """Dynamisch verkeersbord dat verkeerstekens voor een zone 30 kan weergeven."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlDynBordZ30Merk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30.merk",
                                    definition="Merk van het dynamisch zone-30 bord.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk van het dynamisch zone-30 bord."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlDynBordZ30Modelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordZ30.modelnaam",
                                         definition="De modelnaam van het Z30-bord.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """De modelnaam van het Z30-bord."""
