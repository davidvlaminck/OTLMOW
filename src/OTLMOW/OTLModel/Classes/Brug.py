# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.AIMNaamObject import AIMNaamObject
from OTLMOW.OTLModel.Datatypes.KwantWrdInKiloNewton import KwantWrdInKiloNewton
from OTLMOW.OTLModel.Datatypes.KwantWrdInMeter import KwantWrdInMeter
from OTLMOW.OTLModel.Datatypes.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Brug(AIMNaamObject):
    """Een beweegbare, vaste of drijvende verbinding voor het verkeer tussen twee punten, die door water of iets anders gescheiden zijn."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._burgerlijkeKlasse = OTLAttribuut(field=KwantWrdInKiloNewton,
                                               naam='burgerlijkeKlasse',
                                               label='burgerlijke klasse',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.burgerlijkeKlasse',
                                               definition='Maximaal toegelaten belasting door gestandariseerde assen, meestal uitgedrukt als totaalgewicht / aslast in kN. Dit dient als ontwerpbelasting en om te oordelen of reële konvooien de brug kunnen overschrijden.',
                                               owner=self)

        self._ontwerpbelasting = OTLAttribuut(field=StringField,
                                              naam='ontwerpbelasting',
                                              label='ontwerpbelasting',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.ontwerpbelasting',
                                              definition='De draagkracht waarvoor de brug ontworpen is.',
                                              owner=self)

        self._ruimteoverspanning = OTLAttribuut(field=KwantWrdInMeter,
                                                naam='ruimteoverspanning',
                                                label='ruimteoverspanning',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.ruimteoverspanning',
                                                definition='De afstand van de ruimte tussen de steunpunten, die de brug moet overbruggen.',
                                                owner=self)

        self._totaleBreedteBrug = OTLAttribuut(field=KwantWrdInMeter,
                                               naam='totaleBreedteBrug',
                                               label='totale breedte brug',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.totaleBreedteBrug',
                                               definition='De totale breedte van de hele brug, in meter.',
                                               owner=self)

        self._totaleLengteBrug = OTLAttribuut(field=KwantWrdInMeter,
                                              naam='totaleLengteBrug',
                                              label='totale lengte brug',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.totaleLengteBrug',
                                              definition='De totale lengte van de hele brug, in meter.',
                                              owner=self)

        self._vrijeDoorvaarthoogte = OTLAttribuut(field=KwantWrdInMeter,
                                                  naam='vrijeDoorvaarthoogte',
                                                  label='vrije doorvaarthoogte',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.vrijeDoorvaarthoogte',
                                                  definition='De hoogte, uitgedrukt in meter, tussen de onderkant van de brug en het waterpeil.',
                                                  owner=self)

        self._vrijeRuimteOnderBrugTerPlaatseRijweg = OTLAttribuut(field=KwantWrdInMeter,
                                                                  naam='vrijeRuimteOnderBrugTerPlaatseRijweg',
                                                                  label='vrije ruimte onder brug ter plaatse (rij)weg',
                                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Brug.vrijeRuimteOnderBrugTerPlaatseRijweg',
                                                                  definition='De vrije ruimte, uitgedrukt in meter, onder de brug ter plaatse van de (rij)weg.',
                                                                  owner=self)

    @property
    def burgerlijkeKlasse(self):
        """Maximaal toegelaten belasting door gestandariseerde assen, meestal uitgedrukt als totaalgewicht / aslast in kN. Dit dient als ontwerpbelasting en om te oordelen of reële konvooien de brug kunnen overschrijden."""
        return self._burgerlijkeKlasse.get_waarde()

    @burgerlijkeKlasse.setter
    def burgerlijkeKlasse(self, value):
        self._burgerlijkeKlasse.set_waarde(value, owner=self)

    @property
    def ontwerpbelasting(self):
        """De draagkracht waarvoor de brug ontworpen is."""
        return self._ontwerpbelasting.get_waarde()

    @ontwerpbelasting.setter
    def ontwerpbelasting(self, value):
        self._ontwerpbelasting.set_waarde(value, owner=self)

    @property
    def ruimteoverspanning(self):
        """De afstand van de ruimte tussen de steunpunten, die de brug moet overbruggen."""
        return self._ruimteoverspanning.get_waarde()

    @ruimteoverspanning.setter
    def ruimteoverspanning(self, value):
        self._ruimteoverspanning.set_waarde(value, owner=self)

    @property
    def totaleBreedteBrug(self):
        """De totale breedte van de hele brug, in meter."""
        return self._totaleBreedteBrug.get_waarde()

    @totaleBreedteBrug.setter
    def totaleBreedteBrug(self, value):
        self._totaleBreedteBrug.set_waarde(value, owner=self)

    @property
    def totaleLengteBrug(self):
        """De totale lengte van de hele brug, in meter."""
        return self._totaleLengteBrug.get_waarde()

    @totaleLengteBrug.setter
    def totaleLengteBrug(self, value):
        self._totaleLengteBrug.set_waarde(value, owner=self)

    @property
    def vrijeDoorvaarthoogte(self):
        """De hoogte, uitgedrukt in meter, tussen de onderkant van de brug en het waterpeil."""
        return self._vrijeDoorvaarthoogte.get_waarde()

    @vrijeDoorvaarthoogte.setter
    def vrijeDoorvaarthoogte(self, value):
        self._vrijeDoorvaarthoogte.set_waarde(value, owner=self)

    @property
    def vrijeRuimteOnderBrugTerPlaatseRijweg(self):
        """De vrije ruimte, uitgedrukt in meter, onder de brug ter plaatse van de (rij)weg."""
        return self._vrijeRuimteOnderBrugTerPlaatseRijweg.get_waarde()

    @vrijeRuimteOnderBrugTerPlaatseRijweg.setter
    def vrijeRuimteOnderBrugTerPlaatseRijweg(self, value):
        self._vrijeRuimteOnderBrugTerPlaatseRijweg.set_waarde(value, owner=self)
