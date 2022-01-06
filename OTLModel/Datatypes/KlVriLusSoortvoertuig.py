# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVriLusSoortvoertuig(Keuzelijst):
    """Keuzelijst met verschillende types voertuigen die een detectielus volgens diens instellingen kan detecteren."""

    def __init__(self):
        super().__init__(naam="KlVriLusSoortvoertuig",
                         label="VRI-lus soort voertuig",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVriLusSoortvoertuig",
                         definition="Keuzelijst met verschillende types voertuigen die een detectielus volgens diens instellingen kan detecteren.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVriLusSoortvoertuig")

        self.add_option("voertuig", "voertuig", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/voertuig")
        self.add_option("fiets", "fiets", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/fiets")
        self.add_option("motor", "motor", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVriLusSoortvoertuig/motor")
