# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlOverstortrandMateriaal import KlOverstortrandMateriaal
from OTLMOW.OTLModel.Datatypes.KlVariabelDeelType import KlVariabelDeelType
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Overstortrand(AIMObject, VlakGeometrie):
    """Een overstortrand heeft als doel het afvoeren van (pieken in) overtollig rioolwater vanuit de gemengde riolering naar het oppervlaktewater."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.breedte',
                                     definition='De afstand tussen de uiterste zijden van de overstortrand in millimeter.',
                                     owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.hoogte',
                                    definition='De afstand tussen de vaste drempel en het hoogste punt van de overstortrand in millimeter.',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlOverstortrandMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.materiaal',
                                       definition='Het materiaal waaruit de overstortrand vervaardigd is.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.technischeFiche',
                                             definition='De technische fiche van de de overstortrand.',
                                             owner=self)

        self._variabelDeelType = OTLAttribuut(field=KlVariabelDeelType,
                                              naam='variabelDeelType',
                                              label='variabel deel type',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.variabelDeelType',
                                              definition='Bepaalt het type van het variabel deel van de overstortrand.',
                                              owner=self)

        self._wanddikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                       naam='wanddikte',
                                       label='wanddikte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Overstortrand.wanddikte',
                                       definition='De wanddikte van de overstortrand in millimeter.',
                                       owner=self)

    @property
    def breedte(self):
        """De afstand tussen de uiterste zijden van de overstortrand in millimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De afstand tussen de vaste drempel en het hoogste punt van de overstortrand in millimeter."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit de overstortrand vervaardigd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de de overstortrand."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def variabelDeelType(self):
        """Bepaalt het type van het variabel deel van de overstortrand."""
        return self._variabelDeelType.get_waarde()

    @variabelDeelType.setter
    def variabelDeelType(self, value):
        self._variabelDeelType.set_waarde(value, owner=self)

    @property
    def wanddikte(self):
        """De wanddikte van de overstortrand in millimeter."""
        return self._wanddikte.get_waarde()

    @wanddikte.setter
    def wanddikte(self, value):
        self._wanddikte.set_waarde(value, owner=self)
