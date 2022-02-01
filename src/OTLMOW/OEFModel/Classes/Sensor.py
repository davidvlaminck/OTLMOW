# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class Sensor(EMObject):
    """sensor  CO, NO2, explosieve, temp, luchtsnelheid, zicht, ...."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Sensor'
    label = 'Sensor'

    def __init__(self):
        super().__init__()

