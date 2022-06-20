# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Kabel import Kabel
from OTLMOW.OTLModel.Datatypes.KlDatakabelAdersEnSectie import KlDatakabelAdersEnSectie
from OTLMOW.OTLModel.Datatypes.KlDatakabelType import KlDatakabelType
from OTLMOW.OTLModel.Datatypes.KlDatakabelTypeSpecificatie import KlDatakabelTypeSpecificatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Datakabel(Kabel):
    """Een datakabel zorgt voor het uitwisselen van informatie van de ene locatie naar de andere."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._aantalAdersEnSectie = OTLAttribuut(field=KlDatakabelAdersEnSectie,
                                                 naam='aantalAdersEnSectie',
                                                 label='aantal aders en sectie',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel.aantalAdersEnSectie',
                                                 definition='Aantal en sectie van de ader(s) van de kabel volgens een lijst van voorkomende types.',
                                                 owner=self)

        self._type = OTLAttribuut(field=KlDatakabelType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel.type',
                                  definition='Indeling van een datakabel op basis van de gebruikte materialen en volgens een vaste typering.',
                                  owner=self)

        self._typeSpecificatie = OTLAttribuut(field=KlDatakabelTypeSpecificatie,
                                              naam='typeSpecificatie',
                                              label='type specificatie',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Datakabel.typeSpecificatie',
                                              definition='Een verdere specificatie van het type van de datakabel volgens een vaste lijst om bv. de brandklasse mee te geven.',
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
        """Indeling van een datakabel op basis van de gebruikte materialen en volgens een vaste typering."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)

    @property
    def typeSpecificatie(self):
        """Een verdere specificatie van het type van de datakabel volgens een vaste lijst om bv. de brandklasse mee te geven."""
        return self._typeSpecificatie.get_waarde()

    @typeSpecificatie.setter
    def typeSpecificatie(self, value):
        self._typeSpecificatie.set_waarde(value, owner=self)
