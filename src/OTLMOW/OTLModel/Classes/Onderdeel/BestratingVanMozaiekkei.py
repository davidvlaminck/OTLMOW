# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.Bestrating import Bestrating
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.KlMozaiekkeiFormaat import KlMozaiekkeiFormaat


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanMozaiekkei(Bestrating):
    """Bestrating van kasseien, in mozaïekverband gelegd. Kasseien zijn bestratingselementen van porfier, kwartsiet, graniet, of van harde zandsteen die geen schilferige structuur heeft. Ze hebben een dicht aaneengesloten en homogene korrel, zonder steenkorst, kwade aders of kwakaders en vertonen geen diamantkop."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._formaat = OTLAttribuut(field=KlMozaiekkeiFormaat,
                                     naam='formaat',
                                     label='formaat',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei.formaat',
                                     definition='De grootte van mozaïekkei.',
                                     owner=self)

        self._isHerbruik = OTLAttribuut(field=BooleanField,
                                        naam='isHerbruik',
                                        label='is herbruik',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei.isHerbruik',
                                        definition='Bepaling of de mozaïekkeien gerecycleerd werden.',
                                        owner=self)

    @property
    def formaat(self):
        """De grootte van mozaïekkei."""
        return self._formaat.get_waarde()

    @formaat.setter
    def formaat(self, value):
        self._formaat.set_waarde(value, owner=self)

    @property
    def isHerbruik(self):
        """Bepaling of de mozaïekkeien gerecycleerd werden."""
        return self._isHerbruik.get_waarde()

    @isHerbruik.setter
    def isHerbruik(self, value):
        self._isHerbruik.set_waarde(value, owner=self)
