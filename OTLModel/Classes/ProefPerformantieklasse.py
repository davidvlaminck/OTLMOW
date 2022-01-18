# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Proef import Proef
from OTLModel.Datatypes.KlLEACPerformantieklasse import KlLEACPerformantieklasse


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefPerformantieklasse(Proef, AttributeInfo):
    """Proef die de performantie (bij impact) bepaalt."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieklasse'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Proef.__init__(self)

        self._performantieklasse = OTLAttribuut(field=KlLEACPerformantieklasse,
                                                naam='performantieklasse',
                                                label='performantieklasse',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefPerformantieklasse.performantieklasse',
                                                usagenote='Klasse uit gebruik sinds versie 2.0.0',
                                                deprecated_version='2.0.0',
                                                definition='De aanduiding hoe (performantie) de beginconstructie is getest.')

    @property
    def performantieklasse(self):
        """De aanduiding hoe (performantie) de beginconstructie is getest."""
        return self._performantieklasse.waarde

    @performantieklasse.setter
    def performantieklasse(self, value):
        self._performantieklasse.set_waarde(value, owner=self)
