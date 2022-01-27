# coding=utf-8
from OTLMOW.OTLModel.BaseClasses.OTLAttribuut import OTLAttribuut
from OTLMOW.OTLModel.Classes.Energiemeter import Energiemeter


# Generated with OTLClassCreator. To modify: extend, do not edit
class EnergiemeterDerden(Energiemeter):
    """Toestel dat eigendom is van een derde partij, verschillend van de distributienetbeheerder, waarmee het energieverbruik van de installaties van deze derden gemeten wordt. 
Deze energiemeters komen enkel voor op:
- installaties van AWV waarop derden een afzonderlijke kring hebben gekregen voor het voeden van hun eigen installaties
- installaties van derden waarop AWV een afzonderlijke kring heeft gekregen voor het voeden van onze installaties"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDerden'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
