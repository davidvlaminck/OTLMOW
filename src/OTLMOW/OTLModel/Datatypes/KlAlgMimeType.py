# coding=utf-8
import random
from OTLMOW.OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLMOW.OTLModel.Datatypes.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlAlgMimeType(KeuzelijstField):
    """De mime types van bestanden (AWVDocument) beperkt tot mime types voor toegelaten bestandstypen."""
    naam = 'KlAlgMimeType'
    label = 'Mimetype'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlAlgMimeType'
    definition = 'De mime types van bestanden (AWVDocument) beperkt tot mime types voor toegelaten bestandstypen.'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlAlgMimeType'
    options = {
        'application-acad': KeuzelijstWaarde(invulwaarde='application-acad',
                                             label='application-acad',
                                             status='ingebruik',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-acad'),
        'application-acadmap': KeuzelijstWaarde(invulwaarde='application-acadmap',
                                                label='application-acadmap',
                                                status='ingebruik',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-acadmap'),
        'application-pdf': KeuzelijstWaarde(invulwaarde='application-pdf',
                                            label='application-pdf',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-pdf'),
        'application-rtf': KeuzelijstWaarde(invulwaarde='application-rtf',
                                            label='application-rtf',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-rtf'),
        'application-rvt': KeuzelijstWaarde(invulwaarde='application-rvt',
                                            label='application-rvt',
                                            status='ingebruik',
                                            definitie='Revit project file.',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-rvt'),
        'application-vnd.openxmlformats-officedocument.spreadsheetml.sheet': KeuzelijstWaarde(invulwaarde='application-vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                                                                              label='application-vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                                                                                              status='ingebruik',
                                                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
        'application-vnd.openxmlformats-officedocument.wordprocessingml.document': KeuzelijstWaarde(invulwaarde='application-vnd.openxmlformats-officedocument.wordprocessingml.document',
                                                                                                    label='application-vnd.openxmlformats-officedocument.wordprocessingml.document',
                                                                                                    status='ingebruik',
                                                                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-vnd.openxmlformats-officedocument.wordprocessingml.document'),
        'application-xml': KeuzelijstWaarde(invulwaarde='application-xml',
                                            label='application-xml',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-xml'),
        'application-zip': KeuzelijstWaarde(invulwaarde='application-zip',
                                            label='application-zip',
                                            status='ingebruik',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/application-zip'),
        'image-dxf': KeuzelijstWaarde(invulwaarde='image-dxf',
                                      label='image-dxf',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/image-dxf'),
        'image-jpeg': KeuzelijstWaarde(invulwaarde='image-jpeg',
                                       label='image-jpeg',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/image-jpeg'),
        'image-svg': KeuzelijstWaarde(invulwaarde='image-svg',
                                      label='image-svg',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/image-svg'),
        'image-tiff': KeuzelijstWaarde(invulwaarde='image-tiff',
                                       label='image-tiff',
                                       status='ingebruik',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/image-tiff'),
        'text-csv': KeuzelijstWaarde(invulwaarde='text-csv',
                                     label='text-csv',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/text-csv'),
        'text-html': KeuzelijstWaarde(invulwaarde='text-html',
                                      label='text-html',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/text-html'),
        'text-rtf': KeuzelijstWaarde(invulwaarde='text-rtf',
                                     label='text-rtf',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/text-rtf'),
        'text-xml': KeuzelijstWaarde(invulwaarde='text-xml',
                                     label='text-xml',
                                     status='ingebruik',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/text-xml'),
        'video-avi': KeuzelijstWaarde(invulwaarde='video-avi',
                                      label='video-avi',
                                      status='ingebruik',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgMimeType/video-avi')
    }

    @classmethod
    def get_dummy_data(cls):
        return random.choice(list(cls.options.keys()))

    @staticmethod
    def create_dummy_data():
        return KlAlgMimeType.get_dummy_data()

