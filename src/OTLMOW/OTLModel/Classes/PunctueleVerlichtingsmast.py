# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Classes.EMDraagconstructie import EMDraagconstructie
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DteKleurRAL import DteKleurRAL
from OTLMOW.OTLModel.Datatypes.DtuLichtmastMasthoogte import DtuLichtmastMasthoogte
from OTLMOW.OTLModel.Datatypes.DtuWvLichtmastBevsToestelMethode import DtuWvLichtmastBevsToestelMethode
from OTLMOW.OTLModel.Datatypes.KlDraagConstrBeschermlaag import KlDraagConstrBeschermlaag
from OTLMOW.OTLModel.Datatypes.KlDraagconstructieDwarsdoorsnede import KlDraagconstructieDwarsdoorsnede
from OTLMOW.OTLModel.Datatypes.KlLichtmastBotsNormering import KlLichtmastBotsNormering
from OTLMOW.OTLModel.Datatypes.KlLichtmastLeverancier import KlLichtmastLeverancier
from OTLMOW.OTLModel.Datatypes.KlLichtmastMasttype import KlLichtmastMasttype
from OTLMOW.OTLModel.Datatypes.KlMasttypePunctueleVerlichting import KlMasttypePunctueleVerlichting
from OTLMOW.OTLModel.Datatypes.KlWvLichtmastAantArmen import KlWvLichtmastAantArmen
from OTLMOW.OTLModel.Datatypes.KlWvLichtmastArmlengte import KlWvLichtmastArmlengte
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.StringField import StringField
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


class PunctueleVerlichtingsmast(AIMNaamObject, EMDraagconstructie, PuntGeometrie):
    """NOTE"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        EMDraagconstructie.__init__(self)
        PuntGeometrie.__init__(self)

        self._rekennota = OTLAttribuut(field=DtcDocument,
                                       naam='rekennota',
                                       label='rekennota',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.rekennota',
                                       definition='Een bijlage met daarin de rekennota voor de punctuele verlichtingsmast. Deze bevat onder andere ook de omvang/afmetingen van de fundering.',
                                       owner=self)

        self._masthoogte = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='masthoogte',
                                        label='masthoogte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.masthoogte',
                                        definition='Hoogte (in meter) van de punctuele verlichtingsmast.',
                                        owner=self)

        self._isDraaibaar = OTLAttribuut(field=BooleanField,
                                         naam='isDraaibaar',
                                         label='is draaibaar',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.isDraaibaar',
                                         definition='Geeft aan of de punctuele verlichtingsmast draaibaar is, al dan niet.',
                                         owner=self)

        self._masttype = OTLAttribuut(field=KlMasttypePunctueleVerlichting,
                                      naam='masttype',
                                      label='masttype',
                                      objectUri='',
                                      definition='Het type mast voor punctuele verlichting.',
                                      owner=self)

        self._aantalArmen = OTLAttribuut(field=KlWvLichtmastAantArmen,
                                         naam='aantalArmen',
                                         label='aantal armen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.aantalArmen',
                                         definition='Aantal armen van de punctuele verlichtingsmast.',
                                         owner=self)

        self._armlengte = OTLAttribuut(field=KlWvLichtmastArmlengte,
                                       naam='armlengte',
                                       label='armlengte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.armlengte',
                                       definition='Lengte van de arm van de punctuele verlichtingsmast in meter.',
                                       owner=self)

        self._dwarsdoorsnede = OTLAttribuut(field=KlDraagconstructieDwarsdoorsnede,
                                            naam='dwarsdoorsnede',
                                            label='dwarsdoorsnede',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlDraagconstructieDwarsdoorsnede',
                                            definition='De vorm van de dwarsdoorsnede van de punctuele verlichtingsmast.',
                                            owner=self)

        self._leverancier = OTLAttribuut(field=KlLichtmastLeverancier,
                                         naam='leverancier',
                                         label='leverancier',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Lichtmast.leverancier',
                                         definition='Leverancier van de punctuele verlichtingsmast.',
                                         owner=self)

        self._bevestigingToestellen = OTLAttribuut(field=DtuWvLichtmastBevsToestelMethode,
                                                   naam='bevestigingToestellen',
                                                   label='bevestiging toestellen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.bevestigingToestellen',
                                                   kardinaliteit_max='*',
                                                   definition='Geeft de wijze aan waarop elk verlichtingstoestel bevestigd is op de punctuele verlichtingsmast als keuze uit een lijst voor standaardmethodes of verder toegelicht wanneer een afwijkende methode gebruikt wordt.',
                                                   owner=self)

    @property
    def rekennota(self):
        """Een bijlage met daarin de rekennota voor de punctuele verlichtingsmast. Deze bevat onder andere ook de omvang/afmetingen van de fundering."""
        return self._rekennota.waarde

    @rekennota.setter
    def rekennota(self, value):
        self._rekennota.set_waarde(value, owner=self)

    @property
    def masthoogte(self):
        """Hoogte (in meter) van de punctuele verlichtmast."""
        return self._masthoogte.waarde

    @masthoogte.setter
    def masthoogte(self, value):
        self._masthoogte.set_waarde(value, owner=self)

    @property
    def masttype(self):
        """Het type mast voor punctuele verlichting."""
        return self._masttype.waarde

    @masttype.setter
    def masttype(self, value):
        self._masttype.set_waarde(value, owner=self)

    @property
    def isDraaibaar(self):
        """Geeft aan of de punctuele verlichtingsmast draaibaar is, al dan niet."""
        return self._isDraaibaar.waarde

    @isDraaibaar.setter
    def isDraaibaar(self, value):
        self._isDraaibaar.set_waarde(value, owner=self)

    @property
    def aantalArmen(self):
        """Aantal armen van de punctuele verlichtingsmast."""
        return self._aantalArmen.waarde

    @aantalArmen.setter
    def aantalArmen(self, value):
        self._aantalArmen.set_waarde(value, owner=self)

    @property
    def armlengte(self):
        """Lengte van de arm van de punctuele verlichtingsmast in meter."""
        return self._armlengte.waarde

    @armlengte.setter
    def armlengte(self, value):
        self._armlengte.set_waarde(value, owner=self)

    @property
    def bevestigingToestellen(self):
        """Geeft de wijze aan waarop elk verlichtingstoestel bevestigd is op de punctuele verlichtingsmast als keuze uit een lijst voor standaardmethodes of verder toegelicht wanneer een afwijkende methode gebruikt wordt."""
        return self._bevestigingToestellen.waarde

    @bevestigingToestellen.setter
    def bevestigingToestellen(self, value):
        self._bevestigingToestellen.set_waarde(value, owner=self)

    @property
    def dwarsdoorsnede(self):
        """De vorm van de dwarsdoorsnede van de punctuele verlichtingsmast."""
        return self._dwarsdoorsnede.waarde

    @dwarsdoorsnede.setter
    def dwarsdoorsnede(self, value):
        self._dwarsdoorsnede.set_waarde(value, owner=self)

    @property
    def leverancier(self):
        """Leverancier van de punctuele verlichtingsmast."""
        return self._leverancier.waarde

    @leverancier.setter
    def leverancier(self, value):
        self._leverancier.set_waarde(value, owner=self)
