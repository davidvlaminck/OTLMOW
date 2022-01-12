# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRechteSteunType(Keuzelijst):
    """Keuzelijst die de verschillende types rechte steunen aanduidt."""

    def __init__(self):
        super().__init__(naam="KlRechteSteunType",
                         label="Rechte steun type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRechteSteunType",
                         definition="Keuzelijst die de verschillende types rechte steunen aanduidt.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRechteSteunType")

        self.add_option("VRI-met-zwanehals", "VRI met zwanehals", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/VRI-met-zwanehals")
        self.add_option("a-paal", "a-paal", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/a-paal")
        self.add_option("bi-flash", "bi-flash", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/bi-flash")
        self.add_option("d-paal", "d-paal", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/d-paal")
        self.add_option("variabele-Z30", "variabele Z30", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRechteSteunType/variabele-Z30")
