# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVLuskaart(AIMNaamObject, PuntGeometrie):
    """Meten in Vlaanderen : kaart in LVE- of SAT- rack met de analoge circuits voor de lussen en analoog/digitaal conversie."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._lussenMeetrapport = OTLAttribuut(field=DtcDocument,
                                               naam='lussenMeetrapport',
                                               label='lussen meetrapport',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLuskaart.lussenMeetrapport',
                                               usagenote='Bestanden van het type pdf.',
                                               definition='De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen.',
                                               owner=self)

    @property
    def lussenMeetrapport(self):
        """De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen."""
        return self._lussenMeetrapport.get_waarde()

    @lussenMeetrapport.setter
    def lussenMeetrapport(self, value):
        self._lussenMeetrapport.set_waarde(value, owner=self)
