# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLichtmastBevsToestel(KeuzelijstField):
    """De standaard bevestigingen van verlichtingstoestellen aan lichtmasten."""
    naam = 'KlWvLichtmastBevsToestel'
    label = 'Bevestiging voor wegverlichtingstoestellen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastBevsToestel'
    definition = 'De standaard bevestigingen van verlichtingstoestellen aan lichtmasten.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastBevsToestel'
    options = {
        'kroon': KeuzelijstWaarde(invulwaarde='kroon',
                                  label='kroon',
                                  definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/kroon'),
        'mediaanbalk-H': KeuzelijstWaarde(invulwaarde='mediaanbalk-H',
                                          label='mediaanbalk H',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-H'),
        'mediaanbalk-I': KeuzelijstWaarde(invulwaarde='mediaanbalk-I',
                                          label='mediaanbalk I',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-I'),
        'mediaanbalk-U': KeuzelijstWaarde(invulwaarde='mediaanbalk-U',
                                          label='mediaanbalk U',
                                          definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/mediaanbalk-U'),
        'ossenkop': KeuzelijstWaarde(invulwaarde='ossenkop',
                                     label='ossenkop',
                                     definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/ossenkop'),
        'paaltop-108mm': KeuzelijstWaarde(invulwaarde='paaltop-108mm',
                                          label='paaltop 108mm',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-108mm'),
        'paaltop-60mm': KeuzelijstWaarde(invulwaarde='paaltop-60mm',
                                         label='paaltop 60mm',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-60mm'),
        'paaltop-76mm': KeuzelijstWaarde(invulwaarde='paaltop-76mm',
                                         label='paaltop 76mm',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/paaltop-76mm'),
        'plaat': KeuzelijstWaarde(invulwaarde='plaat',
                                  label='plaat',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/plaat'),
        't-stuk': KeuzelijstWaarde(invulwaarde='t-stuk',
                                   label='t-stuk',
                                   definitie='keuzelijst (Niet van toepassing, T-stuk, Mediaanbalk I, Mediaanbalk U, Mediaanbalk H, Ossenkop, Kroon, Andere)./ CLASS : VPLMAST',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastBevsToestel/t-stuk')
    }

