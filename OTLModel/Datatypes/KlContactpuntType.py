# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlContactpuntType(Keuzelijst):
    """Keuzelijst voor types van deurcontacten volgens de gebruikte techniek."""

    def __init__(self):
        super().__init__(naam="KlContactpuntType",
                         label="Contactpunt type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlContactpuntType",
                         definition="Keuzelijst voor types van deurcontacten volgens de gebruikte techniek.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlContactpuntType")

        self.add_option("deurcontact", "deurcontact", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntType/deurcontact")
        self.add_option("magneetcontact", "magneetcontact", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlContactpuntType/magneetcontact")
