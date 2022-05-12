# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from OTLMOW.OTLModel.Datatypes.ComplexField import ComplexField
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from OTLMOW.OTLModel.Datatypes.KlBetonmilieuklasse import KlBetonmilieuklasse
from OTLMOW.OTLModel.Datatypes.KlBetonomgevingsklasse import KlBetonomgevingsklasse
from OTLMOW.OTLModel.Datatypes.KlBetonsterkteklasse import KlBetonsterkteklasse
from OTLMOW.OTLModel.Datatypes.KlGebruiksdomein import KlGebruiksdomein
from OTLMOW.OTLModel.Datatypes.KwantWrdInMillimeter import KwantWrdInMillimeter


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBetonspecificatiesWaarden(AttributeInfo):
    def __init__(self, parent=None):
        AttributeInfo.__init__(self, parent)
        self._betondekking = OTLAttribuut(field=KwantWrdInMillimeter,
                                          naam='betondekking',
                                          label='betondekking',
                                          objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betondekking',
                                          definition='De afstand in millimeter tussen de buitenkant van het beton (het oppervlak van het beton) tot het dichtstbijzijnde wapeningsstaal.',
                                          owner=self)

        self._betonmilieuklassen = OTLAttribuut(field=KlBetonmilieuklasse,
                                                naam='betonmilieuklassen',
                                                label='betonmilieuklassen',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonmilieuklassen',
                                                kardinaliteit_max='*',
                                                definition='Milieuklassen (X-klassen) leggen rechtstreeks de link met bepaalde aantastingsmechanismen, waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere milieuklassen van toepassing zijn.',
                                                owner=self)

        self._betonomgevingsklassen = OTLAttribuut(field=KlBetonomgevingsklasse,
                                                   naam='betonomgevingsklassen',
                                                   label='betonomgevingsklassen',
                                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonomgevingsklassen',
                                                   kardinaliteit_max='*',
                                                   definition='De omgeving waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere omgevingsklassen van toepassing zijn.',
                                                   owner=self)

        self._betonsterkteklasse = OTLAttribuut(field=KlBetonsterkteklasse,
                                                naam='betonsterkteklasse',
                                                label='betonsterkteklasse',
                                                objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.betonsterkteklasse',
                                                definition='De sterkteklasse is een maat voor de druksterkte van beton.',
                                                owner=self)

        self._gebruiksdomein = OTLAttribuut(field=KlGebruiksdomein,
                                            naam='gebruiksdomein',
                                            label='gebruiksdomein',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.gebruiksdomein',
                                            definition='De gebruiksomstandigheden van het beton. Dit bepaalt tevens het maximum chloridegehalte.',
                                            owner=self)

        self._grootsteKorrelafmetingDmax = OTLAttribuut(field=KwantWrdInMillimeter,
                                                        naam='grootsteKorrelafmetingDmax',
                                                        label='grootste korrelafmeting (Dmax)',
                                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.grootsteKorrelafmetingDmax',
                                                        definition='De nominale grootste korrelafmeting (Dmax).',
                                                        owner=self)

        self._isCementMetBeperktAlkaligehalte = OTLAttribuut(field=BooleanField,
                                                             naam='isCementMetBeperktAlkaligehalte',
                                                             label='is cement met beperkt alkaligehalte',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetBeperktAlkaligehalte',
                                                             definition='Aanduiding of het cement een beperkt alkaligehalte heeft (LA).',
                                                             owner=self)

        self._isCementMetHogeAanvangssterkte = OTLAttribuut(field=BooleanField,
                                                            naam='isCementMetHogeAanvangssterkte',
                                                            label='is cement met hoge aanvangssterkte',
                                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetHogeAanvangssterkte',
                                                            definition='Geeft aan of het cement gebruikt wordt voor een snelle binding (bijvoorbeeld in de winter) (HES).',
                                                            owner=self)

        self._isCementMetHogeBestandheidTegenSulfaten = OTLAttribuut(field=BooleanField,
                                                                     naam='isCementMetHogeBestandheidTegenSulfaten',
                                                                     label='is cement met hoge bestandheid tegen sulfaten',
                                                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetHogeBestandheidTegenSulfaten',
                                                                     definition='Geeft aan of het cement een hoge bestandheid heeft tegen sulfaten (SR).',
                                                                     owner=self)

        self._isCementMetLageHydratatiewarmte = OTLAttribuut(field=BooleanField,
                                                             naam='isCementMetLageHydratatiewarmte',
                                                             label='is cement met lage hydratatiewarmte',
                                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isCementMetLageHydratatiewarmte',
                                                             definition='Geeft aan of het cement gebruikt wordt voor een tragere sterkteontwikkeling (LH).',
                                                             owner=self)

        self._isColloidaalbeton = OTLAttribuut(field=BooleanField,
                                               naam='isColloidaalbeton',
                                               label='is colloïdaalbeton',
                                               objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.isColloidaalbeton',
                                               definition='Geeft aan of het beton zich niet ontmengt onder of in water.',
                                               owner=self)

        self._technischeFiche = OTLAttribuut(field=DtcDocument,
                                             naam='technischeFiche',
                                             label='technische fiche',
                                             objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties.technischeFiche',
                                             definition='De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,...',
                                             owner=self)

    @property
    def betondekking(self):
        """De afstand in millimeter tussen de buitenkant van het beton (het oppervlak van het beton) tot het dichtstbijzijnde wapeningsstaal."""
        return self._betondekking.get_waarde()

    @betondekking.setter
    def betondekking(self, value):
        self._betondekking.set_waarde(value, owner=self._parent)

    @property
    def betonmilieuklassen(self):
        """Milieuklassen (X-klassen) leggen rechtstreeks de link met bepaalde aantastingsmechanismen, waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere milieuklassen van toepassing zijn."""
        return self._betonmilieuklassen.get_waarde()

    @betonmilieuklassen.setter
    def betonmilieuklassen(self, value):
        self._betonmilieuklassen.set_waarde(value, owner=self._parent)

    @property
    def betonomgevingsklassen(self):
        """De omgeving waaraan de betonconstructie (of een onderdeel ervan) wordt blootgesteld tijdens het gebruik. Er kunnen meerdere omgevingsklassen van toepassing zijn."""
        return self._betonomgevingsklassen.get_waarde()

    @betonomgevingsklassen.setter
    def betonomgevingsklassen(self, value):
        self._betonomgevingsklassen.set_waarde(value, owner=self._parent)

    @property
    def betonsterkteklasse(self):
        """De sterkteklasse is een maat voor de druksterkte van beton."""
        return self._betonsterkteklasse.get_waarde()

    @betonsterkteklasse.setter
    def betonsterkteklasse(self, value):
        self._betonsterkteklasse.set_waarde(value, owner=self._parent)

    @property
    def gebruiksdomein(self):
        """De gebruiksomstandigheden van het beton. Dit bepaalt tevens het maximum chloridegehalte."""
        return self._gebruiksdomein.get_waarde()

    @gebruiksdomein.setter
    def gebruiksdomein(self, value):
        self._gebruiksdomein.set_waarde(value, owner=self._parent)

    @property
    def grootsteKorrelafmetingDmax(self):
        """De nominale grootste korrelafmeting (Dmax)."""
        return self._grootsteKorrelafmetingDmax.get_waarde()

    @grootsteKorrelafmetingDmax.setter
    def grootsteKorrelafmetingDmax(self, value):
        self._grootsteKorrelafmetingDmax.set_waarde(value, owner=self._parent)

    @property
    def isCementMetBeperktAlkaligehalte(self):
        """Aanduiding of het cement een beperkt alkaligehalte heeft (LA)."""
        return self._isCementMetBeperktAlkaligehalte.get_waarde()

    @isCementMetBeperktAlkaligehalte.setter
    def isCementMetBeperktAlkaligehalte(self, value):
        self._isCementMetBeperktAlkaligehalte.set_waarde(value, owner=self._parent)

    @property
    def isCementMetHogeAanvangssterkte(self):
        """Geeft aan of het cement gebruikt wordt voor een snelle binding (bijvoorbeeld in de winter) (HES)."""
        return self._isCementMetHogeAanvangssterkte.get_waarde()

    @isCementMetHogeAanvangssterkte.setter
    def isCementMetHogeAanvangssterkte(self, value):
        self._isCementMetHogeAanvangssterkte.set_waarde(value, owner=self._parent)

    @property
    def isCementMetHogeBestandheidTegenSulfaten(self):
        """Geeft aan of het cement een hoge bestandheid heeft tegen sulfaten (SR)."""
        return self._isCementMetHogeBestandheidTegenSulfaten.get_waarde()

    @isCementMetHogeBestandheidTegenSulfaten.setter
    def isCementMetHogeBestandheidTegenSulfaten(self, value):
        self._isCementMetHogeBestandheidTegenSulfaten.set_waarde(value, owner=self._parent)

    @property
    def isCementMetLageHydratatiewarmte(self):
        """Geeft aan of het cement gebruikt wordt voor een tragere sterkteontwikkeling (LH)."""
        return self._isCementMetLageHydratatiewarmte.get_waarde()

    @isCementMetLageHydratatiewarmte.setter
    def isCementMetLageHydratatiewarmte(self, value):
        self._isCementMetLageHydratatiewarmte.set_waarde(value, owner=self._parent)

    @property
    def isColloidaalbeton(self):
        """Geeft aan of het beton zich niet ontmengt onder of in water."""
        return self._isColloidaalbeton.get_waarde()

    @isColloidaalbeton.setter
    def isColloidaalbeton(self, value):
        self._isColloidaalbeton.set_waarde(value, owner=self._parent)

    @property
    def technischeFiche(self):
        """De technische fiche van het beton. Deze moet volgende eigenschappen bevatten: de norm waaraan het beton voldoet, de sterkteklasse, de duurzaamheid (bestaande uit het gebruiksdomein en de omgevingsklasse(n)), de consistentieklasse, de nominale grootste korrelafmeting,..."""
        return self._technischeFiche.get_waarde()

    @technischeFiche.setter
    def technischeFiche(self, value):
        self._technischeFiche.set_waarde(value, owner=self._parent)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcBetonspecificaties(ComplexField, AttributeInfo):
    """Complex datatype om de eigenschappen van beton te bundelen."""
    naam = 'DtcBetonspecificaties'
    label = 'Betonspecificaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcBetonspecificaties'
    definition = 'Complex datatype om de eigenschappen van beton te bundelen.'
    waardeObject = DtcBetonspecificatiesWaarden

    def __str__(self):
        return ComplexField.__str__(self)

