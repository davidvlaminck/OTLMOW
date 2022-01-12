# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordRVMSMerk(Keuzelijst):
    """Keuzelijst met de gangbare merken van RVMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier."""

    def __init__(self):
        super().__init__(naam="KlDynBordRVMSMerk",
                         label="Dyn bord RVMS merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordRVMSMerk",
                         definition="Keuzelijst met de gangbare merken van RVMS borden. De merken verwijzen doorgaans naar de fabrikant of leverancier.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordRVMSMerk")

