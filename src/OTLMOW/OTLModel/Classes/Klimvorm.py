# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.VegetatieElement import VegetatieElement
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Klimvorm(VegetatieElement, PuntGeometrie):
    """Plant met buigzame stengels die zich aan muren,bomen,enz. hecht en zodoende omhoog klimt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        VegetatieElement.__init__(self)
        PuntGeometrie.__init__(self)

        self._begroeidOppervlak = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                               naam='begroeidOppervlak',
                                               label='begroeid oppervlak',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm.begroeidOppervlak',
                                               definition='Verticale oppervlakte dat begroeid is in vierkante meter.',
                                               owner=self)

        self._heeftBeheerScheren = OTLAttribuut(field=BooleanField,
                                                naam='heeftBeheerScheren',
                                                label='heeft beheer scheren',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm.heeftBeheerScheren',
                                                definition='Duidt aan of de klimvorm al dan niet geschoren wordt.',
                                                owner=self)

        self._heeftBevestigingconstructie = OTLAttribuut(field=BooleanField,
                                                         naam='heeftBevestigingconstructie',
                                                         label='Heeft bevestigingsconstructie',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm.heeftBevestigingconstructie',
                                                         definition='Aanduiding of de klimvorm een bevestigingsconstructie heeft om aan bv een geluidswerende constructie vastgemaakt te worden.',
                                                         owner=self)

        self._isGrondgebonden = OTLAttribuut(field=BooleanField,
                                             naam='isGrondgebonden',
                                             label='is grondgebonden',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm.isGrondgebonden',
                                             definition='Duidt aan of de klimvorm al dan niet in volle grond staat.',
                                             owner=self)

        self._isZelfhechtend = OTLAttribuut(field=BooleanField,
                                            naam='isZelfhechtend',
                                            label='is zelfhechtend',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimvorm.isZelfhechtend',
                                            definition='Geeft aan of de klimplant (zoals klimop of wingerd) rechtstreeks op de muur kan groeien zonder nood aan een draagstructuur.',
                                            owner=self)

    @property
    def begroeidOppervlak(self):
        """Verticale oppervlakte dat begroeid is in vierkante meter."""
        return self._begroeidOppervlak.waarde

    @begroeidOppervlak.setter
    def begroeidOppervlak(self, value):
        self._begroeidOppervlak.set_waarde(value, owner=self)

    @property
    def heeftBeheerScheren(self):
        """Duidt aan of de klimvorm al dan niet geschoren wordt."""
        return self._heeftBeheerScheren.waarde

    @heeftBeheerScheren.setter
    def heeftBeheerScheren(self, value):
        self._heeftBeheerScheren.set_waarde(value, owner=self)

    @property
    def heeftBevestigingconstructie(self):
        """Aanduiding of de klimvorm een bevestigingsconstructie heeft om aan bv een geluidswerende constructie vastgemaakt te worden."""
        return self._heeftBevestigingconstructie.waarde

    @heeftBevestigingconstructie.setter
    def heeftBevestigingconstructie(self, value):
        self._heeftBevestigingconstructie.set_waarde(value, owner=self)

    @property
    def isGrondgebonden(self):
        """Duidt aan of de klimvorm al dan niet in volle grond staat."""
        return self._isGrondgebonden.waarde

    @isGrondgebonden.setter
    def isGrondgebonden(self, value):
        self._isGrondgebonden.set_waarde(value, owner=self)

    @property
    def isZelfhechtend(self):
        """Geeft aan of de klimplant (zoals klimop of wingerd) rechtstreeks op de muur kan groeien zonder nood aan een draagstructuur."""
        return self._isZelfhechtend.waarde

    @isZelfhechtend.setter
    def isZelfhechtend(self, value):
        self._isZelfhechtend.set_waarde(value, owner=self)
