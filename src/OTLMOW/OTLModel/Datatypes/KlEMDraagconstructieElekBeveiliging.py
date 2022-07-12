# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlEMDraagconstructieElekBeveiliging(KeuzelijstField):
    """Type elektrische beveiliging aanwezig in de draagconstructie."""
    naam = 'KlEMDraagconstructieElekBeveiliging'
    label = 'EM-draagconstructie elektrische beveiliging'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlEMDraagconstructieElekBeveiliging'
    definition = 'Type elektrische beveiliging aanwezig in de draagconstructie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlEMDraagconstructieElekBeveiliging'
    options = {
        'automaat': KeuzelijstWaarde(invulwaarde='automaat',
                                     label='automaat',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/automaat'),
        'differentieelautomaat': KeuzelijstWaarde(invulwaarde='differentieelautomaat',
                                                  label='differentieelautomaat',
                                                  status='ingebruik',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/differentieelautomaat'),
        'smeltzekering': KeuzelijstWaarde(invulwaarde='smeltzekering',
                                          label='smeltzekering',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlEMDraagconstructieElekBeveiliging/smeltzekering')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlEMDraagconstructieElekBeveiliging.get_dummy_data()

