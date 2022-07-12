# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlMaaiPeriode(KeuzelijstField):
    """De maand waarin het maaien wordt uitgevoerd."""
    naam = 'KlMaaiPeriode'
    label = 'Maaiperiode'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlMaaiPeriode'
    definition = 'De maand waarin het maaien wordt uitgevoerd.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlMaaiPeriode'
    options = {
        'april': KeuzelijstWaarde(invulwaarde='april',
                                  label='april',
                                  status='ingebruik',
                                  definitie='De maand april.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/april'),
        'augustus': KeuzelijstWaarde(invulwaarde='augustus',
                                     label='augustus',
                                     status='ingebruik',
                                     definitie='De maand augustus.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/augustus'),
        'juli': KeuzelijstWaarde(invulwaarde='juli',
                                 label='juli',
                                 status='ingebruik',
                                 definitie='De maand juli.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/juli'),
        'juni': KeuzelijstWaarde(invulwaarde='juni',
                                 label='juni',
                                 status='ingebruik',
                                 definitie='De maand juni.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/juni'),
        'mei': KeuzelijstWaarde(invulwaarde='mei',
                                label='mei',
                                status='ingebruik',
                                definitie='De maand mei.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/mei'),
        'oktober': KeuzelijstWaarde(invulwaarde='oktober',
                                    label='oktober',
                                    status='ingebruik',
                                    definitie='De maand oktober.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/oktober'),
        'september': KeuzelijstWaarde(invulwaarde='september',
                                      label='september',
                                      status='ingebruik',
                                      definitie='De maand september.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlMaaiPeriode/september')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlMaaiPeriode.get_dummy_data()

