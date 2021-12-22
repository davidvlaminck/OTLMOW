from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlBoomGroeifase(Keuzelijst):
    """De verschillende fases van beheer volgens de verschillende levensfases."""

    def __init__(self):
        super().__init__(naam="KlBoomGroeifase",
                         label="Groeifasen",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomGroeifase",
                         definition="De verschillende fases van beheer volgens de verschillende levensfases.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomGroeifase")

        self.add_option("plantfase", "plantfase", "De periode na de aanplant waarbij het beheer gericht is op het aanslaan van de boom (water geven, boompalen verwijderen,…)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/plantfase")
        self.add_option("eindfase", "eindfase", "De periode waarbij regressie/aftakeling plaatsvindt – beheer gericht op in stand houding (kroonverzorging)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/eindfase")
        self.add_option("dood", "dood", "Dood", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/dood")
        self.add_option("jeugdfase", "jeugdfase", "De periode van de lengte-ontwikkeling van de boom – beheer gericht op tot stand brengen van de takvrije stamlengte (begeleidingssnoei,..)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/jeugdfase")
        self.add_option("volwassenfase", "volwassenfase", "De periode van de kroonontwikkeling – beheer gericht op in stand houden van de boom (onderhoudssnoei)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGroeifase/volwassenfase")
