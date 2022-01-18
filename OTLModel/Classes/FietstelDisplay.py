# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class FietstelDisplay(AIMNaamObject, AttributeInfo):
    """Verankerd toestel dat een selectie van telgegevens van het fietstelsysteem toont voor passerende fietsers."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)

        self._isDubbelzijdig = OTLAttribuut(field=BooleanField,
                                            naam='isDubbelzijdig',
                                            label='is dubbelzijdig',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay.isDubbelzijdig',
                                            definition='Geeft aan of het display telgegevens toont langs zijn beide zijden of niet.')

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#FietstelDisplay.technischeFiche',
                                             definition='Document met de technische specificaties van het display.')

    @property
    def isDubbelzijdig(self):
        """Geeft aan of het display telgegevens toont langs zijn beide zijden of niet."""
        return self._isDubbelzijdig.waarde

    @isDubbelzijdig.setter
    def isDubbelzijdig(self, value):
        self._isDubbelzijdig.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """Document met de technische specificaties van het display."""
        return self._technischeFiche.waarde

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)
