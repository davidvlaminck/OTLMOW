# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSeinbrugRijrichting(Keuzelijst):
    """Mogelijke rijrichtingen bij een seinbrug (enkele of dubbele)."""

    def __init__(self):
        super().__init__(naam="KlSeinbrugRijrichting",
                         label="Seinbrug rijrichting",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSeinbrugRijrichting",
                         definition="Mogelijke rijrichtingen bij een seinbrug (enkele of dubbele).",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSeinbrugRijrichting")

        self.add_option("dubbele-rijrichting", "dubbele rijrichting", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugRijrichting/dubbele-rijrichting")
        self.add_option("enkele-rijrichting", "enkele rijrichting", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSeinbrugRijrichting/enkele-rijrichting")
