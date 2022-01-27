# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from src.OTLMOW.OTLModel.Datatypes.DteTekstblok import DteTekstblok
from src.OTLMOW.OTLModel.Datatypes.KlAlgMimeType import KlAlgMimeType
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField
from src.OTLMOW.OTLModel.Datatypes.URIField import URIField


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDocumentWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._bestandsnaam = OTLAttribuut(field=StringField,
                                          naam='bestandsnaam',
                                          label='bestandsnaam',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.bestandsnaam',
                                          definition='De naam van het Document inclusief de bestandsextensie, van de naam gescheiden door een punt.')

        self._mimeType = OTLAttribuut(field=KlAlgMimeType,
                                      naam='mimeType',
                                      label='mime-type',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.mimeType',
                                      definition='Het MIME type van het document.')

        self._omschrijving = OTLAttribuut(field=DteTekstblok,
                                          naam='omschrijving',
                                          label='omschrijving',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.omschrijving',
                                          definition='Een korte toelichting over waar het document juist voor dient.')

        self._uri = OTLAttribuut(field=URIField,
                                 naam='uri',
                                 label='uri',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.uri',
                                 definition='De verwijzing naar de bestandslocatie via een link. Bij lokale bestanden kan dit eventueel ook een pad zijn.')

    @property
    def bestandsnaam(self):
        """De naam van het Document inclusief de bestandsextensie, van de naam gescheiden door een punt."""
        return self._bestandsnaam.waarde

    @bestandsnaam.setter
    def bestandsnaam(self, value):
        self._bestandsnaam.set_waarde(value, owner=self._parent)

    @property
    def mimeType(self):
        """Het MIME type van het document."""
        return self._mimeType.waarde

    @mimeType.setter
    def mimeType(self, value):
        self._mimeType.set_waarde(value, owner=self._parent)

    @property
    def omschrijving(self):
        """Een korte toelichting over waar het document juist voor dient."""
        return self._omschrijving.waarde

    @omschrijving.setter
    def omschrijving(self, value):
        self._omschrijving.set_waarde(value, owner=self._parent)

    @property
    def uri(self):
        """De verwijzing naar de bestandslocatie via een link. Bij lokale bestanden kan dit eventueel ook een pad zijn."""
        return self._uri.waarde

    @uri.setter
    def uri(self, value):
        self._uri.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcDocument(ComplexField, AttributeInfo):
    """Complex datatype voor alle bestandsbijlages."""
    naam = 'DtcDocument'
    label = 'Bestandsbijlage'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument'
    definition = 'Complex datatype voor alle bestandsbijlages.'
    waardeObject = DtcDocumentWaarden

    def __str__(self):
        return ComplexField.__str__(self)

