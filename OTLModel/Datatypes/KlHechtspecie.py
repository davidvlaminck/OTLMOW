from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlHechtspecie(Keuzelijst):
    """Keuzelijst met hecht specie van gestapelde ruwe steen."""

    def __init__(self):
        super().__init__(naam="KlHechtspecie",
                         label="Hecht specie",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlHechtspecie",
                         definition="Keuzelijst met hecht specie van gestapelde ruwe steen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlHechtspecie")

        self.add_option("zandcement", "zandcement", "zandcement", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHechtspecie/zandcement")
        self.add_option("gebiedseigen-grond", "gebiedseigen grond", "gebiedseigen grond", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlHechtspecie/gebiedseigen-grond")
