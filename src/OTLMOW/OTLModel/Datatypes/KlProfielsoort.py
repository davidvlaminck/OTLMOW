# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlProfielsoort(KeuzelijstField):
    """Het type profiel (de meest genormeerde types)."""
    naam = 'KlProfielsoort'
    label = 'Profielsoort'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlProfielsoort'
    definition = 'Het type profiel (de meest genormeerde types).'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlProfielsoort'
    options = {
        'hd': KeuzelijstWaarde(invulwaarde='hd',
                               label='HD',
                               definitie='Breedflensprofiel : een HD-profiel heeft dikkere flenzen en lijf. Dit profiel is speciaal voor kolommen.',
                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hd'),
        'hea': KeuzelijstWaarde(invulwaarde='hea',
                                label='HEA',
                                definitie='Meest voorkomende breedflensprofiel (een profiel met brede evenwijdige flenzen).',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hea'),
        'heb': KeuzelijstWaarde(invulwaarde='heb',
                                label='HEB',
                                definitie='Meest voorkomende breedflensprofiel (een profiel met brede evenwijdige flenzen). Het HEB-profiel heeft meer draagkracht dan het HEA-profiel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/heb'),
        'hem': KeuzelijstWaarde(invulwaarde='hem',
                                label='HEM',
                                definitie='Breedflensprofiel : een HEM-profiel heeft dikkere flenzen en lijf dan HEA- en HEB-profielen.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hem'),
        'hp-bulbstaal': KeuzelijstWaarde(invulwaarde='hp-bulbstaal',
                                         label='HP (bulbstaal)',
                                         definitie='Een massief profiel : Hollandprofiel (afgekort HP).',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/hp-bulbstaal'),
        'ipe': KeuzelijstWaarde(invulwaarde='ipe',
                                label='IPE',
                                definitie='Een IPE-profiel (I Profiel Europees) heeft betrekkelijk korte, evenwijdige flenzen met een constante dikte.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/ipe'),
        'ipn': KeuzelijstWaarde(invulwaarde='ipn',
                                label='IPN',
                                definitie='Een IPN-profiel (I Normaal Profiel, ook wel INP genoemd) heeft iets schuinere flenzen dan een IPE-profiel.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/ipn'),
        'upe': KeuzelijstWaarde(invulwaarde='upe',
                                label='UPE',
                                definitie='U-vormig profiel. Een UPE-profiel heeft rechte flenzen die overal even dik zijn en dikker zijn dan het lijf.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/upe'),
        'upn': KeuzelijstWaarde(invulwaarde='upn',
                                label='UPN',
                                definitie='Het meest gebruikte U-vormig profiel. Een UPN-profiel (U Normaal Profiel, ook wel UNP genoemd) heeft schuine flenzen.',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlProfielsoort/upn')
    }

