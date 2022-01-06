from OTLModel.Classes.Bestrating import Bestrating
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlMozaiekkeiFormaat import KlMozaiekkeiFormaat


# Generated with OTLClassCreator. To modify: extend, do not edit
class BestratingVanMozaiekkei(Bestrating):
    """Bestrating van kasseien, in mozaïekverband gelegd. Kasseien zijn bestratingselementen van porfier, kwartsiet, graniet, of van harde zandsteen die geen schilferige structuur heeft. Ze hebben een dicht aaneengesloten en homogene korrel, zonder steenkorst, kwade aders of kwakaders en vertonen geen diamantkop."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.formaat = KeuzelijstField(naam="formaat",
                                       label="formaat",
                                       lijst=KlMozaiekkeiFormaat(),
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei.formaat",
                                       definition="De grootte van mozaïekkei.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """De grootte van mozaïekkei."""

        self.isHerbruik = BooleanField(naam="isHerbruik",
                                       label="is herbruik",
                                       uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BestratingVanMozaiekkei.isHerbruik",
                                       definition="Bepaling of de mozaïekkeien gerecycleerd werden.",
                                       constraints="",
                                       usagenote="",
                                       deprecated_version="")
        """Bepaling of de mozaïekkeien gerecycleerd werden."""
