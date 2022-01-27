# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.PutRelatie import PutRelatie
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.KlPutMateriaal import KlPutMateriaal
from src.OTLMOW.OTLModel.Datatypes.KlRioleringVorm import KlRioleringVorm
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Schacht(PutRelatie):
    """Gedeelte van de put tussen regeling en de kamer."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.breedte',
                                     definition='De afmeting 1 (breedte) van het grondplan van de schacht in millimeter.')

        self._diepte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.diepte',
                                    definition='De diepte vanaf het maaiveld tot onderkant van de afdekplaat in meter.')

        self._heeftLadder = OTLAttribuut(field=BooleanField,
                                         naam='heeftLadder',
                                         label='heeft ladder',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.heeftLadder',
                                         definition='Bepaling of er al dan niet een ladder aanwezig is in de schacht.')

        self._hoogte = OTLAttribuut(field=KwantWrdInMillimeter,
                                    naam='hoogte',
                                    label='hoogte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.hoogte',
                                    definition='De afmeting 2 (hoogte) van het grondplan van de schacht in millimeter.')

        self._materiaal = OTLAttribuut(field=KlPutMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.materiaal',
                                       definition='Het materiaal waaruit de schacht opgebouwd is.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.technischeFiche',
                                             usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van de schacht.')

        self._vorm = OTLAttribuut(field=KlRioleringVorm,
                                  naam='vorm',
                                  label='vorm',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Schacht.vorm',
                                  definition='Vorm van het schachtgedeelte van de kamer.')

    @property
    def breedte(self):
        """De afmeting 1 (breedte) van het grondplan van de schacht in millimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def diepte(self):
        """De diepte vanaf het maaiveld tot onderkant van de afdekplaat in meter."""
        return self._diepte.waarde

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self)

    @property
    def heeftLadder(self):
        """Bepaling of er al dan niet een ladder aanwezig is in de schacht."""
        return self._heeftLadder.waarde

    @heeftLadder.setter
    def heeftLadder(self, value):
        self._heeftLadder.set_waarde(value, owner=self)

    @property
    def hoogte(self):
        """De afmeting 2 (hoogte) van het grondplan van de schacht in millimeter."""
        return self._hoogte.waarde

    @hoogte.setter
    def hoogte(self, value):
        self._hoogte.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Het materiaal waaruit de schacht opgebouwd is."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de schacht."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def vorm(self):
        """Vorm van het schachtgedeelte van de kamer."""
        return self._vorm.waarde

    @vorm.setter
    def vorm(self, value):
        self._vorm.set_waarde(value, owner=self)
