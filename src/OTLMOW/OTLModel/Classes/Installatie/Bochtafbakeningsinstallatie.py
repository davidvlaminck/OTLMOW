# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.EMAfbakening import EMAfbakening
from OTLMOW.OTLModel.Datatypes.KlAlgMateriaal import KlAlgMateriaal
from OTLMOW.OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Bochtafbakeningsinstallatie(EMAfbakening, LijnGeometrie):
    """De verzameling van alle bochtafbakeningsborden in dezelfde bocht en rijrichting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bochtafbakeningsinstallatie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        EMAfbakening.__init__(self)
        LijnGeometrie.__init__(self)

        self._aantalBorden = OTLAttribuut(field=NonNegIntegerField,
                                          naam='aantalBorden',
                                          label='aantal borden',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bochtafbakeningsinstallatie.aantalBorden',
                                          definition='Het aantal borden in de bochtafbakening voor het aanduiden van een bocht in een rijrichting.',
                                          owner=self)

        self._materiaalBehuizing = OTLAttribuut(field=KlAlgMateriaal,
                                                naam='materiaalBehuizing',
                                                label='materiaal behuizing',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Bochtafbakeningsinstallatie.materiaalBehuizing',
                                                definition='Het materiaal waaruit de behuizing gemaakt is.',
                                                owner=self)

    @property
    def aantalBorden(self):
        """Het aantal borden in de bochtafbakening voor het aanduiden van een bocht in een rijrichting."""
        return self._aantalBorden.get_waarde()

    @aantalBorden.setter
    def aantalBorden(self, value):
        self._aantalBorden.set_waarde(value, owner=self)

    @property
    def materiaalBehuizing(self):
        """Het materiaal waaruit de behuizing gemaakt is."""
        return self._materiaalBehuizing.get_waarde()

    @materiaalBehuizing.setter
    def materiaalBehuizing(self, value):
        self._materiaalBehuizing.set_waarde(value, owner=self)
