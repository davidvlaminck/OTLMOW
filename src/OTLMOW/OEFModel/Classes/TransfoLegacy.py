# coding=utf-8
from OTLMOW.OEFModel.EMObject import EMObject


# Generated with OEFClassCreator. To modify: extend, do not edit
class TransfoLegacy(EMObject):
    """transformator die hoogspanning tranformeert in laagspanning"""

    typeURI = 'https://lgc.data.wegenenverkeer.be/ns/installatie#TransfoLegacy'
    label = 'Transformator (Legacy)'

    def __init__(self):
        super().__init__()

