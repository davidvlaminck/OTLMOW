# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMObject import AIMObject
from src.OTLMOW.OTLModel.Datatypes.KlSleufUitvoering import KlSleufUitvoering
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sleuf(AIMObject):
    """Lijnvormige verdieping van de natuurlijke ondergrond, nodig voor het leggen van leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.breedte',
                                     definition='De breedte van de sleuf in meter volgens figuur 7-1-1 van Standaardbestek 250.')

        self._diepte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.diepte',
                                    definition='De diepte van de sleuf tussen toekomstig maaiveld en de binnenonderkant van de buis in meter.')

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.lengte',
                                    definition='De totale lengte van de sleuf in lopende meter.')

        self._uitvoering = OTLAttribuut(field=KlSleufUitvoering,
                                        naam='uitvoering',
                                        label='uitvoering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.uitvoering',
                                        definition='Bepaalt de wijze van de uitvoering van de sleuf.')

    @property
    def breedte(self):
        """De breedte van de sleuf in meter volgens figuur 7-1-1 van Standaardbestek 250."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def diepte(self):
        """De diepte van de sleuf tussen toekomstig maaiveld en de binnenonderkant van de buis in meter."""
        return self._diepte.waarde

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De totale lengte van de sleuf in lopende meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def uitvoering(self):
        """Bepaalt de wijze van de uitvoering van de sleuf."""
        return self._uitvoering.waarde

    @uitvoering.setter
    def uitvoering(self, value):
        self._uitvoering.set_waarde(value, owner=self)
