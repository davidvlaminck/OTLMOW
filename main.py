from datetime import datetime

from Facility.OTLFacility import OTLFacility
from Loggers.ConsoleLogger import ConsoleLogger
from Loggers.LoggerCollection import LoggerCollection
from Loggers.TxtLogger import TxtLogger
from ModelGenerator.BaseClasses.RelatieRichting import RelatieRichting
from OTLModel.Classes.DNBLaagspanning import DNBLaagspanning
from OTLModel.Classes.EnergiemeterDNB import EnergiemeterDNB
from OTLModel.Classes.Voedt import Voedt

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    jsonPath = "C:\\resources\\DA-2022-00006_export_slagbomen.json"

    slagbomen = otl_facility.davieImporter.import_file(jsonPath)

    otl_facility.visualiser.show(slagbomen)
