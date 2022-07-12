# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBSSRandafwerking(KeuzelijstField):
    """De verschillende manieren van de randafwerking van de verharding."""
    naam = 'KlBSSRandafwerking'
    label = 'randafwerking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBSSRandafwerking'
    definition = 'De verschillende manieren van de randafwerking van de verharding.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBSSRandafwerking'
    options = {
        'biscchopsmutsen': KeuzelijstWaarde(invulwaarde='biscchopsmutsen',
                                            label='biscchopsmutsen',
                                            status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='Een kantsteen die wordt toegepast wanneer de betonstraatsteen in keperverband wordt gestraat.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/biscchopsmutsen'),
        'geen': KeuzelijstWaarde(invulwaarde='geen',
                                 label='geen',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='De randafwerking is overbodig. ',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/geen'),
        'gezaagde-betonstraatstenen': KeuzelijstWaarde(invulwaarde='gezaagde-betonstraatstenen',
                                                       label='gezaagde betonstraatstenen',
                                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                       definitie='Een kantsteen, meestal uit hetzelfde materiaal,  die op maat werd gebracht.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/gezaagde-betonstraatstenen'),
        'kardinaalsmutsen': KeuzelijstWaarde(invulwaarde='kardinaalsmutsen',
                                             label='kardinaalsmutsen',
                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='Een kantsteen die wordt toegepast wanneer de betonstraatsteen in keperverband wordt gestraat.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/kardinaalsmutsen')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBSSRandafwerking.get_dummy_data()

