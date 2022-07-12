# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlConstructiestaalsoort(KeuzelijstField):
    """De soort van het constructiestaal."""
    naam = 'KlConstructiestaalsoort'
    label = 'Constructiestaalsoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlConstructiestaalsoort'
    definition = 'De soort van het constructiestaal.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlConstructiestaalsoort'
    options = {
        's-235-j-0': KeuzelijstWaarde(invulwaarde='s-235-j-0',
                                      label='S235J0',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='S staat voor Structural steel (constructiestaal), 235 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 0 voor 0 graden celsius.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-235-j-0'),
        's-235-j-2-n': KeuzelijstWaarde(invulwaarde='s-235-j-2-n',
                                        label='S235J2+N',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='S staat voor Structural steel (constructiestaal), 235 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 2 voor -20 graden celsius. De N duidt aan dat producten in genormaliseerde of equivalente toestand dienen geleverd te worden.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-235-j-2-n'),
        's-235-jr': KeuzelijstWaarde(invulwaarde='s-235-jr',
                                     label='S235JR',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='S staat voor Structural steel (constructiestaal), 235 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en R voor kampertemperatuur.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-235-jr'),
        's-240-gp': KeuzelijstWaarde(invulwaarde='s-240-gp',
                                     label='S240GP',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Warmgewalste staalsoort S 240 GP.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-240-gp'),
        's-270-gp': KeuzelijstWaarde(invulwaarde='s-270-gp',
                                     label='S270GP',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Warmgewalste staalsoort S 270 GP.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-270-gp'),
        's-275-j-0': KeuzelijstWaarde(invulwaarde='s-275-j-0',
                                      label='S275J0',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='S staat voor Structural steel (constructiestaal), 275 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 0 voor 0 graden celsius.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-275-j-0'),
        's-275-j-2-n': KeuzelijstWaarde(invulwaarde='s-275-j-2-n',
                                        label='S275J2+N',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='S staat voor Structural steel (constructiestaal), 275 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 2 voor -20 graden celsius. De N duidt aan dat producten in genormaliseerde of equivalente toestand dienen geleverd te worden.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-275-j-2-n'),
        's-275-jr': KeuzelijstWaarde(invulwaarde='s-275-jr',
                                     label='S275JR',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='S staat voor Structural steel (constructiestaal), 275 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en R voor kampertemperatuur.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-275-jr'),
        's-320-gp': KeuzelijstWaarde(invulwaarde='s-320-gp',
                                     label='S320GP',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Warmgewalste staalsoort S 320 GP.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-320-gp'),
        's-355-gp': KeuzelijstWaarde(invulwaarde='s-355-gp',
                                     label='S355GP',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Warmgewalste staalsoort S 355 GP.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-gp'),
        's-355-j-0': KeuzelijstWaarde(invulwaarde='s-355-j-0',
                                      label='S355J0',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='S staat voor Structural steel (constructiestaal), 355 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 0 voor 0 graden celsius.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-j-0'),
        's-355-j-0-c': KeuzelijstWaarde(invulwaarde='s-355-j-0-c',
                                        label='S355J0C',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='S staat voor Structural steel (constructiestaal), 355 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 0 voor 0 graden celsius. De C duidt aan het staal geschikt is voor specifieke aanwending zoals koudtrekken, profileren, koudflenzen (C van Cold forming) of dat het staal een hoog koolstofgehalte heeft (C van Carbon).',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-j-0-c'),
        's-355-j-2-n': KeuzelijstWaarde(invulwaarde='s-355-j-2-n',
                                        label='S355J2+N',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='S staat voor Structural steel (constructiestaal), 355 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en 2 voor -20 graden celsius. De N duidt aan dat producten in genormaliseerde of equivalente toestand dienen geleverd te worden.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-j-2-n'),
        's-355-jr': KeuzelijstWaarde(invulwaarde='s-355-jr',
                                     label='S355JR',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='S staat voor Structural steel (constructiestaal), 355 voor de vloeigrens in MPa, J staat voor een kerfslagwaarde van 27 Joule en R voor kampertemperatuur.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-jr'),
        's-355-k-2-n': KeuzelijstWaarde(invulwaarde='s-355-k-2-n',
                                        label='S355K2+N',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='S staat voor Structural steel (constructiestaal), 355 voor de vloeigrens in MPa, K staat voor een kerfslagwaarde van 40 Joule en 2 voor -20 graden celsius. De N duidt aan dat producten in genormaliseerde of equivalente toestand dienen geleverd te worden.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-355-k-2-n'),
        's-390-gp': KeuzelijstWaarde(invulwaarde='s-390-gp',
                                     label='S390GP',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Warmgewalste staalsoort S 390 GP.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-390-gp'),
        's-430-gp': KeuzelijstWaarde(invulwaarde='s-430-gp',
                                     label='S430GP',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Warmgewalste staalsoort S 430 GP.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-430-gp'),
        's-460-m': KeuzelijstWaarde(invulwaarde='s-460-m',
                                    label='S460M',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='S staat voor Structural steel (constructiestaal), 460 voor de vloeigrens in MPa en M staat voor thermo mechanisch gewalst staal (M van Mechanically).',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-460-m'),
        's-460-ml': KeuzelijstWaarde(invulwaarde='s-460-ml',
                                     label='S460ML',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='S staat voor Structural steel (constructiestaal), 460 voor de vloeigrens in MPa en ML staat voor thermo mechanisch gewalst staal met min. gespecificeerde kerfslagwaarden onder -50° celsius.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-460-ml'),
        's-460-n': KeuzelijstWaarde(invulwaarde='s-460-n',
                                    label='S460N',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='S staat voor Structural steel (constructiestaal) en 460 voor de vloeigrens in MPa. De N duidt aan dat producten in genormaliseerde of equivalente toestand dienen geleverd te worden.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-460-n'),
        's-460-nl': KeuzelijstWaarde(invulwaarde='s-460-nl',
                                     label='S460NL',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='S staat voor Structural steel (constructiestaal), 460 voor de vloeigrens in MPa en NL staat voor gegloeid en normaliserend gewalst staal met min. gespecificeerde kerfslagwaarden onder -50° celsius.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlConstructiestaalsoort/s-460-nl')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlConstructiestaalsoort.get_dummy_data()

