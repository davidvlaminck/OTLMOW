# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerHoutigeVegetatie(Keuzelijst):
    """De verschillende beheersopties voor houtige vegetatie."""

    def __init__(self):
        super().__init__(naam="KlBeheerHoutigeVegetatie",
                         label="Beheer houtige vegetatie",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerHoutigeVegetatie",
                         definition="De verschillende beheersopties voor houtige vegetatie.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerHoutigeVegetatie")

        self.add_option("afpalingswerken", "afpalingswerken", "Het afpalen van bepaalde oppervlaktes met vegetatie.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/afpalingswerken")
        self.add_option("begieten", "begieten", "Periodisch begieten van vegetatie. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/begieten")
        self.add_option("bestrijding", "bestrijding", "Bestrijding van ongewenste onkruiden.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/bestrijding")
        self.add_option("dunnen", "dunnen", "Het gelijkgronds afzagen van bomen ter bevordering van de groei van omstaande bomen of struiken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/dunnen")
        self.add_option("gedeeltelijk-ontstronken", "gedeeltelijk ontstronken", "Gedeeltelijk ontstronken van bomen. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/gedeeltelijk-ontstronken")
        self.add_option("hakhoutbeheer", "hakhoutbeheer", "Er wordt hakhoutbeheer uitgevoerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/hakhoutbeheer")
        self.add_option("hakken", "hakken", "Hakken van de grond tussen houtige vegetaties.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/hakken")
        self.add_option("maaien", "maaien", "Het maaien van de grazige vegetatie tussen de houtige vegetatie.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/maaien")
        self.add_option("niets-doen", "niets doen", "Er wordt geen beheer uitgevoerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/niets-doen")
        self.add_option("ontstronken", "ontstronken", "Ontstronken van bomen. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/ontstronken")
        self.add_option("rooien", "rooien", "Wegnemen van vegetatie dmv rooien. ", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/rooien")
        self.add_option("scheren", "scheren", "Het vlakvormig gelijkmatig kort afsnijden van takken van hagen, heesters en houtkanten.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/scheren")
        self.add_option("snoeien", "snoeien", "Het inkorten of wegnemen van takken met snoeischaar of zaag.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/snoeien")
        self.add_option("spitten", "spitten", "Spitten van de grond tussen houtige vegetaties.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/spitten")
        self.add_option("wieden", "wieden", "Het wieden van de grond tussen houtige vegetaties. Dit is het verwijderen van onkruid.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerHoutigeVegetatie/wieden")
