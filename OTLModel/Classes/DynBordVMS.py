# coding=utf-8
from OTLModel.Classes.LEDBord import LEDBord
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDynBordVMSMerk import KlDynBordVMSMerk
from OTLModel.Datatypes.KlDynBordVMSModelnaam import KlDynBordVMSModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DynBordVMS(LEDBord):
    """Dynamisch verkeersbord dat dynamische verkeerstekens  (linkerzijde) en teksten (rechterzijde) kan afbeelden. VMS staat voor Variable Message Signs."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.merk = KeuzelijstField(naam="merk",
                                    label="merk",
                                    lijst=KlDynBordVMSMerk(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS.merk",
                                    definition="Merk van het dynamische bord.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Merk van het dynamische bord."""

        self.modelnaam = KeuzelijstField(naam="modelnaam",
                                         label="modelnaam",
                                         lijst=KlDynBordVMSModelnaam(),
                                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DynBordVMS.modelnaam",
                                         definition="Modelnaam van het VMS-bord.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Modelnaam van het VMS-bord."""
