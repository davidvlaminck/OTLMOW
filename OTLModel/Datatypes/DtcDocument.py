from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.DteTekstblok import DteTekstblok
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlAlgMimeType import KlAlgMimeType
from OTLModel.Datatypes.StringField import StringField
from OTLModel.Datatypes.URIField import URIField


# Generated with OTLComplexDatatypeCreator
class DtcDocument(ComplexField):
    """Complex datatype voor alle bestandsbijlages."""

    def __init__(self):
        super().__init__(naam="DtcDocument",
                         label="Bestandsbijlage",
                         uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument",
                         definition="Complex datatype voor alle bestandsbijlages.",
                         usagenote="",
                         deprecated_version="")

        self.waarde.bestandsnaam = StringField(naam="bestandsnaam",
                                               label="bestandsnaam",
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.bestandsnaam",
                                               definition="De naam van het Document inclusief de bestandsextensie, van de naam gescheiden door een punt.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        self.bestandsnaam = self.waarde.bestandsnaam
        """De naam van het Document inclusief de bestandsextensie, van de naam gescheiden door een punt."""

        self.waarde.mimeType = KeuzelijstField(naam="mimeType",
                                               label="mime-type",
                                               lijst=KlAlgMimeType(),
                                               uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.mimeType",
                                               definition="Het MIME type van het document.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        self.mimeType = self.waarde.mimeType
        """Het MIME type van het document."""

        self.waarde.omschrijving = DteTekstblok()
        """Een korte toelichting over waar het document juist voor dient."""
        self.waarde.omschrijving.naam = "omschrijving"
        self.waarde.omschrijving.label = "omschrijving"
        self.waarde.omschrijving.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.omschrijving"
        self.waarde.omschrijving.definition = "Een korte toelichting over waar het document juist voor dient."
        self.waarde.omschrijving.constraints = ""
        self.waarde.omschrijving.usagenote = ""
        self.waarde.omschrijving.deprecated_version = ""
        self.omschrijving = self.waarde.omschrijving

        self.waarde.uri = URIField(naam="uri",
                                   label="uri",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcDocument.uri",
                                   definition="De verwijzing naar de bestandslocatie via een link. Bij lokale bestanden kan dit eventueel ook een pad zijn.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        self.uri = self.waarde.uri
        """De verwijzing naar de bestandslocatie via een link. Bij lokale bestanden kan dit eventueel ook een pad zijn."""
