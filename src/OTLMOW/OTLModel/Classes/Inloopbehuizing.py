# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLMOW.OTLModel.Classes.Behuizing import Behuizing
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlxhInM import DtcAfmetingBxlxhInM
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from OTLMOW.OTLModel.Datatypes.KlCabineMerk import KlCabineMerk
from OTLMOW.OTLModel.Datatypes.KlCabineModelnaam import KlCabineModelnaam
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Inloopbehuizing(Behuizing, VlakGeometrie):
    """Een behuizing voor het beschermen van technieken en materialen waarin het omwille van de grootte en toegankelijkheid mogelijk is om rond te lopen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        Behuizing.__init__(self)
        VlakGeometrie.__init__(self)

        self._afmeting = OTLAttribuut(field=DtcAfmetingBxlxhInM,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.afmeting',
                                      definition='Buitenafmetingen van het bovengronds gedeelte van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid.',
                                      owner=self)

        self._beschrijvingBereikbaarheid = OTLAttribuut(field=StringField,
                                                        naam='beschrijvingBereikbaarheid',
                                                        label='beschrijving bereikbaarheid',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.beschrijvingBereikbaarheid',
                                                        definition='Een beschrijving van de omgeving van de behuizing in functie van de bereikbaarheid en toegankelijkheid voor werken en toezicht.',
                                                        owner=self)

        self._grondplan = OTLAttribuut(field=DtcDocument,
                                       naam='grondplan',
                                       label='grondplan',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.grondplan',
                                       definition='Plattegrond van de behuizing met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer.',
                                       owner=self)

        self._inloopbehuizingMateriaal = OTLAttribuut(field=KlAlgMateriaal,
                                                      naam='inloopbehuizingMateriaal',
                                                      label='Cabine materiaal',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.inloopbehuizingMateriaal',
                                                      definition='Materiaal waaruit de cabine vervaardigd is zonder buitenafwerking van dak of wanden.',
                                                      owner=self)

        self._merk = OTLAttribuut(field=KlCabineMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.merk',
                                  definition='De merknaam volgens de fabrikant van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlCabineModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Inloopbehuizing.modelnaam',
                                       definition='Naam waarmee de fabrikant het model identificeert van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid.',
                                       owner=self)

    @property
    def afmeting(self):
        """Buitenafmetingen van het bovengronds gedeelte van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid."""
        return self._afmeting.waarde

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def beschrijvingBereikbaarheid(self):
        """Een beschrijving van de omgeving van de behuizing in functie van de bereikbaarheid en toegankelijkheid voor werken en toezicht."""
        return self._beschrijvingBereikbaarheid.waarde

    @beschrijvingBereikbaarheid.setter
    def beschrijvingBereikbaarheid(self, value):
        self._beschrijvingBereikbaarheid.set_waarde(value, owner=self)

    @property
    def grondplan(self):
        """Plattegrond van de behuizing met aanduidingen van de verschillende aanwezige elementen zoals kelder, kasten met kastnummers, toegangscontrole en meer."""
        return self._grondplan.waarde

    @grondplan.setter
    def grondplan(self, value):
        self._grondplan.set_waarde(value, owner=self)

    @property
    def inloopbehuizingMateriaal(self):
        """Materiaal waaruit de cabine vervaardigd is zonder buitenafwerking van dak of wanden."""
        return self._inloopbehuizingMateriaal.waarde

    @inloopbehuizingMateriaal.setter
    def inloopbehuizingMateriaal(self, value):
        self._inloopbehuizingMateriaal.set_waarde(value, owner=self)

    @property
    def merk(self):
        """De merknaam volgens de fabrikant van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Naam waarmee de fabrikant het model identificeert van een behuizing waarin het in principe mogelijk is om rond te lopen omwille van de grootte en toegankelijkheid."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
