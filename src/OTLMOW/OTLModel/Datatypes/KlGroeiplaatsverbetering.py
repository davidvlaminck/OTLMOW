# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlGroeiplaatsverbetering(KeuzelijstField):
    """De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren."""
    naam = 'KlGroeiplaatsverbetering'
    label = 'Groeiplaatsverbetering'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlGroeiplaatsverbetering'
    definition = 'De techniek waarmee de groeiplaats wordt verbeterd met als doel de levensverwachting en de conditie van de vegetatie te verbeteren.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlGroeiplaatsverbetering'
    options = {
        'aanleg-drainagebuis': KeuzelijstWaarde(invulwaarde='aanleg-drainagebuis',
                                                label='aanleg drainagebuis',
                                                status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                definitie='Groeiplaatsverbetering dmv aanleg met een drainagebuis.',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/aanleg-drainagebuis'),
        'aanleg-gietrand-overtollige-grond': KeuzelijstWaarde(invulwaarde='aanleg-gietrand-overtollige-grond',
                                                              label='aanleg gietrand overtollige grond',
                                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                              definitie='Groeiplaatsverbetering dmv aanleg met een overtollige grond.',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/aanleg-gietrand-overtollige-grond'),
        'aanleg-kunstmatige-gietrand': KeuzelijstWaarde(invulwaarde='aanleg-kunstmatige-gietrand',
                                                        label='aanleg kunstmatige gietrand',
                                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                        definitie='Groeiplaatsverbetering dmv aanleg met een kunstmatige gietrand.',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/aanleg-kunstmatige-gietrand'),
        'beluchtingssysteem': KeuzelijstWaarde(invulwaarde='beluchtingssysteem',
                                               label='beluchtingssysteem',
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='Een beluchtingssysteem is een groeiplaatsverbetering voor bomen door middel van een draineerbuis onder het wortelgestel of de kluit van een boom te plaatsen.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/beluchtingssysteem'),
        'bezanden': KeuzelijstWaarde(invulwaarde='bezanden',
                                     label='bezanden',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='Het bezanden omvat het gelijkmatig spreiden van zand op bepaalde grondoppervlakken en het inwerken ervan.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/bezanden'),
        'bodembeluchting-luchtinjectie': KeuzelijstWaarde(invulwaarde='bodembeluchting-luchtinjectie',
                                                          label='bodembeluchting-luchtinjectie',
                                                          status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                          definitie='NIET GEBRUIKEN - Groeiplaatsverbetering dmv bodembeluchting-luchtinjectie.',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/bodembeluchting-luchtinjectie'),
        'bodemverbeteraar': KeuzelijstWaarde(invulwaarde='bodemverbeteraar',
                                             label='bodemverbeteraar',
                                             status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                             definitie='Een bodemverbeteraar is een organisch of fysisch middel die inzonderheid ter verbetering van de structuur aan de grond wordt toegevoegd.',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/bodemverbeteraar'),
        'gft-compost': KeuzelijstWaarde(invulwaarde='gft-compost',
                                        label='GFT-compost',
                                        status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                        definitie='GFT-compost is het product verkregen door een gecontroleerde aërobe compostering (anaërobe vergisting met een aërobe nacompostering in het geval van humotex) van het gescheiden ingezamelde organische deel van het huishoudelijk afval (bestaande hoofdzakelijk uit keukenafval en het fijne, niethoutige, gedeelte van het tuinafval) tot volledige rijping.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/gft-compost'),
        'groencompost': KeuzelijstWaarde(invulwaarde='groencompost',
                                         label='groencompost',
                                         status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                         definitie='Groencompost is een product verkregen door een gecontroleerde aerobe compostering van groenafval (bestaande hoofdzakelijk uit snoeihout met een diameter van max. 10 cm, planten (resten), haagscheersel, bladeren, gazon- en wegbermmaaisel) tot volledige rijping, voorafgegaan of gevolgd door mechanische behandelingen (verkleining, zeving, …).',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/groencompost'),
        'horizontale-drainage': KeuzelijstWaarde(invulwaarde='horizontale-drainage',
                                                 label='horizontale drainage',
                                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                 definitie='Groeiplaatsverbetering dmv horizontale drainage.',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/horizontale-drainage'),
        'irrgatie-drainagebuis': KeuzelijstWaarde(invulwaarde='irrgatie-drainagebuis',
                                                  label='irrgatie drainagebuis',
                                                  status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                  definitie='NIET GEBRUIKEN - Groeiplaatsverbetering dmv irrigatie met een drainagebuis.',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/irrgatie-drainagebuis'),
        'irrigatie-gietrand-overtollige-grond': KeuzelijstWaarde(invulwaarde='irrigatie-gietrand-overtollige-grond',
                                                                 label='irrigatie gietrand overtollige grond',
                                                                 status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                                 definitie='NIET GEBRUIKEN - Groeiplaatsverbetering dmv irrigatie met een overtollige grond.',
                                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/irrigatie-gietrand-overtollige-grond'),
        'irrigatie-kunstmatige-gietrand': KeuzelijstWaarde(invulwaarde='irrigatie-kunstmatige-gietrand',
                                                           label='irrigatie kunstmatige gietrand',
                                                           status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                                           definitie='NIET GEBRUIKEN - Groeiplaatsverbetering dmv irrigatie met een kunstmatige gietrand.',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/irrigatie-kunstmatige-gietrand'),
        'meststof': KeuzelijstWaarde(invulwaarde='meststof',
                                     label='meststof',
                                     status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                     definitie='een meststof is een scheikundig of organisch product dat ter verbetering van de vruchtbaarheid aan de grond wordt toegevoegd.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/meststof'),
        'meststoftabletten': KeuzelijstWaarde(invulwaarde='meststoftabletten',
                                              label='meststoftabletten',
                                              status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                              definitie='Tabletten van meststof.',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/meststoftabletten'),
        'verticale-drainage': KeuzelijstWaarde(invulwaarde='verticale-drainage',
                                               label='verticale drainage',
                                               status='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik',
                                               definitie='Groeiplaatsverbetering dmv verticale drainage.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlGroeiplaatsverbetering/verticale-drainage')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlGroeiplaatsverbetering.get_dummy_data()

