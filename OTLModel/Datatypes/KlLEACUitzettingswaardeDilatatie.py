# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEACUitzettingswaardeDilatatie(Keuzelijst):
    """De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing."""

    def __init__(self):
        super().__init__(naam="KlLEACUitzettingswaardeDilatatie",
                         label="Uitzetttingswaarde dilatatie",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEACUitzettingswaardeDilatatie",
                         definition="De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEACUitzettingswaardeDilatatie")

        self.add_option("10-cm", "10 cm", "De uitzettingswaarde is 10 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACUitzettingswaardeDilatatie/10-cm")
        self.add_option("20-cm", "20 cm", "De uitzettingswaarde is 20 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACUitzettingswaardeDilatatie/20-cm")
        self.add_option("90-cm", "90 cm", "De uitzettingswaarde is 90 cm.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEACUitzettingswaardeDilatatie/90-cm")
