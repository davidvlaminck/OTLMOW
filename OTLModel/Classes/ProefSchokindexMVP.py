# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KlLEACSchokindexMVP import KlLEACSchokindexMVP


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefSchokindexMVP(Proef, AttributeInfo):
    """Proef voor de bepaling van de schokindex parameter van de motorvangplank."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindexMVP'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._schokindexMvp = OTLAttribuut(field=KlLEACSchokindexMVP,
                                           naam='schokindexMvp',
                                           label='schokindex mvp',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefSchokindexMVP.schokindexMvp',
                                           usagenote='Klasse uit gebruik sinds versie 2.0.0 ',
                                           deprecated_version='2.0.0',
                                           definition='Head Injury Criterium (HIC) van een motorvangplank.')

    @property
    def schokindexMvp(self):
        """Head Injury Criterium (HIC) van een motorvangplank."""
        return self._schokindexMvp.waarde

    @schokindexMvp.setter
    def schokindexMvp(self, value):
        self._schokindexMvp.set_waarde(value, owner=self)
