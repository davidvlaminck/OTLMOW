# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.Proef import Proef
from src.OTLMOW.OTLModel.Datatypes.KlLEACKerendVermogen import KlLEACKerendVermogen


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefKerendVermogen(Proef):
    """Proef om het vermogen van een voertuigkering te bepalen om een doorbraak bij een bepaald type crash te voorkomen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKerendVermogen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        super().__init__()

        self._kerendVermogen = OTLAttribuut(field=KlLEACKerendVermogen,
                                            naam='kerendVermogen',
                                            label='kerend vermogen',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefKerendVermogen.kerendVermogen',
                                            usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                            deprecated_version='2.0.0',
                                            definition='Het vermogen van een voertuigkering om een doorbraak bij een bepaald type crash te voorkomen.')

    @property
    def kerendVermogen(self):
        """Het vermogen van een voertuigkering om een doorbraak bij een bepaald type crash te voorkomen."""
        return self._kerendVermogen.waarde

    @kerendVermogen.setter
    def kerendVermogen(self, value):
        self._kerendVermogen.set_waarde(value, owner=self)
