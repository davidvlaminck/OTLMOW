# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Proef import Proef
from OTLMOW.OTLModel.Datatypes.DateTimeField import DateTimeField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.FloatOrDecimalField import FloatOrDecimalField
from OTLMOW.OTLModel.Datatypes.KlBoomConditiebeoordeling import KlBoomConditiebeoordeling
from OTLMOW.OTLModel.Datatypes.KlBoomConditiewaarde import KlBoomConditiewaarde
from OTLMOW.OTLModel.Datatypes.KlBoomConflicten import KlBoomConflicten
from OTLMOW.OTLModel.Datatypes.KlBoomGebreken import KlBoomGebreken
from OTLMOW.OTLModel.Datatypes.KlBoomOnderhoudstoestand import KlBoomOnderhoudstoestand
from OTLMOW.OTLModel.Datatypes.KlBoomPlantwijzewaarde import KlBoomPlantwijzewaarde
from OTLMOW.OTLModel.Datatypes.KlBoomStandplaatswaarde import KlBoomStandplaatswaarde
from OTLMOW.OTLModel.Datatypes.KlBoomtoestandMeerwaardefactor import KlBoomtoestandMeerwaardefactor
from OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter
from OTLMOW.OTLModel.Datatypes.KwantWrdInEuro import KwantWrdInEuro
from OTLMOW.GeometrieArtefact.PuntGeometrie import PuntGeometrie
from OTLMOW.GeometrieArtefact.LijnGeometrie import LijnGeometrie
from OTLMOW.GeometrieArtefact.VlakGeometrie import VlakGeometrie


