# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLModel.Datatypes.KwantWrdInAmpere import KwantWrdInAmpere


# Generated with OTLClassCreator. To modify: extend, do not edit
class Laagspanningsbord(AIMNaamObject, AttributeInfo):
    """Verzameling van alle elektrische componenten nodig voor de voeding en sturing van applicaties die erop aangesloten zijn. Omvat onder andere automaten,klemmenblokken,..."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)

        self._elektrischSchema = OTLAttribuut(field=DtcDocument,
                                              naam='elektrischSchema',
                                              label='elektrisch schema',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.elektrischSchema',
                                              definition='Het elektrisch aansluitschema van het laagspanningsbord.')

        self._vermogen = OTLAttribuut(field=KwantWrdInAmpere,
                                      naam='vermogen',
                                      label='vermogen',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Laagspanningsbord.vermogen',
                                      definition='Het vermogen van het laagspanningsbord.')

    @property
    def elektrischSchema(self):
        """Het elektrisch aansluitschema van het laagspanningsbord."""
        return self._elektrischSchema.waarde

    @elektrischSchema.setter
    def elektrischSchema(self, value):
        self._elektrischSchema.set_waarde(value, owner=self)

    @property
    def vermogen(self):
        """Het vermogen van het laagspanningsbord."""
        return self._vermogen.waarde

    @vermogen.setter
    def vermogen(self, value):
        self._vermogen.set_waarde(value, owner=self)
