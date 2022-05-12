# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.SchokindexVoertuigkering import SchokindexVoertuigkering
from OTLMOW.OTLModel.Classes.AfschermendeConstructie import AfschermendeConstructie
from OTLMOW.OTLModel.Datatypes.KlLEACObstakelbeveiligerType import KlLEACObstakelbeveiligerType
from OTLMOW.OTLModel.Datatypes.KlLEACPerformantieniveau import KlLEACPerformantieniveau
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Obstakelbeveiliger(SchokindexVoertuigkering, AfschermendeConstructie, VlakGeometrie):
    """Een energie-absorberende constructie voor voertuigen,geïnstalleerd vóór één of meerdere obstakels,met als doel de ernst van een botsing te reduceren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AfschermendeConstructie.__init__(self)
        SchokindexVoertuigkering.__init__(self)
        VlakGeometrie.__init__(self)

        self._performantieniveau = OTLAttribuut(field=KlLEACPerformantieniveau,
                                                naam='performantieniveau',
                                                label='performantieniveau',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger.performantieniveau',
                                                definition='Het niveau waarop de obstakelbeveiliger is getest.',
                                                owner=self)

        self._type = OTLAttribuut(field=KlLEACObstakelbeveiligerType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger.type',
                                  definition='De functie die de obstakelbeveiliger vervult.',
                                  owner=self)

    @property
    def performantieniveau(self):
        """Het niveau waarop de obstakelbeveiliger is getest."""
        return self._performantieniveau.get_waarde()

    @performantieniveau.setter
    def performantieniveau(self, value):
        self._performantieniveau.set_waarde(value, owner=self)

    @property
    def type(self):
        """De functie die de obstakelbeveiliger vervult."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
