# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSlagboomarmMerk(Keuzelijst):
    """Het merk van de slagboomarm."""

    def __init__(self):
        super().__init__(naam="KlSlagboomarmMerk",
                         label="Slagboomarm merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSlagboomarmMerk",
                         definition="Het merk van de slagboomarm.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSlagboomarmMerk")

