# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.PutRelatie import PutRelatie
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlKamerKlasse import KlKamerKlasse
from OTLModel.Datatypes.KlPutMateriaal import KlPutMateriaal
from OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kamer(PutRelatie, AttributeInfo):
    """Een kamer is een aanééngesloten ondergrondse constructie waarbinnen vrije stroming van water over de bodem mogelijk is. Een constructie of inspectieput kan één of meerdere kamers hebben."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        PutRelatie.__init__(self)

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.breedte',
                                     definition='De afmeting 1 (breedte) van het grondplan van de putkamer in millimeter.')

        self._diepte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.diepte',
                                    definition='De diepte van de putkamer in meter.')

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.hoogte',
                                    definition='De afmeting 2 (hoogte) van het grondplan van de putkamer in millimeter.')

        self._klasse = OTLAttribuut(field=KlKamerKlasse,
                                    naam='klasse',
                                    label='klasse',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.klasse',
                                    definition='De stabiliteitsklasse van de kamer.')

        self._materiaal = OTLAttribuut(field=KlPutMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.materiaal',
                                       definition='Het materiaal waaruit de kamer opgebouwd is.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.technischeFiche',
                                             usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de kamer.')

        self._vorm = OTLAttribuut(field=KlRioleringVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.vorm',
                                  definition='De vorm van de kamer.')

    @property
    def breedte(self):
        """De afmeting 1 (breedte) van het grondplan van de putkamer in millimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def diepte(self):
        """De diepte van de putkamer in meter."""
        return self._diepte.waarde

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De afmeting 2 (hoogte) van het grondplan van de putkamer in millimeter."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def klasse(self):
        """De stabiliteitsklasse van de kamer."""
        return self._klasse.waarde

    @klasse.setter
    def klasse(self, value):
        self._klasse.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit de kamer opgebouwd is."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de kamer."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """De vorm van de kamer."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
