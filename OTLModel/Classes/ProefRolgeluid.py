# coding=utf-8
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefRolgeluid(Proef):
    """Het rolgeluid wordt gemeten met de CPX-methode volgens ISO/CEN 11819-2."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRolgeluid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._rolgeluid = OTLAttribuut(field=DtcDocument,
                                       naam='rolgeluid',
                                       label='rolgeluid',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefRolgeluid.rolgeluid',
                                       definition='Proefresultaten van het rolgeluid van de toplaag.')

    @property
    def rolgeluid(self):
        """Proefresultaten van het rolgeluid van de toplaag."""
        return self._rolgeluid.waarde

    @rolgeluid.setter
    def rolgeluid(self, value):
        self._rolgeluid.set_waarde(value, owner=self)
