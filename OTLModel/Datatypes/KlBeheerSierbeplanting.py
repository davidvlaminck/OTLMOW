# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerSierbeplanting(Keuzelijst):
    """Verschillende mogelijke beheeropties bij sierbeplanting."""

    def __init__(self):
        super().__init__(naam="KlBeheerSierbeplanting",
                         label="Beheer sierbeplanting",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerSierbeplanting",
                         definition="Verschillende mogelijke beheeropties bij sierbeplanting.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerSierbeplanting")

        self.add_option("hakken", "hakken", "Hakken van de grond tussen sierbeplantingen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/hakken")
        self.add_option("niets-doen", "niets doen", "Er wordt geen beheer uitgevoerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/niets-doen")
        self.add_option("opschikken-knippen-dood-materiaal", "opschikken-knippen dood materiaal", "Opschikken/knippen van dood materiaal.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/opschikken-knippen-dood-materiaal")
        self.add_option("scheren", "scheren", "Het vlakvormig gelijkmatig kort afsnijden van takken van hagen, heesters en houtkanten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/scheren")
        self.add_option("snoeien", "snoeien", "Het inkorten of wegnemen van stengels met snoeischaar.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/snoeien")
        self.add_option("wieden", "wieden", "Het wieden van de grond tussen sierbeplanting. Dit is het verwijderen van onkruid.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerSierbeplanting/wieden")
