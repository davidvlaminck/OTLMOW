# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Classes.Detectie import Detectie
from OTLModel.Classes.FirmwareObject import FirmwareObject
from OTLModel.Datatypes.KlWeggebondendetectorDetectieprincipe import KlWeggebondendetectorDetectieprincipe
from OTLModel.Datatypes.KlWeggebondendetectorMerk import KlWeggebondendetectorMerk
from OTLModel.Datatypes.KlWeggebondendetectorModelnaam import KlWeggebondendetectorModelnaam


# Generated with OTLClassCreator. To modify: extend, do not edit
class WeggebondenDetector(Detectie, FirmwareObject, AttributeInfo):
    """Weggebonden detectoren zijn draadloze in het wegdek geïntegreerde radars of magnetische inductiesensoren. Ze zitten ingebed in een cilinder, die geplaatst wordt in het wegdek en die draadloos communiceert met een access point die met de verkeersregelaar verbonden is"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AttributeInfo.__init__(self)
        Detectie.__init__(self)
        FirmwareObject.__init__(self)

        self._detectieprincipe = OTLAttribuut(field=KlWeggebondendetectorDetectieprincipe,
                                              naam='detectieprincipe',
                                              label='detectieprincipe',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector.detectieprincipe',
                                              definition='Het detectieprincipe geeft aan hoe de weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler.')

        self._merk = OTLAttribuut(field=KlWeggebondendetectorMerk,
                                  naam='merk',
                                  label='merk',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector.merk',
                                  definition='Merknaam van een weggebonden detector.')

        self._modelnaam = OTLAttribuut(field=KlWeggebondendetectorModelnaam,
                                       naam='modelnaam',
                                       label='modelnaam',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WeggebondenDetector.modelnaam',
                                       definition='De modelnaam van een weggebonden detector.')

    @property
    def detectieprincipe(self):
        """Het detectieprincipe geeft aan hoe de weggebonden detector voertuigen detecteert, bv. door gebruik te maken van inductie of doppler."""
        return self._detectieprincipe.waarde

    @detectieprincipe.setter
    def detectieprincipe(self, value):
        self._detectieprincipe.set_waarde(value, owner=self)

    @property
    def merk(self):
        """Merknaam van een weggebonden detector."""
        return self._merk.waarde

    @merk.setter
    def merk(self, value):
        self._merk.set_waarde(value, owner=self)

    @property
    def modelnaam(self):
        """De modelnaam van een weggebonden detector."""
        return self._modelnaam.waarde

    @modelnaam.setter
    def modelnaam(self, value):
        self._modelnaam.set_waarde(value, owner=self)
