from OTLModel.Classes.VegetatieElement import VegetatieElement
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DtcAanlegBoomvorm import DtcAanlegBoomvorm
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBoomGroeifase import KlBoomGroeifase
from OTLModel.Datatypes.KlBoomspiegelInvulling import KlBoomspiegelInvulling
from OTLModel.Datatypes.KlEindbeeldOpgaandeBoom import KlEindbeeldOpgaandeBoom
from OTLModel.Datatypes.KlKlassePlantjaar import KlKlassePlantjaar
from OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLModel.Datatypes.KwantWrdInKubiekeMeter import KwantWrdInKubiekeMeter
from OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class OpgaandeBoom(VegetatieElement):
    """Een opgaande boom is een boom waarvan de vorm van de kruin overeenkomt met zijn natuurlijke, soortgebonden habitus. Opgaande bomen kunnen een hoge, lage, brede, smalle of een afwijkende groeivorm hebben, zoals zuil- en treurvormen. De boom kan zich op volstrekt natuurlijke wijze uitgezaaid hebben en zijn groeivorm kan bepaald zijn door de natuurlijke groeiomstandigheden (bv. natuurlijke snoei). Ontstond de boom in kunstmatige omstandigheden, dan is de groeivorm bepaald door de jeugdsnoei in de kwekerij en is het eindbeeld van de boom bepaald door de begeleidingssnoei of vormsnoei die wordt uitgevoerd vanaf het planten."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#OpgaandeBoom"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
