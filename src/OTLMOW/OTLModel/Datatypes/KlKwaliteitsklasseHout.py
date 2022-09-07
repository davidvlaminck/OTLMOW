# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlKwaliteitsklasseHout(KeuzelijstField):
    """De kwaliteitsindeling van hout met betrekking op vervormingen, scheuren en kwasten."""
    naam = 'KlKwaliteitsklasseHout'
    label = 'Kwaliteitsklasse van hout'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlKwaliteitsklasseHout'
    definition = 'De kwaliteitsindeling van hout met betrekking op vervormingen, scheuren en kwasten.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlKwaliteitsklasseHout'
    options = {
        'klasse-a': KeuzelijstWaarde(invulwaarde='klasse-a',
                                     label='Klasse A',
                                     status='ingebruik',
                                     definitie='De hoogste kwaliteitsklasse die uitsluitend bedoeld is voor toepassingen waarbij zeer hoge eisen aan het uiterlijk worden gesteld. Dit hout gevat geen holtes of oneffenheden en is tevens onbehandeld.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKwaliteitsklasseHout/klasse-a'),
        'klasse-b': KeuzelijstWaarde(invulwaarde='klasse-b',
                                     label='Klasse B',
                                     status='ingebruik',
                                     definitie='Hout dat zowel sterk is als er goed uitziet met weinig knoesten en geen hart. Het is afkomstig uit Noord- Europa en wordt ook bestempeld als constructiehout. Klasse B-hout is van lagere kwaliteit dan A-hout en kan niet worden hergebruikt. Als er een afwerklaag wordt aangebracht en onderhouden, heeft het hout een kwaliteitsklasse B.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKwaliteitsklasseHout/klasse-b'),
        'klasse-c': KeuzelijstWaarde(invulwaarde='klasse-c',
                                     label='Klasse C',
                                     status='ingebruik',
                                     definitie='Klasse C-hout geldt als standaard en is voornamelijk afkomstig uit Noord-Europa, waar de bomen in duurzame bossen geteeld worden. Gezonde knoesten zijn toegestaan, evenals een beetje hart. Dit hout is van lagere kwaliteit dan A-hout en kan niet worden hergebruikt. Klasse C houdt ook in dat het hout geïmpregneerd is.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKwaliteitsklasseHout/klasse-c'),
        'tropisch-hardhout': KeuzelijstWaarde(invulwaarde='tropisch-hardhout',
                                              label='Tropisch hardhout',
                                              status='ingebruik',
                                              definitie='Zwaardere houtsoorten uit de tropen, zoals vb.: azobé (afkomstig uit tropische bossen in Afrika).',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlKwaliteitsklasseHout/tropisch-hardhout')
    }

    @classmethod
    def create_dummy_data(cls):
        return random.choice(list(map(lambda x: x.invulwaarde,
                                      filter(lambda option: option.status == 'ingebruik', cls.options.values()))))

