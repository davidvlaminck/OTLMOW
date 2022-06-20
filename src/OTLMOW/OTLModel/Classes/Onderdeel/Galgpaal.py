# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.VRIDraagconstructie import VRIDraagconstructie
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.KlDraagconstructieDwarsdoorsnede import KlDraagconstructieDwarsdoorsnede
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Galgpaal(VRIDraagconstructie, PuntGeometrie):
    """De galgpalen zijn bestemd voor het bevestigen van verkeerslichten, signaalborden, wegwijzers boven het wegdek. Bovendien laten zij het bevestigen toe van één of meerdere lantaarns van het type 200 op de paalschacht. De draagwijdte van de arm moet kunnen reiken tot 9 m. De galgpalen beantwoorden aan SB270-51-6.15"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        VRIDraagconstructie.__init__(self)
        PuntGeometrie.__init__(self)

        self._aantalLiggers = OTLAttribuut(field=FloatOrDecimalField,
                                           naam='aantalLiggers',
                                           label='aantal liggers',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.aantalLiggers',
                                           definition='Het aantal liggers waarmee de arm van de galgpaal is uitgevoerd.',
                                           owner=self)

        self._armlengte = OTLAttribuut(field=KwantWrdInMeter,
                                       naam='armlengte',
                                       label='armlengte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.armlengte',
                                       definition='Lengte van de arm van een galgpaal in meter.',
                                       owner=self)

        self._berekeningsnota = OTLAttribuut(field=DtcDocument,
                                             naam='berekeningsnota',
                                             label='berekeningsnota',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.berekeningsnota',
                                             definition='Een bijlage met daarin de berekeningsnota voor de galgpaal.',
                                             owner=self)

        self._dwarsdoorsnede = OTLAttribuut(field=KlDraagconstructieDwarsdoorsnede,
                                            naam='dwarsdoorsnede',
                                            label='dwarsdoorsnede',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Galgpaal.dwarsdoorsnede',
                                            definition='De vorm van de dwarsdoorsnede van het opstaande deel van de galgpaal.',
                                            owner=self)

    @property
    def aantalLiggers(self):
        """Het aantal liggers waarmee de arm van de galgpaal is uitgevoerd."""
        return self._aantalLiggers.get_waarde()

    @aantalLiggers.setter
    def aantalLiggers(self, value):
        self._aantalLiggers.set_waarde(value, owner=self)

    @property
    def armlengte(self):
        """Lengte van de arm van een galgpaal in meter."""
        return self._armlengte.get_waarde()

    @armlengte.setter
    def armlengte(self, value):
        self._armlengte.set_waarde(value, owner=self)

    @property
    def berekeningsnota(self):
        """Een bijlage met daarin de berekeningsnota voor de galgpaal."""
        return self._berekeningsnota.get_waarde()

    @berekeningsnota.setter
    def berekeningsnota(self, value):
        self._berekeningsnota.set_waarde(value, owner=self)

    @property
    def dwarsdoorsnede(self):
        """De vorm van de dwarsdoorsnede van het opstaande deel van de galgpaal."""
        return self._dwarsdoorsnede.get_waarde()

    @dwarsdoorsnede.setter
    def dwarsdoorsnede(self, value):
        self._dwarsdoorsnede.set_waarde(value, owner=self)
