# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DtcAfmetingBxlxhInMm import DtcAfmetingBxlxhInMm
from OTLMOW.OTLModel.Datatypes.KlBinnenverlichtingstoestelSoortLamp import KlBinnenverlichtingstoestelSoortLamp
from OTLMOW.OTLModel.Datatypes.KlPictogramSymbool import KlPictogramSymbool
from OTLMOW.OTLModel.Datatypes.KwantWrdInMinuut import KwantWrdInMinuut


# Generated with OTLClassCreator. To modify: extend, do not edit
class InwendigVerlichtPictogram(AIMObject):
    """Verlichtingstoestel om de aandacht te vestigen op een pictogram dat erop bevestigd is."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._afmeting = OTLAttribuut(field=DtcAfmetingBxlxhInMm,
                                      naam='afmeting',
                                      label='afmeting',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.afmeting',
                                      definition='Geeft de buitenafmeting van het toestel mee.')

        self._nalichtingstijd = OTLAttribuut(field=KwantWrdInMinuut,
                                             naam='nalichtingstijd',
                                             label='nalichtingstijd',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.nalichtingstijd',
                                             definition='De tijd tussen het uitschakelen van de interne lichtbron en het volledig duister worden van het toestel.')

        self._symbool = OTLAttribuut(field=KlPictogramSymbool,
                                     naam='symbool',
                                     label='symbool',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.symbool',
                                     definition='Het symbool afgebeeld op het toestel.')

        self._typeLamp = OTLAttribuut(field=KlBinnenverlichtingstoestelSoortLamp,
                                      naam='typeLamp',
                                      label='type lamp',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#InwendigVerlichtPictogram.typeLamp',
                                      definition='Het soort lamp waarmee het toestel verlicht wordt.')

    @property
    def afmeting(self):
        """Geeft de buitenafmeting van het toestel mee."""
        return self._afmeting.waarde

    @afmeting.setter
    def afmeting(self, value):
        self._afmeting.set_waarde(value, owner=self)

    @property
    def nalichtingstijd(self):
        """De tijd tussen het uitschakelen van de interne lichtbron en het volledig duister worden van het toestel."""
        return self._nalichtingstijd.waarde

    @nalichtingstijd.setter
    def nalichtingstijd(self, value):
        self._nalichtingstijd.set_waarde(value, owner=self)

    @property
    def symbool(self):
        """Het symbool afgebeeld op het toestel."""
        return self._symbool.waarde

    @symbool.setter
    def symbool(self, value):
        self._symbool.set_waarde(value, owner=self)

    @property
    def typeLamp(self):
        """Het soort lamp waarmee het toestel verlicht wordt."""
        return self._typeLamp.waarde

    @typeLamp.setter
    def typeLamp(self, value):
        self._typeLamp.set_waarde(value, owner=self)
