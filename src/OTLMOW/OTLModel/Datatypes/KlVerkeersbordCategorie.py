# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordCategorie(KeuzelijstField):
    """Klassen van een verkeersbord."""
    naam = 'KlVerkeersbordCategorie'
    label = 'Verkeersbord categorie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordCategorie'
    definition = 'Klassen van een verkeersbord.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordCategorie'
    options = {
        'aanwijzingsborden': KeuzelijstWaarde(invulwaarde='aanwijzingsborden',
                                              label='aanwijzingsborden',
                                              status='ingebruik',
                                              definitie='aanwijzingsborden',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/aanwijzingsborden'),
        'gebodsborden': KeuzelijstWaarde(invulwaarde='gebodsborden',
                                         label='gebodsborden',
                                         status='ingebruik',
                                         definitie='gebodsborden',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/gebodsborden'),
        'gevaarsborden': KeuzelijstWaarde(invulwaarde='gevaarsborden',
                                          label='gevaarsborden',
                                          status='ingebruik',
                                          definitie='gevaarsborden',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/gevaarsborden'),
        'voorrangsborden': KeuzelijstWaarde(invulwaarde='voorrangsborden',
                                            label='voorrangsborden',
                                            status='ingebruik',
                                            definitie='voorrangsborden',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/voorrangsborden')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

