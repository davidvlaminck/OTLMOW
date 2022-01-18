# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.DtcDocument import DtcDocument


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefWaterdichtheid(Proef, AttributeInfo):
    """Testen van het waterverlies van het beproefde leidingsvak."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWaterdichtheid'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._waterdichtheid = OTLAttribuut(field=DtcDocument,
                                            naam='waterdichtheid',
                                            label='waterdichtheid',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefWaterdichtheid.waterdichtheid',
                                            definition='Testresultaten van het opgemeten waterverlies van het beproefde leidingsvak.')

    @property
    def waterdichtheid(self):
        """Testresultaten van het opgemeten waterverlies van het beproefde leidingsvak."""
        return self._waterdichtheid.waarde

    @waterdichtheid.setter
    def waterdichtheid(self, value):
        self._waterdichtheid.set_waarde(value, owner=self)
