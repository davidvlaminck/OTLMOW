# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.SchokindexVoertuigkering import SchokindexVoertuigkering
from OTLModel.Classes.AfschermendeConstructie import AfschermendeConstructie
from OTLModel.Datatypes.KlLEACObstakelbeveiligerType import KlLEACObstakelbeveiligerType
from OTLModel.Datatypes.KlLEACPerformantieniveau import KlLEACPerformantieniveau


# Generated with OTLClassCreator. To modify: extend, do not edit
class Obstakelbeveiliger(SchokindexVoertuigkering, AfschermendeConstructie, AttributeInfo):
    """Een energie-absorberende constructie voor voertuigen,geïnstalleerd vóór één of meerdere obstakels,met als doel de ernst van een botsing te reduceren."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AfschermendeConstructie.__init__(self)
        AttributeInfo.__init__(self)
        SchokindexVoertuigkering.__init__(self)

        self._performantieniveau = OTLAttribuut(field=KlLEACPerformantieniveau,
                                                naam='performantieniveau',
                                                label='performantieniveau',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger.performantieniveau',
                                                definition='Het niveau waarop de obstakelbeveiliger is getest.')

        self._type = OTLAttribuut(field=KlLEACObstakelbeveiligerType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Obstakelbeveiliger.type',
                                  definition='De functie die de obstakelbeveiliger vervult.')

    @property
    def performantieniveau(self):
        """Het niveau waarop de obstakelbeveiliger is getest."""
        return self._performantieniveau.waarde

    @performantieniveau.setter
    def performantieniveau(self, value):
        self._performantieniveau.set_waarde(value, owner=self)

    @property
    def type(self):
        """De functie die de obstakelbeveiliger vervult."""
        return self._type.waarde

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
