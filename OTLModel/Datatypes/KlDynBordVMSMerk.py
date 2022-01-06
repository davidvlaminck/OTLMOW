# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordVMSMerk(Keuzelijst):
    """Keuzelijst met de gangbare merken van VMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""

    def __init__(self):
        super().__init__(naam="KlDynBordVMSMerk",
                         label="Dyn bord VMS merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordVMSMerk",
                         definition="Keuzelijst met de gangbare merken van VMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordVMSMerk")

