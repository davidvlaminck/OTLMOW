# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Abstracten.AndereLaag import AndereLaag
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlHechtspecie import KlHechtspecie
from OTLMOW.OTLModel.Datatypes.KlStortsteenKaliber import KlStortsteenKaliber
from OTLMOW.OTLModel.Datatypes.KlStortsteenPlaatsingswijze import KlStortsteenPlaatsingswijze
from OTLMOW.OTLModel.Datatypes.KlStortsteenType import KlStortsteenType
from OTLMOW.OTLModel.Datatypes.KwantWrdInTon import KwantWrdInTon
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Stortsteen(AndereLaag, VlakGeometrie):
    """Natuursteen van onregelmatige vorm,meestal gebruikt voor verstevigings- en beschermingsdoeleinden."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AndereLaag.__init__(self)
        VlakGeometrie.__init__(self)

        self._gewicht = OTLAttribuut(field=KwantWrdInTon,
                                     naam='gewicht',
                                     label='gewicht',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.gewicht',
                                     definition='De hoeveelheid stortsteen in ton.',
                                     owner=self)

        self._hechtspecie = OTLAttribuut(field=KlHechtspecie,
                                         naam='hechtspecie',
                                         label='hechtspecie',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.hechtspecie',
                                         kardinaliteit_max='*',
                                         definition='Het gebruikte hechtingsmateriaal tussen gestapelde stenen.',
                                         owner=self)

        self._isVerankerd = OTLAttribuut(field=BooleanField,
                                         naam='isVerankerd',
                                         label='is verankerd',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.isVerankerd',
                                         definition='Aanduiding of de gestapelde ruwe steen verankerd is.',
                                         owner=self)

        self._kaliber = OTLAttribuut(field=KlStortsteenKaliber,
                                     naam='kaliber',
                                     label='kaliber',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.kaliber',
                                     definition='De gemiddelde diameter van de stortsteen.',
                                     owner=self)

        self._plaatsingswijze = OTLAttribuut(field=KlStortsteenPlaatsingswijze,
                                             naam='plaatsingswijze',
                                             label='bestortingswijze',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.plaatsingswijze',
                                             definition='De manier waarop de stenen worden geplaatst.',
                                             owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.technischeFiche',
                                             kardinaliteit_max='*',
                                             definition='De technische fiche van stortsteen als bijlage.',
                                             owner=self)

        self._type = OTLAttribuut(field=KlStortsteenType,
                                  naam='type',
                                  label='type',
                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stortsteen.type',
                                  definition='Het type stortsteen.',
                                  owner=self)

    @property
    def gewicht(self):
        """De hoeveelheid stortsteen in ton."""
        return self._gewicht.get_waarde()

    @gewicht.setter
    def gewicht(self, value):
        self._gewicht.set_waarde(value, owner=self)

    @property
    def hechtspecie(self):
        """Het gebruikte hechtingsmateriaal tussen gestapelde stenen."""
        return self._hechtspecie.get_waarde()

    @hechtspecie.setter
    def hechtspecie(self, value):
        self._hechtspecie.set_waarde(value, owner=self)

    @property
    def isVerankerd(self):
        """Aanduiding of de gestapelde ruwe steen verankerd is."""
        return self._isVerankerd.get_waarde()

    @isVerankerd.setter
    def isVerankerd(self, value):
        self._isVerankerd.set_waarde(value, owner=self)

    @property
    def kaliber(self):
        """De gemiddelde diameter van de stortsteen."""
        return self._kaliber.get_waarde()

    @kaliber.setter
    def kaliber(self, value):
        self._kaliber.set_waarde(value, owner=self)

    @property
    def plaatsingswijze(self):
        """De manier waarop de stenen worden geplaatst."""
        return self._plaatsingswijze.get_waarde()

    @plaatsingswijze.setter
    def plaatsingswijze(self, value):
        self._plaatsingswijze.set_waarde(value, owner=self)

    @property
    def technischeFiche(self):
        """De technische fiche van stortsteen als bijlage."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self)

    @property
    def type(self):
        """Het type stortsteen."""
        return self._type.get_waarde()

    @type.setter
    def type(self, value):
        self._type.set_waarde(value, owner=self)
