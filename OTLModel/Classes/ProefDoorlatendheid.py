# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDoorlatendheid(Proef):
    """De controle van de doorlatendheid van het oppervlak met behulp van de dubbele ringmethode."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDoorlatendheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._doorlatendheid = OTLAttribuut(field=DtcDocument,
                                            naam='doorlatendheid',
                                            label='doorlatendheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDoorlatendheid.doorlatendheid',
                                            definition='Proefresultaten van de waterdoorlatendheid.')

    @property
    def doorlatendheid(self):
        """Proefresultaten van de waterdoorlatendheid."""
        return self._doorlatendheid.waarde

    @doorlatendheid.setter
    def doorlatendheid(self, value):
        self._doorlatendheid.set_waarde(value, owner=self)
