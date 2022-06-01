# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject
from OTLMOW.OTLModel.Datatypes.KlZijdenType import KlZijdenType
from OTLMOW.OTLModel.Datatypes.KwantWrdInDecimaleGraden import KwantWrdInDecimaleGraden


# Generated with OTLClassCreator. To modify: extend, do not edit
class Kolom(ConstructiefObject):
    """Een verticale constructie die dient als drager en bestaat uit een zuil of pilaar."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._hellingshoek = OTLAttribuut(field=KwantWrdInDecimaleGraden,
                                          naam='hellingshoek',
                                          label='hellingshoek',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom.hellingshoek',
                                          definition='De hoek die het object maakt met het grondvlak.',
                                          owner=self)

        self._zijden = OTLAttribuut(field=KlZijdenType,
                                    naam='zijden',
                                    label='zijden',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Kolom.zijden',
                                    definition='Het type van de zijden dat de kolom heeft (recht, rond, schuin,...)',
                                    owner=self)

    @property
    def hellingshoek(self):
        """De hoek die het object maakt met het grondvlak."""
        return self._hellingshoek.get_waarde()

    @hellingshoek.setter
    def hellingshoek(self, value):
        self._hellingshoek.set_waarde(value, owner=self)

    @property
    def zijden(self):
        """Het type van de zijden dat de kolom heeft (recht, rond, schuin,...)"""
        return self._zijden.get_waarde()

    @zijden.setter
    def zijden(self, value):
        self._zijden.set_waarde(value, owner=self)
