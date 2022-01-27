# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlVoorschakelapparaatType import KlVoorschakelapparaatType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voorschakelapparaat(AIMObject):
    """Het voorschakelapparaat van een ontladingslamp in ruime zin omvat alle componenten die in serie of in parallel met de lamp geschakeld worden om haar goede werking te verzekeren. Ze bestaat in 2 uitvoeringsvormen elektromagnetische en elektronische.
Voor de elektromagnetische bestaat deze uit 
*de ballast: een elektromagnetische eenheid, die d.m.v. passieve componenten zoals een spoel of een condensator en/of actieve componenten, hoofdzakelijk dient om de lampstroom te beperken tot de vereiste waarde;
*een starter of een ontsteker: levert de vereiste ontsteekspanning;
*een condensator:is een component die de faseverschuiving tussen de stroom en spanning tot een aanvaardbare waarde terugbrengt en op die manier de arbeidsfactor verbetert;
*de eventuele externe beveiligingen;
*de onderlinge bekabeling."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorschakelapparaat'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._type = OTLAttribuut(field=KlVoorschakelapparaatType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voorschakelapparaat.type',
                                  definition='Type van het voorschakelapparaat.')

    @property
    def type(self):
        """Type van het voorschakelapparaat."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
