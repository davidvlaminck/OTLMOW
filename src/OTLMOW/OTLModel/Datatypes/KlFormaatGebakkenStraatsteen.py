# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFormaatGebakkenStraatsteen(KeuzelijstField):
    """De formaten van gebakken straatsteen."""
    naam = 'KlFormaatGebakkenStraatsteen'
    label = 'Formaat gebakken straatsteen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFormaatGebakkenStraatsteen'
    definition = 'De formaten van gebakken straatsteen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFormaatGebakkenStraatsteen'
    options = {
        'dikformaat-(ca.-200-x-ca.-65-mm)': KeuzelijstWaarde(invulwaarde='dikformaat-(ca.-200-x-ca.-65-mm)',
                                                             label='dikformaat (ca. 200 x ca. 65 mm)',
                                                             definitie='Een gestandaardiseerde maat voor de gebakken straatsteen.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFormaatGebakkenStraatsteen/dikformaat-(ca.-200-x-ca.-65-mm)'),
        'keiformaat-(ca.-200-x-ca.-100-mm)': KeuzelijstWaarde(invulwaarde='keiformaat-(ca.-200-x-ca.-100-mm)',
                                                              label='keiformaat (ca. 200 x ca. 100 mm)',
                                                              definitie='Een gestandaardiseerde maat voor de gebakken straatsteen.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFormaatGebakkenStraatsteen/keiformaat-(ca.-200-x-ca.-100-mm)'),
        'langformaat-(ca.-240-x-ca.-80-mm)': KeuzelijstWaarde(invulwaarde='langformaat-(ca.-240-x-ca.-80-mm)',
                                                              label='langformaat (ca. 240 x ca. 80 mm)',
                                                              definitie='Een gestandaardiseerde maat voor de gebakken straatsteen.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFormaatGebakkenStraatsteen/langformaat-(ca.-240-x-ca.-80-mm)'),
        'rijnformaat-(ca.-180-x-ca.-45-mm)': KeuzelijstWaarde(invulwaarde='rijnformaat-(ca.-180-x-ca.-45-mm)',
                                                              label='rijnformaat (ca. 180 x ca. 45 mm)',
                                                              definitie='Een gestandaardiseerde maat voor de gebakken straatsteen.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFormaatGebakkenStraatsteen/rijnformaat-(ca.-180-x-ca.-45-mm)'),
        'waalformaat-(ca.-200-x-ca.-50-mm)': KeuzelijstWaarde(invulwaarde='waalformaat-(ca.-200-x-ca.-50-mm)',
                                                              label='waalformaat (ca. 200 x ca. 50 mm)',
                                                              definitie='Een gestandaardiseerde maat voor de gebakken straatsteen.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFormaatGebakkenStraatsteen/waalformaat-(ca.-200-x-ca.-50-mm)')
    }

