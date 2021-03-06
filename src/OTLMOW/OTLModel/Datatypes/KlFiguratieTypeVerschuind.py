# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFiguratieTypeVerschuind(KeuzelijstField):
    """Types van verschuinde figuratiemarkering."""
    naam = 'KlFiguratieTypeVerschuind'
    label = 'Figuratie type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFiguratieTypeVerschuind'
    definition = 'Types van verschuinde figuratiemarkering.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFiguratieTypeVerschuind'
    options = {
        'STOP-(smal-schuin)': KeuzelijstWaarde(invulwaarde='STOP-(smal-schuin)',
                                               label='STOP (smal schuin)',
                                               status='ingebruik',
                                               definitie='Lettermarkering STOP (smal schuin)',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieTypeVerschuind/STOP-(smal-schuin)'),
        'groot-(schuin)': KeuzelijstWaarde(invulwaarde='groot-(schuin)',
                                           label='groot (schuin)',
                                           status='ingebruik',
                                           definitie='Omgekeerde driehoek markering groot en schuin type.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFiguratieTypeVerschuind/groot-(schuin)')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

