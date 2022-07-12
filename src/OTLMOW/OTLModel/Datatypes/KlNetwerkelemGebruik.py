# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='Het netwerkelement wordt gebruikt binnen een 4G draadloos netwerk.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/4g-wireless-router'),
        '4g-wireless-router-dsl-backup': KeuzelijstWaarde(invulwaarde='4g-wireless-router-dsl-backup',
                                                          label='4G wireless router - DSL backup',
                                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                          definitie='Het netwerkelement wordt gebruikt binnen een 4G draadloos netwerk. DSL wordt gebruikt als backup bij faling van het 4G draadloos netwerk.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/4g-wireless-router-dsl-backup'),
        'cen': KeuzelijstWaarde(invulwaarde='cen',
                                label='CEN',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Het netwerkelement wordt gebruikt binnen het CEN netwerk.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/cen'),
        'dsl-router': KeuzelijstWaarde(invulwaarde='dsl-router',
                                       label='DSL  router',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       definitie='Het netwerkelement wordt gebruikt binnen een DSL netwerk.',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/dsl-router'),
        'dsl-router-4g-wireless-backup': KeuzelijstWaarde(invulwaarde='dsl-router-4g-wireless-backup',
                                                          label='DSL router - 4G wireless backup',
                                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                          definitie='Het netwerkelement wordt gebruikt binnen een DSL netwerk. Een 4G  wordt gebruikt als backup bij faling van het DSL netwerk.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/dsl-router-4g-wireless-backup'),
        'l2-switch': KeuzelijstWaarde(invulwaarde='l2-switch',
                                      label='L2-switch',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Het netwerkelement wordt gebruikt binnen de L2 netwerkstructuur.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/l2-switch'),
        'l3-switch': KeuzelijstWaarde(invulwaarde='l3-switch',
                                      label='L3-switch',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='Het netwerkelement wordt gebruikt binnen de L3 netwerkstructuur.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/l3-switch'),
        'otn': KeuzelijstWaarde(invulwaarde='otn',
                                label='OTN',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Het netwerkelement wordt gebruikt binnen het optisch transport netwerk.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/otn'),
        'sdh': KeuzelijstWaarde(invulwaarde='sdh',
                                label='SDH',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Het netwerkelement wordt gebruikt binnen het SDH netwerk.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkelemGebruik/sdh')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlNetwerkelemGebruik.get_dummy_data()

