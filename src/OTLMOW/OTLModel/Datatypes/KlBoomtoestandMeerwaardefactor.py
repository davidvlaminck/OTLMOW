# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomtoestandMeerwaardefactor(KeuzelijstField):
    """De meerwaarde (ecologisch,erfgoed) van de boom."""
    naam = 'KlBoomtoestandMeerwaardefactor'
    label = 'Boomtoestand meerwaardefactor'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomtoestandMeerwaardefactor'
    definition = 'De meerwaarde (ecologisch,erfgoed) van de boom.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomtoestandMeerwaardefactor'
    options = {
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              definitie='De boom heeft geen of minder dan 3 specifieke kenmerken die de ecologische en/of erfgoedwaarde verhogen.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/1'),
        '15': KeuzelijstWaarde(invulwaarde='15',
                               label='15',
                               definitie='De boom heeft minstens 3 kenmerken van ecologische waarde EN/OF erfgoedwaarde OF boom is opgenomen in de Vlaamse wetenschappelijke erfgoedinventaris',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/15'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              definitie='De boom heeft minstens 4 kenmerken van ecologische EN/OF erfgoedwaarde OF de boom heeft minstens 2 kenmerken van ecologische waarde in combinatie met 1 kenmerk van zeer hoge ecologische waarde; OF de boom maakt deel uit van een (ruimere) bescherming als monument, cultuurhistorisch landschap of stads- en dorpsgezicht',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/2'),
        '25': KeuzelijstWaarde(invulwaarde='25',
                               label='25',
                               definitie='De boom is individueel beschermd als monument',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomtoestandMeerwaardefactor/25')
    }

