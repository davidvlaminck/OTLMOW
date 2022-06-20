import os

from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OTLModel.Classes.Abstracten.Behuizing import Behuizing

if __name__ == '__main__':
    otl_facility = OTLFacility(logfile=r'C:\temp\pythonLogging\pythonlog.txt',
                               settings_path="C:\\resources\\settings_OTLMOW.json")

    abstract_class_type = Behuizing

    for root, dirs, files in os.walk("../OTLModel/Classes"):
        for file in files:
            if file.endswith(".py") and not file[0] == '_':
                try:
                    instance = otl_facility.asset_factory.dynamic_create_instance_from_ns_and_name(file[:-3])
                    if isinstance(instance, abstract_class_type):
                        print(instance.typeURI)
                except:
                    # catch for abstract classes that can't be instantianted
                    pass
