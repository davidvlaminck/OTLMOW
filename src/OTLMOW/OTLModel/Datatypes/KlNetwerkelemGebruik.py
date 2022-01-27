# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNetwerkelemGebruik(KeuzelijstField):
    """Keuzelijst met de verschillende mogelijke netwerkstructuren waarbinnen een netwerkelement kan ingezet worden."""
    naam = 'KlNetwerkelemGebruik'
    label = 'Netwerkelement gebruik'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNetwerkelemGebruik'
    definition = 'Keuzelijst met de verschillende mogelijke netwerkstructuren waarbinnen een netwerkelement kan ingezet worden.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNetwerkelemGebruik'
    options = {
        '4g-wireless-router': KeuzelijstWaarde(invulwaarde='4g-wireless-router',
                                               label='4G wireless router',
                                               definitie='Het netwerkelement wordt gebruikt binnen een 4G draadloos netwerk.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/4g-wireless-router'),
        'cen': KeuzelijstWaarde(invulwaarde='cen',
                                label='CEN',
                                definitie='Het netwerkelement wordt gebruikt binnen het CEN netwerk.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/cen'),
        'l2-switch': KeuzelijstWaarde(invulwaarde='l2-switch',
                                      label='L2-switch',
                                      definitie='Het netwerkelement wordt gebruikt binnen de L2 netwerkstructuur.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/l2-switch'),
        'l3-switch': KeuzelijstWaarde(invulwaarde='l3-switch',
                                      label='L3-switch',
                                      definitie='Het netwerkelement wordt gebruikt binnen de L3 netwerkstructuur.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/l3-switch'),
        'otn': KeuzelijstWaarde(invulwaarde='otn',
                                label='OTN',
                                definitie='Het netwerkelement wordt gebruikt binnen het optisch transport netwerk.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/otn'),
        'sdh': KeuzelijstWaarde(invulwaarde='sdh',
                                label='SDH',
                                definitie='Het netwerkelement wordt gebruikt binnen het SDH netwerk.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/sdh')
    }

