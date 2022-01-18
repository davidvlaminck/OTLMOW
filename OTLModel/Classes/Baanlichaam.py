# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class Baanlichaam(AIMObject, AttributeInfo):
    """De lagen tussen het baanbed en het baanoppervlak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)

        self._dwarsprofiel = OTLAttribuut(field=DtcDocument,
                                          naam='dwarsprofiel',
                                          label='dwarsprofiel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.dwarsprofiel',
                                          usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                          definition='Een dwarsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht loodrecht op de as ervan.')

        self._horizontaleLigging = OTLAttribuut(field=DtcDocument,
                                                naam='horizontaleLigging',
                                                label='horizontale ligging',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.horizontaleLigging',
                                                usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                                definition='De horizontale ligging van het baanlichaam als document bijlage.')

        self._langsprofiel = OTLAttribuut(field=DtcDocument,
                                          naam='langsprofiel',
                                          label='langsprofiel',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Baanlichaam.langsprofiel',
                                          usagenote='Bestanden van het type xlsx, dwg of pdf.',
                                          definition='Een langsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht in de lengterichting van de as ervan.')

    @property
    def dwarsprofiel(self):
        """Een dwarsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht loodrecht op de as ervan."""
        return self._dwarsprofiel.waarde

    @dwarsprofiel.setter
    def dwarsprofiel(self, value):
        self._dwarsprofiel.set_waarde(value, owner=self)

    @property
    def horizontaleLigging(self):
        """De horizontale ligging van het baanlichaam als document bijlage."""
        return self._horizontaleLigging.waarde

    @horizontaleLigging.setter
    def horizontaleLigging(self, value):
        self._horizontaleLigging.set_waarde(value, owner=self)

    @property
    def langsprofiel(self):
        """Een langsprofiel is een doorsnijding van een terrein of constructie met een verticaal vlak, aangebracht in de lengterichting van de as ervan."""
        return self._langsprofiel.waarde

    @langsprofiel.setter
    def langsprofiel(self, value):
        self._langsprofiel.set_waarde(value, owner=self)
