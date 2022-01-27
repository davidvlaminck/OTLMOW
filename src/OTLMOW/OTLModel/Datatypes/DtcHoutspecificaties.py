# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from src.OTLMOW.OTLModel.Datatypes.KlDuurzaamheidsklasseHout import KlDuurzaamheidsklasseHout
from src.OTLMOW.OTLModel.Datatypes.KlKwaliteitsklasseHout import KlKwaliteitsklasseHout
from src.OTLMOW.OTLModel.Datatypes.KlSterkteklasseHout import KlSterkteklasseHout


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcHoutspecificatiesWaarden(AttributeInfo):
    def __init__(self):
        super().__init__()
        self._houtduurzaamheidsklasse = OTLAttribuut(field=KlDuurzaamheidsklasseHout,
                                                     naam='houtduurzaamheidsklasse',
                                                     label='houtduurzaamheidsklasse',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.houtduurzaamheidsklasse',
                                                     definition='De verwachte levensduur van het hout. De klasse geeft de resistentie aan van het kernhout tegen ongunstige omstandigheden.')

        self._houtkwaliteitsklasse = OTLAttribuut(field=KlKwaliteitsklasseHout,
                                                  naam='houtkwaliteitsklasse',
                                                  label='houtkwaliteitsklasse',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.houtkwaliteitsklasse',
                                                  definition='Kwaliteitsindeling van de houtsoort met betrekking op vervormingen, scheuren en kwasten.')

        self._houtsterkteklasse = OTLAttribuut(field=KlSterkteklasseHout,
                                               naam='houtsterkteklasse',
                                               label='houtsterkteklasse',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.houtsterkteklasse',
                                               definition='De maximale belasting van het hout. Deze klasse geeft aan hoe sterk en voor welke constructies de houtsoort geschikt is.')

        self._isResistentTegenMarieneBoorders = OTLAttribuut(field=BooleanField,
                                                             naam='isResistentTegenMarieneBoorders',
                                                             label='is resistent tegen mariene boorders',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties.isResistentTegenMarieneBoorders',
                                                             definition='Geeft aan of het hout resistent is bij toepassingen in contact met zout of brak water.')

    @property
    def houtduurzaamheidsklasse(self):
        """De verwachte levensduur van het hout. De klasse geeft de resistentie aan van het kernhout tegen ongunstige omstandigheden."""
        return self._houtduurzaamheidsklasse.waarde

    @houtduurzaamheidsklasse.setter
    def houtduurzaamheidsklasse(self, value):
        self._houtduurzaamheidsklasse.set_waarde(value, owner=self._parent)

    @property
    def houtkwaliteitsklasse(self):
        """Kwaliteitsindeling van de houtsoort met betrekking op vervormingen, scheuren en kwasten."""
        return self._houtkwaliteitsklasse.waarde

    @houtkwaliteitsklasse.setter
    def houtkwaliteitsklasse(self, value):
        self._houtkwaliteitsklasse.set_waarde(value, owner=self._parent)

    @property
    def houtsterkteklasse(self):
        """De maximale belasting van het hout. Deze klasse geeft aan hoe sterk en voor welke constructies de houtsoort geschikt is."""
        return self._houtsterkteklasse.waarde

    @houtsterkteklasse.setter
    def houtsterkteklasse(self, value):
        self._houtsterkteklasse.set_waarde(value, owner=self._parent)

    @property
    def isResistentTegenMarieneBoorders(self):
        """Geeft aan of het hout resistent is bij toepassingen in contact met zout of brak water."""
        return self._isResistentTegenMarieneBoorders.waarde

    @isResistentTegenMarieneBoorders.setter
    def isResistentTegenMarieneBoorders(self, value):
        self._isResistentTegenMarieneBoorders.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcHoutspecificaties(ComplexField, AttributeInfo):
    """Complex datatype om de eigenschappen van hout te bundelen."""
    naam = 'DtcHoutspecificaties'
    label = 'Houtspecificaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcHoutspecificaties'
    definition = 'Complex datatype om de eigenschappen van hout te bundelen.'
    waardeObject = DtcHoutspecificatiesWaarden

    def __str__(self):
        return ComplexField.__str__(self)

