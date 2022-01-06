# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetcelVeiligheidsfactor(Keuzelijst):
    """Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom."""

    def __init__(self):
        super().__init__(naam="KlMeetcelVeiligheidsfactor",
                         label="Meetcel veiligheidsfactor",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetcelVeiligheidsfactor",
                         definition="Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetcelVeiligheidsfactor")

        self.add_option("fS-5", "fS 5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelVeiligheidsfactor/fS-5")
