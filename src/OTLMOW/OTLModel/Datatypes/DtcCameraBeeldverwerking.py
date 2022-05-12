# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlCameraBeeldverwerkingstype import KlCameraBeeldverwerkingstype


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcCameraBeeldverwerkingWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._configBestand = OTLAttribuut(field=DtcDocument,
                                           naam='configBestand',
                                           label='configuratiebestand beeldverwerking',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCameraBeeldverwerking.configBestand',
                                           definition='Een bestand met de details van de configuratie voor het type beeldverwerking dat gekozen is in het type-attribuut van de instantie.',
                                           owner=self)

        self._typeBeeldverwerking = OTLAttribuut(field=KlCameraBeeldverwerkingstype,
                                                 naam='typeBeeldverwerking',
                                                 label='type beeldverwerking',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCameraBeeldverwerking.typeBeeldverwerking',
                                                 usagenote='Wanneer de camera de beeldverwerking niet zelf doet maar enkel beelden  verstuurt voor verwerking in een externe eenheid, moet die externe eenheid als aparte asset aangemaakt worden indien het specifieke type bestaat in de OTL of moet een instantie van Software gebruikt worden wanneer geen specifieke externe verwerkingseenheid voorzien is.',
                                                 definition='Geeft aan welk type beeldverwerking als onlosmakelijk deel van de camera geconfigureerd is.',
                                                 owner=self)

    @property
    def configBestand(self):
        """Een bestand met de details van de configuratie voor het type beeldverwerking dat gekozen is in het type-attribuut van de instantie."""
        return self._configBestand.get_waarde()

    @configBestand.setter
    def configBestand(self, value):
        self._configBestand.set_waarde(value, owner=self._parent)

    @property
    def typeBeeldverwerking(self):
        """Geeft aan welk type beeldverwerking als onlosmakelijk deel van de camera geconfigureerd is."""
        return self._typeBeeldverwerking.get_waarde()

    @typeBeeldverwerking.setter
    def typeBeeldverwerking(self, value):
        self._typeBeeldverwerking.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcCameraBeeldverwerking(ComplexField, AttributeInfo):
    """Complex datatype waarmee een type beeldverwerking van een camera en het relevant configuratiebestand, bijgehouden worden."""
    naam = 'DtcCameraBeeldverwerking'
    label = 'Camera beeldverwerkingsinstellingen'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcCameraBeeldverwerking'
    definition = 'Complex datatype waarmee een type beeldverwerking van een camera en het relevant configuratiebestand, bijgehouden worden.'
    waardeObject = DtcCameraBeeldverwerkingWaarden

    def __str__(self):
        return ComplexField.__str__(self)

