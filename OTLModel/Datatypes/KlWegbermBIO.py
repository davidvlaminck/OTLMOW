# coding=utf-8
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlWegbermBIO(KeuzelijstField):
    """Bijzonder ingerichte onderdelen van de wegbermen."""
    naam = 'KlWegbermBIO'
    label = 'Wegberm BIO'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#KlWegbermBIO'
    definition = 'Bijzonder ingerichte onderdelen van de wegbermen.'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlWegbermBIO'
    options = {
        'bijzondere-bedding': KeuzelijstWaarde(invulwaarde='bijzondere-bedding',
                                               label='bijzondere bedding',
                                               definitie='Gedeelte van de wegberm, uitsluitend bestemd voor voertuigen van het openbaar vervoer en andere toegelaten voertuigen.',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/bijzondere-bedding'),
        'fietspad': KeuzelijstWaarde(invulwaarde='fietspad',
                                     label='fietspad',
                                     definitie='Gedeelte van het wegplatform, dat bestemd is voor fietsers en bromfietsers en als zodanig aangeduid.',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/fietspad'),
        'ruiterpad': KeuzelijstWaarde(invulwaarde='ruiterpad',
                                      label='ruiterpad',
                                      definitie='Gedeelte van de wegberm, bestemd voor ruiters en als zodanig aangeduid.',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/ruiterpad'),
        'verkeerseiland': KeuzelijstWaarde(invulwaarde='verkeerseiland',
                                           label='verkeerseiland',
                                           definitie='Heeft als doel het verkeer te geleiden en kan verhoogd zijn.',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/verkeerseiland'),
        'vluchtheuvel': KeuzelijstWaarde(invulwaarde='vluchtheuvel',
                                         label='vluchtheuvel',
                                         definitie='Verkeersheuvel ten behoeve van voetgangers.',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/vluchtheuvel'),
        'voetpad': KeuzelijstWaarde(invulwaarde='voetpad',
                                    label='voetpad',
                                    definitie='Gedeelte van de wegberm, bestemd voor voetgangers.',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlWegbermBIO/voetpad')
    }

