from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypeUnion import OSLODatatypeUnion
from ModelGenerator.OSLODatatypeUnionAttribuut import OSLODatatypeUnionAttribuut


class OTLUnionDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        super().__init__(logger, osloCollector)
        self.logger.log("Created an instance of OTLUnionDatatypeCreator", LogType.INFO)

    def CreateBlockToWriteFromUnionTypes(self, oSLODatatypeUnion: OSLODatatypeUnion):
        if not isinstance(oSLODatatypeUnion, OSLODatatypeUnion):
            raise ValueError(f"Input is not a OSLODatatypeUnion")

        if oSLODatatypeUnion.objectUri == '' or not (oSLODatatypeUnion.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/') and 'Dtu' in oSLODatatypeUnion.objectUri):
            raise ValueError(f"OSLODatatypeUnion.objectUri is invalid. Value = '{oSLODatatypeUnion.objectUri}'")

        if oSLODatatypeUnion.name == '':
            raise ValueError(f"OSLODatatypeUnion.name is invalid. Value = '{oSLODatatypeUnion.name}'")

        return self.CreateBlockToWriteFromComplexPrimitiveOrUnionTypes(oSLODatatypeUnion, typeField='UnionType')


