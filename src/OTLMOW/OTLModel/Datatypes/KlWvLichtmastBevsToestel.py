# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLichtmastBevsToestel(KeuzelijstField):
    """De standaard bevestigingen van verlichtingstoestellen aan lichtmasten."""
    naam = 'KlWvLichtmastBevsToestel'
    label = 'Bevestiging voor wegverlichtingstoestellen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastBevsToestel'
    definition = 'De standaard bevestigingen van verlichtingstoestellen aan lichtmasten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastBevsToestel'
    options = {
        'arm-60mm': KeuzelijstWaarde(invulwaarde='arm-60mm',
                                     label='arm 60mm',
                                     status='ingebruik',
                                     definitie='arm 60mm',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/arm-60mm'),
        'kroon': KeuzelijstWaarde(invulwaarde='kroon',
                                  label='kroon',
                                  status='ingebruik',
                                  definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/kroon'),
        'mediaanbalk-H': KeuzelijstWaarde(invulwaarde='mediaanbalk-H',
                                          label='mediaanbalk H',
                                          status='ingebruik',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-H'),
        'mediaanbalk-I': KeuzelijstWaarde(invulwaarde='mediaanbalk-I',
                                          label='mediaanbalk I',
                                          status='ingebruik',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-I'),
        'mediaanbalk-U': KeuzelijstWaarde(invulwaarde='mediaanbalk-U',
                                          label='mediaanbalk U',
                                          status='ingebruik',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-U'),
        'ossenkop': KeuzelijstWaarde(invulwaarde='ossenkop',
                                     label='ossenkop',
                                     status='ingebruik',
                                     definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/ossenkop'),
        'paaltop-108mm': KeuzelijstWaarde(invulwaarde='paaltop-108mm',
                                          label='paaltop 108mm',
                                          status='ingebruik',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-108mm'),
        'paaltop-60mm': KeuzelijstWaarde(invulwaarde='paaltop-60mm',
                                         label='paaltop 60mm',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-60mm'),
        'paaltop-76mm': KeuzelijstWaarde(invulwaarde='paaltop-76mm',
                                         label='paaltop 76mm',
                                         status='ingebruik',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-76mm'),
        'plaat': KeuzelijstWaarde(invulwaarde='plaat',
                                  label='plaat',
                                  status='ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/plaat'),
        't-stuk': KeuzelijstWaarde(invulwaarde='t-stuk',
                                   label='t-stuk',
                                   status='ingebruik',
                                   definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/t-stuk')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

