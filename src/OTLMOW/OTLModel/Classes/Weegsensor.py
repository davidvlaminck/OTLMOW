# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlWeegsensorMerk import KlWeegsensorMerk
from OTLMOW.OTLModel.Datatypes.KlWeegsensorModelnaam import KlWeegsensorModelnaam
from OTLMOW.OTLModel.Datatypes.KlWeegsensorType import KlWeegsensorType
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Weegsensor(AIMNaamObject, LijnGeometrie):
    """Registratie van de wieldruk van een voertuig (alle klassen). Dit wordt vertaald naar een massa."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        LijnGeometrie.__init__(self)

        self._meetrapport = OTLAttribuut(field=DtcDocument,
                                         naam='meetrapport',
                                         label='meetrapport',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.meetrapport',
                                         usagenote='Bestanden van het type pdf.',
                                         definition='Document met kalibratiegegevens (aantal rondes, types voertuigen,...).',
                                         owner=self)

        self._merk = OTLAttribuut(field=KlWeegsensorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.merk',
                                  definition='Het merk van de weegsensor.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlWeegsensorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.modelnaam',
                                       definition='De modelnaam van de weegsensor.',
                                       owner=self)

        self._rijstrook = OTLAttribuut(field=StringField,
                                       naam='rijstrook',
                                       label='rijstrook',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.rijstrook',
                                       definition='Beschrijft de rijstroken die door de weegsensor bewaakt worden.',
                                       owner=self)

        self._serienummer = OTLAttribuut(field=StringField,
                                         naam='serienummer',
                                         label='serienummer',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.serienummer',
                                         definition='Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is.',
                                         owner=self)

        self._type = OTLAttribuut(field=KlWeegsensorType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Weegsensor.type',
                                  definition='Het type van de weegsensor.',
                                  owner=self)

    @property
    def meetrapport(self):
        """Document met kalibratiegegevens (aantal rondes, types voertuigen,...)."""
        return self._meetrapport.get_waarde()

    @meetrapport.setter
    def meetrapport(self, value):
        self._meetrapport.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Het merk van de weegsensor."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de weegsensor."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def rijstrook(self):
        """Beschrijft de rijstroken die door de weegsensor bewaakt worden."""
        return self._rijstrook.get_waarde()

    @rijstrook.setter
    def rijstrook(self, value):
        self._rijstrook.set_waarde(value, owner=self)

    @property
    def serienummer(self):
        """Het unieke nummer waarmee het toestel door de fabrikant geïdentificeerd is."""
        return self._serienummer.get_waarde()

    @serienummer.setter
    def serienummer(self, value):
        self._serienummer.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type van de weegsensor."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
