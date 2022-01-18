# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.ZenderOntvangerToegang import ZenderOntvangerToegang
from OTLModel.Datatypes.KlOntvangerMerk import KlOntvangerMerk
from OTLModel.Datatypes.KlOntvangerModelnaam import KlOntvangerModelnaam
from OTLModel.Datatypes.KlOntvangerToepassing import KlOntvangerToepassing


# Generated with OTLClassCreator. To modify: extend, do not edit
class Ontvanger(ZenderOntvangerToegang, AttributeInfo):
    """Toestel voor het opvangen van signalen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        ZenderOntvangerToegang.__init__(self)

        self._merk = OTLAttribuut(field=KlOntvangerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.merk',
                                  definition='Het merk van een ontvanger.')

        self._modelnaam = OTLAttribuut(field=KlOntvangerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.modelnaam',
                                       definition='De modelnaam/product range van een ontvanger.')

        self._toepassing = OTLAttribuut(field=KlOntvangerToepassing,
                                        naam='toepassing',
                                        label='toepassing',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Ontvanger.toepassing',
                                        definition='De techniek of standaard waarmee signalen over het netwerk verstuurd worden.')

    @property
    def merk(self):
        """Het merk van een ontvanger."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam/product range van een ontvanger."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)

    @property
    def toepassing(self):
        """De techniek of standaard waarmee signalen over het netwerk verstuurd worden."""
        return self._toepassing.waarde

    @toepassing.setter
    def toepassing(self, value):
        self._toepassing.set_waarde(value, owner=self)
