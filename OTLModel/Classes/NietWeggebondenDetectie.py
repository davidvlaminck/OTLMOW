# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from OTLModel.Classes.Detectie import Detectie
from OTLModel.Classes.FirmwareObject import FirmwareObject
from OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt


# Generated with OTLClassCreator. To modify: extend, do not edit
class NietWeggebondenDetectie(Detectie, FirmwareObject, AttributeInfo):
    """Abstracte voor niet weggebonden detectoren. Deze bevinden zich niet in het wegoppervlak en worden aangewend voor volgende doeleinden:
*nabij de stoplijnen van kruispunten als kruispuntdetectoren waardoor de verkeersafhankelijke werking van de verkeersregelaar mogelijk wordt (zogenaamde microregeling);
*op willekeurige plaatsen in het verkeersnet, als selectieve detectoren voor het registreren van een aanvraag voor prioritaire doorgang vanwege het openbaar vervoer (bussen of tramrijtuigen) teneinde de afloop van de cyclus op de kruispunten te beïnvloeden"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        AttributeInfo.__init__(self)
        Detectie.__init__(self)
        FirmwareObject.__init__(self)

        self._voedingsspanning = OTLAttribuut(field=KwantWrdInVolt,
                                              naam='voedingsspanning',
                                              label='voedingsspanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#NietWeggebondenDetectie.voedingsspanning',
                                              definition='Spanning waarmee de detectoren gevoed worden.')

    @property
    def voedingsspanning(self):
        """Spanning waarmee de detectoren gevoed worden."""
        return self._voedingsspanning.waarde

    @voedingsspanning.setter
    def voedingsspanning(self, value):
        self._voedingsspanning.set_waarde(value, owner=self)
