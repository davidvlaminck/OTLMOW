# coding=utf-8
from OTLMOW.OTLModel.Classes.Abstracten.KabelAarding import KabelAarding
from OTLMOW.OTLModel.Classes.Abstracten.KabelAardingSamenstelling import KabelAardingSamenstelling
from OTLMOW.OTLModel.Classes.ImplementatieElement.AIMNaamObject import AIMNaamObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class Aardingslus(KabelAarding, KabelAardingSamenstelling, AIMNaamObject):
    """Een koperen geleider die onder de fundering van een gebouw de contouren van het te aarden gebouw volgt. De lus vertrekt en komt aan op de aardingsonderbreker."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Aardingslus'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        AIMNaamObject.__init__(self)
        KabelAarding.__init__(self)
        KabelAardingSamenstelling.__init__(self)

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HoortBij', target='https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Aardingsinstallatie')
