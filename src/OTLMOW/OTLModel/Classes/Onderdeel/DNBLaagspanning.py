# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.DNB import DNB


# Generated with OTLClassCreator. To modify: extend, do not edit
class DNBLaagspanning(DNB):
    """Aansluiting op het laagspanningsnet van de distributienetbeheerder."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBLaagspanning'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Bevestiging', target='https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#Kast')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB')
        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt', target='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#ForfaitaireAansluiting')
