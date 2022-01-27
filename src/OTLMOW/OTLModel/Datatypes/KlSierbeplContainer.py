# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlSierbeplContainer(KeuzelijstField):
    """Verschillende mogeliike pot- en containermaten voor de sierbeplanting."""
    naam = 'KlSierbeplContainer'
    label = 'Sierbeplanting container'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlSierbeplContainer'
    definition = 'Verschillende mogeliike pot- en containermaten voor de sierbeplanting.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlSierbeplContainer'
    options = {
        'C10': KeuzelijstWaarde(invulwaarde='C10',
                                label='C10',
                                definitie='C10',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/C10'),
        'C5': KeuzelijstWaarde(invulwaarde='C5',
                               label='C5',
                               definitie='C5',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/C5'),
        'C7.5': KeuzelijstWaarde(invulwaarde='C7.5',
                                 label='C7.5',
                                 definitie='C7,5',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/C7.5'),
        'P10.5-C1': KeuzelijstWaarde(invulwaarde='P10.5-C1',
                                     label='P10.5-C1',
                                     definitie='P10,5/C1',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P10.5-C1'),
        'P13-C1.2': KeuzelijstWaarde(invulwaarde='P13-C1.2',
                                     label='P13-C1.2',
                                     definitie='P13/C1,2',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P13-C1.2'),
        'P14-C1.5': KeuzelijstWaarde(invulwaarde='P14-C1.5',
                                     label='P14-C1.5',
                                     definitie='P14/C1,5',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P14-C1.5'),
        'P15-C2': KeuzelijstWaarde(invulwaarde='P15-C2',
                                   label='P15-C2',
                                   definitie='P15/C2',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P15-C2'),
        'P17-C3': KeuzelijstWaarde(invulwaarde='P17-C3',
                                   label='P17-C3',
                                   definitie='P17/C3',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P17-C3'),
        'P19-C4': KeuzelijstWaarde(invulwaarde='P19-C4',
                                   label='P19-C4',
                                   definitie='P19/C4',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P19-C4'),
        'P7': KeuzelijstWaarde(invulwaarde='P7',
                               label='P7',
                               definitie='P7',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P7'),
        'P9': KeuzelijstWaarde(invulwaarde='P9',
                               label='P9',
                               definitie='P9',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlSierbeplContainer/P9')
    }

