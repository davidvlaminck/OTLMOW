# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.EMAfbakening import EMAfbakening
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt
from OTLMOW.OTLModel.Datatypes.KwantWrdInWatt import KwantWrdInWatt
from OTLMOW.OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class LEDRotondeafbakening(EMAfbakening, LijnGeometrie):
    """De verzameling van actieve lichtgevende modules ter hoogte van één toerit die ingeslepen worden in, of geplaatst worden op, de boordsteen van een rotonde en als doel hebben om de rand van de rotonde duidelijk zichtbaar te maken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDRotondeafbakening'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        EMAfbakening.__init__(self)
        LijnGeometrie.__init__(self)

        self._aantalActieveReflectoren = OTLAttribuut(field=NonNegIntegerField,
                                                      naam='aantalActieveReflectoren',
                                                      label='aantal actieve reflectoren',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDRotondeafbakening.aantalActieveReflectoren',
                                                      definition='Het aantal actieve reflectoren in de verzameling van reflectoren die hetzelfde obstakel of risico aangeven.',
                                                      owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDRotondeafbakening.lengte',
                                    definition='De afstand tussen de eerste en de laatste actieve reflector in de verzameling gevoed door dezelfde stroomkring. ',
                                    owner=self)

        self._nominaalVermogen = OTLAttribuut(field=KwantWrdInWatt,
                                              naam='nominaalVermogen',
                                              label='nominale spanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDRotondeafbakening.nominaalVermogen',
                                              definition='Nominale spanning (in volt) van de LED rotondeafbakening.',
                                              owner=self)

        self._nominaleSpanning = OTLAttribuut(field=KwantWrdInVolt,
                                              naam='nominaleSpanning',
                                              label='nominaal vermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDRotondeafbakening.nominaleSpanning',
                                              definition='Nominaal vermogen (in watt) van de LED rotondeafbakening.',
                                              owner=self)

        self._tussenafstand = OTLAttribuut(field=KwantWrdInCentimeter,
                                           naam='tussenafstand',
                                           label='tussenafstand',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#LEDRotondeafbakening.tussenafstand',
                                           definition='De afstand van middelpunt tot middelpunt tussen twee reflectoren in de verzameling.',
                                           owner=self)

    @property
    def aantalActieveReflectoren(self):
        """Het aantal actieve reflectoren in de verzameling van reflectoren die hetzelfde obstakel of risico aangeven."""
        return self._aantalActieveReflectoren.get_waarde()

    @aantalActieveReflectoren.setter
    def aantalActieveReflectoren(self, value):
        self._aantalActieveReflectoren.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De afstand tussen de eerste en de laatste actieve reflector in de verzameling gevoed door dezelfde stroomkring. """
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def nominaalVermogen(self):
        """Nominale spanning (in volt) van de LED rotondeafbakening."""
        return self._nominaalVermogen.get_waarde()

    @nominaalVermogen.setter
    def nominaalVermogen(self, value):
        self._nominaalVermogen.set_waarde(value, owner=self)

    @property
    def nominaleSpanning(self):
        """Nominaal vermogen (in watt) van de LED rotondeafbakening."""
        return self._nominaleSpanning.get_waarde()

    @nominaleSpanning.setter
    def nominaleSpanning(self, value):
        self._nominaleSpanning.set_waarde(value, owner=self)

    @property
    def tussenafstand(self):
        """De afstand van middelpunt tot middelpunt tussen twee reflectoren in de verzameling."""
        return self._tussenafstand.get_waarde()

    @tussenafstand.setter
    def tussenafstand(self, value):
        self._tussenafstand.set_waarde(value, owner=self)
