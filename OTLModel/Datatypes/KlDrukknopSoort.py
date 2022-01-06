# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDrukknopSoort(Keuzelijst):
    """Keuzelijst met verschillende soorten drukknoppen."""

    def __init__(self):
        super().__init__(naam="KlDrukknopSoort",
                         label="Drukknop soort",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDrukknopSoort",
                         definition="Keuzelijst met verschillende soorten drukknoppen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDrukknopSoort")

        self.add_option("voetganger-drukknop", "voetganger drukknop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/voetganger-drukknop")
        self.add_option("WV-drukknop", "WV drukknop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/WV-drukknop")
        self.add_option("combi-v-f-drukknop", "combi v f drukknop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/combi-v-f-drukknop")
        self.add_option("combi-v-vg-drukknop", "combi v vg drukknop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/combi-v-vg-drukknop")
        self.add_option("fietser-drukknop", "fietser drukknop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/fietser-drukknop")
        self.add_option("ruiter-drukknop", "ruiter drukknop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/ruiter-drukknop")
        self.add_option("visueel-gehandicapt-drukknop", "visueel gehandicapt drukknop", "", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDrukknopSoort/visueel-gehandicapt-drukknop")
