# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class DiffRelais(EMObject):
    """relais die al dan niet schakelt indien er een lekstroom optreed"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#DiffRelais'
    label = 'Differentieelrelais'

    def __init__(self):
        super().__init__()

