from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlOverstortrandMateriaal(Keuzelijst):
    """De materialen van de overstortrand."""

    def __init__(self):
        super().__init__(naam="KlOverstortrandMateriaal",
                         label="Overstortrand materiaal",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOverstortrandMateriaal",
                         definition="De materialen van de overstortrand.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOverstortrandMateriaal")

        self.add_option("inox", "inox", "Een overstortrand uit inox.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/inox")
        self.add_option("metselwerk", "metselwerk", "Een overstortrand uit metselwerk.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/metselwerk")
        self.add_option("hout", "hout", "Een overstortrand uit hout.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOverstortrandMateriaal/hout")
