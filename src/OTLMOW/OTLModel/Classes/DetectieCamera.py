# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.NietWeggebondenDetectie import NietWeggebondenDetectie
from OTLMOW.OTLModel.Classes.TypeWeggebruiker import TypeWeggebruiker
from OTLMOW.OTLModel.Datatypes.KlDetectiecameraDetectieprincipe import KlDetectiecameraDetectieprincipe
from OTLMOW.OTLModel.Datatypes.KlDetectiecameraMerk import KlDetectiecameraMerk
from OTLMOW.OTLModel.Datatypes.KlDetectiecameraModelnaam import KlDetectiecameraModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class DetectieCamera(NietWeggebondenDetectie, TypeWeggebruiker):
    """Deze camera's worden onder andere opgesteld op kruispunten om de aanwezigheid van voertuigen te detecteren. De detectie kan optisch en/of thermografisch gebeuren. """

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        NietWeggebondenDetectie.__init__(self)
        TypeWeggebruiker.__init__(self)

        self._detectieprincipe = OTLAttribuut(field=KlDetectiecameraDetectieprincipe,
                                              naam='detectieprincipe',
                                              label='detectieprincipe',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.detectieprincipe',
                                              kardinaliteit_max='*',
                                              definition='Geeft aan of de camera optisch en/of thermografisch werkt.',
                                              owner=self)

        self._merk = OTLAttribuut(field=KlDetectiecameraMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.merk',
                                  definition='Merknaam van de detectiecamera.',
                                  owner=self)

        self._modelnaam = OTLAttribuut(field=KlDetectiecameraModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DetectieCamera.modelnaam',
                                       definition='De modelnaam van de detectiecamera.',
                                       owner=self)

    @property
    def detectieprincipe(self):
        """Geeft aan of de camera optisch en/of thermografisch werkt."""
        return self._detectieprincipe.get_waarde()

    @detectieprincipe.setter
    def detectieprincipe(self, value):
        self._detectieprincipe.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merknaam van de detectiecamera."""
        return self._merk.get_waarde()

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van de detectiecamera."""
        return self._modelnaam.get_waarde()

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
