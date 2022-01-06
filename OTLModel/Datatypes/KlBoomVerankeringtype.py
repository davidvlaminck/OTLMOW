# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomVerankeringtype(Keuzelijst):
    """De verschillende types van verankering van een boom."""

    def __init__(self):
        super().__init__(naam="KlBoomVerankeringtype",
                         label="Boom verankeringtype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomVerankeringtype",
                         definition="De verschillende types van verankering van een boom.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomVerankeringtype")

        self.add_option("boompaalconstructie", "boompaalconstructie", "Een constructie uit houten palen en dwarslatten die de stabiliteit van de boom waarborgt", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankeringtype/boompaalconstructie")
        self.add_option("niet-afbreekbare-grondankers", "niet-afbreekbare grondankers", "Een constructie van stalen grondankers en kunststofverankeringsbanden die de stabilietit van de boom waarborgt", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankeringtype/niet-afbreekbare-grondankers")
        self.add_option("biologisch-afbreekbare-grondankers", "biologisch afbreekbare grondankers", "Een constructie van 100% biologisch afbreekbare grondankers en verankeringstouwen die de stabilietit van de boom waarborgt", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankeringtype/biologisch-afbreekbare-grondankers")
