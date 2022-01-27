# coding=utf-8
from src.OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from abc import abstractmethod
from src.OTLMOW.OTLModel.Classes.Kantopsluiting import Kantopsluiting
from src.OTLMOW.OTLModel.Datatypes.BooleanField import BooleanField
from src.OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocument
from src.OTLMOW.OTLModel.Datatypes.KwantWrdInCentimeter import KwantWrdInCentimeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class AfwijkendeKantopsluiting(Kantopsluiting):
    """Abstracte voor een kantopsluiting die niet voldoet aan een bepaalde standaard."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()

        self._breedte = OTLAttribuut(field=KwantWrdInCentimeter,
                                     naam='breedte',
                                     label='breedte',
                                     objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.breedte',
                                     definition='De breedte van de afwijkende kantopsluiting in centimeter.')

        self._dikte = OTLAttribuut(field=KwantWrdInCentimeter,
                                   naam='dikte',
                                   label='dikte',
                                   objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.dikte',
                                   definition='De dikte van de afwijkende kantopsluiting in centimeter.')

        self._heeftOppervlaktebehandeling = OTLAttribuut(field=BooleanField,
                                                         naam='heeftOppervlaktebehandeling',
                                                         label='heeft oppervlaktebehandeling',
                                                         objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.heeftOppervlaktebehandeling',
                                                         definition='Aanduiding of er een oppervlaktebehandeling is uitgevoerd op de afwijkende kantopsluiting.')

        self._technischeFicheAfwijking = OTLAttribuut(field=DtcDocument,
                                                      naam='technischeFicheAfwijking',
                                                      label='technische fiche afwijking',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AfwijkendeKantopsluiting.technischeFicheAfwijking',
                                                      usagenote='Bestanden van het type xlsx of pdf.',
                                                      kardinaliteit_max='*',
                                                      definition='De technische fiche van de afwijkende kantopsluiting.')

    @property
    def breedte(self):
        """De breedte van de afwijkende kantopsluiting in centimeter."""
        return self._breedte.waarde

    @breedte.setter
    def breedte(self, value):
        self._breedte.set_waarde(value, owner=self)

    @property
    def dikte(self):
        """De dikte van de afwijkende kantopsluiting in centimeter."""
        return self._dikte.waarde

    @dikte.setter
    def dikte(self, value):
        self._dikte.set_waarde(value, owner=self)

    @property
    def heeftOppervlaktebehandeling(self):
        """Aanduiding of er een oppervlaktebehandeling is uitgevoerd op de afwijkende kantopsluiting."""
        return self._heeftOppervlaktebehandeling.waarde

    @heeftOppervlaktebehandeling.setter
    def heeftOppervlaktebehandeling(self, value):
        self._heeftOppervlaktebehandeling.set_waarde(value, owner=self)

    @property
    def technischeFicheAfwijking(self):
        """De technische fiche van de afwijkende kantopsluiting."""
        return self._technischeFicheAfwijking.waarde

    @technischeFicheAfwijking.setter
    def technischeFicheAfwijking(self, value):
        self._technischeFicheAfwijking.set_waarde(value, owner=self)
