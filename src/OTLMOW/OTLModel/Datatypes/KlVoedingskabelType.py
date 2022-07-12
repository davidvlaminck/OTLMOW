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
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Monopolaire middenspanningskabels met aluminium geleiders.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/eaxecwb'),
        'eaxevb': KeuzelijstWaarde(invulwaarde='eaxevb',
                                   label='EAXeVB',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Niet-gewapende energiekabels met aluminium geleiders voor buiten en ondergronds gebruik.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/eaxevb'),
        'emggb-f2': KeuzelijstWaarde(invulwaarde='emggb-f2',
                                     label='EmGGB-F2',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Halogeenvrije energiekabels met functiebehoud Rf1,5h.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/emggb-f2'),
        'emxgb-f2': KeuzelijstWaarde(invulwaarde='emxgb-f2',
                                     label='EmXGB-F2',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Halogeenvrije energiekabels met functiebehoud Rf1h.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/emxgb-f2'),
        'exavb': KeuzelijstWaarde(invulwaarde='exavb',
                                  label='EXAVB',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Gewapende energiekabels met koperen geleiders voor binnen, buiten en ondergronds gebruik.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/exavb'),
        'execvb': KeuzelijstWaarde(invulwaarde='execvb',
                                   label='EXeCVB',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/execvb'),
        'exvb': KeuzelijstWaarde(invulwaarde='exvb',
                                 label='EXVB',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Niet-gewapende energiekabels met koperen geleiders voor buiten en ondergronds gebruik.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/exvb'),
        'h07-rn-f': KeuzelijstWaarde(invulwaarde='h07-rn-f',
                                     label='H07 RN-F',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Flexibele energiekabel (snoer).',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-rn-f'),
        'h07-v-k': KeuzelijstWaarde(invulwaarde='h07-v-k',
                                    label='H07 V-K',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-v-k'),
        'h07-v-r': KeuzelijstWaarde(invulwaarde='h07-v-r',
                                    label='H07 V-R',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-v-r'),
        'h07-v-u': KeuzelijstWaarde(invulwaarde='h07-v-u',
                                    label='H07 V-U',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-v-u'),
        'h07-z1-k': KeuzelijstWaarde(invulwaarde='h07-z1-k',
                                     label='H07 Z1-K',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-z1-k'),
        'h07-z1-r': KeuzelijstWaarde(invulwaarde='h07-z1-r',
                                     label='H07 Z1-R',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/h07-z1-r'),
        'j-h(st)h': KeuzelijstWaarde(invulwaarde='j-h(st)h',
                                     label='J-H(St)H',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/j-h(st)h'),
        'lixy(cub)cy': KeuzelijstWaarde(invulwaarde='lixy(cub)cy',
                                        label='LiXY(Cub)CY',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Installatiekabel voor frequentiesturingen.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/lixy(cub)cy'),
        'svavb': KeuzelijstWaarde(invulwaarde='svavb',
                                  label='SVAVB',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/svavb'),
        'svv': KeuzelijstWaarde(invulwaarde='svv',
                                label='SVV',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/svv'),
        'sxavb': KeuzelijstWaarde(invulwaarde='sxavb',
                                  label='SXAVB',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/sxavb'),
        'twavb': KeuzelijstWaarde(invulwaarde='twavb',
                                  label='TWAVB',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/twavb'),
        'xfgb': KeuzelijstWaarde(invulwaarde='xfgb',
                                 label='XFGB',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Halogeenvrije installatiekabels met metalen bescherming voor binnen.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/xfgb'),
        'xfvb': KeuzelijstWaarde(invulwaarde='xfvb',
                                 label='XFVB',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Installatiekabels met metalen bescherming voor binnen en buiten.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/xfvb'),
        'xgb': KeuzelijstWaarde(invulwaarde='xgb',
                                label='XGB',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Halogeenvrije installatiekabels voor binnen.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/xgb'),
        'xvb': KeuzelijstWaarde(invulwaarde='xvb',
                                label='XVB',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Installatiekabels voor binnen en buiten.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVoedingskabelType/xvb')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlVoedingskabelType.get_dummy_data()

