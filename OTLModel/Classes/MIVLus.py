# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlMIVLusUitslijprichting import KlMIVLusUitslijprichting
from OTLModel.Datatypes.KlMIVLusZichtbaarheid import KlMIVLusZichtbaarheid


# Generated with OTLClassCreator. To modify: extend, do not edit
class MIVLus(AIMNaamObject, AttributeInfo):
    """Meten in Vlaanderen : inductieve lus, ingeslepen in het wegdek."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)

        self._meetrapport = OTLAttribuut(field=DtcDocument,
                                         naam='meetrapport',
                                         label='meetrapport',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus.meetrapport',
                                         usagenote='Bestanden van het type pdf.',
                                         definition='De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen.')

        self._uitslijprichting = OTLAttribuut(field=KlMIVLusUitslijprichting,
                                              naam='uitslijprichting',
                                              label='uitslijprichting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus.uitslijprichting',
                                              definition='De uitlopers van de lus gaan naar links of naar rechts  bekeken ten opzichte van de rijrichting.')

        self._zichtbaarheid = OTLAttribuut(field=KlMIVLusZichtbaarheid,
                                           naam='zichtbaarheid',
                                           label='zichtbaarheid',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MIVLus.zichtbaarheid',
                                           definition='Is dus lus zichtbaar in het wegdek of bedekt door een toplaag.')

    @property
    def meetrapport(self):
        """De elektrische eigenschappen van de lus: R, L, C en de isolatieweerstand. Dit verzekert naast de afmetingen mee de voorziene nauwkeurigheid van de voertuigmetingen."""
        return self._meetrapport.waarde

    @meetrapport.setter
    def meetrapport(self, value):
        self._meetrapport.set_waarde(value, owner=self)

    @property
    def uitslijprichting(self):
        """De uitlopers van de lus gaan naar links of naar rechts  bekeken ten opzichte van de rijrichting."""
        return self._uitslijprichting.waarde

    @uitslijprichting.setter
    def uitslijprichting(self, value):
        self._uitslijprichting.set_waarde(value, owner=self)

    @property
    def zichtbaarheid(self):
        """Is dus lus zichtbaar in het wegdek of bedekt door een toplaag."""
        return self._zichtbaarheid.waarde

    @zichtbaarheid.setter
    def zichtbaarheid(self, value):
        self._zichtbaarheid.set_waarde(value, owner=self)
