from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator
class KlWegdekvoegType(Keuzelijst):
    """Vormen van wegdekvoeg."""

    def __init__(self):
        super().__init__(naam="KlWegdekvoegType",
                         label="Voeg type",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWegdekvoegType",
                         definition="Vormen van wegdekvoeg.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegdekvoegType")

        self.add_option("uitzettingsvoeg", "uitzettingsvoeg", "Een voeg die het uitzetten en krimpen van materialen, ook wel werking genoemd, opvangt.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/uitzettingsvoeg")
        self.add_option("dwarse-werkvoeg", "dwarse werkvoeg", "Een dwarse voeg die het uitzetten en krimpen van materialen, ook wel werking genoemd, opvangt.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/dwarse-werkvoeg")
        self.add_option("DGB-compoundvoeg", "DGB compoundvoeg", "Een voeg die het uitzetten en krimpen van materialen, ook wel werking genoemd, opvangt.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/DGB-compoundvoeg")
        self.add_option("langsvoeg-tussen-asfalt-en-beton", "langsvoeg tussen asfalt en beton", "Een doorgaande voeg in de lengterichting tussen asfalt en beton.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/langsvoeg-tussen-asfalt-en-beton")
        self.add_option("langsvoeg-tussen-lijnvormig-element-en-betonverharding", "langsvoeg tussen lijnvormig element en betonverharding", "Een doorgaande voeg in de lengterichting tussen een lijnvormig element en betonverharding.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/langsvoeg-tussen-lijnvormig-element-en-betonverharding")
        self.add_option("langsvoeg-tussen-fietspad-en-betonverharding", "langsvoeg tussen fietspad en betonverharding", "Een doorgaande voeg in de lengterichting tussen een fietspad en betonverharding.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/langsvoeg-tussen-fietspad-en-betonverharding")
        self.add_option("voorgevormde-voegband", "voorgevormde voegband", "Een voorgevormde voegband die het uitzetten en krimpen van materialen, ook wel werking genoemd, opvangt.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/voorgevormde-voegband")
        self.add_option("geëxtrudeerde-voegband", "geëxtrudeerde voegband", "Een geëxtrudeerde voegband die het uitzetten en krimpen van materialen, ook wel werking genoemd, opvangt.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/geëxtrudeerde-voegband")
        self.add_option("isolatievoeg-tussen-bestaande-constructie-en-betonverharding", "isolatievoeg tussen bestaande constructie en betonverharding", "isolatievoeg tussen bestaande constructie en betonverharding", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/isolatievoeg-tussen-bestaande-constructie-en-betonverharding")
        self.add_option("langsvoeg-tussen-lijnvormig-element-en-bitumineuze-verharding", "langsvoeg tussen lijnvormig element en bitumineuze verharding", "langsvoeg tussen lijnvormig element en bitumineuze verharding", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/langsvoeg-tussen-lijnvormig-element-en-bitumineuze-verharding")
        self.add_option("langse-werkvoeg", "langse werkvoeg", "Een langse voeg die het uitzetten en krimpen van materialen, ook wel werking genoemd, opvangt.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/langse-werkvoeg")
        self.add_option("langse-buigingsvoeg", "langse buigingsvoeg", "Een zaagsnede om de verharding toe te laten te scharnieren volgens de lengteas en om de spanningen ingevolge de thermische gradiënt te beperken.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegdekvoegType/langse-buigingsvoeg")
