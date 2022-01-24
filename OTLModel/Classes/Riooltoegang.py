# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Put import Put
from OTLModel.Classes.PutRelatie import PutRelatie
from OTLModel.Datatypes.KlUitlaatType import KlUitlaatType


# Generated with OTLClassCreator. To modify: extend, do not edit
class Riooltoegang(Put, PutRelatie):
    """Het uiteinde van een rioolbuis."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Put.__init__(self)
        PutRelatie.__init__(self)

        self._typeRiooltoegang = OTLAttribuut(field=KlUitlaatType,
                                              naam='typeRiooltoegang',
                                              label='type riooltoegang',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang.typeRiooltoegang',
                                              definition='Bepaalt het type van een riooltoegang.')

    @property
    def typeRiooltoegang(self):
        """Bepaalt het type van een riooltoegang."""
        return self._typeRiooltoegang.waarde

    @typeRiooltoegang.setter
    def typeRiooltoegang(self, value):
        self._typeRiooltoegang.set_waarde(value, owner=self)
