# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class SNC(EMObject):
    """VHS flitspalen : Installatie snelheidscamera's : dit type flitspaal registreert snelheidsovertredingen, wordt opgesteld langs de weg"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#SNC'
    label = 'Snelheidscamera installatie'

    def __init__(self):
        super().__init__()

