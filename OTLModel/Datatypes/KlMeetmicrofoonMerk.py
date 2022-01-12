# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMeetmicrofoonMerk(Keuzelijst):
    """Het merk van de meetmicrofoon."""

    def __init__(self):
        super().__init__(naam="KlMeetmicrofoonMerk",
                         label="Meetmicrofoon merk",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlMeetmicrofoonMerk",
                         definition="Het merk van de meetmicrofoon.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMeetmicrofoonMerk")

