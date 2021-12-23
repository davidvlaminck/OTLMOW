from OTLModel.Classes.ComplexeGeleiding import ComplexeGeleiding
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator
class Veerooster(ComplexeGeleiding):
    """Een veerooster is een infrastructurele voorziening die is aangebracht in het wegdek om te voorkomen dat vee een gebied binnenkomt of verlaat."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veerooster"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.breedte = KwantWrdInMeter()
        """De breedte van het veerooster in meter."""
        self.breedte.naam = "breedte"
        self.breedte.label = "breedte"
        self.breedte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Veerooster.breedte"
        self.breedte.definition = "De breedte van het veerooster in meter."
        self.breedte.constraints = ""
        self.breedte.usagenote = ""
        self.breedte.deprecated_version = ""
