# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBestratingOpvulsoort(KeuzelijstField):
    """De mogelijke opvulsoorten van de grasbetontegel en graskunststofplaat."""
    naam = 'KlBestratingOpvulsoort'
    label = 'Bestrating opvulsoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBestratingOpvulsoort'
    definition = 'De mogelijke opvulsoorten van de grasbetontegel en graskunststofplaat.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBestratingOpvulsoort'
    options = {
        'bodemsubstraat': KeuzelijstWaarde(invulwaarde='bodemsubstraat',
                                           label='bodemsubstraat',
                                           definitie='Opgevuld met bodemsubstraat.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bodemsubstraat'),
        'bodemsubstraat-en-ingezaaid': KeuzelijstWaarde(invulwaarde='bodemsubstraat-en-ingezaaid',
                                                        label='bodemsubstraat en ingezaaid',
                                                        definitie='Opgevuld met bodemsubstraat en ingezaaid.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bodemsubstraat-en-ingezaaid'),
        'bomenzand': KeuzelijstWaarde(invulwaarde='bomenzand',
                                      label='bomenzand',
                                      definitie='Opgevuld met bomenzand.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bomenzand'),
        'bomenzand-en-ingezaaid': KeuzelijstWaarde(invulwaarde='bomenzand-en-ingezaaid',
                                                   label='bomenzand en ingezaaid',
                                                   definitie='Opgevuld met bomenzand en ingezaaid.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/bomenzand-en-ingezaaid'),
        'steenslag-2-6.3': KeuzelijstWaarde(invulwaarde='steenslag-2-6.3',
                                            label='steenslag 2-6.3',
                                            definitie='Opgevuld met steenslag 2/6,3',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBestratingOpvulsoort/steenslag-2-6.3')
    }

