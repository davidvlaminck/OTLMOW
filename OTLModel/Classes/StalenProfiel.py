from abc import abstractmethod
from OTLModel.Classes.ConstructieElement import ConstructieElement
from OTLModel.Classes.StalenConstructieElement import StalenConstructieElement
from OTLModel.Classes.ConstructieElementenGC import ConstructieElementenGC
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator
class StalenProfiel(ConstructieElement, StalenConstructieElement, ConstructieElementenGC):
    """Bundeling van gemeenschappelijke eigenschappen van standaard en niet-standaard stalen profiel."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        ConstructieElement.__init__(self)
        StalenConstructieElement.__init__(self)
        ConstructieElementenGC.__init__(self)
        self.isVoorgebogen = BooleanField(naam="isVoorgebogen",
                                          label="is voorgebogen",
                                          uri="https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel.isVoorgebogen",
                                          definition="Bij het fabriceren wordt er bewust een ronding aangebracht in het profiel. Dit kan bijvoorbeeld dienen ter compensatie van doorbuiging of omwille van esthetische redenen,...",
                                          constraints="",
                                          usagenote="",
                                          deprecated_version="")
        """Bij het fabriceren wordt er bewust een ronding aangebracht in het profiel. Dit kan bijvoorbeeld dienen ter compensatie van doorbuiging of omwille van esthetische redenen,..."""

        self.lengte = KwantWrdInMeter()
        """De lengte van het profiel uitgedrukt in in meter."""
        self.lengte.naam = "lengte"
        self.lengte.label = "lengte"
        self.lengte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel.lengte"
        self.lengte.definition = "De lengte van het profiel uitgedrukt in in meter."
        self.lengte.constraints = ""
        self.lengte.usagenote = ""
        self.lengte.deprecated_version = ""

        self.technischeFiche = DtcDocument()
        """De technische gegevens van het stalen profiel (relevante normen, detail afmetingen, gewicht,...)."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel.technischeFiche"
        self.technischeFiche.definition = "De technische gegevens van het stalen profiel (relevante normen, detail afmetingen, gewicht,...)."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
