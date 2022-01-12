# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVentilatorGebruik(Keuzelijst):
    """Keuzelijst die de types van gebruik voor de ventilator aangeeft."""

    def __init__(self):
        super().__init__(naam="KlVentilatorGebruik",
                         label="Gebruikstypes ventilator",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVentilatorGebruik",
                         definition="Keuzelijst die de types van gebruik voor de ventilator aangeeft.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVentilatorGebruik")

        self.add_option("dwarsventilatie-aanzuigunit", "dwarsventilatie aanzuigunit", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-aanzuigunit")
        self.add_option("dwarsventilatie-inblaasunit", "dwarsventilatie inblaasunit", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/dwarsventilatie-inblaasunit")
        self.add_option("langsventilator", "langsventilator", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVentilatorGebruik/langsventilator")
