# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDatakabelType(KeuzelijstField):
    """Lijst van types voor datakabels volgens hun constructieve kenmerken."""
    naam = 'KlDatakabelType'
    label = 'Datakabel types'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDatakabelType'
    definition = 'Lijst van types voor datakabels volgens hun constructieve kenmerken.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDatakabelType'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   definitie='Elk types telecommunicatie- of datakabel dat niet opgenomen is in het Standaardbestek 270 en waarover een akkoord bestaat dat die mag gebruikt worden.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/andere'),
        'f-utp-cat-5': KeuzelijstWaarde(invulwaarde='f-utp-cat-5',
                                        label='F/UTP cat 5',
                                        definitie='U/UTP Categorie 5E.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat-5'),
        'f-utp-cat-5-outdoor': KeuzelijstWaarde(invulwaarde='f-utp-cat-5-outdoor',
                                                label='F/UTP cat 5 outdoor',
                                                definitie='U/UTP Categorie 5E.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat-5-outdoor'),
        'f-utp-cat-5e': KeuzelijstWaarde(invulwaarde='f-utp-cat-5e',
                                         label='F/UTP cat 5E',
                                         definitie='U/UTP Categorie 5E.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat-5e'),
        'f-utp-cat-5e-outdoor': KeuzelijstWaarde(invulwaarde='f-utp-cat-5e-outdoor',
                                                 label='F/UTP cat 5E outdoor',
                                                 definitie='U/UTP Categorie 5E.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat-5e-outdoor'),
        'f-utp-cat-6': KeuzelijstWaarde(invulwaarde='f-utp-cat-6',
                                        label='F/UTP cat 6',
                                        definitie='F/UTP Categorie 6.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/f-utp-cat-6'),
        'fo-so': KeuzelijstWaarde(invulwaarde='fo-so',
                                  label='FO/SO',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/fo-so'),
        'j-h(st)h-bd': KeuzelijstWaarde(invulwaarde='j-h(st)h-bd',
                                        label='J-H(St)H-BD',
                                        definitie='Halogeenvrije telefoniekabel.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/j-h(st)h-bd'),
        'je-h(st)h-rf-1h': KeuzelijstWaarde(invulwaarde='je-h(st)h-rf-1h',
                                            label='JE-H(St)H Rf 1h',
                                            definitie='Telefoniekabel met functiebehoud.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/je-h(st)h-rf-1h'),
        'rg11': KeuzelijstWaarde(invulwaarde='rg11',
                                 label='RG11',
                                 definitie='RG 11 Coaxkabel.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/rg11'),
        'rg12': KeuzelijstWaarde(invulwaarde='rg12',
                                 label='RG12',
                                 definitie='RG 12 Coaxkabel.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/rg12'),
        'rg59': KeuzelijstWaarde(invulwaarde='rg59',
                                 label='RG59',
                                 definitie='RG 59 Coaxkabel.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/rg59'),
        'rg6': KeuzelijstWaarde(invulwaarde='rg6',
                                label='RG6',
                                definitie='RG 6 Coaxkabel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/rg6'),
        'stralende-kabel': KeuzelijstWaarde(invulwaarde='stralende-kabel',
                                            label='Stralende kabel',
                                            definitie='Stralende kabel.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/stralende-kabel'),
        'tpgf': KeuzelijstWaarde(invulwaarde='tpgf',
                                 label='TPGF',
                                 definitie='Halogeenvrije telefoniekabel met enkel afgeschermde paren voor binnen.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/tpgf'),
        'twavb': KeuzelijstWaarde(invulwaarde='twavb',
                                  label='TWAVB',
                                  definitie='Gewapende telefoniekabel voor buiten en ondergronds gebruik.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/twavb'),
        'u-utp-cat-5e': KeuzelijstWaarde(invulwaarde='u-utp-cat-5e',
                                         label='U/UTP cat 5E',
                                         definitie='U/UTP Categorie 5E.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/u-utp-cat-5e'),
        'u-utp-cat-6e': KeuzelijstWaarde(invulwaarde='u-utp-cat-6e',
                                         label='U/UTP cat 6E',
                                         definitie='U/UTP Categorie 6.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/u-utp-cat-6e'),
        'u-utp-cat-6e-outdoor': KeuzelijstWaarde(invulwaarde='u-utp-cat-6e-outdoor',
                                                 label='U/UTP cat 6E outdoor',
                                                 definitie='U/UTP Categorie 6.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/u-utp-cat-6e-outdoor'),
        'u-utp-categorie-5e-outdoor': KeuzelijstWaarde(invulwaarde='u-utp-categorie-5e-outdoor',
                                                       label='U/UTP categorie 5E outdoor',
                                                       definitie='U/UTP Categorie 5E.',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/u-utp-categorie-5e-outdoor'),
        'utp': KeuzelijstWaarde(invulwaarde='utp',
                                label='UTP',
                                definitie='U/UTP Categorie 5E.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDatakabelType/utp')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlDatakabelType.get_dummy_data()

