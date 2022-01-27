# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBetrokkenheidRol(KeuzelijstField):
    """Keuzelijst met mogelijke waarden voor de rol waarmee een agent betrokken is bij een object."""
    naam = 'KlBetrokkenheidRol'
    label = 'Betrokkenheid rol'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBetrokkenheidRol'
    definition = 'Keuzelijst met mogelijke waarden voor de rol waarmee een agent betrokken is bij een object.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBetrokkenheidRol'
    options = {
        'beheerder': KeuzelijstWaarde(invulwaarde='beheerder',
                                      label='beheerder',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/beheerder'),
        'berekende-beheerder': KeuzelijstWaarde(invulwaarde='berekende-beheerder',
                                                label='berekende beheerder',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/berekende-beheerder'),
        'eigenaar': KeuzelijstWaarde(invulwaarde='eigenaar',
                                     label='eigenaar',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/eigenaar'),
        'installatieverantwoordelijke': KeuzelijstWaarde(invulwaarde='installatieverantwoordelijke',
                                                         label='Installatieverantwoordelijke',
                                                         definitie='De installatieverantwoordelijke is de persoon, aangeduid door de werkgever, om de verantwoordelijkheid voor de exploitatie van de elektrische installatie op zich te nemen. Indien nodig kan hij die verantwoordelijkheid wel gedeeltelijk op andere personen overdragen. Concreet is hij op de hoogte van de eventuele afwijkende situaties en gaat, in overleg met de werkverantwoordelijke, na of de nodige maatregelen genomen worden om op een veilige manier te werken met een dergelijke installatie.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/installatieverantwoordelijke'),
        'keuringsinstantie': KeuzelijstWaarde(invulwaarde='keuringsinstantie',
                                              label='keuringsinstantie',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/keuringsinstantie'),
        'klant': KeuzelijstWaarde(invulwaarde='klant',
                                  label='klant',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/klant'),
        'leidinggevende': KeuzelijstWaarde(invulwaarde='leidinggevende',
                                           label='leidinggevende',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/leidinggevende'),
        'lid': KeuzelijstWaarde(invulwaarde='lid',
                                label='lid',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/lid'),
        'schadebeheerder': KeuzelijstWaarde(invulwaarde='schadebeheerder',
                                            label='schadebeheerder',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/schadebeheerder'),
        'suborganisatie-van': KeuzelijstWaarde(invulwaarde='suborganisatie-van',
                                               label='suborganisatie van',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/suborganisatie-van'),
        'toezicht-onderhoud': KeuzelijstWaarde(invulwaarde='toezicht-onderhoud',
                                               label='toezicht onderhoud',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezicht-onderhoud'),
        'toezichter': KeuzelijstWaarde(invulwaarde='toezichter',
                                       label='toezichter',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezichter'),
        'toezichtsgroep': KeuzelijstWaarde(invulwaarde='toezichtsgroep',
                                           label='toezichtsgroep',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezichtsgroep'),
        'verantwoordelijke-reiniging': KeuzelijstWaarde(invulwaarde='verantwoordelijke-reiniging',
                                                        label='verantwoordelijke reiniging',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/verantwoordelijke-reiniging')
    }

