# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Buis import Buis
from OTLMOW.OTLModel.Datatypes.IntegerField import IntegerField
from OTLMOW.OTLModel.Datatypes.KlRioleringsbuisFunctie import KlRioleringsbuisFunctie
from OTLMOW.OTLModel.Datatypes.KlRioleringsbuisMateriaal import KlRioleringsbuisMateriaal
from OTLMOW.OTLModel.Datatypes.KlSterktereeks import KlSterktereeks


# Generated with OTLClassCreator. To modify: extend, do not edit
class Rioleringsbuis(Buis):
    """Ondergronds kanaal of pijp voor gravitaire afvoer van water."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalAfgedichteAansluitingen = OTLAttribuut(field=IntegerField,
                                                           naam='aantalAfgedichteAansluitingen',
                                                           label='Aantal afgedichte aansluitingen',
                                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.aantalAfgedichteAansluitingen',
                                                           definition='De afgedichte verlaten aansluitingsopeningen van straatkolken en/of huisaansluitingen in de rioleringsbuis.')

        self._functie = OTLAttribuut(field=KlRioleringsbuisFunctie,
                                     naam='functie',
                                     label='functie',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.functie',
                                     definition='Bepaalt de functie van de rioleringsbuis.')

        self._materiaal = OTLAttribuut(field=KlRioleringsbuisMateriaal,
                                       naam='materiaal',
                                       label='materiaal',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.materiaal',
                                       definition='Bepaalt het materiaal van de rioleringsbuis.')

        self._sterktereeks = OTLAttribuut(field=KlSterktereeks,
                                          naam='sterktereeks',
                                          label='sterktereeks',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Rioleringsbuis.sterktereeks',
                                          definition='De stabiliteitsklasse van de buis.')

    @property
    def aantalAfgedichteAansluitingen(self):
        """De afgedichte verlaten aansluitingsopeningen van straatkolken en/of huisaansluitingen in de rioleringsbuis."""
        return self._aantalAfgedichteAansluitingen.waarde

    @aantalAfgedichteAansluitingen.setter
    def aantalAfgedichteAansluitingen(self, value):
        self._aantalAfgedichteAansluitingen.set_waarde(value, owner=self)

    @property
    def functie(self):
        """Bepaalt de functie van de rioleringsbuis."""
        return self._functie.waarde

    @functie.setter
    def functie(self, value):
        self._functie.set_waarde(value, owner=self)

    @property
    def materiaal(self):
        """Bepaalt het materiaal van de rioleringsbuis."""
        return self._materiaal.waarde

    @materiaal.setter
    def materiaal(self, value):
        self._materiaal.set_waarde(value, owner=self)

    @property
    def sterktereeks(self):
        """De stabiliteitsklasse van de buis."""
        return self._sterktereeks.waarde

    @sterktereeks.setter
    def sterktereeks(self, value):
        self._sterktereeks.set_waarde(value, owner=self)
