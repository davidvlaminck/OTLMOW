# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoBoombrugType(Keuzelijst):
    """Types van boombrug."""

    def __init__(self):
        super().__init__(naam="KlEcoBoombrugType",
                         label="Boombrug type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoBoombrugType",
                         definition="Types van boombrug.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoBoombrugType")

        self.add_option("ladderbrug", "ladderbrug", "Een boombrug waarbij de oversteek bestaat uit een laddervorm gemaakt uit touw (touwladder) of metaal-kunststof (kabelnet) of een weefsel van takken en nylon (Takkenmat).", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoBoombrugType/ladderbrug")
        self.add_option("portaal-boomgoot", "portaal boomgoot", "Een bestaande portaal voor signalisatie ingericht als boomrug door middel van een aluminium ladder of houten loopplank of goot.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoBoombrugType/portaal-boomgoot")
        self.add_option("touwbrug", "touwbrug", "Een boombrug bestaande uit een gedraaid touw van natuurlijke of kunstmatige vezels, dat strak over de weg wordt gespannen en voldoende dik is om er dieren op een stabiele wijze overheen te laten lopen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoBoombrugType/touwbrug")
        self.add_option("tunnelbrug", "tunnelbrug", "Een boombrug bestaande uit een tunnelvormige oversteek gemaakt uit geweven touwen (touwtunnel) of een buisvormige draadkoker (kokerbrug)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoBoombrugType/tunnelbrug")
