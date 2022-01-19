# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Buitenkast import Buitenkast
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Montagekast(Buitenkast, AttributeInfo):
    """Een kleine kast voor binnen of buiten die net omwille van zijn beperkte omvang doorgaans aan een paal,muur of andere objecten bevestigd wordt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Buitenkast.__init__(self)

        self._eplanMechanischPlan = OTLAttribuut(field=DtcDocument,
                                                 naam='eplanMechanischPlan',
                                                 label='e-plan en m-plan',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast.eplanMechanischPlan',
                                                 usagenote='Bestanden van het type dwg.',
                                                 definition='Elektrisch aansluitschema van de kast en mechanisch plan van de volledige installatie in de kast.')

        self._opstelhoogte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='opstelhoogte',
                                          label='opstelhoogte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Montagekast.opstelhoogte',
                                          definition='De afstand tussen het maaiveld en de bovenrand van de montagekast in meter.')

    @property
    def eplanMechanischPlan(self):
        """Elektrisch aansluitschema van de kast en mechanisch plan van de volledige installatie in de kast."""
        return self._eplanMechanischPlan.waarde

    @eplanMechanischPlan.setter
    def eplanMechanischPlan(self, value):
        self._eplanMechanischPlan.set_waarde(value, owner=self)

    @property
    def opstelhoogte(self):
        """De afstand tussen het maaiveld en de bovenrand van de montagekast in meter."""
        return self._opstelhoogte.waarde

    @opstelhoogte.setter
    def opstelhoogte(self, value):
        self._opstelhoogte.set_waarde(value, owner=self)
