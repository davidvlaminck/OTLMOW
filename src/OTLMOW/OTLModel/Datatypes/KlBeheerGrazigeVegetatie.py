# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBeheerGrazigeVegetatie(KeuzelijstField):
    """De verschillende soorten van beheer voor grazige vegetatie."""
    naam = 'KlBeheerGrazigeVegetatie'
    label = 'Beheer grazige vegetatie '
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#KlBeheerGrazigeVegetatie'
    definition = 'De verschillende soorten van beheer voor grazige vegetatie.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBeheerGrazigeVegetatie'
    options = {
        'afboorden': KeuzelijstWaarde(invulwaarde='afboorden',
                                      label='afboorden',
                                      status='ingebruik',
                                      definitie='Het afsteken van de overgroeiende vegetatie langs de rand van de verharding. (wordt afranden genoemd in SB250) ',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/afboorden'),
        'aflagen': KeuzelijstWaarde(invulwaarde='aflagen',
                                    label='aflagen',
                                    status='ingebruik',
                                    definitie='Het verwijderen van de bovenste grondlaag met begroeiing om afwatering te garanderen',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/aflagen'),
        'begrazing': KeuzelijstWaarde(invulwaarde='begrazing',
                                      label='begrazing',
                                      status='ingebruik',
                                      definitie='De vegetatie wordt begraasd door dieren.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/begrazing'),
        'beluchten': KeuzelijstWaarde(invulwaarde='beluchten',
                                      label='beluchten',
                                      status='ingebruik',
                                      definitie='Beluchten van grazige vegetatie.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/beluchten'),
        'bestrijden-ongewenste-vegetatie': KeuzelijstWaarde(invulwaarde='bestrijden-ongewenste-vegetatie',
                                                            label='bestrijden ongewenste vegetatie',
                                                            status='ingebruik',
                                                            definitie='Bestrijden van ongewenste vegetatie die zich bevingt in het perceel van grazige vegetatie..',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/bestrijden-ongewenste-vegetatie'),
        'konijnenbeheer': KeuzelijstWaarde(invulwaarde='konijnenbeheer',
                                           label='konijnenbeheer',
                                           status='ingebruik',
                                           definitie='Het reduceren van konijnenpopulaties om de stabilietit van taluds te blijven garanderen',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/konijnenbeheer'),
        'maaisel-verwijderen-directe-opzuig': KeuzelijstWaarde(invulwaarde='maaisel-verwijderen-directe-opzuig',
                                                               label='maaisel verwijderen directe opzuig',
                                                               status='ingebruik',
                                                               definitie='het verwijderen van het maaisel met een maaizuigcombinatie',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/maaisel-verwijderen-directe-opzuig'),
        'maaisel-verwijderen-hooien-oprapen': KeuzelijstWaarde(invulwaarde='maaisel-verwijderen-hooien-oprapen',
                                                               label='maaisel verwijderen hooien-oprapen',
                                                               status='ingebruik',
                                                               definitie='het maaisel wordt gehooid en binnen de 10 dagen opgeraapt en verwijderd',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/maaisel-verwijderen-hooien-oprapen'),
        'niets-doen': KeuzelijstWaarde(invulwaarde='niets-doen',
                                       label='niets doen',
                                       status='ingebruik',
                                       definitie='Er wordt geen beheer uitgevoerd',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/niets-doen'),
        'plaggen': KeuzelijstWaarde(invulwaarde='plaggen',
                                    label='plaggen',
                                    status='ingebruik',
                                    definitie='Plaggen is het verwijderen van de bovenste grondlaag met begroeiing om grond te verschralen',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/plaggen'),
        'profielherstelling-zonder-herinzaaien': KeuzelijstWaarde(invulwaarde='profielherstelling-zonder-herinzaaien',
                                                                  label='profielherstelling zonder herinzaaien',
                                                                  status='ingebruik',
                                                                  definitie='Profielherstelling zonder herinzaaiing van grazige vegetatie.',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/profielherstelling-zonder-herinzaaien'),
        'reiten': KeuzelijstWaarde(invulwaarde='reiten',
                                   label='reiten',
                                   status='ingebruik',
                                   definitie='Het inkorten van het riet tot ongeveer 10 cm boven het wateroppervlak met maaikorf. Maaisel wordt verwijderd.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/reiten'),
        'uitharken': KeuzelijstWaarde(invulwaarde='uitharken',
                                      label='uitharken',
                                      status='ingebruik',
                                      definitie='Uitharken van grazige vegetatie.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBeheerGrazigeVegetatie/uitharken')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlBeheerGrazigeVegetatie.get_dummy_data()

