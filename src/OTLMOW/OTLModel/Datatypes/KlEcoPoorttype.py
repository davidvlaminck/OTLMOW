# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoPoorttype(KeuzelijstField):
    """Types van de poort."""
    naam = 'KlEcoPoorttype'
    label = 'Poorttype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoPoorttype'
    definition = 'Types van de poort.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoPoorttype'
    options = {
        'dubbel': KeuzelijstWaarde(invulwaarde='dubbel',
                                   label='dubbel',
                                   status='ingebruik',
                                   definitie='Een dubble poort.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPoorttype/dubbel'),
        'enkel': KeuzelijstWaarde(invulwaarde='enkel',
                                  label='enkel',
                                  status='ingebruik',
                                  definitie='Een enkele poort.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPoorttype/enkel')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

