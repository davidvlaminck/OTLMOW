from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlGroeiplaatsverbetering(Keuzelijst):
    """De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren."""

    def __init__(self):
        super().__init__(naam="KlGroeiplaatsverbetering",
                         label="Groeiplaatsverbetering",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGroeiplaatsverbetering",
                         definition="De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGroeiplaatsverbetering")

        self.add_option("horizontale-drainage", "horizontale drainage", "Groeiplaatsverbetering dmv horizontale drainage.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/horizontale-drainage")
        self.add_option("verticale-drainage", "verticale drainage", "Groeiplaatsverbetering dmv verticale drainage.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/verticale-drainage")
        self.add_option("bodembeluchting-luchtinjectie", "bodembeluchting-luchtinjectie", "Groeiplaatsverbetering dmv bodembeluchting-luchtinjectie.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/bodembeluchting-luchtinjectie")
        self.add_option("irrgatie-drainagebuis", "irrgatie drainagebuis", "Groeiplaatsverbetering dmv irrigatie met een drainagebuis.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/irrgatie-drainagebuis")
        self.add_option("irrigatie-kunstmatige-gietrand", "irrigatie kunstmatige gietrand", "Groeiplaatsverbetering dmv irrigatie met een kunstmatige gietrand.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/irrigatie-kunstmatige-gietrand")
        self.add_option("irrigatie-gietrand-overtollige-grond", "irrigatie gietrand overtollige grond", "Groeiplaatsverbetering dmv irrigatie met een overtollige grond.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/irrigatie-gietrand-overtollige-grond")
