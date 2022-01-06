# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOnbegroeidVoorkomenType(Keuzelijst):
    """De mogelijke afwerkingen van het onbegroeide voorkomen."""

    def __init__(self):
        super().__init__(naam="KlOnbegroeidVoorkomenType",
                         label="Onbegroeid voorkomen type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOnbegroeidVoorkomenType",
                         definition="De mogelijke afwerkingen van het onbegroeide voorkomen.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOnbegroeidVoorkomenType")

        self.add_option("grindgazon-tweelaags", "grindgazon tweelaags", "Afwerking van tweelaagse grindgazon.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/grindgazon-tweelaags")
        self.add_option("kunstgras", "kunstgras", "Bedekking bestaande uit synthetisch materiaal, met de bedoeling om natuurlijk gras te imiteren.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/kunstgras")
        self.add_option("gesloten-kunststofverharding", "gesloten kunststofverharding", "Kunststofverharding die over de totale oppervlakte in één continue laag werd aangebracht.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/gesloten-kunststofverharding")
        self.add_option("schors", "schors", "Bedekking bestaande uit mengsel van schors (gefragmenteerde boomschors)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/schors")
        self.add_option("tegels-met-groenvoeg", "tegels met groenvoeg", "Tegels die zo gelegd zijn dat de voeg begroeibaar is en waterdoorlaatbaar.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/tegels-met-groenvoeg")
        self.add_option("steenslag-rolgrind", "steenslag rolgrind", "Bedekking van een onverharde zone die opgebouwd is uit een niet-gecompacteerde groep van individuele componenten die voldoen aan de volgende specificaties: losse steenslag, behalve dolomiet, afgeronde en onregelmatige vorm en onregelmatig verband.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/steenslag-rolgrind")
        self.add_option("schelpen", "schelpen", "Bedekking van een onverharde zone die opgebouwd is uit een niet-gecompacteerde groep van individuele componenten die voldoen aan de volgende specificaties: hoofdbestanddeel schelpen, onregelmatige vorm en onregelmatig verband.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/schelpen")
        self.add_option("rubberen-matten-tegels", "rubberen matten tegels", "Verharding bestaande uit afzonderlijke elementen kunststofverharding.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/rubberen-matten-tegels")
        self.add_option("mulch", "mulch", "Bedekking bestaande uit een laag organisch materiaal. (Herfstbladeren, grasmaaisel, houtsnippers, compost...).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/mulch")
        self.add_option("gravel", "gravel", "Puinmengsel specifiek bestaande uit zuiver gebroken baksteen- en dakpannenpuin.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/gravel")
        self.add_option("harsgebonden-siersplit", "harsgebonden siersplit", "Afwerking van harsgebonden siersplit.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/harsgebonden-siersplit")
        self.add_option("grindgazon-eenlaags", "grindgazon eenlaags", "Een substraat ontwikkeld om voertuigen sporadisch toe te laten op gazons zonder dater spoorvorming optreedt.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/grindgazon-eenlaags")
