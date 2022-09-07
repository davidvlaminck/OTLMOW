# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Onderdeel.Lichtmast import Lichtmast
from OTLMOW.OTLModel.Datatypes.DtuWvLichtmastBevsToestelMethode import DtuWvLichtmastBevsToestelMethode
from OTLMOW.OTLModel.Datatypes.KlWvLichtmastAantArmen import KlWvLichtmastAantArmen
from OTLMOW.OTLModel.Datatypes.KlWvLichtmastArmlengte import KlWvLichtmastArmlengte


# Generated with OTLClassCreator. To modify: extend, do not edit
class WVLichtmast(Lichtmast):
    """Paal voorzien van armen voor het bevestigen van wegverlichtingstoestellen. Omvat het deurtje, klemmenblok, montagekastje, de bevestigingsmaterialen (bv. voetplaten) en fundering of verankeringsmassief. Gebruik Lichtmast voor de bevestiging van andere toestellen dan wegverlichting."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#KabelgeleidingEnLeidingBevestiging')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#StalenProfiel')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Waarschuwingslantaarn')

        self._aantalArmen = OTLAttribuut(field=KlWvLichtmastAantArmen,
                                         naam='aantalArmen',
                                         label='aantal armen',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.aantalArmen',
                                         definition='Aantal armen van de lichtmast.',
                                         owner=self)

        self._armlengte = OTLAttribuut(field=KlWvLichtmastArmlengte,
                                       naam='armlengte',
                                       label='armlengte',
                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.armlengte',
                                       definition='Lengte van de arm van de lichtmast in meter.',
                                       owner=self)

        self._bevestigingToestellen = OTLAttribuut(field=DtuWvLichtmastBevsToestelMethode,
                                                   naam='bevestigingToestellen',
                                                   label='bevestiging toestellen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#WVLichtmast.bevestigingToestellen',
                                                   kardinaliteit_max='*',
                                                   definition='Geeft de wijze aan waarop elk verlichtingstoestel bevestigd is op de lichtmast als keuze uit een lijst voor standaardmethodes of verder toegelicht wanneer een afwijkende methode gebruikt wordt.',
                                                   owner=self)

    @property
    def aantalArmen(self):
        """Aantal armen van de lichtmast."""
        return self._aantalArmen.get_waarde()

    @aantalArmen.setter
    def aantalArmen(self, value):
        self._aantalArmen.set_waarde(value, owner=self)

    @property
    def armlengte(self):
        """Lengte van de arm van de lichtmast in meter."""
        return self._armlengte.get_waarde()

    @armlengte.setter
    def armlengte(self, value):
        self._armlengte.set_waarde(value, owner=self)

    @property
    def bevestigingToestellen(self):
        """Geeft de wijze aan waarop elk verlichtingstoestel bevestigd is op de lichtmast als keuze uit een lijst voor standaardmethodes of verder toegelicht wanneer een afwijkende methode gebruikt wordt."""
        return self._bevestigingToestellen.get_waarde()

    @bevestigingToestellen.setter
    def bevestigingToestellen(self, value):
        self._bevestigingToestellen.set_waarde(value, owner=self)
