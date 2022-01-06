# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLetterCijferType(Keuzelijst):
    """De mogelijke types van een individuele letter- of cijfermarkering."""

    def __init__(self):
        super().__init__(naam="KlLetterCijferType",
                         label="Type van de letter of het cijfer",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLetterCijferType",
                         definition="De mogelijke types van een individuele letter- of cijfermarkering.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLetterCijferType")

        self.add_option("normaal---Hoofdletters-(basishoogte)", "normaal - Hoofdletters (basishoogte)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/normaal---Hoofdletters-(basishoogte)")
        self.add_option("normaal---Kleine-letters-(basishoogte)", "normaal - Kleine letters (basishoogte)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/normaal---Kleine-letters-(basishoogte)")
        self.add_option("versmald---Hoofdletters-(basishoogte)", "versmald - Hoofdletters (basishoogte)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Hoofdletters-(basishoogte)")
        self.add_option("versmald---Kleine-letters-(basishoogte)", "versmald - Kleine letters (basishoogte)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Kleine-letters-(basishoogte)")
        self.add_option("versmald---Hoofdletters-(4m-hoogte)", "versmald - Hoofdletters (4m hoogte)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Hoofdletters-(4m-hoogte)")
        self.add_option("versmald---Hoofdletters-(6m-hoogte)", "versmald - Hoofdletters (6m hoogte)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Hoofdletters-(6m-hoogte)")
        self.add_option("normaal---Cijfers-(basishoogte)", "normaal - Cijfers (basishoogte)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/normaal---Cijfers-(basishoogte)")
        self.add_option("versmald---Cijfers-(basishoogte)", "versmald - Cijfers (basishoogte)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Cijfers-(basishoogte)")
        self.add_option("versmald---Cijfers-(4m-hoogte)", "versmald - Cijfers (4m hoogte)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Cijfers-(4m-hoogte)")
        self.add_option("versmald---Cijfers-(6m-hoogte)", "versmald - Cijfers (6m hoogte)", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLetterCijferType/versmald---Cijfers-(6m-hoogte)")
