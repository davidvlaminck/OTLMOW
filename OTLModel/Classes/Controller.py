from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DteIPv4Adres import DteIPv4Adres
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator
class Controller(AIMNaamObject):
    """Abstracte voor allerlei types van controllers."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
        self.batchnummer = StringField(naam="batchnummer",
                                       label="batchnummer",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller.batchnummer",
                                       definition="Nummer van de batch.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Nummer van de batch."""

        self.dNSNaam = StringField(naam="dNSNaam",
                                   label="DNS-naam",
                                   uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller.dNSNaam",
                                   definition="DNS-naam van de controller.",
                                   constraints="",
                                   usagenote="",
                                   deprecated_version="")
        """DNS-naam van de controller."""

        self.firmwareversie = StringField(naam="firmwareversie",
                                          label="firmwareversie",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller.firmwareversie",
                                          definition="Firmwareversie van de controller.",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Firmwareversie van de controller."""

        self.iPAdres = DteIPv4Adres()
        """IP-adres van de controller."""
        self.iPAdres.naam = "iPAdres"
        self.iPAdres.label = "IP-adres"
        self.iPAdres.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller.iPAdres"
        self.iPAdres.definition = "IP-adres van de controller."
        self.iPAdres.constraints = ""
        self.iPAdres.usagenote = ""
        self.iPAdres.deprecated_version = ""

        self.serienummer = StringField(naam="serienummer",
                                       label="serienummer",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Controller.serienummer",
                                       definition="Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
