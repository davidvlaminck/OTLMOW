# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerBoomvorm(Keuzelijst):
    """Behandelingswijzen van bomen."""

    def __init__(self):
        super().__init__(naam="KlBeheerBoomvorm",
                         label="Beheer boomvorm",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerBoomvorm",
                         definition="Behandelingswijzen van bomen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerBoomvorm")

        self.add_option("begieten", "begieten", "Periodisch begieten van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/begieten")
        self.add_option("verplanten", "verplanten", "Verplanten van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/verplanten")
        self.add_option("bodemafdekking", "bodemafdekking", "Bodemafdekking van de grond rond bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/bodemafdekking")
        self.add_option("begeleidingssnoei", "begeleidingssnoei", "Begeleidingssnoei van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/begeleidingssnoei")
        self.add_option("onderhoudssnoei", "onderhoudssnoei", "Onderhoudssnoei van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/onderhoudssnoei")
        self.add_option("kroonreductie", "kroonreductie", "Kroonreductie van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/kroonreductie")
        self.add_option("kandelaren", "kandelaren", "Kandelaren van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/kandelaren")
        self.add_option("knotten", "knotten", "Knotten van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/knotten")
        self.add_option("wegnemen-waterloten-en-wortelopslag", "wegnemen waterloten en wortelopslag", "Wegnemen van waterloten en wortelopslag van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/wegnemen-waterloten-en-wortelopslag")
        self.add_option("leiboomsnoei", "leiboomsnoei", "Leiboomsnoei van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/leiboomsnoei")
        self.add_option("scheren", "scheren", "Scheren van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/scheren")
        self.add_option("vellen", "vellen", "Vellen van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/vellen")
        self.add_option("gedeeltelijk-ontstronken", "gedeeltelijk ontstronken", "Gedeeltelijk ontstronken van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/gedeeltelijk-ontstronken")
        self.add_option("volledig-ontstronken", "volledig ontstronken", "Volledig ontstronken van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/volledig-ontstronken")
        self.add_option("rooien", "rooien", "Rooien van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/rooien")
        self.add_option("stam--en-takbescherming", "stam- en takbescherming", "Stam- en takbescherming van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/stam--en-takbescherming")
        self.add_option("stambescherming-zonnebrand", "stambescherming zonnebrand", "Bescherming van de stam van bomen tegen zonnebrand.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/stambescherming-zonnebrand")
        self.add_option("verwijderen-gietrand", "verwijderen gietrand", "Verwijderen van de gietrand die soms aangelegd wordt rond de basis van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/verwijderen-gietrand")
        self.add_option("afzagen-boompalen", "afzagen boompalen", "Afzagen van boompalen van boompaalconstructies.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/afzagen-boompalen")
        self.add_option("verwijderen-boompalen", "verwijderen boompalen", "Verwijderen van boompalen van boompaalconstructies.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/verwijderen-boompalen")
        self.add_option("vormsnoei", "vormsnoei", "Vormsnoei van bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/vormsnoei")
        self.add_option("bodembeluchting-luchtinjectie", "bodembeluchting-luchtinjectie", "Bodembeluchting-luchtinjectie van de grond rond bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/bodembeluchting-luchtinjectie")
        self.add_option("gronduitwisseling-wortelzone", "gronduitwisseling wortelzone", "Gronduitwisseling wortelzone van de grond rond bomen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/gronduitwisseling-wortelzone")
        self.add_option("boren-grondpijler", "boren grondpijler", "Boren van een grondpijler in de grond rond de boom.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/boren-grondpijler")
        self.add_option("statische-kroonverankering", "statische kroonverankering", "Statische kroonverankering van een boom.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/statische-kroonverankering")
        self.add_option("dynamische-kroonverankering", "dynamische kroonverankering", "dynamische kroonverankering van een boom.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/dynamische-kroonverankering")
        self.add_option("anti-wortelscherm", "anti-wortelscherm", "Plaatsen van anti-wortel scherm in de grond onder een boom.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerBoomvorm/anti-wortelscherm")
