# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class Beton(EMObject):
    """Dit is voor als een techniek aan een tunnel, een tunnelwand of en brug gemonteerd is"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Beton'
    label = 'Betonstructuur'

    def __init__(self):
        super().__init__()

