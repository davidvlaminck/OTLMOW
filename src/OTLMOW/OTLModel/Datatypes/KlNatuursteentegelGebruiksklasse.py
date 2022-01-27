# coding=utf-8
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlNatuursteentegelGebruiksklasse(KeuzelijstField):
    """Mogelijke waarden voor de gebruiksklasse, vorm en afwerking van de natuursteentegel."""
    naam = 'KlNatuursteentegelGebruiksklasse'
    label = 'Natuursteentegel gebruiksklasse'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlNatuursteentegelGebruiksklasse'
    definition = 'Mogelijke waarden voor de gebruiksklasse, vorm en afwerking van de natuursteentegel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlNatuursteentegelGebruiksklasse'
    options = {
        '0': KeuzelijstWaarde(invulwaarde='0',
                              label='0',
                              definitie='Keuzeoptie decoratie als gebruiksklasse van natuursteentegels.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/0'),
        '1': KeuzelijstWaarde(invulwaarde='1',
                              label='1',
                              definitie='Keuzeoptie voetgangerszones als gebruiksklasse van natuursteentegels.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/1'),
        '2': KeuzelijstWaarde(invulwaarde='2',
                              label='2',
                              definitie='Keuzeoptie voetgangers- en fietszones als gebruiksklasse van natuursteentegels.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/2'),
        '3': KeuzelijstWaarde(invulwaarde='3',
                              label='3',
                              definitie='Keuzeoptie voetgangerszones, occasioneel belast door wagens en lichte voertuigen, inritten van garages als gebruiksklasse van natuursteentegels.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/3'),
        '4': KeuzelijstWaarde(invulwaarde='4',
                              label='4',
                              definitie='Keuzeoptie voetgangerszones en marktplaatsen, occasioneel belast voor leveringen en door hulpdiensten als gebruiksklasse van natuursteentegels.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/4'),
        '5': KeuzelijstWaarde(invulwaarde='5',
                              label='5',
                              definitie='Keuzeoptie voetgangerszones, regelmatig belast door zwaar verkeer als gebruiksklasse van natuursteentegels.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/5'),
        '6': KeuzelijstWaarde(invulwaarde='6',
                              label='6',
                              definitie='Keuzeoptie wegen als gebruiksklasse van natuursteentegels.',
                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNatuursteentegelGebruiksklasse/6')
    }

