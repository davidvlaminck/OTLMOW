from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlMeetcelNauwkeurigheidsklasse(Keuzelijst):
    """Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...)."""

    def __init__(self):
        super().__init__(naam="KlMeetcelNauwkeurigheidsklasse",
                         label="Meetcel nauwkeurigheidsklasse",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetcelNauwkeurigheidsklasse",
                         definition="Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...).",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetcelNauwkeurigheidsklasse")

        self.add_option("0.2", "0.2", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsklasse/0.2")
        self.add_option("0.2-S", "0.2 S", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsklasse/0.2-S")
        self.add_option("0.5", "0.5", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMeetcelNauwkeurigheidsklasse/0.5")
