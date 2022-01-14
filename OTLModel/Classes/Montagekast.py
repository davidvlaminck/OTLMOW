# coding=utf-8
from OTLModel.Classes.Buitenkast import Buitenkast
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Montagekast(Buitenkast):
    """Een kleine kast voor binnen of buiten die net omwille van zijn beperkte omvang doorgaans aan een paal,muur of andere objecten bevestigd wordt."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.eplanMechanischPlan = DtcDocument()
        """Elektrisch aansluitschema van de kast en mechanisch plan van de volledige installatie in de kast."""
        self.eplanMechanischPlan.naam = "eplanMechanischPlan"
        self.eplanMechanischPlan.label = "e-plan en m-plan"
        self.eplanMechanischPlan.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast.eplanMechanischPlan"
        self.eplanMechanischPlan.definition = "Elektrisch aansluitschema van de kast en mechanisch plan van de volledige installatie in de kast."
        self.eplanMechanischPlan.constraints = ""
        self.eplanMechanischPlan.usagenote = "Bestanden van het type dwg."
        self.eplanMechanischPlan.deprecated_version = ""

        self.opstelhoogte = KwantWrdInMeter()
        """De afstand tussen het maaiveld en de bovenrand van de montagekast in meter."""
        self.opstelhoogte.naam = "opstelhoogte"
        self.opstelhoogte.label = "opstelhoogte"
        self.opstelhoogte.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast.opstelhoogte"
        self.opstelhoogte.definition = "De afstand tussen het maaiveld en de bovenrand van de montagekast in meter."
        self.opstelhoogte.constraints = ""
        self.opstelhoogte.usagenote = ""
        self.opstelhoogte.deprecated_version = ""
