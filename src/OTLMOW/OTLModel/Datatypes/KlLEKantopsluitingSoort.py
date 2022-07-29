# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlLEKantopsluitingSoort(KeuzelijstField):
    """Soorten van kantopsluiting."""
    naam = 'KlLEKantopsluitingSoort'
    label = 'Kantopsluiting soort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlLEKantopsluitingSoort'
    definition = 'Soorten van kantopsluiting.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlLEKantopsluitingSoort'
    options = {
        'betonnen-kantstroken': KeuzelijstWaarde(invulwaarde='betonnen-kantstroken',
                                                 label='betonnen kantstroken',
                                                 status='ingebruik',
                                                 definitie='Geprefabriceerde of ter plaatste vervaardigde betonnen kantstroken.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/betonnen-kantstroken'),
        'betonnen-kantstroken-en-watergreppels': KeuzelijstWaarde(invulwaarde='betonnen-kantstroken-en-watergreppels',
                                                                  label='betonnen kantstroken en watergreppels',
                                                                  status='ingebruik',
                                                                  definitie='Geprefabriceerde of ter plaatste vervaardigde betonnen kantstroken en watergreppels.',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/betonnen-kantstroken-en-watergreppels'),
        'betonnen-overgangstrottoirbanden': KeuzelijstWaarde(invulwaarde='betonnen-overgangstrottoirbanden',
                                                             label='betonnen overgangstrottoirbanden',
                                                             status='ingebruik',
                                                             definitie='Geprefabriceerde of ter plaatste vervaardigde betonnen overgangstrottoirbanden.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/betonnen-overgangstrottoirbanden'),
        'betonnen-schampkant': KeuzelijstWaarde(invulwaarde='betonnen-schampkant',
                                                label='betonnen schampkant',
                                                status='ingebruik',
                                                definitie='Geprefabriceerde of ter plaatste vervaardigde schampkant.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/betonnen-schampkant'),
        'betonnen-trottoirbanden': KeuzelijstWaarde(invulwaarde='betonnen-trottoirbanden',
                                                    label='betonnen trottoirbanden',
                                                    status='ingebruik',
                                                    definitie='Geprefabriceerde of ter plaatste vervaardigde betonnen trottoirbanden.',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/betonnen-trottoirbanden'),
        'betonnen-trottoirbanden-voor-mindervaliden': KeuzelijstWaarde(invulwaarde='betonnen-trottoirbanden-voor-mindervaliden',
                                                                       label='betonnen trottoirbanden voor mindervaliden',
                                                                       status='ingebruik',
                                                                       definitie='Geprefabriceerde of ter plaatste vervaardigde betonnen trottoirbanden voor minder_validen.',
                                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/betonnen-trottoirbanden-voor-mindervaliden'),
        'betonnen-trottoirbanden-watergreppels': KeuzelijstWaarde(invulwaarde='betonnen-trottoirbanden-watergreppels',
                                                                  label='betonnen trottoirbanden-watergreppels',
                                                                  status='ingebruik',
                                                                  definitie='Geprefabriceerde of ter plaatste vervaardigde betonnen trottoirbanden_watergreppels.',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/betonnen-trottoirbanden-watergreppels'),
        'betonnen-watergreppels': KeuzelijstWaarde(invulwaarde='betonnen-watergreppels',
                                                   label='betonnen watergreppels',
                                                   status='ingebruik',
                                                   definitie='Geprefabriceerde of ter plaatste vervaardigde watergreppels.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/betonnen-watergreppels'),
        'hoekstukken-van-betonnen-trottoirbanden': KeuzelijstWaarde(invulwaarde='hoekstukken-van-betonnen-trottoirbanden',
                                                                    label='hoekstukken van betonnen trottoirbanden',
                                                                    status='ingebruik',
                                                                    definitie='Geprefabriceerde of ter plaatste vervaardigde hoekstukken van betonnen trottoirbanden.',
                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/hoekstukken-van-betonnen-trottoirbanden'),
        'hoekstukken-van-betonnen-trottoirbanden-watergreppels': KeuzelijstWaarde(invulwaarde='hoekstukken-van-betonnen-trottoirbanden-watergreppels',
                                                                                  label='hoekstukken van betonnen trottoirbanden-watergreppels',
                                                                                  status='ingebruik',
                                                                                  definitie='Geprefabriceerde of ter plaatste vervaardigde hoekstukken van betonnen trottoirbanden_watergreppels.',
                                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/hoekstukken-van-betonnen-trottoirbanden-watergreppels'),
        'kantstroken-of-watergreppels-in-betonstraatstenen': KeuzelijstWaarde(invulwaarde='kantstroken-of-watergreppels-in-betonstraatstenen',
                                                                              label='kantstroken of watergreppels in betonstraatstenen',
                                                                              status='ingebruik',
                                                                              definitie='Kantstroken en watergreppels in betonstraatstenen.',
                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/kantstroken-of-watergreppels-in-betonstraatstenen'),
        'trottoirbanden-van-natuursteen': KeuzelijstWaarde(invulwaarde='trottoirbanden-van-natuursteen',
                                                           label='trottoirbanden van natuursteen',
                                                           status='ingebruik',
                                                           definitie='Trottoirbanden van natuursteen.',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/trottoirbanden-van-natuursteen'),
        'watergreppels-in-gietasfalt': KeuzelijstWaarde(invulwaarde='watergreppels-in-gietasfalt',
                                                        label='watergreppels in gietasfalt',
                                                        status='ingebruik',
                                                        definitie='Watergreppels in gietasfalt.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlLEKantopsluitingSoort/watergreppels-in-gietasfalt')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

