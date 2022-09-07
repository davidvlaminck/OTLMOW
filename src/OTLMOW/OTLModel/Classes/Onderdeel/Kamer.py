# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.PutRelatie import PutRelatie
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlKamerKlasse import KlKamerKlasse
from OTLMOW.OTLModel.Datatypes.KlPutMateriaal import KlPutMateriaal
from OTLMOW.OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kamer(PutRelatie, VlakGeometrie):
    """Een kamer is een aanééngesloten ondergrondse constructie waarbinnen vrije stroming van water over de bodem mogelijk is. Een constructie of inspectieput kan één of meerdere kamers hebben."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        PutRelatie.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bovenbouw', deprecated='2.1.0')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PutBovenbouw')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#BlindePut')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#InspectieputRiolering')

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.breedte',
                                     definition='De afmeting 1 (breedte) van het grondplan van de putkamer in millimeter.',
                                     owner=self)

        self._diepte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.diepte',
                                    definition='De diepte van de putkamer in meter.',
                                    owner=self)

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.hoogte',
                                    definition='De afmeting 2 (hoogte) van het grondplan van de putkamer in millimeter.',
                                    owner=self)

        self._klasse = OTLAttribuut(field=KlKamerKlasse,
                                    naam='klasse',
                                    label='klasse',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.klasse',
                                    definition='De stabiliteitsklasse van de kamer.',
                                    owner=self)

        self._materiaal = OTLAttribuut(field=KlPutMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.materiaal',
                                       definition='Het materiaal waaruit de kamer opgebouwd is.',
                                       owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.technischeFiche',
                                             usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de kamer.',
                                             owner=self)

        self._vorm = OTLAttribuut(field=KlRioleringVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Kamer.vorm',
                                  definition='De vorm van de kamer.',
                                  owner=self)

    @property
    def breedte(self):
        """De afmeting 1 (breedte) van het grondplan van de putkamer in millimeter."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def diepte(self):
        """De diepte van de putkamer in meter."""
        return self._diepte.get_waarde()

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De afmeting 2 (hoogte) van het grondplan van de putkamer in millimeter."""
        return self._hoogte.get_waarde()

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def klasse(self):
        """De stabiliteitsklasse van de kamer."""
        return self._klasse.get_waarde()

    @klasse.setter
    def klasse(self, value):
        self._klasse.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit de kamer opgebouwd is."""
        return self._materiaal.get_waarde()

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de kamer."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """De vorm van de kamer."""
        return self._vorm.get_waarde()

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
