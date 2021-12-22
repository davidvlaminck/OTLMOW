from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlLuchtkwaliteitOpstellingMerk(Keuzelijst):
    """Het merk van een onderdeel uit een luchtkwaliteitsinstallatie."""

    def __init__(self):
        super().__init__(naam="KlLuchtkwaliteitOpstellingMerk",
                         label="Luchtkwaliteitsopstelling merk",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLuchtkwaliteitOpstellingMerk",
                         definition="Het merk van een onderdeel uit een luchtkwaliteitsinstallatie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLuchtkwaliteitOpstellingMerk")

        self.add_option("sick", "sick", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingMerk/sick")
