from OTLModel.Classes.AIMObject import AIMObject
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlBeheerHoutigeVegetatie import KlBeheerHoutigeVegetatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class BeheerHoutigeVegetatie(AIMObject):
    """Het beheerobject voor de houtige vegetatie."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        beheeroptieField = KeuzelijstField(naam="beheeroptie",
                                           label="beheeroptie",
                                           lijst=KlBeheerHoutigeVegetatie(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie.beheeroptie",
                                           definition="Aanduiding van welk beheer wordt toegepast op de houtige vegetatie.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        self.beheeroptie = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=beheeroptieField)
        """Aanduiding van welk beheer wordt toegepast op de houtige vegetatie."""

        self.heeftBeheerplan = BooleanField(naam="heeftBeheerplan",
                                            label="heeft beheerplan",
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#BeheerHoutigeVegetatie.heeftBeheerplan",
                                            definition="Aanduiding of er een beheerplan bestaat.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Aanduiding of er een beheerplan bestaat."""
