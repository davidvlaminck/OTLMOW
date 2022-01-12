# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLichtmastLeverancier(Keuzelijst):
    """Lijst van mogelijke leveranciers van lichtmasten."""

    def __init__(self):
        super().__init__(naam="KlLichtmastLeverancier",
                         label="Lichtmast leverancier",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLichtmastLeverancier",
                         definition="Lijst van mogelijke leveranciers van lichtmasten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLichtmastLeverancier")

        self.add_option("andere", "andere", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/andere")
        self.add_option("baert", "baert", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/baert")
        self.add_option("industrielle-Borraine", "industrielle Borraine", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/industrielle-Borraine")
        self.add_option("metalogalva", "metalogalva", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/metalogalva")
        self.add_option("petitJean", "petitJean", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/petitJean")
        self.add_option("safetyProducts", "safetyProducts", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/safetyProducts")
        self.add_option("valmont", "valmont", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLichtmastLeverancier/valmont")
