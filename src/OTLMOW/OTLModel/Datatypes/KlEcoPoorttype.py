# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEcoPoorttype(KeuzelijstField):
    """Types van de poort."""
    naam = 'KlEcoPoorttype'
    label = 'Poorttype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlEcoPoorttype'
    definition = 'Types van de poort.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEcoPoorttype'
    options = {
        'dubbel': KeuzelijstWaarde(invulwaarde='dubbel',
                                   label='dubbel',
                                   definitie='Een dubble poort.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPoorttype/dubbel'),
        'enkel': KeuzelijstWaarde(invulwaarde='enkel',
                                  label='enkel',
                                  definitie='Een enkele poort.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEcoPoorttype/enkel')
    }

