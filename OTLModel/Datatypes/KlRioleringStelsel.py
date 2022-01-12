# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRioleringStelsel(Keuzelijst):
    """Stelsels van de riool."""

    def __init__(self):
        super().__init__(naam="KlRioleringStelsel",
                         label="Riolering stelsel",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRioleringStelsel",
                         definition="Stelsels van de riool.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRioleringStelsel")

        self.add_option("drain", "drain", "Stelsel om grondwater op te vangen en af te voeren.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringStelsel/drain")
        self.add_option("infiltratie", "infiltratie", "Het water in het systeem kan rechtstreeks in de grond infiltreren.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringStelsel/infiltratie")
        self.add_option("n-vuil", "n vuil", "Stelsel bedoeld voor de afvoer van onvervuild water. Het deksel van dit stelsel kan de code RWA (regenwaterafvoer) of W (eigendom van de watermaatschappij) hebben.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringStelsel/n-vuil")
        self.add_option("onbekend", "onbekend", "Stelsel waarvan afvoer onbekend is.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringStelsel/onbekend")
        self.add_option("vuil", "vuil", "Stelsel bedoeld voor de afvoer van vervuild water. Het deksel van dit stelsel kan de code DWA (sterk geconcentreerd afvalwater), DRWA (combinatie van regenwater en afvalwater) of W (eigendom van de watermaatschappij) hebben.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringStelsel/vuil")
