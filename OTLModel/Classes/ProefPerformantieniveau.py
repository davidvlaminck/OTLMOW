# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KlLEACPerformantieniveau import KlLEACPerformantieniveau


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefPerformantieniveau(Proef, AttributeInfo):
    """Bepaling van het performantieniveau."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieniveau'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._performantieniveau = OTLAttribuut(field=KlLEACPerformantieniveau,
                                                naam='performantieniveau',
                                                label='performantieniveau',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieniveau.performantieniveau',
                                                usagenote='Klasse uit gebruik sinds versie 2.0.0',
                                                deprecated_version='2.0.0',
                                                definition='Het niveau waarop de obstakelbeveiliger is getest.')

    @property
    def performantieniveau(self):
        """Het niveau waarop de obstakelbeveiliger is getest."""
        return self._performantieniveau.waarde

    @performantieniveau.setter
    def performantieniveau(self, value):
        self._performantieniveau.set_waarde(value, owner=self)
