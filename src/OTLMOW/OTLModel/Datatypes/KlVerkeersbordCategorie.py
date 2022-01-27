# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordCategorie(KeuzelijstField):
    """Klassen van een verkeersbord."""
    naam = 'KlVerkeersbordCategorie'
    label = 'Verkeersbord categorie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordCategorie'
    definition = 'Klassen van een verkeersbord.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordCategorie'
    options = {
        'aanwijzingsborden': KeuzelijstWaarde(invulwaarde='aanwijzingsborden',
                                              label='aanwijzingsborden',
                                              definitie='aanwijzingsborden',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/aanwijzingsborden'),
        'gebodsborden': KeuzelijstWaarde(invulwaarde='gebodsborden',
                                         label='gebodsborden',
                                         definitie='gebodsborden',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/gebodsborden'),
        'gevaarsborden': KeuzelijstWaarde(invulwaarde='gevaarsborden',
                                          label='gevaarsborden',
                                          definitie='gevaarsborden',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/gevaarsborden'),
        'voorrangsborden': KeuzelijstWaarde(invulwaarde='voorrangsborden',
                                            label='voorrangsborden',
                                            definitie='voorrangsborden',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordCategorie/voorrangsborden')
    }

