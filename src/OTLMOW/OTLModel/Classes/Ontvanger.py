# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ZenderOntvangerToegang import ZenderOntvangerToegang
from OTLMOW.OTLModel.Datatypes.KlOntvangerMerk import KlOntvangerMerk
from OTLMOW.OTLModel.Datatypes.KlOntvangerModelnaam import KlOntvangerModelnaam
from OTLMOW.OTLModel.Datatypes.KlOntvangerToepassing import KlOntvangerToepassing


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ontvanger(ZenderOntvangerToegang):
    """Toestel voor het opvangen van signalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._merk = OTLAttribuut(field=KlOntvangerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.merk',
                                  definition='Het merk van een ontvanger.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlOntvangerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.modelnaam',
                                       definition='De modelnaam/product range van een ontvanger.',
                                       owner=self)

        self._toepassing = OTLAttribuut(field=KlOntvangerToepassing,
                                        naam='toepassing',
                                        label='toepassing',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.toepassing',
                                        definition='De techniek of standaard waarmee signalen over het netwerk verstuurd worden.',
                                        owner=self)

    @property
    def merk(self):
        """Het merk van een ontvanger."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van een ontvanger."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def toepassing(self):
        """De techniek of standaard waarmee signalen over het netwerk verstuurd worden."""
        return self._toepassing.get_waarde()

    @toepassing.setter
    def toepassing(self, value):
        self._toepassing.set_waarde(value, owner=self)