# Generated with OTLClassCreator. To modify: extend, do not edit
class ProefBoomtoestand(Proef, PuntGeometrie, LijnGeometrie, VlakGeometrie):
    """De toestand met waarnemingen per inspectie van een boom."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        Proef.__init__(self)
        LijnGeometrie.__init__(self)
        PuntGeometrie.__init__(self)
        VlakGeometrie.__init__(self)

        self._basiswaarde = OTLAttribuut(field=KwantWrdInEuro,
                                         naam='basiswaarde',
                                         label='rapportage onderzoek',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.basiswaarde',
                                         definition='Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt.',
                                         owner=self)

        self._conditiebeoordeling = OTLAttribuut(field=KlBoomConditiebeoordeling,
                                                 naam='conditiebeoordeling',
                                                 label='conditiebeoordeling',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.conditiebeoordeling',
                                                 definition='De conditie beoordeeld volgens de kronenstructuur van Dr. A. Roloff, gelet op de scheutlengte ontwikkeling en vorming van dood hout.',
                                                 owner=self)

        self._conditiewaarde = OTLAttribuut(field=KlBoomConditiewaarde,
                                            naam='conditiewaarde',
                                            label='conditiewaarde',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.conditiewaarde',
                                            definition='Een coëfficiënt die iets vertelt over de gezondheidstoestand (vitaliteit, conditie) en de levensverwachting van een boom.',
                                            owner=self)

        self._conflicten = OTLAttribuut(field=KlBoomConflicten,
                                        naam='conflicten',
                                        label='conflicten',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.conflicten',
                                        definition='Mogelijke standplaatsconflicten die de condities of structuur van de boom negatief kunnen beïnvloeden.',
                                        owner=self)

        self._gebreken = OTLAttribuut(field=KlBoomGebreken,
                                      naam='gebreken',
                                      label='gebreken',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.gebreken',
                                      kardinaliteit_max='*',
                                      definition='Een visueel defect aan een boom wat dient gemonitord te worden.',
                                      owner=self)

        self._krooninspectie = OTLAttribuut(field=DtcDocument,
                                            naam='krooninspectie',
                                            label='krooninspectie',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.krooninspectie',
                                            definition='Controle van gebrekssymptomen in de kroon.',
                                            owner=self)

        self._meerwaarde = OTLAttribuut(field=KlBoomtoestandMeerwaardefactor,
                                        naam='meerwaarde',
                                        label='meerwaarde',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.meerwaarde',
                                        definition='Mogelijkheid om de boom een waarde toe te kennen op basis van hun uitzonderlijke ecologische of erfgoedwaarde .',
                                        owner=self)

        self._onderhoudstoestand = OTLAttribuut(field=KlBoomOnderhoudstoestand,
                                                naam='onderhoudstoestand',
                                                label='onderhoudstoestand',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.onderhoudstoestand',
                                                definition='De toestand van een boom die de eventuele snoeiachterstand aangeeft.',
                                                owner=self)

        self._onderzoekVisueleBoomcontrole = OTLAttribuut(field=DtcDocument,
                                                          naam='onderzoekVisueleBoomcontrole',
                                                          label='Onderzoek visuele boomcontrole',
                                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.onderzoekVisueleBoomcontrole',
                                                          definition='Visueel bepalen van de veiligheid en conditie van een boom.',
                                                          owner=self)

        self._plantwijzewaarde = OTLAttribuut(field=KlBoomPlantwijzewaarde,
                                              naam='plantwijzewaarde',
                                              label='plantwijzewaarde',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.plantwijzewaarde',
                                              definition='Een factor die de ontwikkeling van het uiterlijk (de habitus) van een boom relateert met de manier waarop hij geplant wordt.',
                                              owner=self)

        self._rapportageOnderzoek = OTLAttribuut(field=DtcDocument,
                                                 naam='rapportageOnderzoek',
                                                 label='rapportage onderzoek',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.rapportageOnderzoek',
                                                 definition='Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt.',
                                                 owner=self)

        self._soortwaarde = OTLAttribuut(field=FloatOrDecimalField,
                                         naam='soortwaarde',
                                         label='soortwaarde',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.soortwaarde',
                                         definition='Geeft voor een bepaalde boomsoort of -variëteit de verhouding weer tussen de prijs per cm² van die soort en de eenheidsprijs.',
                                         owner=self)

        self._stamomtrek = OTLAttribuut(field=KwantWrdInCentimeter,
                                        naam='stamomtrek',
                                        label='stamomtrek',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.stamomtrek',
                                        definition='Omtrek van de stam van de boom in cm, gemeten op 1 meter boven de grond.',
                                        owner=self)

        self._standplaatswaarde = OTLAttribuut(field=KlBoomStandplaatswaarde,
                                               naam='standplaatswaarde',
                                               label='standplaatswaarde',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.standplaatswaarde',
                                               definition='De waarde van de boom afhankelijk van de bebouwingsdichtheid en de aanplantingsmogelijkheden rondom en voor de boom.',
                                               owner=self)

        self._tijdstempelBoomtoestand = OTLAttribuut(field=DateTimeField,
                                                     naam='tijdstempelBoomtoestand',
                                                     label='tijdstempel boomtoestand',
                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.tijdstempelBoomtoestand',
                                                     definition='Datum van laatste snoeibeurt.',
                                                     owner=self)

        self._uitgebreidPlaatsonderzoek = OTLAttribuut(field=DtcDocument,
                                                       naam='uitgebreidPlaatsonderzoek',
                                                       label='uitgebreid plaatsonderzoek',
                                                       objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.uitgebreidPlaatsonderzoek',
                                                       definition='Grondige beoordeling van de textuur en structuur van de bodem, met als doel een voorstel tot conditieverbeterende maatregelen.',
                                                       owner=self)

        self._wortelonderzoek = OTLAttribuut(field=DtcDocument,
                                             naam='wortelonderzoek',
                                             label='Wortelonderzoek',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#ProefBoomtoestand.wortelonderzoek',
                                             definition='Bepalen van de kwaliteit van de wortels (bv. aantasting door schimmels) of het bepalen van de reikwijdte van de wortels (bv. om een wortelbeschermingszone op te zetten in de buurt van werken van de  bomen).',
                                             owner=self)

    @property
    def basiswaarde(self):
        """Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt."""
        return self._basiswaarde.get_waarde()

    @basiswaarde.setter
    def basiswaarde(self, value):
        self._basiswaarde.set_waarde(value, owner=self)

    @property
    def conditiebeoordeling(self):
        """De conditie beoordeeld volgens de kronenstructuur van Dr. A. Roloff, gelet op de scheutlengte ontwikkeling en vorming van dood hout."""
        return self._conditiebeoordeling.get_waarde()

    @conditiebeoordeling.setter
    def conditiebeoordeling(self, value):
        self._conditiebeoordeling.set_waarde(value, owner=self)

    @property
    def conditiewaarde(self):
        """Een coëfficiënt die iets vertelt over de gezondheidstoestand (vitaliteit, conditie) en de levensverwachting van een boom."""
        return self._conditiewaarde.get_waarde()

    @conditiewaarde.setter
    def conditiewaarde(self, value):
        self._conditiewaarde.set_waarde(value, owner=self)

    @property
    def conflicten(self):
        """Mogelijke standplaatsconflicten die de condities of structuur van de boom negatief kunnen beïnvloeden."""
        return self._conflicten.get_waarde()

    @conflicten.setter
    def conflicten(self, value):
        self._conflicten.set_waarde(value, owner=self)

    @property
    def gebreken(self):
        """Een visueel defect aan een boom wat dient gemonitord te worden."""
        return self._gebreken.get_waarde()

    @gebreken.setter
    def gebreken(self, value):
        self._gebreken.set_waarde(value, owner=self)

    @property
    def krooninspectie(self):
        """Controle van gebrekssymptomen in de kroon."""
        return self._krooninspectie.get_waarde()

    @krooninspectie.setter
    def krooninspectie(self, value):
        self._krooninspectie.set_waarde(value, owner=self)

    @property
    def meerwaarde(self):
        """Mogelijkheid om de boom een waarde toe te kennen op basis van hun uitzonderlijke ecologische of erfgoedwaarde ."""
        return self._meerwaarde.get_waarde()

    @meerwaarde.setter
    def meerwaarde(self, value):
        self._meerwaarde.set_waarde(value, owner=self)

    @property
    def onderhoudstoestand(self):
        """De toestand van een boom die de eventuele snoeiachterstand aangeeft."""
        return self._onderhoudstoestand.get_waarde()

    @onderhoudstoestand.setter
    def onderhoudstoestand(self, value):
        self._onderhoudstoestand.set_waarde(value, owner=self)

    @property
    def onderzoekVisueleBoomcontrole(self):
        """Visueel bepalen van de veiligheid en conditie van een boom."""
        return self._onderzoekVisueleBoomcontrole.get_waarde()

    @onderzoekVisueleBoomcontrole.setter
    def onderzoekVisueleBoomcontrole(self, value):
        self._onderzoekVisueleBoomcontrole.set_waarde(value, owner=self)

    @property
    def plantwijzewaarde(self):
        """Een factor die de ontwikkeling van het uiterlijk (de habitus) van een boom relateert met de manier waarop hij geplant wordt."""
        return self._plantwijzewaarde.get_waarde()

    @plantwijzewaarde.setter
    def plantwijzewaarde(self, value):
        self._plantwijzewaarde.set_waarde(value, owner=self)

    @property
    def rapportageOnderzoek(self):
        """Het schriftelijk verslag dat na onderzoek of visuele controle wordt opgemaakt."""
        return self._rapportageOnderzoek.get_waarde()

    @rapportageOnderzoek.setter
    def rapportageOnderzoek(self, value):
        self._rapportageOnderzoek.set_waarde(value, owner=self)

    @property
    def soortwaarde(self):
        """Geeft voor een bepaalde boomsoort of -variëteit de verhouding weer tussen de prijs per cm² van die soort en de eenheidsprijs."""
        return self._soortwaarde.get_waarde()

    @soortwaarde.setter
    def soortwaarde(self, value):
        self._soortwaarde.set_waarde(value, owner=self)

    @property
    def stamomtrek(self):
        """Omtrek van de stam van de boom in cm, gemeten op 1 meter boven de grond."""
        return self._stamomtrek.get_waarde()

    @stamomtrek.setter
    def stamomtrek(self, value):
        self._stamomtrek.set_waarde(value, owner=self)

    @property
    def standplaatswaarde(self):
        """De waarde van de boom afhankelijk van de bebouwingsdichtheid en de aanplantingsmogelijkheden rondom en voor de boom."""
        return self._standplaatswaarde.get_waarde()

    @standplaatswaarde.setter
    def standplaatswaarde(self, value):
        self._standplaatswaarde.set_waarde(value, owner=self)

    @property
    def tijdstempelBoomtoestand(self):
        """Datum van laatste snoeibeurt."""
        return self._tijdstempelBoomtoestand.get_waarde()

    @tijdstempelBoomtoestand.setter
    def tijdstempelBoomtoestand(self, value):
        self._tijdstempelBoomtoestand.set_waarde(value, owner=self)

    @property
    def uitgebreidPlaatsonderzoek(self):
        """Grondige beoordeling van de textuur en structuur van de bodem, met als doel een voorstel tot conditieverbeterende maatregelen."""
        return self._uitgebreidPlaatsonderzoek.get_waarde()

    @uitgebreidPlaatsonderzoek.setter
    def uitgebreidPlaatsonderzoek(self, value):
        self._uitgebreidPlaatsonderzoek.set_waarde(value, owner=self)

    @property
    def wortelonderzoek(self):
        """Bepalen van de kwaliteit van de wortels (bv. aantasting door schimmels) of het bepalen van de reikwijdte van de wortels (bv. om een wortelbeschermingszone op te zetten in de buurt van werken van de  bomen)."""
        return self._wortelonderzoek.get_waarde()

    @wortelonderzoek.setter
    def wortelonderzoek(self, value):
        self._wortelonderzoek.set_waarde(value, owner=self)
