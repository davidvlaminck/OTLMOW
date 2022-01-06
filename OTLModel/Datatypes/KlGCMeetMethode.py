# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGCMeetMethode(Keuzelijst):
    """Locaties van de geluidstestproef."""

    def __init__(self):
        super().__init__(naam="KlGCMeetMethode",
                         label="Meet methode",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGCMeetMethode",
                         definition="Locaties van de geluidstestproef.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGCMeetMethode")

        self.add_option("inSitu", "inSitu", "Proef uitgevoerd op de werf", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGCMeetMethode/inSitu")
        self.add_option("labo", "labo", "Proef uitgevoerd in het labo", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGCMeetMethode/labo")
