# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStortsteenType(Keuzelijst):
    """Stortsteen types."""

    def __init__(self):
        super().__init__(naam="KlStortsteenType",
                         label="Stortsteen type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStortsteenType",
                         definition="Stortsteen types.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStortsteenType")

        self.add_option("rolsteen", "rolsteen", "rolsteen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/rolsteen")
        self.add_option("ruwe-breuksteen", "ruwe breuksteen", "een natuursteen van onregelmatige vorm", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/ruwe-breuksteen")
        self.add_option("brokken-van-betonpuin", "brokken van betonpuin", "brokken van betonpuin", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-betonpuin")
        self.add_option("brokken-van-mengpuin", "brokken van mengpuin", "brokken van mengpuin", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-mengpuin")
        self.add_option("brokken-van-metselwerkpuin", "brokken van metselwerkpuin", "brokken van metselwerkpuin", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-metselwerkpuin")
        self.add_option("brokken-van-breuksteenpuin", "brokken van breuksteenpuin", "brokken van breuksteenpuin", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/brokken-van-breuksteenpuin")
        self.add_option("natuursteenslag", "natuursteenslag", "natuursteenslag", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/natuursteenslag")
        self.add_option("dolomiet", "dolomiet", "dolomiet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/dolomiet")
        self.add_option("rolgrind", "rolgrind", "Grind met goed afgeronde korrels.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/rolgrind")
        self.add_option("kunststeenslag", "kunststeenslag", "brokken van betonpuin", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStortsteenType/kunststeenslag")
