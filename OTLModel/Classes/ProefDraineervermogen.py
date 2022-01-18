# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefDraineervermogen(Proef, AttributeInfo):
    """Controle van de waterdoorlatendheid van een open verharding."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraineervermogen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._draineervermogen = OTLAttribuut(field=DtcDocument,
                                              naam='draineervermogen',
                                              label='draineervermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefDraineervermogen.draineervermogen',
                                              definition='Proefresultaten van het drainvermogen.')

    @property
    def draineervermogen(self):
        """Proefresultaten van het drainvermogen."""
        return self._draineervermogen.waarde

    @draineervermogen.setter
    def draineervermogen(self, value):
        self._draineervermogen.set_waarde(value, owner=self)
