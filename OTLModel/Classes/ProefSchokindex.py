# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KlLEACSchokindex import KlLEACSchokindex


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefSchokindex(Proef, AttributeInfo):
    """Proef voor de bepaling van de schokindex parameter."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindex'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    deprecated_version = '2.0.0'

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._schokindex = OTLAttribuut(field=KlLEACSchokindex,
                                        naam='schokindex',
                                        label='schokindex',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindex.schokindex',
                                        usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                        deprecated_version='2.0.0',
                                        definition='De parameter die weergeeft hoe groot de kans op ernstige letsels is van de inzittenden bij een aanrijding.')

    @property
    def schokindex(self):
        """De parameter die weergeeft hoe groot de kans op ernstige letsels is van de inzittenden bij een aanrijding."""
        return self._schokindex.waarde

    @schokindex.setter
    def schokindex(self, value):
        self._schokindex.set_waarde(value, owner=self)
