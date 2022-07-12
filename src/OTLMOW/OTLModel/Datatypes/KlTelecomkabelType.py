# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlTelecomkabelType(KeuzelijstField):
    """Lijst van types voor datakabels en telefoniekabels volgens hun constructieve kenmerken."""
    naam = 'KlTelecomkabelType'
    label = 'Telecom- en datakabel types'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlTelecomkabelType'
    definition = 'Lijst van types voor datakabels en telefoniekabels volgens hun constructieve kenmerken.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlTelecomkabelType'
    options = {
        'alu-pet': KeuzelijstWaarde(invulwaarde='alu-pet',
                                    label='Alu/PET',
                                    status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                    definitie='Telecom koper kabels waarvan de geleiders ge&#239;soleerd zijn door plastic met daarrond een omhulsel van aluminium en PET.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/alu-pet'),
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Elk types telecommunicatie- of datakabel dat niet opgenomen is in het Standaardbestek 270 en waarover een akkoord bestaat dat die mag gebruikt worden.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/andere'),
        'app': KeuzelijstWaarde(invulwaarde='app',
                                label='APP',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='Papier-lood ge&#239;soleerde telecom koper kabels. Zogenaamde Armee Papier Plomb geleiders, ge&#239;soleerd door papier met daarrond een loden mantel en daarrond bewapening.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/app'),
        'app-pe': KeuzelijstWaarde(invulwaarde='app-pe',
                                   label='APP/PE',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/app-pe'),
        'appj': KeuzelijstWaarde(invulwaarde='appj',
                                 label='APPj',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Papier-lood ge&#239;soleerde telecom koper kabels met een omhulsel in jute. ',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/appj'),
        'j-h(st)h-bd': KeuzelijstWaarde(invulwaarde='j-h(st)h-bd',
                                        label='J-H(St)H-BD',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='Halogeenvrije telefoniekabel.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/j-h(st)h-bd'),
        'je-h(st)h-rf-1h': KeuzelijstWaarde(invulwaarde='je-h(st)h-rf-1h',
                                            label='JE-H(St)H Rf 1h',
                                            status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            definitie='Telefoniekabel met functiebehoud.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/je-h(st)h-rf-1h'),
        'mok': KeuzelijstWaarde(invulwaarde='mok',
                                label='MOK',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='MOnomode optische Kabel, voor gebruik in volle grond of blaasbuis.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/mok'),
        'mok-micro': KeuzelijstWaarde(invulwaarde='mok-micro',
                                      label='MOK micro',
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      definitie='MOnomode optische MICROKabel voor aanleg in microtubes.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/mok-micro'),
        'muk': KeuzelijstWaarde(invulwaarde='muk',
                                label='MUK',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                definitie='MUltimode optische Kabel, voor gebruik in volle grond of blaasbuis.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/muk'),
        'pepy': KeuzelijstWaarde(invulwaarde='pepy',
                                 label='PePy',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Telecom koper kabels waarvan de geleiders ge&#239;soleerd zijn door plastic (pe) omhuld door bescherming in Py zonder bewapening.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/pepy'),
        'rg11': KeuzelijstWaarde(invulwaarde='rg11',
                                 label='RG11',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='RG 11 Coaxkabel.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/rg11'),
        'rg12': KeuzelijstWaarde(invulwaarde='rg12',
                                 label='RG12',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='RG 12 Coaxkabel.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/rg12'),
        'rg59': KeuzelijstWaarde(invulwaarde='rg59',
                                 label='RG59',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='RG 59 Coaxkabel.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/rg59'),
        'rg6a': KeuzelijstWaarde(invulwaarde='rg6a',
                                 label='RG6A',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='RG 6 Coaxkabel.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/rg6a'),
        'rtt-34': KeuzelijstWaarde(invulwaarde='rtt-34',
                                   label='RTT-34',
                                   status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                   definitie='Oude RRT-kabels.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/rtt-34'),
        'teletransmissiekabel-uit-kwarten': KeuzelijstWaarde(invulwaarde='teletransmissiekabel-uit-kwarten',
                                                             label='teletransmissiekabel uit kwarten',
                                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                             definitie='Gevulde kabels met dampscherm en bepantsering van staalband en thermoplastische buitenmantel. Alle kabels voldoen aan EN 60811 testnormen en aan de recentste specificaties van Belgacom en ze behoren tot de reeks 831.',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/teletransmissiekabel-uit-kwarten'),
        'tpgf': KeuzelijstWaarde(invulwaarde='tpgf',
                                 label='TPGF',
                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                 definitie='Halogeenvrije telefoniekabel met enkel afgeschermde paren voor binnen.',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/tpgf'),
        'twavb': KeuzelijstWaarde(invulwaarde='twavb',
                                  label='TWAVB',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  definitie='Gewapende telefoniekabel voor buiten en ondergronds gebruik.',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlTelecomkabelType/twavb')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlTelecomkabelType.get_dummy_data()

