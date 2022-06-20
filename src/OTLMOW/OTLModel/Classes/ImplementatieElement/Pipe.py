# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Leiding import Leiding
from OTLMOW.OTLModel.Classes.Abstracten.OmhullendeInrichting import OmhullendeInrichting
from OTLMOW.OTLModel.Datatypes.KlBeschermbuisKleur import KlBeschermbuisKleur
from OTLMOW.OTLModel.Datatypes.KlNetwerkType import KlNetwerkType
from OTLMOW.OTLModel.Datatypes.KlPipeContainerType import KlPipeContainerType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pipe(Leiding, OmhullendeInrichting):
    """Een buis die dienst kan doen als object voor het omhullen van meerdere kabels of andere (kleinere) leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pipe'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Leiding.__init__(self)
        OmhullendeInrichting.__init__(self)

        self._containerType = OTLAttribuut(field=KlPipeContainerType,
                                           naam='containerType',
                                           label='containertype',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pipe.containerType',
                                           definition='Attribuut dat het soort van kabel- en leidingcontainer aangeeft.',
                                           owner=self)

        self._kleur = OTLAttribuut(field=KlBeschermbuisKleur,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pipe.kleur',
                                   definition='Kleur van buitenmantel volgens een vaste lijst.',
                                   owner=self)

        self._netwerkType = OTLAttribuut(field=KlNetwerkType,
                                         naam='netwerkType',
                                         label='netwerktype',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Pipe.netwerkType',
                                         definition='Geeft aan bij welk type nutsvoorzieningennet de kabelmof hoort volgens de types uit IMKL en Inspire.',
                                         owner=self)

    @property
    def containerType(self):
        """Attribuut dat het soort van kabel- en leidingcontainer aangeeft."""
        return self._containerType.get_waarde()

    @containerType.setter
    def containerType(self, value):
        self._containerType.set_waarde(value, owner=self)

    @property
    def kleur(self):
        """Kleur van buitenmantel volgens een vaste lijst."""
        return self._kleur.get_waarde()

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def netwerkType(self):
        """Geeft aan bij welk type nutsvoorzieningennet de kabelmof hoort volgens de types uit IMKL en Inspire."""
        return self._netwerkType.get_waarde()

    @netwerkType.setter
    def netwerkType(self, value):
        self._netwerkType.set_waarde(value, owner=self)
