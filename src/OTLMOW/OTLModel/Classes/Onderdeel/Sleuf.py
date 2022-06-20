# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.KlSleufUitvoering import KlSleufUitvoering
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Sleuf(AIMObject, VlakGeometrie):
    """Lijnvormige verdieping van de natuurlijke ondergrond, nodig voor het leggen van leidingen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        VlakGeometrie.__init__(self)

        self._breedte = OTLAttribuut(field=KwantWrdInMeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.breedte',
                                     definition='De breedte van de sleuf in meter volgens figuur 7-1-1 van Standaardbestek 250.',
                                     owner=self)

        self._diepte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='diepte',
                                    label='diepte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.diepte',
                                    definition='De diepte van de sleuf tussen toekomstig maaiveld en de binnenonderkant van de buis in meter.',
                                    owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.lengte',
                                    definition='De totale lengte van de sleuf in lopende meter.',
                                    owner=self)

        self._uitvoering = OTLAttribuut(field=KlSleufUitvoering,
                                        naam='uitvoering',
                                        label='uitvoering',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sleuf.uitvoering',
                                        definition='Bepaalt de wijze van de uitvoering van de sleuf.',
                                        owner=self)

    @property
    def breedte(self):
        """De breedte van de sleuf in meter volgens figuur 7-1-1 van Standaardbestek 250."""
        return self._breedte.get_waarde()

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def diepte(self):
        """De diepte van de sleuf tussen toekomstig maaiveld en de binnenonderkant van de buis in meter."""
        return self._diepte.get_waarde()

    @diepte.setter
    def diepte(self, value):
        self._diepte.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De totale lengte van de sleuf in lopende meter."""
        return self._lengte.get_waarde()

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def uitvoering(self):
        """Bepaalt de wijze van de uitvoering van de sleuf."""
        return self._uitvoering.get_waarde()

    @uitvoering.setter
    def uitvoering(self, value):
        self._uitvoering.set_waarde(value, owner=self)
