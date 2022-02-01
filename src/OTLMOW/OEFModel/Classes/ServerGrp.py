# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class ServerGrp(EMObject):
    """Bundeling van logische & fysische servers die samenhoren"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#ServerGrp'
    label = 'Server groep'

    def __init__(self):
        super().__init__()

