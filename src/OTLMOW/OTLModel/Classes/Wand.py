# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ConstructiefObject import ConstructiefObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlTypeWand import KlTypeWand
from OTLMOW.OTLModel.Datatypes.KlZijdenType import KlZijdenType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Wand(ConstructiefObject):
    """Een verticaal constructiedeel, vrijstaand of omsluitend die een afscheiding vormt, bv. tussen 2 ruimtes."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._isDragend = OTLAttribuut(field=BooleanField,
                                       naam='isDragend',
                                       label='is dragend',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand.isDragend',
                                       definition='Geeft aan of de wand dragend is, al dan niet.',
                                       owner=self)

        self._typeWand = OTLAttribuut(field=KlTypeWand,
                                      naam='typeWand',
                                      label='type wand',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand.typeWand',
                                      definition='De functie die de wand uitoefent.',
                                      owner=self)

        self._zijden = OTLAttribuut(field=KlZijdenType,
                                    naam='zijden',
                                    label='zijden',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Wand.zijden',
                                    definition='Het type van de zijden dat de wand heeft (recht, rond, schuin,...).',
                                    owner=self)

    @property
    def isDragend(self):
        """Geeft aan of de wand dragend is, al dan niet."""
        return self._isDragend.get_waarde()

    @isDragend.setter
    def isDragend(self, value):
        self._isDragend.set_waarde(value, owner=self)

    @property
    def typeWand(self):
        """De functie die de wand uitoefent."""
        return self._typeWand.get_waarde()

    @typeWand.setter
    def typeWand(self, value):
        self._typeWand.set_waarde(value, owner=self)

    @property
    def zijden(self):
        """Het type van de zijden dat de wand heeft (recht, rond, schuin,...)."""
        return self._zijden.get_waarde()

    @zijden.setter
    def zijden(self, value):
        self._zijden.set_waarde(value, owner=self)
