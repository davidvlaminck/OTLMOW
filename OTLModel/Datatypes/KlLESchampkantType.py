# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLESchampkantType(KeuzelijstField):
    """Types van de schampkant."""
    naam = 'KlLESchampkantType'
    label = 'Schampkant type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLESchampkantType'
    definition = 'Types van de schampkant.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLESchampkantType'
    options = {
        'afgeknotte-New-Jersey-eenzijdig': KeuzelijstWaarde(invulwaarde='afgeknotte-New-Jersey-eenzijdig',
                                                            label='afgeknotte New Jersey eenzijdig',
                                                            definitie='Betonnen veiligheidsstootband type New Jersey die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/afgeknotte-New-Jersey-eenzijdig'),
        'afgeknotte-New-Jersey-tweezijdig': KeuzelijstWaarde(invulwaarde='afgeknotte-New-Jersey-tweezijdig',
                                                             label='afgeknotte New Jersey tweezijdig',
                                                             definitie='Betonnen veiligheidsstootband type New Jersey die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/afgeknotte-New-Jersey-tweezijdig'),
        'ander-type-schampkant-eenzijdig': KeuzelijstWaarde(invulwaarde='ander-type-schampkant-eenzijdig',
                                                            label='ander type schampkant eenzijdig',
                                                            definitie='Betonnen veiligheidsstootband die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/ander-type-schampkant-eenzijdig'),
        'ander-type-schampkant-tweezijdig': KeuzelijstWaarde(invulwaarde='ander-type-schampkant-tweezijdig',
                                                             label='ander type schampkant tweezijdig',
                                                             definitie='Betonnen veiligheidsstootband die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/ander-type-schampkant-tweezijdig'),
        'eindschikking-voor-ander-type-schampkant.-eenzijdig': KeuzelijstWaarde(invulwaarde='eindschikking-voor-ander-type-schampkant.-eenzijdig',
                                                                                label='eindschikking voor ander type schampkant. eenzijdig',
                                                                                definitie='Eindschikking voor betonnen veiligheidsstootband die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.',
                                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/eindschikking-voor-ander-type-schampkant.-eenzijdig'),
        'eindschikking-voor-ander-type-schampkant.-tweezijdig': KeuzelijstWaarde(invulwaarde='eindschikking-voor-ander-type-schampkant.-tweezijdig',
                                                                                 label='eindschikking voor ander type schampkant. tweezijdig',
                                                                                 definitie='Eindschikking voor betonnen veiligheidsstootband die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.',
                                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/eindschikking-voor-ander-type-schampkant.-tweezijdig'),
        'eindschikking-voor-type-afgeknotte-New-Jersey-eenzijdig': KeuzelijstWaarde(invulwaarde='eindschikking-voor-type-afgeknotte-New-Jersey-eenzijdig',
                                                                                    label='eindschikking voor type afgeknotte New Jersey eenzijdig',
                                                                                    definitie='Eindschikking voor betonnen veiligheidsstootband type New Jersey die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.',
                                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/eindschikking-voor-type-afgeknotte-New-Jersey-eenzijdig'),
        'eindschikking-voor-type-afgeknotte-New-Jersey-tweezijdig': KeuzelijstWaarde(invulwaarde='eindschikking-voor-type-afgeknotte-New-Jersey-tweezijdig',
                                                                                     label='eindschikking voor type afgeknotte New Jersey tweezijdig',
                                                                                     definitie='Eindschikking voor betonnen veiligheidsstootband type New Jersey die over haar gehele lengte op de bodem rust. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.',
                                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/eindschikking-voor-type-afgeknotte-New-Jersey-tweezijdig'),
        'stootband-dupuis': KeuzelijstWaarde(invulwaarde='stootband-dupuis',
                                             label='stootband dupuis',
                                             definitie='Geprefabriceerde betonnen veiligheidsstootband die over haar gehele lengte op de bodem rust en geplaatst werd om te voorkomen dat voertuigen van de weg afgeraken. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/stootband-dupuis'),
        'varkensrug-of-biggenrug': KeuzelijstWaarde(invulwaarde='varkensrug-of-biggenrug',
                                                    label='varkensrug of biggenrug',
                                                    definitie='Geprefabriceerde zeer lage (betonnen) veiligheidsstootband die over haar gehele lengte in de bodem is ingewerkt. Deze zijn overwegend parallel aan de hartlijn van de wegbaan georiënteerd en worden individueel geplaatst.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLESchampkantType/varkensrug-of-biggenrug')
    }

