# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KlTransformatorIsolatiemedium import KlTransformatorIsolatiemedium
from OTLMOW.OTLModel.Datatypes.KlTransformatorTrafobeveiliging import KlTransformatorTrafobeveiliging
from OTLMOW.OTLModel.Datatypes.KwantWrdInKiloVolt import KwantWrdInKiloVolt
from OTLMOW.OTLModel.Datatypes.KwantWrdInKiloVoltAmpere import KwantWrdInKiloVoltAmpere
from OTLMOW.OTLModel.Datatypes.KwantWrdInProcent import KwantWrdInProcent
from OTLMOW.OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Transformator(AIMNaamObject, PuntGeometrie):
    """Elektrische apparatuur, bestaande uit magnetisch gekoppelde spoelen, die instaat voor het transformeren van de voedingsspanning."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        PuntGeometrie.__init__(self)

        self._isolatiemedium = OTLAttribuut(field=KlTransformatorIsolatiemedium,
                                            naam='isolatiemedium',
                                            label='isolatiemedium',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.isolatiemedium',
                                            definition='Wijze van onderdompeling van de magnetische kring en van de wikkelingen van de transformator.',
                                            owner=self)

        self._kortsluitspanning = OTLAttribuut(field=KwantWrdInProcent,
                                               naam='kortsluitspanning',
                                               label='kortsluitspanning',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.kortsluitspanning',
                                               definition='Kortsluitspanning van de transformator (in %).',
                                               owner=self)

        self._nominaalVermogen = OTLAttribuut(field=KwantWrdInKiloVoltAmpere,
                                              naam='nominaalVermogen',
                                              label='nominaal vermogen',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.nominaalVermogen',
                                              definition='nominale vermogen van de transformator.',
                                              owner=self)

        self._nominalePrimaireSpanning = OTLAttribuut(field=KwantWrdInKiloVolt,
                                                      naam='nominalePrimaireSpanning',
                                                      label='nominale primaire spanning',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.nominalePrimaireSpanning',
                                                      definition='Nominale spanning van de primaire wikkeling in kV.',
                                                      owner=self)

        self._nominaleSecundaireSpanning = OTLAttribuut(field=KwantWrdInVolt,
                                                        naam='nominaleSecundaireSpanning',
                                                        label='nominale secundaire spanning',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.nominaleSecundaireSpanning',
                                                        definition='Nominale spanning van de secundaire wikkeling in V.',
                                                        owner=self)

        self._schakelgroep = OTLAttribuut(field=StringField,
                                          naam='schakelgroep',
                                          label='schakelgroep',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.schakelgroep',
                                          definition='Verzameling van 3 schakelcombinaties waarbij de hoofdletter de schakelwijze van de primaire weergeeft, de kleine letter(s) de schakelwijze van de secundaire weergeeft (en eventueel het feit dat het sterpunt naar buiten werd gebracht) en het getal geeft het klokgetal (of het aantal keer dat er 30° faseverschuiving tussen HS- en LS-spanning is) vb Dyn11',
                                          owner=self)

        self._typeBeveiliging = OTLAttribuut(field=KlTransformatorTrafobeveiliging,
                                             naam='typeBeveiliging',
                                             label='type beveiliging',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Transformator.typeBeveiliging',
                                             definition='Type transformatorbeveiliging.',
                                             owner=self)

    @property
    def isolatiemedium(self):
        """Wijze van onderdompeling van de magnetische kring en van de wikkelingen van de transformator."""
        return self._isolatiemedium.waarde

    @isolatiemedium.setter
    def isolatiemedium(self, value):
        self._isolatiemedium.set_waarde(value, owner=self)

    @property
    def kortsluitspanning(self):
        """Kortsluitspanning van de transformator (in %)."""
        return self._kortsluitspanning.waarde

    @kortsluitspanning.setter
    def kortsluitspanning(self, value):
        self._kortsluitspanning.set_waarde(value, owner=self)

    @property
    def nominaalVermogen(self):
        """nominale vermogen van de transformator."""
        return self._nominaalVermogen.waarde

    @nominaalVermogen.setter
    def nominaalVermogen(self, value):
        self._nominaalVermogen.set_waarde(value, owner=self)

    @property
    def nominalePrimaireSpanning(self):
        """Nominale spanning van de primaire wikkeling in kV."""
        return self._nominalePrimaireSpanning.waarde

    @nominalePrimaireSpanning.setter
    def nominalePrimaireSpanning(self, value):
        self._nominalePrimaireSpanning.set_waarde(value, owner=self)

    @property
    def nominaleSecundaireSpanning(self):
        """Nominale spanning van de secundaire wikkeling in V."""
        return self._nominaleSecundaireSpanning.waarde

    @nominaleSecundaireSpanning.setter
    def nominaleSecundaireSpanning(self, value):
        self._nominaleSecundaireSpanning.set_waarde(value, owner=self)

    @property
    def schakelgroep(self):
        """Verzameling van 3 schakelcombinaties waarbij de hoofdletter de schakelwijze van de primaire weergeeft, de kleine letter(s) de schakelwijze van de secundaire weergeeft (en eventueel het feit dat het sterpunt naar buiten werd gebracht) en het getal geeft het klokgetal (of het aantal keer dat er 30° faseverschuiving tussen HS- en LS-spanning is) vb Dyn11"""
        return self._schakelgroep.waarde

    @schakelgroep.setter
    def schakelgroep(self, value):
        self._schakelgroep.set_waarde(value, owner=self)

    @property
    def typeBeveiliging(self):
        """Type transformatorbeveiliging."""
        return self._typeBeveiliging.waarde

    @typeBeveiliging.setter
    def typeBeveiliging(self, value):
        self._typeBeveiliging.set_waarde(value, owner=self)
