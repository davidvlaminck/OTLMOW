# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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
                                            definitie='Een kantsteen die wordt toegepast wanneer de betonstraatsteen in keperverband wordt gestraat.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/biscchopsmutsen'),
        'geen': KeuzelijstWaarde(invulwaarde='geen',
                                 label='geen',
                                 definitie='De randafwerking is overbodig. ',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/geen'),
        'gezaagde-betonstraatstenen': KeuzelijstWaarde(invulwaarde='gezaagde-betonstraatstenen',
                                                       label='gezaagde betonstraatstenen',
                                                       definitie='Een kantsteen, meestal uit hetzelfde materiaal,  die op maat werd gebracht.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/gezaagde-betonstraatstenen'),
        'kardinaalsmutsen': KeuzelijstWaarde(invulwaarde='kardinaalsmutsen',
                                             label='kardinaalsmutsen',
                                             definitie='Een kantsteen die wordt toegepast wanneer de betonstraatsteen in keperverband wordt gestraat.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBSSRandafwerking/kardinaalsmutsen')
    }

