# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTransformatorIsolatiemedium(KeuzelijstField):
    """Wijze van onderdompeling van de magnetische kring en van de wikkelingen van de transformator."""
    naam = 'KlTransformatorIsolatiemedium'
    label = 'Transformator isolatiemedium'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTransformatorIsolatiemedium'
    definition = 'Wijze van onderdompeling van de magnetische kring en van de wikkelingen van de transformator.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTransformatorIsolatiemedium'
    options = {
        'droog': KeuzelijstWaarde(invulwaarde='droog',
                                  label='droog',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/droog'),
        'esterolie': KeuzelijstWaarde(invulwaarde='esterolie',
                                      label='esterolie',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/esterolie'),
        'giethars': KeuzelijstWaarde(invulwaarde='giethars',
                                     label='giethars',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/giethars'),
        'minerale-olie': KeuzelijstWaarde(invulwaarde='minerale-olie',
                                          label='minerale olie',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/minerale-olie'),
        'siliconenvloeistof': KeuzelijstWaarde(invulwaarde='siliconenvloeistof',
                                               label='siliconenvloeistof',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/siliconenvloeistof'),
        'vegetale-olie': KeuzelijstWaarde(invulwaarde='vegetale-olie',
                                          label='vegetale olie',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/vegetale-olie')
    }

