# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlDynBordExternePUMerk(KeuzelijstField):
    """Keuzelijst met merknamen van externe PUs."""
    naam = 'KlDynBordExternePUMerk'
    label = 'Keuzelijst met merknamen van externe PUs'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDynBordExternePUMerk'
    definition = 'Keuzelijst met merknamen van externe PUs.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlDynBordExternePUMerk'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

