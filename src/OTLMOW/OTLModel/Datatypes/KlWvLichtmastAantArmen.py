# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWvLichtmastAantArmen(KeuzelijstField):
    """Aantal armen van de lichtmast."""
    naam = 'KlWvLichtmastAantArmen'
    label = 'WV-mast aantal armen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlWvLichtmastAantArmen'
    definition = 'Aantal armen van de lichtmast.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWvLichtmastAantArmen'
    options = {
        '0': KeuzelijstWaarde(invulwaarde='0',
                              label='0',
                              definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/0'),
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/3'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              definitie="keuzelijst aantal armen aan lichtmast (0-4). Indien lichtmast 'M', 'MS', 'B','BS', 'K' of 'KS' dan 0,1, 2,3 of 4. Anders altijd 0./ CLASS : VPLMAST",
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWvLichtmastAantArmen/4')
    }

