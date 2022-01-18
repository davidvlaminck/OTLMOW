# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.KlVriBewaking import KlVriBewaking


# Generated with OTLClassCreator. To modify: extend, do not edit
class Detectie(AIMNaamObject, AttributeInfo):
    """Abstracte voor de overige detecties, zijnde die die niet onder de groepen "niet weggebonden detecties", " weggebonden detecties" of "detectielussen" vallen."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)

        self._soortBewaking = OTLAttribuut(field=KlVriBewaking,
                                           naam='soortBewaking',
                                           label='soort bewaking',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Detectie.soortBewaking',
                                           definition='Type bewaking van de detectie.')

    @property
    def soortBewaking(self):
        """Type bewaking van de detectie."""
        return self._soortBewaking.waarde

    @soortBewaking.setter
    def soortBewaking(self, value):
        self._soortBewaking.set_waarde(value, owner=self)
