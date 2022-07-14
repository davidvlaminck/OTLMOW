# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLuchtkwaliteitOpstellingMerk(KeuzelijstField):
    """Het merk van een onderdeel uit een luchtkwaliteitsinstallatie."""
    naam = 'KlLuchtkwaliteitOpstellingMerk'
    label = 'Luchtkwaliteitsopstelling merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlLuchtkwaliteitOpstellingMerk'
    definition = 'Het merk van een onderdeel uit een luchtkwaliteitsinstallatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLuchtkwaliteitOpstellingMerk'
    options = {
        'sick': KeuzelijstWaarde(invulwaarde='sick',
                                 label='sick',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLuchtkwaliteitOpstellingMerk/sick')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

