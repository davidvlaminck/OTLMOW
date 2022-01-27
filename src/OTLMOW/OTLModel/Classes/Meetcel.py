# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Datatypes.KlMeetcelNauwkeurigheidsklasse import KlMeetcelNauwkeurigheidsklasse
from src.OTLMOW.OTLModel.Datatypes.KlMeetcelNauwkeurigheidsvermogen import KlMeetcelNauwkeurigheidsvermogen
from src.OTLMOW.OTLModel.Datatypes.KlMeetcelVeiligheidsfactor import KlMeetcelVeiligheidsfactor
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Meetcel(AIMNaamObject):
    """Een cel voorzien met uitrusting voor het meten van het energieverbruik aan de hoogspanningszijde van de transformator."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._nauwkeurigheidsklasse = OTLAttribuut(field=KlMeetcelNauwkeurigheidsklasse,
                                                   naam='nauwkeurigheidsklasse',
                                                   label='nauwkeurigheidsklasse',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.nauwkeurigheidsklasse',
                                                   definition='Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...).')

        self._nauwkeurigheidsvermogen = OTLAttribuut(field=KlMeetcelNauwkeurigheidsvermogen,
                                                     naam='nauwkeurigheidsvermogen',
                                                     label='nauwkeurigheidsvermogen',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.nauwkeurigheidsvermogen',
                                                     definition='Nauwkeurigheidsvermogen van de meetcel (vb 5;15).')

        self._transformatieverhouding = OTLAttribuut(field=StringField,
                                                     naam='transformatieverhouding',
                                                     label='transformatieverhouding',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.transformatieverhouding',
                                                     definition='Verhouding van de transformatie (vb 25/5;50/5; (5500/v3)/( 110/v3);...).')

        self._veiligheidsfactor = OTLAttribuut(field=KlMeetcelVeiligheidsfactor,
                                               naam='veiligheidsfactor',
                                               label='veiligheidsfactor',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.veiligheidsfactor',
                                               definition='Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom.')

    @property
    def nauwkeurigheidsklasse(self):
        """Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...)."""
        return self._nauwkeurigheidsklasse.waarde

    @nauwkeurigheidsklasse.setter
    def nauwkeurigheidsklasse(self, value):
        self._nauwkeurigheidsklasse.set_waarde(value, owner=self)

    @property
    def nauwkeurigheidsvermogen(self):
        """Nauwkeurigheidsvermogen van de meetcel (vb 5;15)."""
        return self._nauwkeurigheidsvermogen.waarde

    @nauwkeurigheidsvermogen.setter
    def nauwkeurigheidsvermogen(self, value):
        self._nauwkeurigheidsvermogen.set_waarde(value, owner=self)

    @property
    def transformatieverhouding(self):
        """Verhouding van de transformatie (vb 25/5;50/5; (5500/v3)/( 110/v3);...)."""
        return self._transformatieverhouding.waarde

    @transformatieverhouding.setter
    def transformatieverhouding(self, value):
        self._transformatieverhouding.set_waarde(value, owner=self)

    @property
    def veiligheidsfactor(self):
        """Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom."""
        return self._veiligheidsfactor.waarde

    @veiligheidsfactor.setter
    def veiligheidsfactor(self, value):
        self._veiligheidsfactor.set_waarde(value, owner=self)
