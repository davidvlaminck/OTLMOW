# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLetterVerschaaldType(Keuzelijst):
    """De mogelijke types van een individueel verschaalde lettermarkering."""

    def __init__(self):
        super().__init__(naam="KlLetterVerschaaldType",
                         label="Type van de verschaalde letter",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLetterVerschaaldType",
                         definition="De mogelijke types van een individueel verschaalde lettermarkering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLetterVerschaaldType")

        self.add_option("versmald---Hoofdletters-(basishoogte-0.4-meter)", "versmald - Hoofdletters (basishoogte 0.4 meter)", "Versmalde hoofdletters bij verschaling (basishoogte 0.4 meter)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterVerschaaldType/versmald---Hoofdletters-(basishoogte-0.4-meter)")
