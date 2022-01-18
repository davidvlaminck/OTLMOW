# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class NaampadObject(AIMNaamObject, AttributeInfo):
    """Abstracte als de basisklasse voor elk OTL object dat gebruik maakt van een naampad."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AIMNaamObject.__init__(self)
        AttributeInfo.__init__(self)

        self._naampad = OTLAttribuut(field=StringField,
                                     naam='naampad',
                                     label='naampad',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#NaampadObject.naampad',
                                     definition='Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra).')

    @property
    def naampad(self):
        """Een set van objecten (bv. collecties) die aanduiden waar het object zich bevindt in de objectenboom (EM-Infra)."""
        return self._naampad.waarde

    @naampad.setter
    def naampad(self, value):
        self._naampad.set_waarde(value, owner=self)
