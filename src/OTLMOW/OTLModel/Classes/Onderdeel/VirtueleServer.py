# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.HardwareToegang import HardwareToegang
from OTLMOW.OTLModel.Datatypes.KlVirtueleServerMerk import KlVirtueleServerMerk
from OTLMOW.OTLModel.Datatypes.KlVirtueleServerModelnaam import KlVirtueleServerModelnaam
from OTLMOW.GeometrieArtefact.GeenGeometrie import GeenGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class VirtueleServer(HardwareToegang, GeenGeometrie):
    """Gedeelte van een fysieke server, dat zich met behulp van software gedraagt als een 'echte' server."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        HardwareToegang.__init__(self)
        GeenGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=KlVirtueleServerMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer.merk',
                                  definition='Het merk van de virtuele server.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlVirtueleServerModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#VirtueleServer.modelnaam',
                                       definition='De modelnaam van de virtuele server.',
                                       owner=self)

    @property
    def merk(self):
        """Het merk van de virtuele server."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de virtuele server."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
