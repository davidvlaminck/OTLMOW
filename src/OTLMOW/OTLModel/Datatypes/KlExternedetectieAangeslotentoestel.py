# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlExternedetectieAangeslotentoestel(KeuzelijstField):
    """Keuzelijst met de voorkomende types van aangesloten toestellen (trein, brug, FCD) aan een externe detectie."""
    naam = 'KlExternedetectieAangeslotentoestel'
    label = 'Externedetectie aangeslotentoestel'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlExternedetectieAangeslotentoestel'
    definition = 'Keuzelijst met de voorkomende types van aangesloten toestellen (trein, brug, FCD) aan een externe detectie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlExternedetectieAangeslotentoestel'
    options = {
        'MIVB': KeuzelijstWaarde(invulwaarde='MIVB',
                                 label='MIVB',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/MIVB'),
        'brug': KeuzelijstWaarde(invulwaarde='brug',
                                 label='brug',
                                 status='ingebruik',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/brug'),
        'de-Lijn': KeuzelijstWaarde(invulwaarde='de-Lijn',
                                    label='de Lijn',
                                    status='ingebruik',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/de-Lijn'),
        'hulpdiensten': KeuzelijstWaarde(invulwaarde='hulpdiensten',
                                         label='hulpdiensten',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/hulpdiensten'),
        'luchthaven': KeuzelijstWaarde(invulwaarde='luchthaven',
                                       label='luchthaven',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/luchthaven'),
        'militaire-kazerne': KeuzelijstWaarde(invulwaarde='militaire-kazerne',
                                              label='militaire kazerne',
                                              status='ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/militaire-kazerne'),
        'spoorweg': KeuzelijstWaarde(invulwaarde='spoorweg',
                                     label='spoorweg',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/spoorweg'),
        'tunnel': KeuzelijstWaarde(invulwaarde='tunnel',
                                   label='tunnel',
                                   status='ingebruik',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlExternedetectieAangeslotentoestel/tunnel')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

