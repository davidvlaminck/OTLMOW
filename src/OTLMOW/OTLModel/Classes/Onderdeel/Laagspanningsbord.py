# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Laagspanningsbord(AIMNaamObject, PuntGeometrie):
    """Verzameling van alle elektrische componenten nodig voor de voeding en sturing van applicaties die erop aangesloten zijn. Omvat onder andere automaten,klemmenblokken,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Behuizing')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#DNBMeter')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aftakking')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Cabinecontroller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Contactor')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDerden')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Hoofdschakelaar')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Segmentcontroller')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring')

        self._elektrischSchema = OTLAttribuut(field=DtcDocument,
                                              naam='elektrischSchema',
                                              label='elektrisch schema',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.elektrischSchema',
                                              definition='Het elektrisch aansluitschema van het laagspanningsbord.',
                                              owner=self)

        self._vermogen = OTLAttribuut(field=KwantWrdInAmpere,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.vermogen',
                                      definition='Het vermogen van het laagspanningsbord.',
                                      owner=self)

    @property
    def elektrischSchema(self):
        """Het elektrisch aansluitschema van het laagspanningsbord."""
        return self._elektrischSchema.get_waarde()

    @elektrischSchema.setter
    def elektrischSchema(self, value):
        self._elektrischSchema.set_waarde(value, owner=self)

    @property
    def vermogen(self):
        """Het vermogen van het laagspanningsbord."""
        return self._vermogen.get_waarde()

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
