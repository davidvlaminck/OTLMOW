# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBijlageMetGeometrieType(KeuzelijstField):
    """De mogelijke opties als type van een bijlage met geometrie."""
    naam = 'KlBijlageMetGeometrieType'
    label = 'Bijlage met geometrie type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBijlageMetGeometrieType'
    definition = 'De mogelijke opties als type van een bijlage met geometrie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBijlageMetGeometrieType'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageMetGeometrieType/andere'),
        'detailplan': KeuzelijstWaarde(invulwaarde='detailplan',
                                       label='detailplan',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageMetGeometrieType/detailplan'),
        'field-of-view': KeuzelijstWaarde(invulwaarde='field-of-view',
                                          label='field of view',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageMetGeometrieType/field-of-view'),
        'lengteprofiel': KeuzelijstWaarde(invulwaarde='lengteprofiel',
                                          label='lengteprofiel',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageMetGeometrieType/lengteprofiel'),
        'veiligheidsvoorschriften': KeuzelijstWaarde(invulwaarde='veiligheidsvoorschriften',
                                                     label='veiligheidsvoorschriften',
                                                     status='ingebruik',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBijlageMetGeometrieType/veiligheidsvoorschriften')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

