# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGekleurdWVSoort(KeuzelijstField):
    """Types van gekleurd wegvlak."""
    naam = 'KlGekleurdWVSoort'
    label = 'Gekleurd WV type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGekleurdWVSoort'
    definition = 'Types van gekleurd wegvlak.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGekleurdWVSoort'
    options = {
        'OFOS-(Opgeblazen-fietsopstelstrook)': KeuzelijstWaarde(invulwaarde='OFOS-(Opgeblazen-fietsopstelstrook)',
                                                                label='OFOS (Opgeblazen fietsopstelstrook)',
                                                                definitie='Gekleurd wegvlak als OFOS.',
                                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/OFOS-(Opgeblazen-fietsopstelstrook)'),
        'OFOS-variant': KeuzelijstWaarde(invulwaarde='OFOS-variant',
                                         label='OFOS variant',
                                         definitie='Gekleurd wegvlak als OFOS variant.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/OFOS-variant'),
        'fiets-suggestiestrook': KeuzelijstWaarde(invulwaarde='fiets-suggestiestrook',
                                                  label='fiets suggestiestrook',
                                                  definitie='Gekleurd wegvlak als fiets suggestiestrook.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/fiets-suggestiestrook'),
        'fietsoversteekplaats-met-blokken-(FOP)': KeuzelijstWaarde(invulwaarde='fietsoversteekplaats-met-blokken-(FOP)',
                                                                   label='fietsoversteekplaats met blokken (FOP)',
                                                                   definitie='Gekleurd wegvlak als fietsoversteekplaats met blokken.',
                                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/fietsoversteekplaats-met-blokken-(FOP)'),
        'fietspad-(met-lijnen)': KeuzelijstWaarde(invulwaarde='fietspad-(met-lijnen)',
                                                  label='fietspad (met lijnen)',
                                                  definitie='Gekleurd wegvlak als fietspad (met lijnen).',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/fietspad-(met-lijnen)'),
        'middengeleider-(Bv.-Groene-strook)': KeuzelijstWaarde(invulwaarde='middengeleider-(Bv.-Groene-strook)',
                                                               label='middengeleider (Bv. Groene strook)',
                                                               definitie='Gekleurd wegvlak als middengeleider.',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/middengeleider-(Bv.-Groene-strook)'),
        'parkeerplaats-mindervaliden': KeuzelijstWaarde(invulwaarde='parkeerplaats-mindervaliden',
                                                        label='parkeerplaats mindervaliden',
                                                        definitie='Gekleurd wegvlak als parkeerplaats mindervaliden.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/parkeerplaats-mindervaliden'),
        'verkeersplateau': KeuzelijstWaarde(invulwaarde='verkeersplateau',
                                            label='verkeersplateau',
                                            definitie='Gekleurd wegvlak als verkeersplateau.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/verkeersplateau'),
        'voetgangers-oversteekplaats': KeuzelijstWaarde(invulwaarde='voetgangers-oversteekplaats',
                                                        label='voetgangers-oversteekplaats',
                                                        definitie='Gekleurd wegvlak als voetgangers-oversteekplaats.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGekleurdWVSoort/voetgangers-oversteekplaats')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlGekleurdWVSoort.get_dummy_data()

