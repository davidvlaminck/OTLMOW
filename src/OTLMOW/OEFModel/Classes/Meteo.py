# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class Meteo(EMObject):
    """METEOSTATION"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Meteo'
    label = 'Meteostation'

    def __init__(self):
        super().__init__()

