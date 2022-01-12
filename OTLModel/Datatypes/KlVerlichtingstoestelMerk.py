# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelMerk(Keuzelijst):
    """Het merk van het verlichtingstoestel."""

    def __init__(self):
        super().__init__(naam="KlVerlichtingstoestelMerk",
                         label="Verlichtingstoestel merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelMerk",
                         definition="Het merk van het verlichtingstoestel.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelMerk")

        self.add_option("ARC", "ARC", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/ARC")
        self.add_option("HCI-TS", "HCI-TS", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/HCI-TS")
        self.add_option("Philips", "Philips", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/Philips")
        self.add_option("Rombalux", "Rombalux", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/Rombalux")
        self.add_option("Schreder", "Schreder", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/Schreder")
        self.add_option("andere", "andere", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/andere")
