from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBSSRandafwerking(Keuzelijst):
    """De verschillende manieren van de randafwerking van de verharding."""

    def __init__(self):
        super().__init__(naam="KlBSSRandafwerking",
                         label="randafwerking",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBSSRandafwerking",
                         definition="De verschillende manieren van de randafwerking van de verharding.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBSSRandafwerking")

        self.add_option("kardinaalsmutsen", "kardinaalsmutsen", "Een kantsteen die wordt toegepast wanneer de betonstraatsteen in keperverband wordt gestraat.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/kardinaalsmutsen")
        self.add_option("biscchopsmutsen", "biscchopsmutsen", "Een kantsteen die wordt toegepast wanneer de betonstraatsteen in keperverband wordt gestraat.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/biscchopsmutsen")
        self.add_option("gezaagde-betonstraatstenen", "gezaagde betonstraatstenen", "Een kantsteen, meestal uit hetzelfde materiaal,  die op maat werd gebracht.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/gezaagde-betonstraatstenen")
        self.add_option("geen", "geen", "De randafwerking is overbodig. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/geen")
