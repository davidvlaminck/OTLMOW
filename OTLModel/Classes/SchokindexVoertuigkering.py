# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod, ABC
from OTLModel.Datatypes.KlLEACSchokindex import KlLEACSchokindex


# Generated with OTLClassCreator. To modify: extend, do not edit
class SchokindexVoertuigkering(ABC, AttributeInfo):
    """Abstracte waarin de resultaten van de proef voor de bepaling van de schokindex parameter worden bijgehouden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SchokindexVoertuigkering'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._schokindex = OTLAttribuut(field=KlLEACSchokindex,
                                        naam='schokindex',
                                        label='schokindex',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SchokindexVoertuigkering.schokindex',
                                        definition='De parameter die weergeeft hoe groot de kans op ernstige letsels is van de inzittenden bij een aanrijding.')

    @property
    def schokindex(self):
        """De parameter die weergeeft hoe groot de kans op ernstige letsels is van de inzittenden bij een aanrijding."""
        return self._schokindex.waarde

    @schokindex.setter
    def schokindex(self, value):
        self._schokindex.set_waarde(value, owner=self)
