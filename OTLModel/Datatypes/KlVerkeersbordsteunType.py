# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerkeersbordsteunType(KeuzelijstField):
    """Types voor een verkeersbordsteun."""
    naam = 'KlVerkeersbordsteunType'
    label = 'Verkeersbordsteuntype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlVerkeersbordsteunType'
    definition = 'Types voor een verkeersbordsteun.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerkeersbordsteunType'
    options = {
        'botsvriendelijke-steun': KeuzelijstWaarde(invulwaarde='botsvriendelijke-steun',
                                                   label='botsvriendelijke steun',
                                                   definitie='Constructie die na aanrijding zijn oorspronkelijke positie hersteld',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun'),
        'botsvriendelijke-steun-type-100NE2': KeuzelijstWaarde(invulwaarde='botsvriendelijke-steun-type-100NE2',
                                                               label='botsvriendelijke steun type 100NE2',
                                                               definitie='te bepalen',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun-type-100NE2'),
        'botsvriendelijke-steun-type-100NE3': KeuzelijstWaarde(invulwaarde='botsvriendelijke-steun-type-100NE3',
                                                               label='botsvriendelijke steun type 100NE3',
                                                               definitie='te bepalen',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/botsvriendelijke-steun-type-100NE3'),
        'galgpaal': KeuzelijstWaarde(invulwaarde='galgpaal',
                                     label='galgpaal',
                                     definitie="Deze optie mag niet aangeduid worden! Bij instantiëren van galgpalen moet je het onderdeel 'Galgpaal' gebruiken.",
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/galgpaal'),
        'rechte-paal': KeuzelijstWaarde(invulwaarde='rechte-paal',
                                        label='rechte paal',
                                        definitie='Een rechte paal met als doel een verkeersbord te bevestigen.',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/rechte-paal'),
        'seinbrug': KeuzelijstWaarde(invulwaarde='seinbrug',
                                     label='seinbrug',
                                     definitie="Deze optie mag niet aangeduid worden! Bij instantiëren van seinbruggen moet je het onderdeel 'Seinbrug' gebruiken.",
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/seinbrug'),
        'vakwerksteun': KeuzelijstWaarde(invulwaarde='vakwerksteun',
                                         label='vakwerksteun',
                                         definitie='Een keuzelijst om het type verkeersbordpaal te bepalen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerkeersbordsteunType/vakwerksteun')
    }

