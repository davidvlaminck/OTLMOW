from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlMeetcelNauwkeurigheidsvermogen(Keuzelijst):
    """Nauwkeurigheidsvermogen van de meetcel in voltampère (bv. 5 of 15)."""

    def __init__(self):
        super().__init__(naam="KlMeetcelNauwkeurigheidsvermogen",
                         label="Meetcel nauwkeurigheidsvermogen",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetcelNauwkeurigheidsvermogen",
                         definition="Nauwkeurigheidsvermogen van de meetcel in voltampère (bv. 5 of 15).",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetcelNauwkeurigheidsvermogen")

        self.add_option("5", "5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsvermogen/5")
        self.add_option("15", "15", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsvermogen/15")
