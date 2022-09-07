# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.EMDraagconstructie import EMDraagconstructie
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.DtuWvLichtmastBevsToestelMethode import DtuWvLichtmastBevsToestelMethode
from OTLMOW.OTLModel.Datatypes.KlDraagconstructieDwarsdoorsnede import KlDraagconstructieDwarsdoorsnede
from OTLMOW.OTLModel.Datatypes.KlLichtmastLeverancier import KlLichtmastLeverancier
from OTLMOW.OTLModel.Datatypes.KlMasttypePunctueleVerlichting import KlMasttypePunctueleVerlichting
from OTLMOW.OTLModel.Datatypes.KlWvLichtmastAantArmen import KlWvLichtmastAantArmen
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class PunctueleVerlichtingsmast(EMDraagconstructie, AIMNaamObject, PuntGeometrie):
    """Paal waarop punctuele verlichting van niet-beveiligde oversteekplaatsen bevestigd kan worden, inclusief deurtje, klemmenblok, montagekastje, bevestigingsmaterialen (bv. voetplaten) en fundering (bv. buisfundering) of verankeringsmassief. Deze wordt geschilderd in afwisselende stroken zwart/geel."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        EMDraagconstructie.__init__(self)
        PuntGeometrie.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')

        self._aantalArmen = OTLAttribuut(field=KlWvLichtmastAantArmen,
                                         naam='aantalArmen',
                                         label='aantal armen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.aantalArmen',
                                         definition='Aantal armen van de punctuele verlichtingsmast.',
                                         owner=self)

        self._armlengte = OTLAttribuut(field=KwantWrdInMeter,
                                       naam='armlengte',
                                       label='armlengte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.armlengte',
                                       definition='Lengte van de arm van de punctuele verlichtingsmast, in meter.',
                                       owner=self)

        self._bevestigingToestellen = OTLAttribuut(field=DtuWvLichtmastBevsToestelMethode,
                                                   naam='bevestigingToestellen',
                                                   label='bevestiging toestellen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.bevestigingToestellen',
                                                   definition='Geeft de wijze aan waarop elk verlichtingstoestel bevestigd is op de punctuele verlichtingsmast als keuze uit een lijst voor standaardmethodes of verder toegelicht wanneer een afwijkende methode gebruikt wordt.',
                                                   owner=self)

        self._dwarsdoorsnede = OTLAttribuut(field=KlDraagconstructieDwarsdoorsnede,
                                            naam='dwarsdoorsnede',
                                            label='dwarsdoorsnede',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.dwarsdoorsnede',
                                            definition='De vorm van de dwarsdoorsnede van het opstaande deel van de punctuele verlichtingsmast.',
                                            owner=self)

        self._isDraaibaar = OTLAttribuut(field=BooleanField,
                                         naam='isDraaibaar',
                                         label='is draaibaar',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.isDraaibaar',
                                         definition='Geeft aan of de punctuele verlichtingsmast draaibaar is, al dan niet.',
                                         owner=self)

        self._leverancier = OTLAttribuut(field=KlLichtmastLeverancier,
                                         naam='leverancier',
                                         label='leverancier',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.leverancier',
                                         definition='Leverancier van de punctuele verlichtingsmast.',
                                         owner=self)

        self._masthoogte = OTLAttribuut(field=KwantWrdInMeter,
                                        naam='masthoogte',
                                        label='masthoogte',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.masthoogte',
                                        definition='Hoogte (in meter) van de punctuele verlichtingsmast.',
                                        owner=self)

        self._masttype = OTLAttribuut(field=KlMasttypePunctueleVerlichting,
                                      naam='masttype',
                                      label='masttype',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.masttype',
                                      definition='Het type mast voor punctuele verlichting.',
                                      owner=self)

        self._rekennota = OTLAttribuut(field=DtcDocument,
                                       naam='rekennota',
                                       label='rekennota',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#PunctueleVerlichtingsmast.rekennota',
                                       definition='Een bijlage met daarin de rekennota voor de punctuele verlichtingsmast. Deze bevat onder andere ook de omvang/afmetingen van de fundering.',
                                       owner=self)

    @property
    def aantalArmen(self):
        """Aantal armen van de punctuele verlichtingsmast."""
        return self._aantalArmen.get_waarde()

    @aantalArmen.setter
    def aantalArmen(self, value):
        self._aantalArmen.set_waarde(value, owner=self)

    @property
    def armlengte(self):
        """Lengte van de arm van de punctuele verlichtingsmast, in meter."""
        return self._armlengte.get_waarde()

    @armlengte.setter
    def armlengte(self, value):
        self._armlengte.set_waarde(value, owner=self)

    @property
    def bevestigingToestellen(self):
        """Geeft de wijze aan waarop elk verlichtingstoestel bevestigd is op de punctuele verlichtingsmast als keuze uit een lijst voor standaardmethodes of verder toegelicht wanneer een afwijkende methode gebruikt wordt."""
        return self._bevestigingToestellen.get_waarde()

    @bevestigingToestellen.setter
    def bevestigingToestellen(self, value):
        self._bevestigingToestellen.set_waarde(value, owner=self)

    @property
    def dwarsdoorsnede(self):
        """De vorm van de dwarsdoorsnede van het opstaande deel van de punctuele verlichtingsmast."""
        return self._dwarsdoorsnede.get_waarde()

    @dwarsdoorsnede.setter
    def dwarsdoorsnede(self, value):
        self._dwarsdoorsnede.set_waarde(value, owner=self)

    @property
    def isDraaibaar(self):
        """Geeft aan of de punctuele verlichtingsmast draaibaar is, al dan niet."""
        return self._isDraaibaar.get_waarde()

    @isDraaibaar.setter
    def isDraaibaar(self, value):
        self._isDraaibaar.set_waarde(value, owner=self)

    @property
    def leverancier(self):
        """Leverancier van de punctuele verlichtingsmast."""
        return self._leverancier.get_waarde()

    @leverancier.setter
    def leverancier(self, value):
        self._leverancier.set_waarde(value, owner=self)

    @property
    def masthoogte(self):
        """Hoogte (in meter) van de punctuele verlichtingsmast."""
        return self._masthoogte.get_waarde()

    @masthoogte.setter
    def masthoogte(self, value):
        self._masthoogte.set_waarde(value, owner=self)

    @property
    def masttype(self):
        """Het type mast voor punctuele verlichting."""
        return self._masttype.get_waarde()

    @masttype.setter
    def masttype(self, value):
        self._masttype.set_waarde(value, owner=self)

    @property
    def rekennota(self):
        """Een bijlage met daarin de rekennota voor de punctuele verlichtingsmast. Deze bevat onder andere ook de omvang/afmetingen van de fundering."""
        return self._rekennota.get_waarde()

    @rekennota.setter
    def rekennota(self, value):
        self._rekennota.set_waarde(value, owner=self)
