# coding=utf-8
from OTLModel.Classes.Lichtmast import Lichtmast
from OTLModel.Datatypes.KardinaliteitField import KardinaliteitField
from OTLModel.Datatypes.DtuWvLichtmastBevsToestelMethode import DtuWvLichtmastBevsToestelMethode
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlWvLichtmastAantArmen import KlWvLichtmastAantArmen
from OTLModel.Datatypes.KlWvLichtmastArmlengte import KlWvLichtmastArmlengte


# Generated with OTLClassCreator. To modify: extend, do not edit
class WVLichtmast(Lichtmast):
    """Paal voorzien van armen voor het bevestigen van wegverlichtingstoestellen. Omvat het deurtje, klemmenblok, montagekastje, de bevestigingsmaterialen (bv. voetplaten) en fundering of verankeringsmassief. Gebruik Lichtmast voor de bevestiging van andere toestellen dan wegverlichting."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.aantalArmen = KeuzelijstField(naam="aantalArmen",
                                           label="aantal armen",
                                           lijst=KlWvLichtmastAantArmen(),
                                           objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.aantalArmen",
                                           definition="Aantal armen van de lichtmast.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Aantal armen van de lichtmast."""

        self.armlengte = KeuzelijstField(naam="armlengte",
                                         label="armlengte",
                                         lijst=KlWvLichtmastArmlengte(),
                                         objectUri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.armlengte",
                                         definition="Lengte van de arm van de lichtmast in meter.",
                                         constraints="",
                                         usagenote="",
                                         deprecated_version="")
        """Lengte van de arm van de lichtmast in meter."""

        bevestigingToestellenField = DtuWvLichtmastBevsToestelMethode()
        bevestigingToestellenField.naam = "bevestigingToestellen"
        bevestigingToestellenField.label = "bevestiging toestellen"
        bevestigingToestellenField.objectUri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.bevestigingToestellen"
        bevestigingToestellenField.definition = "Geeft de wijze aan waarop elk verlichtingstoestel bevestigd is op de lichtmast als keuze uit een lijst voor standaardmethodes of verder toegelicht wanneer een afwijkende methode gebruikt wordt."
        bevestigingToestellenField.constraints = ""
        bevestigingToestellenField.usagenote = ""
        bevestigingToestellenField.deprecated_version = ""
        self.bevestigingToestellen = KardinaliteitField(minKardinaliteit="1", maxKardinaliteit="*", fieldToMultiply=bevestigingToestellenField)
        """Geeft de wijze aan waarop elk verlichtingstoestel bevestigd is op de lichtmast als keuze uit een lijst voor standaardmethodes of verder toegelicht wanneer een afwijkende methode gebruikt wordt."""
