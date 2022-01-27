# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVormTerugslagklep(KeuzelijstField):
    """De vorm van opening van de terugslagklep."""
    naam = 'KlVormTerugslagklep'
    label = 'Vorm terugslagklep'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVormTerugslagklep'
    definition = 'De vorm van opening van de terugslagklep.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVormTerugslagklep'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   definitie='andere',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/andere'),
        'circkelvormig': KeuzelijstWaarde(invulwaarde='circkelvormig',
                                          label='circkelvormig',
                                          definitie='circkelvormig',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/circkelvormig'),
        'rechthoekig': KeuzelijstWaarde(invulwaarde='rechthoekig',
                                        label='rechthoekig',
                                        definitie='rechthoekig',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVormTerugslagklep/rechthoekig')
    }

