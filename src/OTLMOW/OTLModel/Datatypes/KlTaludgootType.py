# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTaludgootType(KeuzelijstField):
    """Het type van taludgoot."""
    naam = 'KlTaludgootType'
    label = 'Taludgoot type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTaludgootType'
    definition = 'Het type van taludgoot.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTaludgootType'
    options = {
        'Beginstuk-taludgoten-type-A-met-twee-openingen': KeuzelijstWaarde(invulwaarde='Beginstuk-taludgoten-type-A-met-twee-openingen',
                                                                           label='Beginstuk taludgoten type A met twee openingen',
                                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Beginstuk-taludgoten-type-A-met-twee-openingen'),
        'Beginstuk-taludgoten-type-A-met-één-opening': KeuzelijstWaarde(invulwaarde='Beginstuk-taludgoten-type-A-met-één-opening',
                                                                        label='Beginstuk taludgoten type A met één opening',
                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Beginstuk-taludgoten-type-A-met-één-opening'),
        'Beginstuk-taludgoten-type-B-met-twee-openingen': KeuzelijstWaarde(invulwaarde='Beginstuk-taludgoten-type-B-met-twee-openingen',
                                                                           label='Beginstuk taludgoten type B met twee openingen',
                                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Beginstuk-taludgoten-type-B-met-twee-openingen'),
        'Beginstuk-taludgoten-type-B-met-één-opening': KeuzelijstWaarde(invulwaarde='Beginstuk-taludgoten-type-B-met-één-opening',
                                                                        label='Beginstuk taludgoten type B met één opening',
                                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Beginstuk-taludgoten-type-B-met-één-opening'),
        'Eindstuk-taludgoten-type-A': KeuzelijstWaarde(invulwaarde='Eindstuk-taludgoten-type-A',
                                                       label='Eindstuk taludgoten type A',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Eindstuk-taludgoten-type-A'),
        'Eindstuk-taludgoten-type-B': KeuzelijstWaarde(invulwaarde='Eindstuk-taludgoten-type-B',
                                                       label='Eindstuk taludgoten type B',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/Eindstuk-taludgoten-type-B'),
        'taludgoot-type-A': KeuzelijstWaarde(invulwaarde='taludgoot-type-A',
                                             label='taludgoot type A',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/taludgoot-type-A'),
        'taludgoot-type-B': KeuzelijstWaarde(invulwaarde='taludgoot-type-B',
                                             label='taludgoot type B',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTaludgootType/taludgoot-type-B')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTaludgootType.get_dummy_data()

