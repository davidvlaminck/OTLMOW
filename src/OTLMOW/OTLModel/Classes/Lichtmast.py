# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from src.OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from src.OTLMOW.OTLModel.Classes.EMDraagconstructie import EMDraagconstructie
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from src.OTLMOW.OTLModel.Datatypes.DtuLichtmastMasthoogte import DtuLichtmastMasthoogte
from src.OTLMOW.OTLModel.Datatypes.KlDraagConstrBeschermlaag import KlDraagConstrBeschermlaag
from src.OTLMOW.OTLModel.Datatypes.KlDraagconstructieDwarsdoorsnede import KlDraagconstructieDwarsdoorsnede
from src.OTLMOW.OTLModel.Datatypes.KlLichtmastBotsNormering import KlLichtmastBotsNormering
from src.OTLMOW.OTLModel.Datatypes.KlLichtmastLeverancier import KlLichtmastLeverancier
from src.OTLMOW.OTLModel.Datatypes.KlLichtmastMasttype import KlLichtmastMasttype
from src.OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Lichtmast(AIMNaamObject, EMDraagconstructie):
    """Paal waarop een verlichtingstoestel of andere toestellen zoals een camera bevestigd kunnen worden met uitzondering van wegverlichting. Omvat het deurtje, klemmenblok, montagekastje, bevestigingsmaterialen (bv. voetplaten) en fundering of verankeringsmassief. Indien de paal gebruikt wordt voor wegverlichting moet het objecttype WVLichtmast gebruikt worden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        EMDraagconstructie.__init__(self)

        self._beschermlaag = OTLAttribuut(field=KlDraagConstrBeschermlaag,
                                          naam='beschermlaag',
                                          label='beschermlaag',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.beschermlaag',
                                          definition='Beschermlaag van de lichtmast.')

        self._dwarsdoorsnede = OTLAttribuut(field=KlDraagconstructieDwarsdoorsnede,
                                            naam='dwarsdoorsnede',
                                            label='dwarsdoorsnede',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.dwarsdoorsnede',
                                            definition='De vorm van de dwarsdoorsnede van de lichtmast.')

        self._heeftStopcontact = OTLAttribuut(field=BooleanField,
                                              naam='heeftStopcontact',
                                              label='heeft stopcontact aanwezig',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.heeftStopcontact',
                                              definition='Geeft aan of er een stopcontact aanwezig is op de lichtmast.')

        self._kleur = OTLAttribuut(field=DteKleurRAL,
                                   naam='kleur',
                                   label='kleur',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.kleur',
                                   definition='RAL kleur van de lichtmast.')

        self._leverancier = OTLAttribuut(field=KlLichtmastLeverancier,
                                         naam='leverancier',
                                         label='leverancier',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.leverancier',
                                         definition='Leverancier van de lichtmast.')

        self._masthoogte = OTLAttribuut(field=DtuLichtmastMasthoogte,
                                        naam='masthoogte',
                                        label='masthoogte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.masthoogte',
                                        definition='Hoogte (in meter) van de lichtmast.')

        self._masttype = OTLAttribuut(field=KlLichtmastMasttype,
                                      naam='masttype',
                                      label='masttype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.masttype',
                                      definition='Type mast bv. rechte metalen paal, rechte metalen paal op voet, kreukelpaal met arm,...')

        self._normeringBotsvriendelijk = OTLAttribuut(field=KlLichtmastBotsNormering,
                                                      naam='normeringBotsvriendelijk',
                                                      label='normering botsvriendelijk',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.normeringBotsvriendelijk',
                                                      definition='Categorie in normering botsvriendelijkheid.')

        self._specialeUitvoeringswijze = OTLAttribuut(field=StringField,
                                                      naam='specialeUitvoeringswijze',
                                                      label='speciale uitvoeringswijze',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.specialeUitvoeringswijze',
                                                      definition='Omschrijving van de speciale uitvoeringswijze van de lichtmast indien van toepassing.')

    @property
    def beschermlaag(self):
        """Beschermlaag van de lichtmast."""
        return self._beschermlaag.waarde

    @beschermlaag.setter
    def beschermlaag(self, value):
        self._beschermlaag.set_waarde(value, owner=self)

    @property
    def dwarsdoorsnede(self):
        """De vorm van de dwarsdoorsnede van de lichtmast."""
        return self._dwarsdoorsnede.waarde

    @dwarsdoorsnede.setter
    def dwarsdoorsnede(self, value):
        self._dwarsdoorsnede.set_waarde(value, owner=self)

    @property
    def heeftStopcontact(self):
        """Geeft aan of er een stopcontact aanwezig is op de lichtmast."""
        return self._heeftStopcontact.waarde

    @heeftStopcontact.setter
    def heeftStopcontact(self, value):
        self._heeftStopcontact.set_waarde(value, owner=self)

    @property
    def kleur(self):
        """RAL kleur van de lichtmast."""
        return self._kleur.waarde

    @kleur.setter
    def kleur(self, value):
        self._kleur.set_waarde(value, owner=self)

    @property
    def leverancier(self):
        """Leverancier van de lichtmast."""
        return self._leverancier.waarde

    @leverancier.setter
    def leverancier(self, value):
        self._leverancier.set_waarde(value, owner=self)

    @property
    def masthoogte(self):
        """Hoogte (in meter) van de lichtmast."""
        return self._masthoogte.waarde

    @masthoogte.setter
    def masthoogte(self, value):
        self._masthoogte.set_waarde(value, owner=self)

    @property
    def masttype(self):
        """Type mast bv. rechte metalen paal, rechte metalen paal op voet, kreukelpaal met arm,..."""
        return self._masttype.waarde

    @masttype.setter
    def masttype(self, value):
        self._masttype.set_waarde(value, owner=self)

    @property
    def normeringBotsvriendelijk(self):
        """Categorie in normering botsvriendelijkheid."""
        return self._normeringBotsvriendelijk.waarde

    @normeringBotsvriendelijk.setter
    def normeringBotsvriendelijk(self, value):
        self._normeringBotsvriendelijk.set_waarde(value, owner=self)

    @property
    def specialeUitvoeringswijze(self):
        """Omschrijving van de speciale uitvoeringswijze van de lichtmast indien van toepassing."""
        return self._specialeUitvoeringswijze.waarde

    @specialeUitvoeringswijze.setter
    def specialeUitvoeringswijze(self, value):
        self._specialeUitvoeringswijze.set_waarde(value, owner=self)
