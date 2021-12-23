from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlLEACUitzettingswaardeDilatatie import KlLEACUitzettingswaardeDilatatie


# Generated with OTLClassCreator
class Dilatatie(AIMObject):
    """Dilataties zijn bedoeld om ervoor te zorgen dat bouwconstructies vrij kunnen krimpen en uitzetten bij onder andere temperatuurwisselingen."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dilatatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
        self.uitzettingswaarde = KeuzelijstField(naam="uitzettingswaarde",
                                                 label="Uitzettingswaarde",
                                                 lijst=KlLEACUitzettingswaardeDilatatie(),
                                                 uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Dilatatie.uitzettingswaarde",
                                                 definition="De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing.",
                                                 constraints="",
                                                 usagenote="",
                                                 deprecated_version="")
        """De grootst mogelijke uitzetting die mogelijk is voor een bepaalde dilatatieoplossing."""
