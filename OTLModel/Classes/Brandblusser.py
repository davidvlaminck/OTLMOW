# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DateField import DateField
from OTLModel.Datatypes.KlBrandblusserBlusmiddel import KlBrandblusserBlusmiddel
from OTLModel.Datatypes.KlBrandblusserGewicht import KlBrandblusserGewicht
from OTLModel.Datatypes.KlBrandblusserType import KlBrandblusserType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brandblusser(AIMObject):
    """Een apparaat om het vuur van een kleine brand mee te doven. Het bestaat uit een cilinder waarin een beperkte hoeveelheid blusmiddel onder druk staat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aankoopdatum = OTLAttribuut(field=DateField,
                                          naam='aankoopdatum',
                                          label='aankoopdatum',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.aankoopdatum',
                                          definition='Datum wordt het toestel is aangekocht.')

        self._blusmiddel = OTLAttribuut(field=KlBrandblusserBlusmiddel,
                                        naam='blusmiddel',
                                        label='blusmiddel',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.blusmiddel',
                                        definition='Substantie waarmee het toestel gevuld is in functie van het blussen van vuur.')

        self._gewicht = OTLAttribuut(field=KlBrandblusserGewicht,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.gewicht',
                                     definition='Totaal gewicht van het gevulde toestel.')

        self._keuringsdatum = OTLAttribuut(field=DateField,
                                           naam='keuringsdatum',
                                           label='keuringsdatum',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.keuringsdatum',
                                           definition='Datum waarop het toestel laatst is gekeurd.')

        self._type = OTLAttribuut(field=KlBrandblusserType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.type',
                                  definition='Het type van de brandblusser.')

    @property
    def aankoopdatum(self):
        """Datum wordt het toestel is aangekocht."""
        return self._aankoopdatum.waarde

    @aankoopdatum.setter
    def aankoopdatum(self, value):
        self._aankoopdatum.set_waarde(value, owner=self)

    @property
    def blusmiddel(self):
        """Substantie waarmee het toestel gevuld is in functie van het blussen van vuur."""
        return self._blusmiddel.waarde

    @blusmiddel.setter
    def blusmiddel(self, value):
        self._blusmiddel.set_waarde(value, owner=self)

    @property
    def gewicht(self):
        """Totaal gewicht van het gevulde toestel."""
        return self._gewicht.waarde

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def keuringsdatum(self):
        """Datum waarop het toestel laatst is gekeurd."""
        return self._keuringsdatum.waarde

    @keuringsdatum.setter
    def keuringsdatum(self, value):
        self._keuringsdatum.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de brandblusser."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
