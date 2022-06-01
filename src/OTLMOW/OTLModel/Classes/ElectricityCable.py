# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Kabel import Kabel
from OTLMOW.OTLModel.Datatypes.KlElectricitySubthema import KlElectricitySubthema
from OTLMOW.OTLModel.Datatypes.KwantWrdInVolt import KwantWrdInVolt


# Generated with OTLClassCreator. To modify: extend, do not edit
class ElectricityCable(Kabel):
    """Een aansluiting of reeks aansluitingen van een nutsvoorzieningennet voor het overbrengen van elektriciteit van de ene locatie naar een andere."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityCable'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self._nominaleSpanning = OTLAttribuut(field=KwantWrdInVolt,
                                              naam='nominaleSpanning',
                                              label='nominale spanning',
                                              objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityCable.nominaleSpanning',
                                              definition='Beschrijft de nominale systeemspanning op de plaats van levering.',
                                              owner=self)

        self._operationeleSpanning = OTLAttribuut(field=KwantWrdInVolt,
                                                  naam='operationeleSpanning',
                                                  label='operationele spanning',
                                                  objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityCable.operationeleSpanning',
                                                  definition='Beschrijft de gebruiks- of bedrijfsspanning op de leiding.',
                                                  owner=self)

        self._subthema = OTLAttribuut(field=KlElectricitySubthema,
                                      naam='subthema',
                                      label='subthema',
                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#ElectricityCable.subthema',
                                      definition='Classificatie van een kabel, leiding, of leidingelementen volgens het thematisch domein waar deze toe behoren.',
                                      owner=self)

    @property
    def nominaleSpanning(self):
        """Beschrijft de nominale systeemspanning op de plaats van levering."""
        return self._nominaleSpanning.get_waarde()

    @nominaleSpanning.setter
    def nominaleSpanning(self, value):
        self._nominaleSpanning.set_waarde(value, owner=self)

    @property
    def operationeleSpanning(self):
        """Beschrijft de gebruiks- of bedrijfsspanning op de leiding."""
        return self._operationeleSpanning.get_waarde()

    @operationeleSpanning.setter
    def operationeleSpanning(self, value):
        self._operationeleSpanning.set_waarde(value, owner=self)

    @property
    def subthema(self):
        """Classificatie van een kabel, leiding, of leidingelementen volgens het thematisch domein waar deze toe behoren."""
        return self._subthema.get_waarde()

    @subthema.setter
    def subthema(self, value):
        self._subthema.set_waarde(value, owner=self)
