# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVoedingskabelTypeSpecificatie(KeuzelijstField):
    """Lijst met mogelijke specificaties van het type van de voedingskabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
    naam = 'KlVoedingskabelTypeSpecificatie'
    label = 'Voedingskabel type specificatie'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVoedingskabelTypeSpecificatie'
    definition = 'Lijst met mogelijke specificaties van het type van de voedingskabel volgens een vaste lijst om bv. de brandklasse mee te geven.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVoedingskabelTypeSpecificatie'
    options = {
        'cca': KeuzelijstWaarde(invulwaarde='cca',
                                label='Cca',
                                status='ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca'),
        'cca-a1': KeuzelijstWaarde(invulwaarde='cca-a1',
                                   label='Cca-a1',
                                   status='ingebruik',
                                   definitie='Halogeenvrije installatiekabels voor binnen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca-a1'),
        'cca-a3': KeuzelijstWaarde(invulwaarde='cca-a3',
                                   label='Cca-a3',
                                   status='ingebruik',
                                   definitie='Installatiekabels voor binnen en buiten.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca-a3'),
        'cca-a3-d2-s3': KeuzelijstWaarde(invulwaarde='cca-a3-d2-s3',
                                         label='Cca-a3 d2 s3',
                                         status='ingebruik',
                                         definitie='Gewapende energiekabels met koperen geleiders voor binnen, buiten en ondergronds gebruik.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca-a3-d2-s3'),
        'cca-d2': KeuzelijstWaarde(invulwaarde='cca-d2',
                                   label='Cca-d2',
                                   status='ingebruik',
                                   definitie='Installatiekabels voor binnen en buiten.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca-d2'),
        'cca-s1': KeuzelijstWaarde(invulwaarde='cca-s1',
                                   label='Cca-s1',
                                   status='ingebruik',
                                   definitie='Halogeenvrije installatiekabels voor binnen.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca-s1'),
        'cca-s1-d2-a1': KeuzelijstWaarde(invulwaarde='cca-s1-d2-a1',
                                         label='Cca-s1 d2 a1',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca-s1-d2-a1'),
        'cca-s1-d2-a2': KeuzelijstWaarde(invulwaarde='cca-s1-d2-a2',
                                         label='Cca-s1 d2 a2',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca-s1-d2-a2'),
        'cca-s1-d2-a3': KeuzelijstWaarde(invulwaarde='cca-s1-d2-a3',
                                         label='Cca-s1 d2 a3',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca-s1-d2-a3'),
        'cca-s3': KeuzelijstWaarde(invulwaarde='cca-s3',
                                   label='Cca-s3',
                                   status='ingebruik',
                                   definitie='Installatiekabels voor binnen en buiten.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca-s3'),
        'cca-s3-d2-a3': KeuzelijstWaarde(invulwaarde='cca-s3-d2-a3',
                                         label='Cca-s3 d2 a3',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/cca-s3-d2-a3'),
        'eca': KeuzelijstWaarde(invulwaarde='eca',
                                label='Eca',
                                status='ingebruik',
                                definitie='Niet-gewapende energiekabels met aluminium geleiders voor buiten en ondergronds gebruik.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/eca'),
        'rf1.5h': KeuzelijstWaarde(invulwaarde='rf1.5h',
                                   label='Rf1.5h',
                                   status='ingebruik',
                                   definitie='Halogeenvrije energiekabels met functiebehoud Rf1,5h.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/rf1.5h'),
        'rf1h': KeuzelijstWaarde(invulwaarde='rf1h',
                                 label='Rf1h',
                                 status='ingebruik',
                                 definitie='Halogeenvrije energiekabels met functiebehoud Rf1h.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelTypeSpecificatie/rf1h')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

