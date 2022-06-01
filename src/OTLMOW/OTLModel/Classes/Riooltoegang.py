# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.PutRelatie import PutRelatie
from OTLMOW.OTLModel.Classes.Put import Put
from OTLMOW.OTLModel.Datatypes.KlUitlaatType import KlUitlaatType
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Riooltoegang(PutRelatie, Put, PuntGeometrie):
    """Het uiteinde van een rioolbuis."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Put.__init__(self)
        PutRelatie.__init__(self)
        PuntGeometrie.__init__(self)

        self._typeRiooltoegang = OTLAttribuut(field=KlUitlaatType,
                                              naam='typeRiooltoegang',
                                              label='type riooltoegang',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Riooltoegang.typeRiooltoegang',
                                              definition='Bepaalt het type van een riooltoegang.',
                                              owner=self)

    @property
    def typeRiooltoegang(self):
        """Bepaalt het type van een riooltoegang."""
        return self._typeRiooltoegang.get_waarde()

    @typeRiooltoegang.setter
    def typeRiooltoegang(self, value):
        self._typeRiooltoegang.set_waarde(value, owner=self)
