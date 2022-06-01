# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomGebreken(KeuzelijstField):
    """De verschillende mogelijke gebreken bij een boom."""
    naam = 'KlBoomGebreken'
    label = 'Boom gebreken'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomGebreken'
    definition = 'De verschillende mogelijke gebreken bij een boom.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomGebreken'
    options = {
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   definitie='Andere gebreken',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/andere'),
        'bladverkleuring': KeuzelijstWaarde(invulwaarde='bladverkleuring',
                                            label='bladverkleuring',
                                            definitie='Abnormale verkleuring van het blad in het groeiseizoen',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/bladverkleuring'),
        'dood-hout-afgestorven-takken': KeuzelijstWaarde(invulwaarde='dood-hout-afgestorven-takken',
                                                         label='dood hout-afgestorven takken',
                                                         definitie='Dood hout of afgestorven takken',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/dood-hout-afgestorven-takken'),
        'holte': KeuzelijstWaarde(invulwaarde='holte',
                                  label='holte',
                                  definitie='Diepere opening in stam of tak',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/holte'),
        'houtscheuren': KeuzelijstWaarde(invulwaarde='houtscheuren',
                                         label='houtscheuren',
                                         definitie='Dwarse of lengtescheuren in de stam of takken',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/houtscheuren'),
        'insecten': KeuzelijstWaarde(invulwaarde='insecten',
                                     label='insecten',
                                     definitie='Insecten die de boom aantasten',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/insecten'),
        'kanker-bacterie': KeuzelijstWaarde(invulwaarde='kanker-bacterie',
                                            label='kanker-bacterie',
                                            definitie='Aantasting door een schimmelziekte of bacterie met een vergroeiing van de boom tot gevolg',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/kanker-bacterie'),
        'maaischade': KeuzelijstWaarde(invulwaarde='maaischade',
                                       label='maaischade',
                                       definitie='Schade aan de stamvoet door maaien',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/maaischade'),
        'plakoksel': KeuzelijstWaarde(invulwaarde='plakoksel',
                                      label='plakoksel',
                                      definitie='Een tak die niet vergroeid is met de stam of andere tak, waarbij de schors van beide tegen elkaar aangedrukt wordt en dus niet vasthangen aan elkaar.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/plakoksel'),
        'stamschade': KeuzelijstWaarde(invulwaarde='stamschade',
                                       label='stamschade',
                                       definitie='Schade aan stam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/stamschade'),
        'takschade': KeuzelijstWaarde(invulwaarde='takschade',
                                      label='takschade',
                                      definitie='Schade aan tak of kroon',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/takschade'),
        'verminderde-bladbezetting': KeuzelijstWaarde(invulwaarde='verminderde-bladbezetting',
                                                      label='verminderde bladbezetting',
                                                      definitie='Abnormale afname van de hoeveelheid bladeren verspreid over de kroon in het groeiseizoen',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/verminderde-bladbezetting'),
        'waterloten-stamvoetopslag': KeuzelijstWaarde(invulwaarde='waterloten-stamvoetopslag',
                                                      label='waterloten-stamvoetopslag',
                                                      definitie='Scheuten die, vaak massaal, gevormd worden aan de stamvoet. Waterloten zijn slapende knopen op stam of takken die uitlopen',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/waterloten-stamvoetopslag'),
        'wortelschade': KeuzelijstWaarde(invulwaarde='wortelschade',
                                         label='wortelschade',
                                         definitie='Schade aan wortels',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/wortelschade'),
        'zwammen-schimmels': KeuzelijstWaarde(invulwaarde='zwammen-schimmels',
                                              label='zwammen-schimmels',
                                              definitie='Aanwezigheid van zwammen en/of schimmels',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomGebreken/zwammen-schimmels')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBoomGebreken.get_dummy_data()

