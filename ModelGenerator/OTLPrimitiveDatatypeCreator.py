from Loggers.AbstractLogger import AbstractLogger
from Loggers.LogType import LogType
from ModelGenerator.AbstractDatatypeCreator import AbstractDatatypeCreator
from ModelGenerator.OSLOCollector import OSLOCollector
from ModelGenerator.OSLODatatypePrimitive import OSLODatatypePrimitive
from ModelGenerator.StringHelper import wrap_in_quotes


class OTLPrimitiveDatatypeCreator(AbstractDatatypeCreator):
    def __init__(self, logger: AbstractLogger, osloCollector: OSLOCollector):
        super().__init__(logger, osloCollector)
        self.logger.log("Created an instance of OTLPrimitiveDatatypeCreator", LogType.INFO)

    def CreateBlockToWriteFromPrimitiveTypes(self, osloDatatypePrimitive: OSLODatatypePrimitive):
        if not isinstance(osloDatatypePrimitive, OSLODatatypePrimitive):
            raise ValueError(f"Input is not a OSLODatatypePrimitive")
        if osloDatatypePrimitive.objectUri == '' or not (osloDatatypePrimitive.objectUri.startswith('http://www.w3.org/200') or
                                                         osloDatatypePrimitive.objectUri.startswith(
                                                             'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte')
                                                         or osloDatatypePrimitive.objectUri.startswith(
                    'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd')):
            raise ValueError(f"OSLODatatypePrimitive.objectUri is invalid. Value = '{osloDatatypePrimitive.objectUri}'")
        if osloDatatypePrimitive.name == '':
            raise ValueError(f"OSLODatatypePrimitive.name is invalid. Value = '{osloDatatypePrimitive.name}'")

        if osloDatatypePrimitive.objectUri.startswith(
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KwantWrd'):
            return self.CreateBlockToWriteFromComplexPrimitiveOrUnionTypes(osloDatatypePrimitive, typeField='KwantWrd')
        if osloDatatypePrimitive.objectUri.startswith('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#Dte'):
            return self.CreateBlockToWriteFromComplexPrimitiveOrUnionTypes(osloDatatypePrimitive, typeField='Primitive')
