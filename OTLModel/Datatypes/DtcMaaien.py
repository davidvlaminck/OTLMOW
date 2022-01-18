# coding=utf-8
from OTLModel.BaseClasses.AttributeInfo import AttributeInfo
from OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLModel.Datatypes.BooleanField import BooleanField
from OTLModel.Datatypes.ComplexField import ComplexField
from OTLModel.Datatypes.KlMaaiFrequentie import KlMaaiFrequentie
from OTLModel.Datatypes.KlMaaiPeriode import KlMaaiPeriode


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMaaienWaarden(AttributeInfo):
    def __init__(self):
        self._frequentie = OTLAttribuut(field=KlMaaiFrequentie,
                                        naam='frequentie',
                                        label='frequentie',
                                        objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.frequentie',
                                        kardinaliteit_max='*',
                                        definition='Het aantal keer dat er gemaaid wordt per jaar.')

        self._isGazonbeheer = OTLAttribuut(field=BooleanField,
                                           naam='isGazonbeheer',
                                           label='is gazonbeheer',
                                           objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.isGazonbeheer',
                                           definition='Aanduiding of de grazige vegetatie meer dan 3x per jaar gemaaid wordt.')

        self._isMachinaal = OTLAttribuut(field=BooleanField,
                                         naam='isMachinaal',
                                         label='is machinaal',
                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.isMachinaal',
                                         definition='Aanduiding of het maaien machinaal of handmatig wordt uitgevoerd.')

        self._isRuigtebeheer = OTLAttribuut(field=BooleanField,
                                            naam='isRuigtebeheer',
                                            label='is ruigtebeheer',
                                            objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.isRuigtebeheer',
                                            definition='Aanduiding of de grazige vegetatie minder dan 1x per jaar gemaaid wordt.')

        self._isVeiligheidsmaaien = OTLAttribuut(field=BooleanField,
                                                 naam='isVeiligheidsmaaien',
                                                 label='is veiligheidsmaaien',
                                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.isVeiligheidsmaaien',
                                                 definition='Aanduiding of er een maaistrook aanwezig is voor het vrijwaren van de zichtbaarheid en voor het vrijhouden van de bebakening en signalisatie.')

        self._klepelmaaierToegelaten = OTLAttribuut(field=BooleanField,
                                                    naam='klepelmaaierToegelaten',
                                                    label='klepelmaaier toegelaten',
                                                    objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.klepelmaaierToegelaten',
                                                    definition='Aanduiding of er gemaaid mag worden met een klepelmaaier.')

        self._periode = OTLAttribuut(field=KlMaaiPeriode,
                                     naam='periode',
                                     label='periode',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien.periode',
                                     kardinaliteit_max='*',
                                     definition='De maand waarin het maaien wordt uitgevoerd.')

    @property
    def frequentie(self):
        """Het aantal keer dat er gemaaid wordt per jaar."""
        return self._frequentie.waarde

    @frequentie.setter
    def frequentie(self, value):
        self._frequentie.set_waarde(value)

    @property
    def isGazonbeheer(self):
        """Aanduiding of de grazige vegetatie meer dan 3x per jaar gemaaid wordt."""
        return self._isGazonbeheer.waarde

    @isGazonbeheer.setter
    def isGazonbeheer(self, value):
        self._isGazonbeheer.set_waarde(value)

    @property
    def isMachinaal(self):
        """Aanduiding of het maaien machinaal of handmatig wordt uitgevoerd."""
        return self._isMachinaal.waarde

    @isMachinaal.setter
    def isMachinaal(self, value):
        self._isMachinaal.set_waarde(value)

    @property
    def isRuigtebeheer(self):
        """Aanduiding of de grazige vegetatie minder dan 1x per jaar gemaaid wordt."""
        return self._isRuigtebeheer.waarde

    @isRuigtebeheer.setter
    def isRuigtebeheer(self, value):
        self._isRuigtebeheer.set_waarde(value)

    @property
    def isVeiligheidsmaaien(self):
        """Aanduiding of er een maaistrook aanwezig is voor het vrijwaren van de zichtbaarheid en voor het vrijhouden van de bebakening en signalisatie."""
        return self._isVeiligheidsmaaien.waarde

    @isVeiligheidsmaaien.setter
    def isVeiligheidsmaaien(self, value):
        self._isVeiligheidsmaaien.set_waarde(value)

    @property
    def klepelmaaierToegelaten(self):
        """Aanduiding of er gemaaid mag worden met een klepelmaaier."""
        return self._klepelmaaierToegelaten.waarde

    @klepelmaaierToegelaten.setter
    def klepelmaaierToegelaten(self, value):
        self._klepelmaaierToegelaten.set_waarde(value)

    @property
    def periode(self):
        """De maand waarin het maaien wordt uitgevoerd."""
        return self._periode.waarde

    @periode.setter
    def periode(self, value):
        self._periode.set_waarde(value)


# Generated with OTLComplexDatatypeCreator. To modify: extend, do not edit
class DtcMaaien(ComplexField, AttributeInfo):
    """Complex datatype voor de eigenschappen van maaien."""
    naam = 'DtcMaaien'
    label = 'Maaien'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/levenscyclus#DtcMaaien'
    definition = 'Complex datatype voor de eigenschappen van maaien.'
    waardeObject = DtcMaaienWaarden

    def __str__(self):
        return ComplexField.__str__(self)

