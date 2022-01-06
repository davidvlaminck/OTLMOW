# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomspiegelInvulling(Keuzelijst):
    """Keuzelijst, die de manieren om de boomspiegel in te vullen, oplijst."""

    def __init__(self):
        super().__init__(naam="KlBoomspiegelInvulling",
                         label="Boomspiegel",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomspiegelInvulling",
                         definition="Keuzelijst, die de manieren om de boomspiegel in te vullen, oplijst.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomspiegelInvulling")

        self.add_option("gras", "gras", "De boomspiegel bestaat voornamelijk uit grazige vegetatie die gemaaid kan worden", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/gras")
        self.add_option("groencompost", "groencompost", "Afdekking van de bodem rond de boom met groencompost.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/groencompost")
        self.add_option("beplanting", "beplanting", "De boomspiegel bestaat voornamelijk uit sierbeplanting of houtige vegetatie", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/beplanting")
        self.add_option("houtsnippers", "houtsnippers", "Afdekking van de bodem rond de boom met houtsnippers.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/houtsnippers")
        self.add_option("boomschors", "boomschors", "Afdekking van de bodem rond de boom met boomschors.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/boomschors")
        self.add_option("rooster", "rooster", "De boomspiegel is een rooster", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/rooster")
        self.add_option("biologisch-afbreekbaar-doek-PLA", "biologisch afbreekbaar doek PLA", "Afdekking van de bodem rond de boom met een biologisch afbreekbaar doek in PLA.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/biologisch-afbreekbaar-doek-PLA")
        self.add_option("verharding", "verharding", "In de boomspiegel is verharding aanwezig tot op minder dan 30cm van de stamvoet", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/verharding")
        self.add_option("biologisch-afbreekbaar-doek-jute", "biologisch afbreekbaar doek jute", "Afdekking van de bodem rond de boom met een biologisch afbreekbaar doek in jute.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/biologisch-afbreekbaar-doek-jute")
        self.add_option("minerale-mulch", "minerale mulch", "De boomspiegel bestaat uit een bodembedekking van minerale oorsprong (vb. grind, dolomiet)", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/minerale-mulch")
        self.add_option("kaal", "kaal", "De boomspiegel is kaal of licht begroeid met onkruid (<25%) en word niet gemaaid", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/kaal")
        self.add_option("andere", "andere", "De boomspiegel bestaat uit ander materiaal dan opgelijst", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomspiegelInvulling/andere")
