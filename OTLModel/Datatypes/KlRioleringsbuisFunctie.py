# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlRioleringsbuisFunctie(KeuzelijstField):
    """Mogelijke functies van de riolering."""
    naam = 'KlRioleringsbuisFunctie'
    label = 'Rioleringsbuis functie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlRioleringsbuisFunctie'
    definition = 'Mogelijke functies van de riolering.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlRioleringsbuisFunctie'
    options = {
        'bufferleiding': KeuzelijstWaarde(invulwaarde='bufferleiding',
                                          label='bufferleiding',
                                          definitie='buis bedoeld voor gravitaire afvoer en tijdelijke buffering van water',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/bufferleiding'),
        'gravitaire-leiding': KeuzelijstWaarde(invulwaarde='gravitaire-leiding',
                                               label='gravitaire leiding',
                                               definitie='buis bedoeld voor de gravitaire afvoer van water',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/gravitaire-leiding'),
        'infiltratieleiding': KeuzelijstWaarde(invulwaarde='infiltratieleiding',
                                               label='infiltratieleiding',
                                               definitie='buis bedoeld voor gravitaire afvoer en infiltratie van niet vervuild water',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/infiltratieleiding'),
        'syphon': KeuzelijstWaarde(invulwaarde='syphon',
                                   label='syphon',
                                   definitie='buis bedoeld voor gravitaire afvoer van water met omgekeerde hevelwerking',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlRioleringsbuisFunctie/syphon')
    }

