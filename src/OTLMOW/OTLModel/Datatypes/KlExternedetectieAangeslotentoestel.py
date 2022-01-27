# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlExternedetectieAangeslotentoestel(KeuzelijstField):
    """Keuzelijst met de voorkomende types van aangesloten toestellen (trein, brug, FCD) aan een externe detectie."""
    naam = 'KlExternedetectieAangeslotentoestel'
    label = 'Externedetectie aangeslotentoestel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlExternedetectieAangeslotentoestel'
    definition = 'Keuzelijst met de voorkomende types van aangesloten toestellen (trein, brug, FCD) aan een externe detectie.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlExternedetectieAangeslotentoestel'
    options = {
        'MIVB': KeuzelijstWaarde(invulwaarde='MIVB',
                                 label='MIVB',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/MIVB'),
        'brug': KeuzelijstWaarde(invulwaarde='brug',
                                 label='brug',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/brug'),
        'de-Lijn': KeuzelijstWaarde(invulwaarde='de-Lijn',
                                    label='de Lijn',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/de-Lijn'),
        'hulpdiensten': KeuzelijstWaarde(invulwaarde='hulpdiensten',
                                         label='hulpdiensten',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/hulpdiensten'),
        'luchthaven': KeuzelijstWaarde(invulwaarde='luchthaven',
                                       label='luchthaven',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/luchthaven'),
        'militaire-kazerne': KeuzelijstWaarde(invulwaarde='militaire-kazerne',
                                              label='militaire kazerne',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/militaire-kazerne'),
        'spoorweg': KeuzelijstWaarde(invulwaarde='spoorweg',
                                     label='spoorweg',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/spoorweg'),
        'tunnel': KeuzelijstWaarde(invulwaarde='tunnel',
                                   label='tunnel',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/tunnel')
    }

