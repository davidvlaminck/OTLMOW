# coding=utf-8
import random
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
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/droog'),
        'esterolie': KeuzelijstWaarde(invulwaarde='esterolie',
                                      label='esterolie',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/esterolie'),
        'giethars': KeuzelijstWaarde(invulwaarde='giethars',
                                     label='giethars',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/giethars'),
        'minerale-olie': KeuzelijstWaarde(invulwaarde='minerale-olie',
                                          label='minerale olie',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/minerale-olie'),
        'siliconenvloeistof': KeuzelijstWaarde(invulwaarde='siliconenvloeistof',
                                               label='siliconenvloeistof',
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/siliconenvloeistof'),
        'vegetale-olie': KeuzelijstWaarde(invulwaarde='vegetale-olie',
                                          label='vegetale olie',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTransformatorIsolatiemedium/vegetale-olie')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTransformatorIsolatiemedium.get_dummy_data()

