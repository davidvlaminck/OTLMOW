# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEindbeeldOpgaandeBoom(Keuzelijst):
    """Het nagestreefde beeld van de volgroeide boom of struik op deze specifieke standplaats."""

    def __init__(self):
        super().__init__(naam="KlEindbeeldOpgaandeBoom",
                         label="Eindbeeld opgaande boom",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEindbeeldOpgaandeBoom",
                         definition="Het nagestreefde beeld van de volgroeide boom of struik op deze specifieke standplaats.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEindbeeldOpgaandeBoom")

        self.add_option("gekandelaarde-boom", "gekandelaarde boom", "Het eindbeeld is een gekandelaarde boom. Een gekandelaarde boom is een boom waarvan alle gesteltakken periodiek op een bepaalde lengte worden afgezet en die hierop opnieuw uitlopen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/gekandelaarde-boom")
        self.add_option("geschoren-boom", "geschoren boom", "Het eindbeeld is een geschoren boom.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/geschoren-boom")
        self.add_option("knotboom", "knotboom", "Het eindbeeld is een knotboom. Dit is een snoeivorm waarbij periodiek alle takken afgezaagd worden tot op een verdikte knot bovenaan de stam.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/knotboom")
        self.add_option("leiboom", "leiboom", "Het eindbeeld is een leiboom. Een leiboom is een boom waarvan alle gesteltakken gedwongen worden in één (verticaal) vlak te groeien door geleiding. Soms worden de geleide bomen tegen een muur geleid of wordt er in een leidconstructie voorzien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/leiboom")
        self.add_option("niet-vrij-uitgroeiend", "niet vrij uitgroeiend", "Het eindbeeld is een boom die niet vrij kan uitgroeien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/niet-vrij-uitgroeiend")
        self.add_option("vrij-uitgroeiend", "vrij uitgroeiend", "Het eindbeeld is een boom die vrij kan uitgroeien.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEindbeeldOpgaandeBoom/vrij-uitgroeiend")
