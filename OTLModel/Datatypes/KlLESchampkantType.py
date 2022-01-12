# coding=utf-8
from OTLModel.Datatypes.Keuzelijst import Keuzelijst


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLESchampkantType(Keuzelijst):
    """Types van de schampkant."""

    def __init__(self):
        super().__init__(naam="KlLESchampkantType",
                         label="Schampkant type",
                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLESchampkantType",
                         definition="Types van de schampkant.",
                         usagenote="",
                         deprecated_version="",
                         codelist="https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLESchampkantType")

        self.add_option("afgeknotte-New-Jersey-eenzijdig", "afgeknotte New Jersey eenzijdig", "Betonnen veiligheidsstootband type New Jersey die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/afgeknotte-New-Jersey-eenzijdig")
        self.add_option("afgeknotte-New-Jersey-tweezijdig", "afgeknotte New Jersey tweezijdig", "Betonnen veiligheidsstootband type New Jersey die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/afgeknotte-New-Jersey-tweezijdig")
        self.add_option("ander-type-schampkant-eenzijdig", "ander type schampkant eenzijdig", "Betonnen veiligheidsstootband die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/ander-type-schampkant-eenzijdig")
        self.add_option("ander-type-schampkant-tweezijdig", "ander type schampkant tweezijdig", "Betonnen veiligheidsstootband die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/ander-type-schampkant-tweezijdig")
        self.add_option("eindschikking-voor-ander-type-schampkant.-eenzijdig", "eindschikking voor ander type schampkant. eenzijdig", "Eindschikking voor betonnen veiligheidsstootband die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/eindschikking-voor-ander-type-schampkant.-eenzijdig")
        self.add_option("eindschikking-voor-ander-type-schampkant.-tweezijdig", "eindschikking voor ander type schampkant. tweezijdig", "Eindschikking voor betonnen veiligheidsstootband die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/eindschikking-voor-ander-type-schampkant.-tweezijdig")
        self.add_option("eindschikking-voor-type-afgeknotte-New-Jersey-eenzijdig", "eindschikking voor type afgeknotte New Jersey eenzijdig", "Eindschikking voor betonnen veiligheidsstootband type New Jersey die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/eindschikking-voor-type-afgeknotte-New-Jersey-eenzijdig")
        self.add_option("eindschikking-voor-type-afgeknotte-New-Jersey-tweezijdig", "eindschikking voor type afgeknotte New Jersey tweezijdig", "Eindschikking voor betonnen veiligheidsstootband type New Jersey die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/eindschikking-voor-type-afgeknotte-New-Jersey-tweezijdig")
        self.add_option("stootband-dupuis", "stootband dupuis", "Geprefabriceerde betonnen veiligheidsstootband die over haar gehele lengte op de bodem rust en geplaatst werd om te voorkomen dat voertuigen van de weg afgeraken. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/stootband-dupuis")
        self.add_option("varkensrug-of-biggenrug", "varkensrug of biggenrug", "Geprefabriceerde zeer lage (betonnen) veiligheidsstootband die over haar gehele lengte in de bodem is ingewerkt. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd en worden individueel geplaatst.", "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/varkensrug-of-biggenrug")
