from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlPictogramSymbool(Keuzelijst):
    """De mogelijke symbolen op het pictogram."""

    def __init__(self):
        super().__init__(naam="KlPictogramSymbool",
                         label="Pictogram symbool",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlPictogramSymbool",
                         definition="De mogelijke symbolen op het pictogram.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlPictogramSymbool")

        self.add_option("nooddeurnummer", "nooddeurnummer", "nooddeurnummer", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/nooddeurnummer")
        self.add_option("nummer-veiligheidsnis", "nummer veiligheidsnis", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/nummer-veiligheidsnis")
        self.add_option("hydrant-bovengronds-(H)", "hydrant bovengronds (H)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/hydrant-bovengronds-(H)")
        self.add_option("hydrant-ondergronds-(B)", "hydrant ondergronds (B)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/hydrant-ondergronds-(B)")
        self.add_option("tunnelnaam", "tunnelnaam", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/tunnelnaam")
        self.add_option("verbodsbord", "verbodsbord", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/verbodsbord")
        self.add_option("vluchtend-persoon", "vluchtend persoon", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/vluchtend-persoon")
        self.add_option("halte", "halte", "Duidt de locatie aan waar het openbaar vervoer, bv. bus, tram of trolley, stopt om passagiers te laten in- en uitstappen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPictogramSymbool/halte")
