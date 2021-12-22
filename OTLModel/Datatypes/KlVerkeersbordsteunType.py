from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlVerkeersbordsteunType(Keuzelijst):
    """Types voor een verkeersbordsteun."""

    def __init__(self):
        super().__init__(naam="KlVerkeersbordsteunType",
                         label="Verkeersbordsteuntype",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordsteunType",
                         definition="Types voor een verkeersbordsteun.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordsteunType")

        self.add_option("seinbrug", "seinbrug", "Deze optie mag niet aangeduid worden! Bij instantiëren van seinbruggen moet je het onderdeel 'Seinbrug' gebruiken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/seinbrug")
        self.add_option("galgpaal", "galgpaal", "Deze optie mag niet aangeduid worden! Bij instantiëren van galgpalen moet je het onderdeel 'Galgpaal' gebruiken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/galgpaal")
        self.add_option("botsvriendelijke-steun-type-100NE2", "botsvriendelijke steun type 100NE2", "te bepalen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun-type-100NE2")
        self.add_option("vakwerksteun", "vakwerksteun", "Een keuzelijst om het type verkeersbordpaal te bepalen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/vakwerksteun")
        self.add_option("botsvriendelijke-steun-type-100NE3", "botsvriendelijke steun type 100NE3", "te bepalen", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun-type-100NE3")
        self.add_option("rechte-paal", "rechte paal", "Een rechte paal met als doel een verkeersbord te bevestigen.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/rechte-paal")
        self.add_option("botsvriendelijke-steun", "botsvriendelijke steun", "Constructie die na aanrijding zijn oorspronkelijke positie hersteld", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun")
