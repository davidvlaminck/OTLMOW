# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.NietWeggebondenDetectie import NietWeggebondenDetectie
from OTLModel.Classes.TypeWeggebruiker import TypeWeggebruiker
from OTLModel.Datatypes.KlDetectiecameraDetectieprincipe import KlDetectiecameraDetectieprincipe
from OTLModel.Datatypes.KlDetectiecameraMerk import KlDetectiecameraMerk
from OTLModel.Datatypes.KlDetectiecameraModelnaam import KlDetectiecameraModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DetectieCamera(NietWeggebondenDetectie, TypeWeggebruiker, AttributeInfo):
    """Deze camera's worden onder andere opgesteld op kruispunten om de aanwezigheid van voertuigen te detecteren. De detectie kan optisch en/of thermografisch gebeuren. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        NietWeggebondenDetectie.__init__(self)
        TypeWeggebruiker.__init__(self)

        self._detectieprincipe = OTLAttribuut(field=KlDetectiecameraDetectieprincipe,
                                              naam='detectieprincipe',
                                              label='detectieprincipe',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.detectieprincipe',
                                              kardinaliteit_max='*',
                                              definition='Geeft aan of de camera optisch en/of thermografisch werkt.')

        self._merk = OTLAttribuut(field=KlDetectiecameraMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.merk',
                                  definition='Merknaam van de detectiecamera.')

        self._modelnaam = OTLAttribuut(field=KlDetectiecameraModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.modelnaam',
                                       definition='De modelnaam van de detectiecamera.')

    @property
    def detectieprincipe(self):
        """Geeft aan of de camera optisch en/of thermografisch werkt."""
        return self._detectieprincipe.waarde

    @detectieprincipe.setter
    def detectieprincipe(self, value):
        self._detectieprincipe.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merknaam van de detectiecamera."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de detectiecamera."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
