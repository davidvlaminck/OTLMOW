# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNeerslagsensorModelnaam(Keuzelijst):
    """De modelnaam van de neerslagsensor."""

    def __init__(self):
        super().__init__(naam="KlNeerslagsensorModelnaam",
                         label="Neerslagsensor modelnaam",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNeerslagsensorModelnaam",
                         definition="De modelnaam van de neerslagsensor.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNeerslagsensorModelnaam")

        self.add_option("WS100", "WS100", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNeerslagsensorModelnaam/WS100")
