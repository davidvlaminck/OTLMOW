# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Classes.Draagconstructie import Draagconstructie
from OTLMOW.OTLModel.Datatypes.KlOperationeleStatus import KlOperationeleStatus
from OTLMOW.OTLModel.Datatypes.KlVerkeersbordsteunType import KlVerkeersbordsteunType
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Verkeersbordsteun(AIMNaamObject, Draagconstructie, PuntGeometrie):
    """Een draagconstructie voor verkeersborden of pictogrammen. Dit kan een ronde paal of een vakwerksteun zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        Draagconstructie.__init__(self)
        PuntGeometrie.__init__(self)

        self._breedte = OTLAttribuut(field=KwantWrdInMillimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.breedte',
                                     usagenote='Attribuut uit gebruik sinds versie 2.1.0-RC2',
                                     deprecated_version='2.1.0-RC2',
                                     definition='De breedte van een verkeersbordpaal in millimeter.',
                                     owner=self)

        self._diameter = OTLAttribuut(field=KwantWrdInMillimeter,
                                      naam='diameter',
                                      label='diameter',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.diameter',
                                      definition='De diameter van de verkeersbordpaal in millimeter.',
                                      owner=self)

        self._fabricagevoorschrift = OTLAttribuut(field=StringField,
                                                  naam='fabricagevoorschrift',
                                                  label='fabricagevoorschrift',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.fabricagevoorschrift',
                                                  definition='Genormaliseerde referentie waaraan het infrastructuur element aan voldoet.',
                                                  owner=self)

        self._lengte = OTLAttribuut(field=KwantWrdInMeter,
                                    naam='lengte',
                                    label='lengte',
                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.lengte',
                                    definition='De lengte van de verkeersbordpaal in meter.',
                                    owner=self)

        self._lengteBovengronds = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='lengteBovengronds',
                                               label='lengte bovengronds',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.lengteBovengronds',
                                               definition='De bovengrondse lengte van de verkeersbordpaal in meter.',
                                               owner=self)

        self._lengteOndergronds = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='lengteOndergronds',
                                               label='lengte ondergronds',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.lengteOndergronds',
                                               definition='De ondergrondse lengte van de verkeersbordpaal in meter.',
                                               owner=self)

        self._operationeleStatus = OTLAttribuut(field=KlOperationeleStatus,
                                                naam='operationeleStatus',
                                                label='operationele status',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.operationeleStatus',
                                                usagenote="Attribuut uit gebruik sinds versie 2.0.0-RC3. Enkel te gebruiken wanneer een object 'in gebruik' is. Zie ook attribuut toestand overgeërfd van AIMToestand om de asset levenscyclus aan te duiden.",
                                                deprecated_version='2.0.0-RC3.',
                                                definition='De operationele status van de verkeersbordsteun.',
                                                owner=self)

        self._type = OTLAttribuut(field=KlVerkeersbordsteunType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.type',
                                  definition='Het type verkeersbordpaal.',
                                  owner=self)

        self._wanddikte = OTLAttribuut(field=KwantWrdInMillimeter,
                                       naam='wanddikte',
                                       label='wanddikte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Verkeersbordsteun.wanddikte',
                                       definition='De dikte van de wand in millimeter.',
                                       owner=self)

    @property
    def breedte(self):
        """De breedte van een verkeersbordpaal in millimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def diameter(self):
        """De diameter van de verkeersbordpaal in millimeter."""
        return self._diameter.waarde

    @diameter.setter
    def diameter(self, value):
        self._diameter.set_waarde(value, owner=self)

    @property
    def fabricagevoorschrift(self):
        """Genormaliseerde referentie waaraan het infrastructuur element aan voldoet."""
        return self._fabricagevoorschrift.waarde

    @fabricagevoorschrift.setter
    def fabricagevoorschrift(self, value):
        self._fabricagevoorschrift.set_waarde(value, owner=self)

    @property
    def lengte(self):
        """De lengte van de verkeersbordpaal in meter."""
        return self._lengte.waarde

    @lengte.setter
    def lengte(self, value):
        self._lengte.set_waarde(value, owner=self)

    @property
    def lengteBovengronds(self):
        """De bovengrondse lengte van de verkeersbordpaal in meter."""
        return self._lengteBovengronds.waarde

    @lengteBovengronds.setter
    def lengteBovengronds(self, value):
        self._lengteBovengronds.set_waarde(value, owner=self)

    @property
    def lengteOndergronds(self):
        """De ondergrondse lengte van de verkeersbordpaal in meter."""
        return self._lengteOndergronds.waarde

    @lengteOndergronds.setter
    def lengteOndergronds(self, value):
        self._lengteOndergronds.set_waarde(value, owner=self)

    @property
    def operationeleStatus(self):
        """De operationele status van de verkeersbordsteun."""
        return self._operationeleStatus.waarde

    @operationeleStatus.setter
    def operationeleStatus(self, value):
        self._operationeleStatus.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type verkeersbordpaal."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def wanddikte(self):
        """De dikte van de wand in millimeter."""
        return self._wanddikte.waarde

    @wanddikte.setter
    def wanddikte(self, value):
        self._wanddikte.set_waarde(value, owner=self)
