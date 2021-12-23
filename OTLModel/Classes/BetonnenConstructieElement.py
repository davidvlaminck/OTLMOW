from abc import abstractmethod, ABC
from OTLModel.Datatypes.DtcBetonspecificaties import DtcBetonspecificaties
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlUitvoeringsmethode import KlUitvoeringsmethode


# Generated with OTLClassCreator
class BetonnenConstructieElement(ABC):
    """Bundeling van gemeenschappelijke eigenschappen van betonnen constructie-elementen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        self.betonspecificaties = DtcBetonspecificaties()
        """Eigenschappen van het gebruikte beton."""
        self.betonspecificaties.naam = "betonspecificaties"
        self.betonspecificaties.label = "betonspecificaties"
        self.betonspecificaties.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement.betonspecificaties"
        self.betonspecificaties.definition = "Eigenschappen van het gebruikte beton."
        self.betonspecificaties.constraints = ""
        self.betonspecificaties.usagenote = ""
        self.betonspecificaties.deprecated_version = ""

        self.uitvoeringsmethode = KeuzelijstField(naam="uitvoeringsmethode",
                                                  label="uitvoeringsmethode",
                                                  lijst=KlUitvoeringsmethode(),
                                                  uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement.uitvoeringsmethode",
                                                  definition="Op welke manier het beton wordt aangebracht.",
                                                  constraints="",
                                                  usagenote="",
                                                  deprecated_version="")
        """Op welke manier het beton wordt aangebracht."""

        self.wapeningsplan = DtcDocument()
        """Plan waarin de wapening zo gedetailleerd mogelijk wordt uitgetekend (met materiaalspecificaties en de afmetingen worden weergegeven in millimeters)."""
        self.wapeningsplan.naam = "wapeningsplan"
        self.wapeningsplan.label = "wapeningsplan"
        self.wapeningsplan.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#BetonnenConstructieElement.wapeningsplan"
        self.wapeningsplan.definition = "Plan waarin de wapening zo gedetailleerd mogelijk wordt uitgetekend (met materiaalspecificaties en de afmetingen worden weergegeven in millimeters)."
        self.wapeningsplan.constraints = ""
        self.wapeningsplan.usagenote = ""
        self.wapeningsplan.deprecated_version = ""
