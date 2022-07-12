# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormTerugslagklep(KeuzelijstField):
    """De vorm van opening van de terugslagklep."""
    naam = 'KlVormTerugslagklep'
    label = 'Vorm terugslagklep'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormTerugslagklep'
    definition = 'De vorm van opening van de terugslagklep.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormTerugslagklep'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='andere',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/andere'),
        'circkelvormig': KeuzelijstWaarde(invulwaarde='circkelvormig',
                                          label='circkelvormig',
                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                          definitie='circkelvormig',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/circkelvormig'),
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='rechthoekig',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='rechthoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/rechthoekig')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVormTerugslagklep.get_dummy_data()

