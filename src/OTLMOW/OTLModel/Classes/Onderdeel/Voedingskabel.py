# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Kabel import Kabel
from OTLMOW.OTLModel.Datatypes.KlVoedingskabelAdersEnSectie import KlVoedingskabelAdersEnSectie
from OTLMOW.OTLModel.Datatypes.KlVoedingskabelType import KlVoedingskabelType
from OTLMOW.OTLModel.Datatypes.KlVoedingskabelTypeSpecificatie import KlVoedingskabelTypeSpecificatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Voedingskabel(Kabel):
    """Zorgt voor het overbrengen van een elektrisch vermogen van de ene locatie naar de andere binnen een privaat netwerk. Onder dit type vallen ook installatiedraden die beschouwd worden als kabels met slechts één ader."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalAdersEnSectie = OTLAttribuut(field=KlVoedingskabelAdersEnSectie,
                                                 naam='aantalAdersEnSectie',
                                                 label='aantal aders en sectie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel.aantalAdersEnSectie',
                                                 definition='Aantal en sectie van de ader(s) van de kabel volgens een lijst van voorkomende types.',
                                                 owner=self)

        self._type = OTLAttribuut(field=KlVoedingskabelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel.type',
                                  definition='Indeling van een energie- of installatiekabel of -draad op basis van de gebruikte materialen en volgens een vaste typering.',
                                  owner=self)

        self._typeSpecificatie = OTLAttribuut(field=KlVoedingskabelTypeSpecificatie,
                                              naam='typeSpecificatie',
                                              label='type specificatie',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedingskabel.typeSpecificatie',
                                              definition='Een verdere specificatie van het type van de voedingskabel volgens een vaste lijst om bv. de brandklasse mee te geven.',
                                              owner=self)

    @property
    def aantalAdersEnSectie(self):
        """Aantal en sectie van de ader(s) van de kabel volgens een lijst van voorkomende types."""
        return self._aantalAdersEnSectie.get_waarde()

    @aantalAdersEnSectie.setter
    def aantalAdersEnSectie(self, value):
        self._aantalAdersEnSectie.set_waarde(value, owner=self)

    @property
    def type(self):
        """Indeling van een energie- of installatiekabel of -draad op basis van de gebruikte materialen en volgens een vaste typering."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def typeSpecificatie(self):
        """Een verdere specificatie van het type van de voedingskabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
        return self._typeSpecificatie.get_waarde()

    @typeSpecificatie.setter
    def typeSpecificatie(self, value):
        self._typeSpecificatie.set_waarde(value, owner=self)
