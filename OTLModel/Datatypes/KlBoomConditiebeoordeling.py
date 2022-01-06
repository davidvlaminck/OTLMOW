# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomConditiebeoordeling(Keuzelijst):
    """De conditie beoordeeld volgens de kronenstructuur van Dr. A. Roloff, gelet op de scheutlengte ontwikkeling en vorming van dood hout."""

    def __init__(self):
        super().__init__(naam="KlBoomConditiebeoordeling",
                         label="Boom conditiebeoordeling",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomConditiebeoordeling",
                         definition="De conditie beoordeeld volgens de kronenstructuur van Dr. A. Roloff, gelet op de scheutlengte ontwikkeling en vorming van dood hout.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomConditiebeoordeling")

        self.add_option("1", "1", "De conditie is verminderd, maar op korte termijn (< 5 jaar) worden ten aanzien van de fysiologische toestand van de boom geen problemen verwacht.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiebeoordeling/1")
        self.add_option("2", "2", "De conditie is duidelijk verminderd. De fysiologische toestand van de boom is slecht, maar herstel van de boom is eventueel mogelijk.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiebeoordeling/2")
        self.add_option("3", "3", "De conditie en toekomstverwachting van de boom is minimaal. De mechanische en/of fysiologische toestand van de boom is dusdanig slecht dat 'herstel' van de boom niet of nauwelijks mogelijk is.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiebeoordeling/3")
        self.add_option("0", "0", "De conditie is goed. Op middellange termijn (10 tot 15 jaar) worden geen problemen verwacht.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomConditiebeoordeling/0")
