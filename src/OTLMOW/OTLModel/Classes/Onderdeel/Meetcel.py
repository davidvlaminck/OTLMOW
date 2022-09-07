# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlMeetcelNauwkeurigheidsklasse import KlMeetcelNauwkeurigheidsklasse
from OTLMOW.OTLModel.Datatypes.KlMeetcelNauwkeurigheidsvermogen import KlMeetcelNauwkeurigheidsvermogen
from OTLMOW.OTLModel.Datatypes.KlMeetcelVeiligheidsfactor import KlMeetcelVeiligheidsfactor
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Meetcel(AIMNaamObject, PuntGeometrie):
    """Een cel voorzien met uitrusting voor het meten van het energieverbruik aan de hoogspanningszijde van de transformator."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator')

        self._nauwkeurigheidsklasse = OTLAttribuut(field=KlMeetcelNauwkeurigheidsklasse,
                                                   naam='nauwkeurigheidsklasse',
                                                   label='nauwkeurigheidsklasse',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.nauwkeurigheidsklasse',
                                                   definition='Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...).',
                                                   owner=self)

        self._nauwkeurigheidsvermogen = OTLAttribuut(field=KlMeetcelNauwkeurigheidsvermogen,
                                                     naam='nauwkeurigheidsvermogen',
                                                     label='nauwkeurigheidsvermogen',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.nauwkeurigheidsvermogen',
                                                     definition='Nauwkeurigheidsvermogen van de meetcel (vb 5;15).',
                                                     owner=self)

        self._transformatieverhouding = OTLAttribuut(field=StringField,
                                                     naam='transformatieverhouding',
                                                     label='transformatieverhouding',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.transformatieverhouding',
                                                     definition='Verhouding van de transformatie (vb 25/5;50/5; (5500/v3)/( 110/v3);...).',
                                                     owner=self)

        self._veiligheidsfactor = OTLAttribuut(field=KlMeetcelVeiligheidsfactor,
                                               naam='veiligheidsfactor',
                                               label='veiligheidsfactor',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Meetcel.veiligheidsfactor',
                                               definition='Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom.',
                                               owner=self)

    @property
    def nauwkeurigheidsklasse(self):
        """Nauwkeurigheidsklasse van de meetcel (vb 0,2; 0,2s; 0,5; ...)."""
        return self._nauwkeurigheidsklasse.get_waarde()

    @nauwkeurigheidsklasse.setter
    def nauwkeurigheidsklasse(self, value):
        self._nauwkeurigheidsklasse.set_waarde(value, owner=self)

    @property
    def nauwkeurigheidsvermogen(self):
        """Nauwkeurigheidsvermogen van de meetcel (vb 5;15)."""
        return self._nauwkeurigheidsvermogen.get_waarde()

    @nauwkeurigheidsvermogen.setter
    def nauwkeurigheidsvermogen(self, value):
        self._nauwkeurigheidsvermogen.set_waarde(value, owner=self)

    @property
    def transformatieverhouding(self):
        """Verhouding van de transformatie (vb 25/5;50/5; (5500/v3)/( 110/v3);...)."""
        return self._transformatieverhouding.get_waarde()

    @transformatieverhouding.setter
    def transformatieverhouding(self, value):
        self._transformatieverhouding.set_waarde(value, owner=self)

    @property
    def veiligheidsfactor(self):
        """Verhouding tussen de toegekende primaire limietstroom van de meetcel en de toegekende primaire stroom."""
        return self._veiligheidsfactor.get_waarde()

    @veiligheidsfactor.setter
    def veiligheidsfactor(self, value):
        self._veiligheidsfactor.set_waarde(value, owner=self)
