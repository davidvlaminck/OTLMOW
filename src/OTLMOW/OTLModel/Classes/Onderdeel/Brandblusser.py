# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DateField import DateField
from OTLMOW.OTLModel.Datatypes.KlBrandblusserBlusmiddel import KlBrandblusserBlusmiddel
from OTLMOW.OTLModel.Datatypes.KlBrandblusserGewicht import KlBrandblusserGewicht
from OTLMOW.OTLModel.Datatypes.KlBrandblusserType import KlBrandblusserType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brandblusser(AIMObject, PuntGeometrie):
    """Een apparaat om het vuur van een kleine brand mee te doven. Het bestaat uit een cilinder waarin een beperkte hoeveelheid blusmiddel onder druk staat."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactpunt')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hulppostkast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Hulppost')

        self._aankoopdatum = OTLAttribuut(field=DateField,
                                          naam='aankoopdatum',
                                          label='aankoopdatum',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.aankoopdatum',
                                          definition='Datum wordt het toestel is aangekocht.',
                                          owner=self)

        self._blusmiddel = OTLAttribuut(field=KlBrandblusserBlusmiddel,
                                        naam='blusmiddel',
                                        label='blusmiddel',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.blusmiddel',
                                        definition='Substantie waarmee het toestel gevuld is in functie van het blussen van vuur.',
                                        owner=self)

        self._gewicht = OTLAttribuut(field=KlBrandblusserGewicht,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.gewicht',
                                     definition='Totaal gewicht van het gevulde toestel.',
                                     owner=self)

        self._keuringsdatum = OTLAttribuut(field=DateField,
                                           naam='keuringsdatum',
                                           label='keuringsdatum',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.keuringsdatum',
                                           definition='Datum waarop het toestel laatst is gekeurd.',
                                           owner=self)

        self._type = OTLAttribuut(field=KlBrandblusserType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brandblusser.type',
                                  definition='Het type van de brandblusser.',
                                  owner=self)

    @property
    def aankoopdatum(self):
        """Datum wordt het toestel is aangekocht."""
        return self._aankoopdatum.get_waarde()

    @aankoopdatum.setter
    def aankoopdatum(self, value):
        self._aankoopdatum.set_waarde(value, owner=self)

    @property
    def blusmiddel(self):
        """Substantie waarmee het toestel gevuld is in functie van het blussen van vuur."""
        return self._blusmiddel.get_waarde()

    @blusmiddel.setter
    def blusmiddel(self, value):
        self._blusmiddel.set_waarde(value, owner=self)

    @property
    def gewicht(self):
        """Totaal gewicht van het gevulde toestel."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def keuringsdatum(self):
        """Datum waarop het toestel laatst is gekeurd."""
        return self._keuringsdatum.get_waarde()

    @keuringsdatum.setter
    def keuringsdatum(self, value):
        self._keuringsdatum.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de brandblusser."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
