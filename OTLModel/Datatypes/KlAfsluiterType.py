from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlAfsluiterType(Keuzelijst):
    """De types van de afsluiter."""

    def __init__(self):
        super().__init__(naam="KlAfsluiterType",
                         label="Afsluiter type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlAfsluiterType",
                         definition="De types van de afsluiter.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAfsluiterType")

        self.add_option("wandafsluiter", "wandafsluiter", "Een afsluiter voor de beheersing van water", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluiterType/wandafsluiter")
        self.add_option("steekschuif", "steekschuif", "De steekschuif is een verticaal bewegend afsluitorgaan, en kan rond, vierkant of rechthoekig zijn.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAfsluiterType/steekschuif")
