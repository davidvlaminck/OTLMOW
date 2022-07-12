# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegbermBIO(KeuzelijstField):
    """Bijzonder ingerichte onderdelen van de wegbermen."""
    naam = 'KlWegbermBIO'
    label = 'Wegberm BIO'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlWegbermBIO'
    definition = 'Bijzonder ingerichte onderdelen van de wegbermen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegbermBIO'
    options = {
        'bijzondere-bedding': KeuzelijstWaarde(invulwaarde='bijzondere-bedding',
                                               label='bijzondere bedding',
                                               status='ingebruik',
                                               definitie='Gedeelte van de wegberm, uitsluitend bestemd voor voertuigen van het openbaar vervoer en andere toegelaten voertuigen.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/bijzondere-bedding'),
        'fietspad': KeuzelijstWaarde(invulwaarde='fietspad',
                                     label='fietspad',
                                     status='ingebruik',
                                     definitie='Gedeelte van het wegplatform, dat bestemd is voor fietsers en bromfietsers en als zodanig aangeduid.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/fietspad'),
        'ruiterpad': KeuzelijstWaarde(invulwaarde='ruiterpad',
                                      label='ruiterpad',
                                      status='ingebruik',
                                      definitie='Gedeelte van de wegberm, bestemd voor ruiters en als zodanig aangeduid.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/ruiterpad'),
        'verkeerseiland': KeuzelijstWaarde(invulwaarde='verkeerseiland',
                                           label='verkeerseiland',
                                           status='ingebruik',
                                           definitie='Heeft als doel het verkeer te geleiden en kan verhoogd zijn.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/verkeerseiland'),
        'vluchtheuvel': KeuzelijstWaarde(invulwaarde='vluchtheuvel',
                                         label='vluchtheuvel',
                                         status='ingebruik',
                                         definitie='Verkeersheuvel ten behoeve van voetgangers.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/vluchtheuvel'),
        'voetpad': KeuzelijstWaarde(invulwaarde='voetpad',
                                    label='voetpad',
                                    status='ingebruik',
                                    definitie='Gedeelte van de wegberm, bestemd voor voetgangers.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/voetpad')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlWegbermBIO.get_dummy_data()

