# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerExoten(Keuzelijst):
    """Behandelingswijzen van exoten."""

    def __init__(self):
        super().__init__(naam="KlBeheerExoten",
                         label="Beheer exoten",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerExoten",
                         definition="Behandelingswijzen van exoten.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerExoten")

        self.add_option("afbakenen", "afbakenen", "Afbakenen van exoten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/afbakenen")
        self.add_option("afdekken-EPDM-folie", "afdekken EPDM folie", "Afdekken met EPDM folie van exoten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/afdekken-EPDM-folie")
        self.add_option("chemisch-behandelen", "chemisch behandelen", "Chemisch behandelen van exoten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/chemisch-behandelen")
        self.add_option("machinaal-maaien", "machinaal maaien", "Machinaal maaien van exoten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/machinaal-maaien")
        self.add_option("manueel-maaien", "manueel maaien", "Manueel maaien van exoten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/manueel-maaien")
        self.add_option("niets-doen", "niets doen", "Niets doen met betrekken tot het beheer van exoten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/niets-doen")
        self.add_option("uitgraven", "uitgraven", "Uitgraven van exoten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/uitgraven")
        self.add_option("uitspitten", "uitspitten", "Uitspitten van exoten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerExoten/uitspitten")
