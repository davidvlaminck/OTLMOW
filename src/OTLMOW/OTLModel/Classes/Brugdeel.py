# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlGraadVanBeweegbaardheid import KlGraadVanBeweegbaardheid
from OTLMOW.OTLModel.Datatypes.KlGraadVanStatischeBepaaldheid import KlGraadVanStatischeBepaaldheid
from OTLMOW.OTLModel.Datatypes.KlTypeBrugdeel import KlTypeBrugdeel
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInVierkanteMeter import KwantWrdInVierkanteMeter
from OTLMOW.OTLModel.Datatypes.NonNegIntegerField import NonNegIntegerField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brugdeel(AIMNaamObject):
    """Het deel dat je kan wegnemen van een brug in zijn geheel. Dit kan ook meerdere overspanningen hebben."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalOverspanningen = OTLAttribuut(field=NonNegIntegerField,
                                                  naam='aantalOverspanningen',
                                                  label='aantal overspanningen',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.aantalOverspanningen',
                                                  definition='Aantal overspanningen.',
                                                  owner=self)

        self._graadVanBeweegbaarheid = OTLAttribuut(field=KlGraadVanBeweegbaardheid,
                                                    naam='graadVanBeweegbaarheid',
                                                    label='graad van beweegbaarheid',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.graadVanBeweegbaarheid',
                                                    definition='De manier waarop het brugdeel beweegt.',
                                                    owner=self)

        self._graadVanStatischeBepaaldheid = OTLAttribuut(field=KlGraadVanStatischeBepaaldheid,
                                                          naam='graadVanStatischeBepaaldheid',
                                                          label='graad van statische bepaaldheid',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.graadVanStatischeBepaaldheid',
                                                          definition='Welke statische bepaaldheid het brugdeel heeft.',
                                                          owner=self)

        self._individueleAfstandOverspanningen = OTLAttribuut(field=KwantWrdInMeter,
                                                              naam='individueleAfstandOverspanningen',
                                                              label='individuele afstand overspanningen',
                                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.individueleAfstandOverspanningen',
                                                              kardinaliteit_max='*',
                                                              definition='De individuele afstand tussen opeenvolgende opleggingen (van LO>RO of stijgend kilometerpunt). Er kunnen meerdere waarden mogelijk zijn (vb.: voor hyperstatische brugdelen).',
                                                              owner=self)

        self._totaleBreedte = OTLAttribuut(field=KwantWrdInMeter,
                                           naam='totaleBreedte',
                                           label='totale breedte',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.totaleBreedte',
                                           definition='De totale breedte van het brugdeel, uitgedrukt in meter.',
                                           owner=self)

        self._totaleLengte = OTLAttribuut(field=KwantWrdInMeter,
                                          naam='totaleLengte',
                                          label='totale lengte',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.totaleLengte',
                                          definition='De totale lengte van het brugdeel vanaf de uiterste opleggingen, uitgedrukt in meter.',
                                          owner=self)

        self._totaleOppervlakte = OTLAttribuut(field=KwantWrdInVierkanteMeter,
                                               naam='totaleOppervlakte',
                                               label='totale oppervlakte',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.totaleOppervlakte',
                                               definition='De totale oppervlakte van het gehele brugdeel (van hetzelfde type), uitgedrukt in vierkante meter.',
                                               owner=self)

        self._type = OTLAttribuut(field=KlTypeBrugdeel,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brugdeel.type',
                                  definition='Het type brugdeel.',
                                  owner=self)

    @property
    def aantalOverspanningen(self):
        """Aantal overspanningen."""
        return self._aantalOverspanningen.get_waarde()

    @aantalOverspanningen.setter
    def aantalOverspanningen(self, value):
        self._aantalOverspanningen.set_waarde(value, owner=self)

    @property
    def graadVanBeweegbaarheid(self):
        """De manier waarop het brugdeel beweegt."""
        return self._graadVanBeweegbaarheid.get_waarde()

    @graadVanBeweegbaarheid.setter
    def graadVanBeweegbaarheid(self, value):
        self._graadVanBeweegbaarheid.set_waarde(value, owner=self)

    @property
    def graadVanStatischeBepaaldheid(self):
        """Welke statische bepaaldheid het brugdeel heeft."""
        return self._graadVanStatischeBepaaldheid.get_waarde()

    @graadVanStatischeBepaaldheid.setter
    def graadVanStatischeBepaaldheid(self, value):
        self._graadVanStatischeBepaaldheid.set_waarde(value, owner=self)

    @property
    def individueleAfstandOverspanningen(self):
        """De individuele afstand tussen opeenvolgende opleggingen (van LO>RO of stijgend kilometerpunt). Er kunnen meerdere waarden mogelijk zijn (vb.: voor hyperstatische brugdelen)."""
        return self._individueleAfstandOverspanningen.get_waarde()

    @individueleAfstandOverspanningen.setter
    def individueleAfstandOverspanningen(self, value):
        self._individueleAfstandOverspanningen.set_waarde(value, owner=self)

    @property
    def totaleBreedte(self):
        """De totale breedte van het brugdeel, uitgedrukt in meter."""
        return self._totaleBreedte.get_waarde()

    @totaleBreedte.setter
    def totaleBreedte(self, value):
        self._totaleBreedte.set_waarde(value, owner=self)

    @property
    def totaleLengte(self):
        """De totale lengte van het brugdeel vanaf de uiterste opleggingen, uitgedrukt in meter."""
        return self._totaleLengte.get_waarde()

    @totaleLengte.setter
    def totaleLengte(self, value):
        self._totaleLengte.set_waarde(value, owner=self)

    @property
    def totaleOppervlakte(self):
        """De totale oppervlakte van het gehele brugdeel (van hetzelfde type), uitgedrukt in vierkante meter."""
        return self._totaleOppervlakte.get_waarde()

    @totaleOppervlakte.setter
    def totaleOppervlakte(self, value):
        self._totaleOppervlakte.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type brugdeel."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
