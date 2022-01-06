# coding=utf-8
from OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLModel.Classes.EMDraagconstructie import EMDraagconstructie
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLModel.Datatypes.DtuLichtmastMasthoogte import DtuLichtmastMasthoogte
from OTLModel.Datatypes.KeuzelijstField import KeuzelijstField
from OTLModel.Datatypes.KlDraagConstrBeschermlaag import KlDraagConstrBeschermlaag
from OTLModel.Datatypes.KlDraagconstructieDwarsdoorsnede import KlDraagconstructieDwarsdoorsnede
from OTLModel.Datatypes.KlLichtmastBotsNormering import KlLichtmastBotsNormering
from OTLModel.Datatypes.KlLichtmastLeverancier import KlLichtmastLeverancier
from OTLModel.Datatypes.KlLichtmastMasttype import KlLichtmastMasttype
from OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lichtmast(AIMNaamObject, EMDraagconstructie):
    """Paal waarop een verlichtingstoestel of andere toestellen zoals een camera bevestigd kunnen worden met uitzondering van wegverlichting. Omvat het deurtje, klemmenblok, montagekastje, bevestigingsmaterialen (bv. voetplaten) en fundering of verankeringsmassief. Indien de paal gebruikt wordt voor wegverlichting moet het objecttype WVLichtmast gebruikt worden."""

    typeURI = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast"
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        EMDraagconstructie.__init__(self)

        self.beschermlaag = KeuzelijstField(naam="beschermlaag",
                                            label="beschermlaag",
                                            lijst=KlDraagConstrBeschermlaag(),
                                            uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.beschermlaag",
                                            definition="Beschermlaag van de lichtmast.",
                                            constraints="",
                                            usagenote="",
                                            deprecated_version="")
        """Beschermlaag van de lichtmast."""

        self.dwarsdoorsnede = KeuzelijstField(naam="dwarsdoorsnede",
                                              label="dwarsdoorsnede",
                                              lijst=KlDraagconstructieDwarsdoorsnede(),
                                              uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.dwarsdoorsnede",
                                              definition="De vorm van de dwarsdoorsnede van de lichtmast.",
                                              constraints="",
                                              usagenote="",
                                              deprecated_version="")
        """De vorm van de dwarsdoorsnede van de lichtmast."""

        self.heeftStopcontact = BooleanField(naam="heeftStopcontact",
                                             label="heeft stopcontact aanwezig",
                                             uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftStopcontact",
                                             definition="Geeft aan of er een stopcontact aanwezig is op de lichtmast.",
                                             constraints="",
                                             usagenote="",
                                             deprecated_version="")
        """Geeft aan of er een stopcontact aanwezig is op de lichtmast."""

        self.kleur = DteKleurRAL()
        """RAL kleur van de lichtmast."""
        self.kleur.naam = "kleur"
        self.kleur.label = "kleur"
        self.kleur.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.kleur"
        self.kleur.definition = "RAL kleur van de lichtmast."
        self.kleur.constraints = ""
        self.kleur.usagenote = ""
        self.kleur.deprecated_version = ""

        self.leverancier = KeuzelijstField(naam="leverancier",
                                           label="leverancier",
                                           lijst=KlLichtmastLeverancier(),
                                           uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.leverancier",
                                           definition="Leverancier van de lichtmast.",
                                           constraints="",
                                           usagenote="",
                                           deprecated_version="")
        """Leverancier van de lichtmast."""

        self.masthoogte = DtuLichtmastMasthoogte()
        """Hoogte (in meter) van de lichtmast."""
        self.masthoogte.naam = "masthoogte"
        self.masthoogte.label = "masthoogte"
        self.masthoogte.uri = "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.masthoogte"
        self.masthoogte.definition = "Hoogte (in meter) van de lichtmast."
        self.masthoogte.constraints = ""
        self.masthoogte.usagenote = ""
        self.masthoogte.deprecated_version = ""

        self.masttype = KeuzelijstField(naam="masttype",
                                        label="masttype",
                                        lijst=KlLichtmastMasttype(),
                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.masttype",
                                        definition="Type mast bv. rechte metalen paal, rechte metalen paal op voet, kreukelpaal met arm,...",
                                        constraints="",
                                        usagenote="",
                                        deprecated_version="")
        """Type mast bv. rechte metalen paal, rechte metalen paal op voet, kreukelpaal met arm,..."""

        self.normeringBotsvriendelijk = KeuzelijstField(naam="normeringBotsvriendelijk",
                                                        label="normering botsvriendelijk",
                                                        lijst=KlLichtmastBotsNormering(),
                                                        uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.normeringBotsvriendelijk",
                                                        definition="Categorie in normering botsvriendelijkheid.",
                                                        constraints="",
                                                        usagenote="",
                                                        deprecated_version="")
        """Categorie in normering botsvriendelijkheid."""

        self.specialeUitvoeringswijze = StringField(naam="specialeUitvoeringswijze",
                                                    label="speciale uitvoeringswijze",
                                                    uri="https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.specialeUitvoeringswijze",
                                                    definition="Omschrijving van de speciale uitvoeringswijze van de lichtmast indien van toepassing.",
                                                    constraints="",
                                                    usagenote="",
                                                    deprecated_version="")
        """Omschrijving van de speciale uitvoeringswijze van de lichtmast indien van toepassing."""
