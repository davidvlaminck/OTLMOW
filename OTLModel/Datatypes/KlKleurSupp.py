# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKleurSupp(Keuzelijst):
    """Keuzelijst om de kleur van de toegevoegde supplementen van de verharding te bepalen."""

    def __init__(self):
        super().__init__(naam="KlKleurSupp",
                         label="Kleur supplementen",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlKleurSupp",
                         definition="Keuzelijst om de kleur van de toegevoegde supplementen van de verharding te bepalen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKleurSupp")

        self.add_option("rood", "rood", "De kleur beige.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurSupp/rood")
        self.add_option("bordeaux-bruin", "bordeaux-bruin", "De kleur bordeaux/bruin.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurSupp/bordeaux-bruin")
        self.add_option("oker", "oker", "De kleur oker.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurSupp/oker")
        self.add_option("beige", "beige", "De kleur rood.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurSupp/beige")
        self.add_option("geen", "geen", "Geen of standaard kleur.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKleurSupp/geen")
