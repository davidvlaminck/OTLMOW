# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere


# Generated with OTLClassCreator. To modify: extend, do not edit
class Laagspanningsbord(AIMNaamObject):
    """Verzameling van alle elektrische componenten nodig voor de voeding en sturing van applicaties die erop aangesloten zijn. Omvat onder andere automaten,klemmenblokken,..."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.elektrischSchema = DtcDocument()
        """Het elektrisch aansluitschema van het laagspanningsbord."""
        self.elektrischSchema.naam = "elektrischSchema"
        self.elektrischSchema.label = "elektrisch schema"
        self.elektrischSchema.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.elektrischSchema"
        self.elektrischSchema.definition = "Het elektrisch aansluitschema van het laagspanningsbord."
        self.elektrischSchema.constraints = ""
        self.elektrischSchema.usagenote = ""
        self.elektrischSchema.deprecated_version = ""

        self.vermogen = KwantWrdInAmpere()
        """Het vermogen van het laagspanningsbord."""
        self.vermogen.naam = "vermogen"
        self.vermogen.label = "vermogen"
        self.vermogen.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.vermogen"
        self.vermogen.definition = "Het vermogen van het laagspanningsbord."
        self.vermogen.constraints = ""
        self.vermogen.usagenote = ""
        self.vermogen.deprecated_version = ""
