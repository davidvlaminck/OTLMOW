# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KlBekledingPlaats import KlBekledingPlaats
from OTLModel.Datatypes.KlBuisbekledingUitvoeringswijze import KlBuisbekledingUitvoeringswijze
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Buisbekleding(AIMObject, AttributeInfo):
    """De bekleding of coating ter bescherming van de buis."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._laagdikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                       naam='laagdikte',
                                       label='Laagdikte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.laagdikte',
                                       definition='De dikte van de bekledingslaag in millimeter.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='Lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.lengte',
                                    definition='De totale lengte van de buisbekleding in lopende meter.')

        self._plaats = OTLAttribuut(field=KlBekledingPlaats,
                                    naam='plaats',
                                    label='plaats',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.plaats',
                                    definition='De kant waar de bekleding van de buis zich bevindt.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.technischeFiche',
                                             definition='De technische fiche van de buisbekleding.')

        self._tot = OTLAttribuut(field=KwantWrdInMeter,
                                 naam='tot',
                                 label='tot',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.tot',
                                 definition='Het einde van de buisbekleding in meter ten opzichte van de beginput van de buis.')

        self._uitvoeringswijze = OTLAttribuut(field=KlBuisbekledingUitvoeringswijze,
                                              naam='uitvoeringswijze',
                                              label='uitvoeringswijze',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.uitvoeringswijze',
                                              definition='Materiaal en manier van aanbrengen van de buisbekleding.')

        self._van = OTLAttribuut(field=KwantWrdInMeter,
                                 naam='van',
                                 label='van',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Buisbekleding.van',
                                 definition='Het begin van de buisbekleding in meter ten opzichte van de beginput van de leiding.')

    @property
    def laagdikte(self):
        """De dikte van de bekledingslaag in millimeter."""
        return self._laagdikte.waarde

    @laagdikte.setter
    def laagdikte(self, value):
        self._laagdikte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De totale lengte van de buisbekleding in lopende meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def plaats(self):
        """De kant waar de bekleding van de buis zich bevindt."""
        return self._plaats.waarde

    @plaats.setter
    def plaats(self, value):
        self._plaats.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van de buisbekleding."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def tot(self):
        """Het einde van de buisbekleding in meter ten opzichte van de beginput van de buis."""
        return self._tot.waarde

    @tot.setter
    def tot(self, value):
        self._tot.set_waarde(value, owner=self)

    @property
    def uitvoeringswijze(self):
        """Materiaal en manier van aanbrengen van de buisbekleding."""
        return self._uitvoeringswijze.waarde

    @uitvoeringswijze.setter
    def uitvoeringswijze(self, value):
        self._uitvoeringswijze.set_waarde(value, owner=self)

    @property
    def van(self):
        """Het begin van de buisbekleding in meter ten opzichte van de beginput van de leiding."""
        return self._van.waarde

    @van.setter
    def van(self, value):
        self._van.set_waarde(value, owner=self)
