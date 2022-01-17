# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlCodeklavierWerking(KeuzelijstField):
    """Een keuzelijst met werkingsprincipes van een codeklavier."""
    naam = 'KlCodeklavierWerking'
    label = 'Codeklavier werking'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlCodeklavierWerking'
    definition = 'Een keuzelijst met werkingsprincipes van een codeklavier.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlCodeklavierWerking'
    options = {
        'cijfercodeslot': KeuzelijstWaarde(invulwaarde='cijfercodeslot',
                                           label='cijfercodeslot',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/cijfercodeslot'),
        'cijfercodeslot-met-drukknop': KeuzelijstWaarde(invulwaarde='cijfercodeslot-met-drukknop',
                                                        label='cijfercodeslot met drukknop',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/cijfercodeslot-met-drukknop'),
        'drukknop': KeuzelijstWaarde(invulwaarde='drukknop',
                                     label='drukknop',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlCodeklavierWerking/drukknop')
    }

