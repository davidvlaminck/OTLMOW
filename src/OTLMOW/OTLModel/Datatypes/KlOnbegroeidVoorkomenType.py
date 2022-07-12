# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOnbegroeidVoorkomenType(KeuzelijstField):
    """De mogelijke afwerkingen van het onbegroeide voorkomen."""
    naam = 'KlOnbegroeidVoorkomenType'
    label = 'Onbegroeid voorkomen type'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlOnbegroeidVoorkomenType'
    definition = 'De mogelijke afwerkingen van het onbegroeide voorkomen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOnbegroeidVoorkomenType'
    options = {
        'gesloten-kunststofverharding': KeuzelijstWaarde(invulwaarde='gesloten-kunststofverharding',
                                                         label='gesloten kunststofverharding',
                                                         status='ingebruik',
                                                         definitie='Kunststofverharding die over de totale oppervlakte in één continue laag werd aangebracht.',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/gesloten-kunststofverharding'),
        'gravel': KeuzelijstWaarde(invulwaarde='gravel',
                                   label='gravel',
                                   status='ingebruik',
                                   definitie='Puinmengsel specifiek bestaande uit zuiver gebroken baksteen- en dakpannenpuin.',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/gravel'),
        'grindgazon-eenlaags': KeuzelijstWaarde(invulwaarde='grindgazon-eenlaags',
                                                label='grindgazon eenlaags',
                                                status='ingebruik',
                                                definitie='Een substraat ontwikkeld om voertuigen sporadisch toe te laten op gazons zonder dater spoorvorming optreedt.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/grindgazon-eenlaags'),
        'grindgazon-tweelaags': KeuzelijstWaarde(invulwaarde='grindgazon-tweelaags',
                                                 label='grindgazon tweelaags',
                                                 status='ingebruik',
                                                 definitie='Afwerking van tweelaagse grindgazon.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/grindgazon-tweelaags'),
        'harsgebonden-siersplit': KeuzelijstWaarde(invulwaarde='harsgebonden-siersplit',
                                                   label='harsgebonden siersplit',
                                                   status='ingebruik',
                                                   definitie='Afwerking van harsgebonden siersplit.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/harsgebonden-siersplit'),
        'kunstgras': KeuzelijstWaarde(invulwaarde='kunstgras',
                                      label='kunstgras',
                                      status='ingebruik',
                                      definitie='Bedekking bestaande uit synthetisch materiaal, met de bedoeling om natuurlijk gras te imiteren.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/kunstgras'),
        'mulch': KeuzelijstWaarde(invulwaarde='mulch',
                                  label='mulch',
                                  status='ingebruik',
                                  definitie='Bedekking bestaande uit een laag organisch materiaal. (Herfstbladeren, grasmaaisel, houtsnippers, compost...).',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/mulch'),
        'rubberen-matten-tegels': KeuzelijstWaarde(invulwaarde='rubberen-matten-tegels',
                                                   label='rubberen matten tegels',
                                                   status='ingebruik',
                                                   definitie='Verharding bestaande uit afzonderlijke elementen kunststofverharding.',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/rubberen-matten-tegels'),
        'schelpen': KeuzelijstWaarde(invulwaarde='schelpen',
                                     label='schelpen',
                                     status='ingebruik',
                                     definitie='Bedekking van een onverharde zone die opgebouwd is uit een niet-gecompacteerde groep van individuele componenten die voldoen aan de volgende specificaties: hoofdbestanddeel schelpen, onregelmatige vorm en onregelmatig verband.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/schelpen'),
        'schors': KeuzelijstWaarde(invulwaarde='schors',
                                   label='schors',
                                   status='ingebruik',
                                   definitie='Bedekking bestaande uit mengsel van schors (gefragmenteerde boomschors)',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/schors'),
        'steenslag-rolgrind': KeuzelijstWaarde(invulwaarde='steenslag-rolgrind',
                                               label='steenslag rolgrind',
                                               status='ingebruik',
                                               definitie='Bedekking van een onverharde zone die opgebouwd is uit een niet-gecompacteerde groep van individuele componenten die voldoen aan de volgende specificaties: losse steenslag, behalve dolomiet, afgeronde en onregelmatige vorm en onregelmatig verband.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/steenslag-rolgrind'),
        'tegels-met-groenvoeg': KeuzelijstWaarde(invulwaarde='tegels-met-groenvoeg',
                                                 label='tegels met groenvoeg',
                                                 status='ingebruik',
                                                 definitie='Tegels die zo gelegd zijn dat de voeg begroeibaar is en waterdoorlaatbaar.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOnbegroeidVoorkomenType/tegels-met-groenvoeg')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlOnbegroeidVoorkomenType.get_dummy_data()

