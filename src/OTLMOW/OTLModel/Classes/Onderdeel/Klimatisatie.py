# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlKlimatisatieMerk import KlKlimatisatieMerk
from OTLMOW.OTLModel.Datatypes.KlKlimatisatieModelnaam import KlKlimatisatieModelnaam
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Klimatisatie(AIMNaamObject, PuntGeometrie):
    """Component waarmee de temperatuur en klimaat geregeld wordt van het objecttype waaraan het bevestigd is zoals een behuizing of ruimte."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._merk = OTLAttribuut(field=KlKlimatisatieMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie.merk',
                                  definition='De merknaam van de klimatisatie volgens de fabrikant.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlKlimatisatieModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Klimatisatie.modelnaam',
                                       definition='Naam waarmee de fabrikant het model van de klimatisatie identificeert.',
                                       owner=self)

    @property
    def merk(self):
        """De merknaam van de klimatisatie volgens de fabrikant."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """Naam waarmee de fabrikant het model van de klimatisatie identificeert."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
