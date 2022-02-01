# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class AntenneI2V(EMObject):
    """Road side unit (RSU) voor ITS-G5 broadcasting. Deze antenne faciliteert in Infrastructuur-naar-Voertuig (I2V) communicatie."""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#AntenneI2V'
    label = 'Antenne I2V'

    def __init__(self):
        super().__init__()

