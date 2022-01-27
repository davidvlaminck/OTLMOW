# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlStraatkolkType(KeuzelijstField):
    """Types van straatkolk."""
    naam = 'KlStraatkolkType'
    label = 'Straatkolk type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlStraatkolkType'
    definition = 'Types van straatkolk.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlStraatkolkType'
    options = {
        'geisoleerd': KeuzelijstWaarde(invulwaarde='geisoleerd',
                                       label='geisoleerd',
                                       definitie='Een straatkolk die niet in een rij geplaatst werd maar bijvoorbeeld ergens solitair op een plein.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkType/geisoleerd'),
        'horizontaal': KeuzelijstWaarde(invulwaarde='horizontaal',
                                        label='horizontaal',
                                        definitie='Een gietijzeren rooster met horizontale afvoeropening dat op regelmatige afstand geplaatst wordt langs of in een weg, fietspad of voetpad.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkType/horizontaal'),
        'verticaal': KeuzelijstWaarde(invulwaarde='verticaal',
                                      label='verticaal',
                                      definitie='Verticale afvoeropening die op regelmatige afstand geplaatst wordt langs of in een boordsteen van de weg, fietspad of voetpad.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlStraatkolkType/verticaal')
    }

