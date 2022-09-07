# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.PU import PU


# Generated with OTLClassCreator. To modify: extend, do not edit
class MACQPUFrontend(PU):
    """Een processing unit van MACQ die de link legt tussen de AID-module en de AID-push server en de correlatiemodule."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#MACQPUFrontend'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#SoftwareToegang')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Sturing', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#AIDModule')
