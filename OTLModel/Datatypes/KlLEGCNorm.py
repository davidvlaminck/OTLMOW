# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEGCNorm(KeuzelijstField):
    """De mogelijke normen."""
    naam = 'KlLEGCNorm'
    label = 'Norm'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEGCNorm'
    definition = 'De mogelijke normen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEGCNorm'
    options = {
        'NBN-EN-1793-1': KeuzelijstWaarde(invulwaarde='NBN-EN-1793-1',
                                          label='NBN EN 1793-1',
                                          definitie='Beproevingsmethode deel 1 'Intrinsieke kenmerken van de geluidabsorptie'',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCNorm/NBN-EN-1793-1'),
        'NBN-EN-1793-2': KeuzelijstWaarde(invulwaarde='NBN-EN-1793-2',
                                          label='NBN EN 1793-2',
                                          definitie='Beproevingsmethode deel 2 'Intrinsieke kenmerken van de luchtgeluidisolatie'',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCNorm/NBN-EN-1793-2'),
        'NBN-EN-1793-5': KeuzelijstWaarde(invulwaarde='NBN-EN-1793-5',
                                          label='NBN EN 1793-5',
                                          definitie='Beproevingsmethode deel 5 'Intrinsieke kenmerken - In situ waarden van geluidsisolatie onder directe geluidveld omstandigheden'',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCNorm/NBN-EN-1793-5'),
        'NBN-EN-1793-6': KeuzelijstWaarde(invulwaarde='NBN-EN-1793-6',
                                          label='NBN EN 1793-6',
                                          definitie='Beproevingsmethode deel 6 'In-situ waarden van luchtgeluidisolatie onder directe geluidsveldcondities'',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEGCNorm/NBN-EN-1793-6')
    }

