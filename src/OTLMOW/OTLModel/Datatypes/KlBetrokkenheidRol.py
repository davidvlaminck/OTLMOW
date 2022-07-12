# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


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
                                      status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/beheerder'),
        'berekende-beheerder': KeuzelijstWaarde(invulwaarde='berekende-beheerder',
                                                label='berekende beheerder',
                                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/berekende-beheerder'),
        'eigenaar': KeuzelijstWaarde(invulwaarde='eigenaar',
                                     label='eigenaar',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/eigenaar'),
        'installatieverantwoordelijke': KeuzelijstWaarde(invulwaarde='installatieverantwoordelijke',
                                                         label='Installatieverantwoordelijke',
                                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                         definitie='De installatieverantwoordelijke is de persoon, aangeduid door de werkgever, om de verantwoordelijkheid voor de exploitatie van de elektrische installatie op zich te nemen. Indien nodig kan hij die verantwoordelijkheid wel gedeeltelijk op andere personen overdragen. Concreet is hij op de hoogte van de eventuele afwijkende situaties en gaat, in overleg met de werkverantwoordelijke, na of de nodige maatregelen genomen worden om op een veilige manier te werken met een dergelijke installatie.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/installatieverantwoordelijke'),
        'keuringsinstantie': KeuzelijstWaarde(invulwaarde='keuringsinstantie',
                                              label='keuringsinstantie',
                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/keuringsinstantie'),
        'klant': KeuzelijstWaarde(invulwaarde='klant',
                                  label='klant',
                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/klant'),
        'leidinggevende': KeuzelijstWaarde(invulwaarde='leidinggevende',
                                           label='leidinggevende',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/leidinggevende'),
        'lid': KeuzelijstWaarde(invulwaarde='lid',
                                label='lid',
                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/lid'),
        'schadebeheerder': KeuzelijstWaarde(invulwaarde='schadebeheerder',
                                            label='schadebeheerder',
                                            status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/schadebeheerder'),
        'suborganisatie-van': KeuzelijstWaarde(invulwaarde='suborganisatie-van',
                                               label='suborganisatie van',
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/suborganisatie-van'),
        'toezicht-onderhoud': KeuzelijstWaarde(invulwaarde='toezicht-onderhoud',
                                               label='toezicht onderhoud',
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezicht-onderhoud'),
        'toezichter': KeuzelijstWaarde(invulwaarde='toezichter',
                                       label='toezichter',
                                       status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezichter'),
        'toezichtsgroep': KeuzelijstWaarde(invulwaarde='toezichtsgroep',
                                           label='toezichtsgroep',
                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/toezichtsgroep'),
        'verantwoordelijke-reiniging': KeuzelijstWaarde(invulwaarde='verantwoordelijke-reiniging',
                                                        label='verantwoordelijke reiniging',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBetrokkenheidRol/verantwoordelijke-reiniging')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBetrokkenheidRol.get_dummy_data()

