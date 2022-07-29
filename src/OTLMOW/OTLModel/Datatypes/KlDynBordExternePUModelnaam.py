# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordExternePUModelnaam(KeuzelijstField):
    """De modelnaam van externe processing unit voor dynamische verkeersborden. Wordt bepaald door de lverancier."""
    naam = 'KlDynBordExternePUModelnaam'
    label = 'Keuzelijst met modellen van Externe PU'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordExternePUModelnaam'
    definition = 'De modelnaam van externe processing unit voor dynamische verkeersborden. Wordt bepaald door de lverancier.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordExternePUModelnaam'
    options = {
        'diamond': KeuzelijstWaarde(invulwaarde='diamond',
                                    label='diamond',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordExternePUModelnaam/diamond'),
        'ixor': KeuzelijstWaarde(invulwaarde='ixor',
                                 label='ixor',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordExternePUModelnaam/ixor'),
        'moxa': KeuzelijstWaarde(invulwaarde='moxa',
                                 label='moxa',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlDynBordExternePUModelnaam/moxa')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

