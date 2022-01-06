from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.Signalisatie import Signalisatie
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlVerkeersspiegelVorm import KlVerkeersspiegelVorm


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersspiegel(AIMObject, Signalisatie):
    """Een verkeersspiegel is een spiegel die de zichtbaarheid verbetert van het aankomende verkeer."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        Signalisatie.__init__(self)

        bijlageDocumentField = DtcDocument()
        bijlageDocumentField.naam = "bijlageDocument"
        bijlageDocumentField.label = "bijlage document"
        bijlageDocumentField.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel.bijlageDocument"
        bijlageDocumentField.definition = "Een document met dossiernummer waardoor men kan terugkoppelen naar de vergunning."
        bijlageDocumentField.constraints = ""
        bijlageDocumentField.usagenote = ""
        bijlageDocumentField.deprecated_version = ""
        self.bijlageDocument = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=bijlageDocumentField)
        """Een document met dossiernummer waardoor men kan terugkoppelen naar de vergunning."""

        self.isGoedgekeurd = BooleanField(naam="isGoedgekeurd",
                                          label="is goedgekeurd",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel.isGoedgekeurd",
                                          definition="Geeft of de verkeersspiegel al dan niet goedgekeurd is.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Geeft of de verkeersspiegel al dan niet goedgekeurd is."""

        self.vorm = KeuzelijstField(naam="vorm",
                                    label="vorm",
                                    lijst=KlVerkeersspiegelVorm(),
                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersspiegel.vorm",
                                    definition="Bepaling van de vorm van de gebruikte verkeersspiegel.",
                                    constraints="",
                                    usagenote="",
                                    deprecated_version="")
        """Bepaling van de vorm van de gebruikte verkeersspiegel."""
