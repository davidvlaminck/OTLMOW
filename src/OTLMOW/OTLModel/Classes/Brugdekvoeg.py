# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlTypeBrugdekvoeg import KlTypeBrugdekvoeg
from OTLMOW.OTLModel.Datatypes.KlTypeVerankeringBrugdekvoeg import KlTypeVerankeringBrugdekvoeg
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brugdekvoeg(AIMNaamObject):
    """Voegconstructie die dient om een opening te overbruggen. Voldoende vervormbaar om zich te kunnen aanpassen aan de bewegingen van de boorden en weerstandbiedend om belastingen te kunnen opvangen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._detailplan = OTLAttribuut(field=DtcDocument,
                                        naam='detailplan',
                                        label='detailplan',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.detailplan',
                                        definition='Het detailplan van de brugdekvoeg.',
                                        owner=self)

        self._dilatatieCapaciteit = OTLAttribuut(field=KwantWrdInMillimeter,
                                                 naam='dilatatieCapaciteit',
                                                 label='dilatatie capaciteit',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.dilatatieCapaciteit',
                                                 definition='TODO',
                                                 owner=self)

        self._isGeluidsarm = OTLAttribuut(field=BooleanField,
                                          naam='isGeluidsarm',
                                          label='is geluidsarm',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.isGeluidsarm',
                                          definition='Geeft aan of de brugdekvoeg al dan niet geluidsarm is.',
                                          owner=self)

        self._isWaterdicht = OTLAttribuut(field=BooleanField,
                                          naam='isWaterdicht',
                                          label='is waterdicht',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.isWaterdicht',
                                          definition='Geeft aan of de brugdekvoeg al dan niet waterdicht is.',
                                          owner=self)

        self._lopendeMeterVoeg = OTLAttribuut(field=KwantWrdInMeter,
                                              naam='lopendeMeterVoeg',
                                              label='lopende meter voeg',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.lopendeMeterVoeg',
                                              definition='De lopende meter van de brugdekvoeg.',
                                              owner=self)

        self._typeBrugdekvoeg = OTLAttribuut(field=KlTypeBrugdekvoeg,
                                             naam='typeBrugdekvoeg',
                                             label='type brugdekvoeg',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.typeBrugdekvoeg',
                                             definition='Het type van de brugdekvoeg.',
                                             owner=self)

        self._typeVerankering = OTLAttribuut(field=KlTypeVerankeringBrugdekvoeg,
                                             naam='typeVerankering',
                                             label='type verankering',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Brugdekvoeg.typeVerankering',
                                             definition='Het type van de verankering van de brugdekvoeg.',
                                             owner=self)

    @property
    def detailplan(self):
        """Het detailplan van de brugdekvoeg."""
        return self._detailplan.get_waarde()

    @detailplan.setter
    def detailplan(self, value):
        self._detailplan.set_waarde(value, owner=self)

    @property
    def dilatatieCapaciteit(self):
        """TODO"""
        return self._dilatatieCapaciteit.get_waarde()

    @dilatatieCapaciteit.setter
    def dilatatieCapaciteit(self, value):
        self._dilatatieCapaciteit.set_waarde(value, owner=self)

    @property
    def isGeluidsarm(self):
        """Geeft aan of de brugdekvoeg al dan niet geluidsarm is."""
        return self._isGeluidsarm.get_waarde()

    @isGeluidsarm.setter
    def isGeluidsarm(self, value):
        self._isGeluidsarm.set_waarde(value, owner=self)

    @property
    def isWaterdicht(self):
        """Geeft aan of de brugdekvoeg al dan niet waterdicht is."""
        return self._isWaterdicht.get_waarde()

    @isWaterdicht.setter
    def isWaterdicht(self, value):
        self._isWaterdicht.set_waarde(value, owner=self)

    @property
    def lopendeMeterVoeg(self):
        """De lopende meter van de brugdekvoeg."""
        return self._lopendeMeterVoeg.get_waarde()

    @lopendeMeterVoeg.setter
    def lopendeMeterVoeg(self, value):
        self._lopendeMeterVoeg.set_waarde(value, owner=self)

    @property
    def typeBrugdekvoeg(self):
        """Het type van de brugdekvoeg."""
        return self._typeBrugdekvoeg.get_waarde()

    @typeBrugdekvoeg.setter
    def typeBrugdekvoeg(self, value):
        self._typeBrugdekvoeg.set_waarde(value, owner=self)

    @property
    def typeVerankering(self):
        """Het type van de verankering van de brugdekvoeg."""
        return self._typeVerankering.get_waarde()

    @typeVerankering.setter
    def typeVerankering(self, value):
        self._typeVerankering.set_waarde(value, owner=self)
