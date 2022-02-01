# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class Instal(EMObject):
    """Generiek onderdeeltype voor top van de installatieboom, niet gebruiken voor subonderdelen"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#Instal'
    label = 'Installatie'

    def __init__(self):
        super().__init__()

