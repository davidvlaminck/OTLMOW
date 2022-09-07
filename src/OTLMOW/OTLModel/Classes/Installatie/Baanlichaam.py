# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMObject import AIMObject
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Baanlichaam(AIMObject, VlakGeometrie):
    """De lagen tussen het baanbed en het baanoppervlak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        VlakGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Draagconstructie')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#LijnvormigElement')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Signalisatie')

        self._dwarsprofiel = OTLAttribuut(field=DtcDocument,
                                          naam='dwarsprofiel',
                                          label='dwarsprofiel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.dwarsprofiel',
                                          usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                          definition='Een dwarsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht loodrecht op de as ervan.',
                                          owner=self)

        self._horizontaleLigging = OTLAttribuut(field=DtcDocument,
                                                naam='horizontaleLigging',
                                                label='horizontale ligging',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.horizontaleLigging',
                                                usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                                definition='De horizontale ligging van het baanlichaam als document bijlage.',
                                                owner=self)

        self._langsprofiel = OTLAttribuut(field=DtcDocument,
                                          naam='langsprofiel',
                                          label='langsprofiel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.langsprofiel',
                                          usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                          definition='Een langsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht in de lengterichting van de as ervan.',
                                          owner=self)

    @property
    def dwarsprofiel(self):
        """Een dwarsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht loodrecht op de as ervan."""
        return self._dwarsprofiel.get_waarde()

    @dwarsprofiel.setter
    def dwarsprofiel(self, value):
        self._dwarsprofiel.set_waarde(value, owner=self)

    @property
    def horizontaleLigging(self):
        """De horizontale ligging van het baanlichaam als document bijlage."""
        return self._horizontaleLigging.get_waarde()

    @horizontaleLigging.setter
    def horizontaleLigging(self, value):
        self._horizontaleLigging.set_waarde(value, owner=self)

    @property
    def langsprofiel(self):
        """Een langsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht in de lengterichting van de as ervan."""
        return self._langsprofiel.get_waarde()

    @langsprofiel.setter
    def langsprofiel(self, value):
        self._langsprofiel.set_waarde(value, owner=self)
