# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlVerlichtingstoestelMerk(KeuzelijstField):
    """Het merk van het verlichtingstoestel."""
    naam = 'KlVerlichtingstoestelMerk'
    label = 'Verlichtingstoestel merk'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KlVerlichtingstoestelMerk'
    definition = 'Het merk van het verlichtingstoestel.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlVerlichtingstoestelMerk'
    options = {
        'ARC': KeuzelijstWaarde(invulwaarde='ARC',
                                label='ARC',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/ARC'),
        'HCI-TS': KeuzelijstWaarde(invulwaarde='HCI-TS',
                                   label='HCI-TS',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/HCI-TS'),
        'Philips': KeuzelijstWaarde(invulwaarde='Philips',
                                    label='Philips',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/Philips'),
        'Rombalux': KeuzelijstWaarde(invulwaarde='Rombalux',
                                     label='Rombalux',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/Rombalux'),
        'Schreder': KeuzelijstWaarde(invulwaarde='Schreder',
                                     label='Schreder',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/Schreder'),
        'andere': KeuzelijstWaarde(invulwaarde='andere',
                                   label='andere',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlVerlichtingstoestelMerk/andere')
    }

