# coding=utf-8
from OTLModel.Classes.ConstructieElement import ConstructieElement
from OTLModel.Classes.BetonnenConstructieElement import BetonnenConstructieElement
from OTLModel.Classes.ConstructieElementenGC import ConstructieElementenGC
from OTLModel.Datatypes.DtcAfmetingBxlxhInM import DtcAfmetingBxlxhInM
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlPlaatsingswijzePlint import KlPlaatsingswijzePlint


# Generated with OTLClassCreator. To modify: extend, do not edit
class PlintGC(ConstructieElement, BetonnenConstructieElement, ConstructieElementenGC):
    """Een plint is een betonnen balk/plaat die de akoestische dichtheid verzekert tussen de schermelementen van de geluidswerende constructie en de bodem."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PlintGC"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        BetonnenConstructieElement.__init__(self)
        ConstructieElement.__init__(self)
        ConstructieElementenGC.__init__(self)

        self.afmetingen = DtcAfmetingBxlxhInM()
        """Met dit complex datatype worden de afmetingen van de plint weergegeven. Indien de plint afwijkt van een rechthoekige vorm wordt deze informatie in de technische fiche opgeslagen."""
        self.afmetingen.naam = "afmetingen"
        self.afmetingen.label = "afmetingen"
        self.afmetingen.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PlintGC.afmetingen"
        self.afmetingen.definition = "Met dit complex datatype worden de afmetingen van de plint weergegeven. Indien de plint afwijkt van een rechthoekige vorm wordt deze informatie in de technische fiche opgeslagen."
        self.afmetingen.constraints = ""
        self.afmetingen.usagenote = ""
        self.afmetingen.deprecated_version = ""

        self.plaatsingswijze = KeuzelijstField(naam="plaatsingswijze",
                                               label="plaatsingswijze",
                                               lijst=KlPlaatsingswijzePlint(),
                                               objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PlintGC.plaatsingswijze",
                                               definition="De manier waarop de plint geplaatst is ten opzichte van de profielen.",
                                               constraints="",
                                               usagenote="",
                                               deprecated_version="")
        """De manier waarop de plint geplaatst is ten opzichte van de profielen."""

        self.technischeFiche = DtcDocument()
        """Document met verdere specificaties van de plint die niet opgevangen worden met de aanwezige attributen."""
        self.technischeFiche.naam = "technischeFiche"
        self.technischeFiche.label = "technische fiche"
        self.technischeFiche.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PlintGC.technischeFiche"
        self.technischeFiche.definition = "Document met verdere specificaties van de plint die niet opgevangen worden met de aanwezige attributen."
        self.technischeFiche.constraints = ""
        self.technischeFiche.usagenote = ""
        self.technischeFiche.deprecated_version = ""
