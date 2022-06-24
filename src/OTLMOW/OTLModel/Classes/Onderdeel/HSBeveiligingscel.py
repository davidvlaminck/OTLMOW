# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlHSBeveiligingscelHoogspanningszekering import KlHSBeveiligingscelHoogspanningszekering
from OTLMOW.OTLModel.Datatypes.KlHSBeveiligingscelMerk import KlHSBeveiligingscelMerk
from OTLMOW.OTLModel.Datatypes.KlHSBeveiligingscelModelnaam import KlHSBeveiligingscelModelnaam
from OTLMOW.OTLModel.Datatypes.KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar import KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar
from OTLMOW.OTLModel.Datatypes.KlHSBeveiligingscelSchakelmateriaalKlasse import KlHSBeveiligingscelSchakelmateriaalKlasse
from OTLMOW.OTLModel.Datatypes.KlHSBeveiligingscelSchakelmateriaalType import KlHSBeveiligingscelSchakelmateriaalType
from OTLMOW.OTLModel.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere
from OTLMOW.OTLModel.Datatypes.KwantWrdInJaar import KwantWrdInJaar
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HSBeveiligingscel(AIMNaamObject, PuntGeometrie):
    """Cel die de hoogspanningsschakelinrichting omvat. Hieronder vallen onder meer de lastscheidingsschakelaar, smeltveiligheden, aardingsschakelaar,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._elektrischSchema = OTLAttribuut(field=DtcDocument,
                                              naam='elektrischSchema',
                                              label='elektrisch schema',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.elektrischSchema',
                                              definition='Elektrisch aansluitschema van de HS beveiligingscel.',
                                              owner=self)

        self._heeftreserveZekering = OTLAttribuut(field=BooleanField,
                                                  naam='heeftreserveZekering',
                                                  label='heeft reserve zekering',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.heeftreserveZekering',
                                                  definition='Is er een reserve zekering aanwezig?',
                                                  owner=self)

        self._hoogspanningszekering = OTLAttribuut(field=KlHSBeveiligingscelHoogspanningszekering,
                                                   naam='hoogspanningszekering',
                                                   label='hoogspanningszekering',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.hoogspanningszekering',
                                                   definition='Waarde van de hoogspanningszekering.',
                                                   owner=self)

        self._keuringsfrequentie = OTLAttribuut(field=KwantWrdInJaar,
                                                naam='keuringsfrequentie',
                                                label='keuringsfrequentie',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.keuringsfrequentie',
                                                definition='Frequentie (in jaar) waarmee de installatie moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle.',
                                                owner=self)

        self._merk = OTLAttribuut(field=KlHSBeveiligingscelMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.merk',
                                  definition='Merk van de HS beveiligingscel.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlHSBeveiligingscelModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.modelnaam',
                                       definition='Modelnaam van de HS beveiligingscel.',
                                       owner=self)

        self._overstroombeveiligingInstelwaarde = OTLAttribuut(field=KwantWrdInAmpere,
                                                               naam='overstroombeveiligingInstelwaarde',
                                                               label='overstroombeveiliging instelwaarde',
                                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.overstroombeveiligingInstelwaarde',
                                                               definition='Instelwaarde van de overstroombeveiliging.',
                                                               owner=self)

        self._overstroombeveiligingType = OTLAttribuut(field=StringField,
                                                       naam='overstroombeveiligingType',
                                                       label='overstroombeveiliging type',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.overstroombeveiligingType',
                                                       definition='Type overstroombeveiliging.',
                                                       owner=self)

        self._overstroombeveiligingVermogenschakelaar = OTLAttribuut(field=KlHSBeveiligingscelOverstroombeveiligingVermogenschakelaar,
                                                                     naam='overstroombeveiligingVermogenschakelaar',
                                                                     label='overstroombeveiliging vermogenschakelaar',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.overstroombeveiligingVermogenschakelaar',
                                                                     definition='Directe of indirecte overstroombeveiliging van de vermogenschakelaar.',
                                                                     owner=self)

        self._schakelmateriaalKlasse = OTLAttribuut(field=KlHSBeveiligingscelSchakelmateriaalKlasse,
                                                    naam='schakelmateriaalKlasse',
                                                    label='schakelmateriaal klasse',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.schakelmateriaalKlasse',
                                                    definition='Klasse van het schakelmateriaal volgens Synergrid.',
                                                    owner=self)

        self._schakelmateriaalType = OTLAttribuut(field=KlHSBeveiligingscelSchakelmateriaalType,
                                                  naam='schakelmateriaalType',
                                                  label='schakelmateriaal type',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HSBeveiligingscel.schakelmateriaalType',
                                                  definition='Type van schakelmateriaal.',
                                                  owner=self)

    @property
    def elektrischSchema(self):
        """Elektrisch aansluitschema van de HS beveiligingscel."""
        return self._elektrischSchema.get_waarde()

    @elektrischSchema.setter
    def elektrischSchema(self, value):
        self._elektrischSchema.set_waarde(value, owner=self)

    @property
    def heeftreserveZekering(self):
        """Is er een reserve zekering aanwezig?"""
        return self._heeftreserveZekering.get_waarde()

    @heeftreserveZekering.setter
    def heeftreserveZekering(self, value):
        self._heeftreserveZekering.set_waarde(value, owner=self)

    @property
    def hoogspanningszekering(self):
        """Waarde van de hoogspanningszekering."""
        return self._hoogspanningszekering.get_waarde()

    @hoogspanningszekering.setter
    def hoogspanningszekering(self, value):
        self._hoogspanningszekering.set_waarde(value, owner=self)

    @property
    def keuringsfrequentie(self):
        """Frequentie (in jaar) waarmee de installatie moet onderworpen worden aan een periodieke keuring door een externe dienst voor technische controle."""
        return self._keuringsfrequentie.get_waarde()

    @keuringsfrequentie.setter
    def keuringsfrequentie(self, value):
        self._keuringsfrequentie.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merk van de HS beveiligingscel."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Modelnaam van de HS beveiligingscel."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def overstroombeveiligingInstelwaarde(self):
        """Instelwaarde van de overstroombeveiliging."""
        return self._overstroombeveiligingInstelwaarde.get_waarde()

    @overstroombeveiligingInstelwaarde.setter
    def overstroombeveiligingInstelwaarde(self, value):
        self._overstroombeveiligingInstelwaarde.set_waarde(value, owner=self)

    @property
    def overstroombeveiligingType(self):
        """Type overstroombeveiliging."""
        return self._overstroombeveiligingType.get_waarde()

    @overstroombeveiligingType.setter
    def overstroombeveiligingType(self, value):
        self._overstroombeveiligingType.set_waarde(value, owner=self)

    @property
    def overstroombeveiligingVermogenschakelaar(self):
        """Directe of indirecte overstroombeveiliging van de vermogenschakelaar."""
        return self._overstroombeveiligingVermogenschakelaar.get_waarde()

    @overstroombeveiligingVermogenschakelaar.setter
    def overstroombeveiligingVermogenschakelaar(self, value):
        self._overstroombeveiligingVermogenschakelaar.set_waarde(value, owner=self)

    @property
    def schakelmateriaalKlasse(self):
        """Klasse van het schakelmateriaal volgens Synergrid."""
        return self._schakelmateriaalKlasse.get_waarde()

    @schakelmateriaalKlasse.setter
    def schakelmateriaalKlasse(self, value):
        self._schakelmateriaalKlasse.set_waarde(value, owner=self)

    @property
    def schakelmateriaalType(self):
        """Type van schakelmateriaal."""
        return self._schakelmateriaalType.get_waarde()

    @schakelmateriaalType.setter
    def schakelmateriaalType(self, value):
        self._schakelmateriaalType.set_waarde(value, owner=self)
