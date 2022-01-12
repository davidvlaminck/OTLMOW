# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomGebreken(Keuzelijst):
    """De verschillende mogelijke gebreken bij een boom."""

    def __init__(self):
        super().__init__(naam="KlBoomGebreken",
                         label="Boom gebreken",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomGebreken",
                         definition="De verschillende mogelijke gebreken bij een boom.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomGebreken")

        self.add_option("andere", "andere", "Andere gebreken", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/andere")
        self.add_option("bladverkleuring", "bladverkleuring", "Abnormale verkleuring van het blad in het groeiseizoen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/bladverkleuring")
        self.add_option("dood-hout-afgestorven-takken", "dood hout-afgestorven takken", "Dood hout of afgestorven takken", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/dood-hout-afgestorven-takken")
        self.add_option("holte", "holte", "Diepere opening in stam of tak", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/holte")
        self.add_option("houtscheuren", "houtscheuren", "Dwarse of lengtescheuren in de stam of takken", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/houtscheuren")
        self.add_option("insecten", "insecten", "Insecten die de boom aantasten", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/insecten")
        self.add_option("kanker-bacterie", "kanker-bacterie", "Aantasting door een schimmelziekte of bacterie met een vergroeiing van de boom tot gevolg", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/kanker-bacterie")
        self.add_option("maaischade", "maaischade", "Schade aan de stamvoet door maaien", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/maaischade")
        self.add_option("plakoksel", "plakoksel", "Een tak die niet vergroeid is met de stam of andere tak, waarbij de schors van beide tegen elkaar aangedrukt wordt en dus niet vasthangen aan elkaar.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/plakoksel")
        self.add_option("stamschade", "stamschade", "Schade aan stam", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/stamschade")
        self.add_option("takschade", "takschade", "Schade aan tak of kroon", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/takschade")
        self.add_option("verminderde-bladbezetting", "verminderde bladbezetting", "Abnormale afname van de hoeveelheid bladeren verspreid over de kroon in het groeiseizoen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/verminderde-bladbezetting")
        self.add_option("waterloten-stamvoetopslag", "waterloten-stamvoetopslag", "Scheuten die, vaak massaal, gevormd worden aan de stamvoet. Waterloten zijn slapende knopen op stam of takken die uitlopen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/waterloten-stamvoetopslag")
        self.add_option("wortelschade", "wortelschade", "Schade aan wortels", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/wortelschade")
        self.add_option("zwammen-schimmels", "zwammen-schimmels", "Aanwezigheid van zwammen en/of schimmels", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/zwammen-schimmels")
