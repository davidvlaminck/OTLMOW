# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Classes.BevestigingGC import BevestigingGC
from OTLModel.Datatypes.KlPictogramSymbool import KlPictogramSymbool
from OTLModel.Datatypes.KwantWrdInMinuut import KwantWrdInMinuut
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Pictogram(AIMObject, BevestigingGC, AttributeInfo):
    """Een bord dat een symbool of afbeelding bevat dat de plaats inneemt van een tekst."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMObject.__init__(self)
        AttributeInfo.__init__(self)
        BevestigingGC.__init__(self)

        self._nalichtingstijd = OTLAttribuut(field=KwantWrdInMinuut,
                                             naam='nalichtingstijd',
                                             label='nalichtingstijd',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram.nalichtingstijd',
                                             definition='De tijd dat het opgeslagen licht (bij bv. fosforen) in een andere lichtfrequentie (met minder energie) weer wordt uitgezonden.')

        self._opschrift = OTLAttribuut(field=StringField,
                                       naam='opschrift',
                                       label='opschrift',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram.opschrift',
                                       definition='Eventueel begeleidende tekst bij het symbool.')

        self._symbool = OTLAttribuut(field=KlPictogramSymbool,
                                     naam='symbool',
                                     label='symbool',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Pictogram.symbool',
                                     definition='Het symbool op het pictogram.')

    @property
    def nalichtingstijd(self):
        """De tijd dat het opgeslagen licht (bij bv. fosforen) in een andere lichtfrequentie (met minder energie) weer wordt uitgezonden."""
        return self._nalichtingstijd.waarde

    @nalichtingstijd.setter
    def nalichtingstijd(self, value):
        self._nalichtingstijd.set_waarde(value, owner=self)

    @property
    def opschrift(self):
        """Eventueel begeleidende tekst bij het symbool."""
        return self._opschrift.waarde

    @opschrift.setter
    def opschrift(self, value):
        self._opschrift.set_waarde(value, owner=self)

    @property
    def symbool(self):
        """Het symbool op het pictogram."""
        return self._symbool.waarde

    @symbool.setter
    def symbool(self, value):
        self._symbool.set_waarde(value, owner=self)
