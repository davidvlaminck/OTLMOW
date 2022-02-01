# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class VSB(EMObject):
    """Dynamische borden : Soort van restgroep van allerlei dynamische borden die niet onder een meer specifiek type vallen. Exacte verschil met VGL is me niet duidelijk"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#VSB'
    label = 'Veranderlijke signalisatie borden'

    def __init__(self):
        super().__init__()

