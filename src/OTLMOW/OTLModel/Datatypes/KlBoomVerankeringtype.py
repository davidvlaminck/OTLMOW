# coding=utf-8
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from src.OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlBoomVerankeringtype(KeuzelijstField):
    """De verschillende types van verankering van een boom."""
    naam = 'KlBoomVerankeringtype'
    label = 'Boom verankeringtype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlBoomVerankeringtype'
    definition = 'De verschillende types van verankering van een boom.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlBoomVerankeringtype'
    options = {
        'biologisch-afbreekbare-grondankers': KeuzelijstWaarde(invulwaarde='biologisch-afbreekbare-grondankers',
                                                               label='biologisch afbreekbare grondankers',
                                                               definitie='Een constructie van 100% biologisch afbreekbare grondankers en verankeringstouwen die de stabilietit van de boom waarborgt',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankeringtype/biologisch-afbreekbare-grondankers'),
        'boompaalconstructie': KeuzelijstWaarde(invulwaarde='boompaalconstructie',
                                                label='boompaalconstructie',
                                                definitie='Een constructie uit houten palen en dwarslatten die de stabiliteit van de boom waarborgt',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankeringtype/boompaalconstructie'),
        'niet-afbreekbare-grondankers': KeuzelijstWaarde(invulwaarde='niet-afbreekbare-grondankers',
                                                         label='niet-afbreekbare grondankers',
                                                         definitie='Een constructie van stalen grondankers en kunststofverankeringsbanden die de stabilietit van de boom waarborgt',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlBoomVerankeringtype/niet-afbreekbare-grondankers')
    }

