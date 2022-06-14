# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVoedingskabelType(KeuzelijstField):
    """Lijst met types voor energie- en installatiekabels volgens de gebruikte materialen zoals opgenomen in het Standaarbestek 270."""
    naam = 'KlVoedingskabelType'
    label = 'Voedingskabel types'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVoedingskabelType'
    definition = 'Lijst met types voor energie- en installatiekabels volgens de gebruikte materialen zoals opgenomen in het Standaarbestek 270.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVoedingskabelType'
    options = {
        'eaxecwb': KeuzelijstWaarde(invulwaarde='eaxecwb',
                                    label='EAXeCWB',
                                    definitie='Monopolaire middenspanningskabels met aluminium geleiders.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/eaxecwb'),
        'eaxevb': KeuzelijstWaarde(invulwaarde='eaxevb',
                                   label='EAXeVB',
                                   definitie='Niet-gewapende energiekabels met aluminium geleiders voor buiten en ondergronds gebruik.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/eaxevb'),
        'emggb-f2': KeuzelijstWaarde(invulwaarde='emggb-f2',
                                     label='EmGGB-F2',
                                     definitie='Halogeenvrije energiekabels met functiebehoud Rf1,5h.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/emggb-f2'),
        'emxgb-f2': KeuzelijstWaarde(invulwaarde='emxgb-f2',
                                     label='EmXGB-F2',
                                     definitie='Halogeenvrije energiekabels met functiebehoud Rf1h.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/emxgb-f2'),
        'exavb': KeuzelijstWaarde(invulwaarde='exavb',
                                  label='EXAVB',
                                  definitie='Gewapende energiekabels met koperen geleiders voor binnen, buiten en ondergronds gebruik.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/exavb'),
        'execvb': KeuzelijstWaarde(invulwaarde='execvb',
                                   label='EXeCVB',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/execvb'),
        'exvb': KeuzelijstWaarde(invulwaarde='exvb',
                                 label='EXVB',
                                 definitie='Niet-gewapende energiekabels met koperen geleiders voor buiten en ondergronds gebruik.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/exvb'),
        'h07-rn-f': KeuzelijstWaarde(invulwaarde='h07-rn-f',
                                     label='H07 RN-F',
                                     definitie='Flexibele energiekabel (snoer).',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-rn-f'),
        'h07-v-k': KeuzelijstWaarde(invulwaarde='h07-v-k',
                                    label='H07 V-K',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-v-k'),
        'h07-v-r': KeuzelijstWaarde(invulwaarde='h07-v-r',
                                    label='H07 V-R',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-v-r'),
        'h07-v-u': KeuzelijstWaarde(invulwaarde='h07-v-u',
                                    label='H07 V-U',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-v-u'),
        'h07-z1-k': KeuzelijstWaarde(invulwaarde='h07-z1-k',
                                     label='H07 Z1-K',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-z1-k'),
        'h07-z1-r': KeuzelijstWaarde(invulwaarde='h07-z1-r',
                                     label='H07 Z1-R',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-z1-r'),
        'j-h(st)h': KeuzelijstWaarde(invulwaarde='j-h(st)h',
                                     label='J-H(St)H',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/j-h(st)h'),
        'lixy(cub)cy': KeuzelijstWaarde(invulwaarde='lixy(cub)cy',
                                        label='LiXY(Cub)CY',
                                        definitie='Installatiekabel voor frequentiesturingen.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/lixy(cub)cy'),
        'svavb': KeuzelijstWaarde(invulwaarde='svavb',
                                  label='SVAVB',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/svavb'),
        'svv': KeuzelijstWaarde(invulwaarde='svv',
                                label='SVV',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/svv'),
        'sxavb': KeuzelijstWaarde(invulwaarde='sxavb',
                                  label='SXAVB',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/sxavb'),
        'twavb': KeuzelijstWaarde(invulwaarde='twavb',
                                  label='TWAVB',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/twavb'),
        'xfgb': KeuzelijstWaarde(invulwaarde='xfgb',
                                 label='XFGB',
                                 definitie='Halogeenvrije installatiekabels met metalen bescherming voor binnen.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/xfgb'),
        'xfvb': KeuzelijstWaarde(invulwaarde='xfvb',
                                 label='XFVB',
                                 definitie='Installatiekabels met metalen bescherming voor binnen en buiten.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/xfvb'),
        'xgb': KeuzelijstWaarde(invulwaarde='xgb',
                                label='XGB',
                                definitie='Halogeenvrije installatiekabels voor binnen.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/xgb'),
        'xvb': KeuzelijstWaarde(invulwaarde='xvb',
                                label='XVB',
                                definitie='Installatiekabels voor binnen en buiten.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/xvb')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVoedingskabelType.get_dummy_data()

