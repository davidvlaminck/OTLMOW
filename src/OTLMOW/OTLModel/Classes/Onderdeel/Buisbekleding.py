# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlBekledingPlaats import KlBekledingPlaats
from OTLMOW.OTLModel.Datatypes.KlBuisbekledingUitvoeringswijze import KlBuisbekledingUitvoeringswijze
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Buisbekleding(AIMObject, LijnGeometrie):
    """De bekleding of coating ter bescherming van de buis."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        LijnGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Buis')

        self._laagdikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                       naam='laagdikte',
                                       label='Laagdikte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.laagdikte',
                                       definition='De dikte van de bekledingslaag in millimeter.',
                                       owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='Lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.lengte',
                                    definition='De totale lengte van de buisbekleding in lopende meter.',
                                    owner=self)

        self._plaats = OTLAttribuut(field=KlBekledingPlaats,
                                    naam='plaats',
                                    label='plaats',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.plaats',
                                    definition='De kant waar de bekleding van de buis zich bevindt.',
                                    owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.technischeFiche',
                                             definition='De technische fiche van de buisbekleding.',
                                             owner=self)

        self._tot = OTLAttribuut(field=KwantWrdInMeter,
                                 naam='tot',
                                 label='tot',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.tot',
                                 definition='Het einde van de buisbekleding in meter ten opzichte van de beginput van de buis.',
                                 owner=self)

        self._uitvoeringswijze = OTLAttribuut(field=KlBuisbekledingUitvoeringswijze,
                                              naam='uitvoeringswijze',
                                              label='uitvoeringswijze',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.uitvoeringswijze',
                                              definition='Materiaal en manier van aanbrengen van de buisbekleding.',
                                              owner=self)

        self._van = OTLAttribuut(field=KwantWrdInMeter,
                                 naam='van',
                                 label='van',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.van',
                                 definition='Het begin van de buisbekleding in meter ten opzichte van de beginput van de leiding.',
                                 owner=self)

    @property
    def laagdikte(self):
        """De dikte van de bekledingslaag in millimeter."""
        return self._laagdikte.get_waarde()

    @laagdikte.setter
    def laagdikte(self, value):
        self._laagdikte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De totale lengte van de buisbekleding in lopende meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def plaats(self):
        """De kant waar de bekleding van de buis zich bevindt."""
        return self._plaats.get_waarde()

    @plaats.setter
    def plaats(self, value):
        self._plaats.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de buisbekleding."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def tot(self):
        """Het einde van de buisbekleding in meter ten opzichte van de beginput van de buis."""
        return self._tot.get_waarde()

    @tot.setter
    def tot(self, value):
        self._tot.set_waarde(value, owner=self)

    @property
    def uitvoeringswijze(self):
        """Materiaal en manier van aanbrengen van de buisbekleding."""
        return self._uitvoeringswijze.get_waarde()

    @uitvoeringswijze.setter
    def uitvoeringswijze(self, value):
        self._uitvoeringswijze.set_waarde(value, owner=self)

    @property
    def van(self):
        """Het begin van de buisbekleding in meter ten opzichte van de beginput van de leiding."""
        return self._van.get_waarde()

    @van.setter
    def van(self, value):
        self._van.set_waarde(value, owner=self)
