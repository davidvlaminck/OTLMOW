from datetime import datetime

from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.OTLModel.Classes.Onderdeel.Stroomkring import Stroomkring


def main():
    otl_facility = OTLFacility(logfile=fr'C:\temp\pythonLogging\{datetime.now().strftime("%Y%m%d%H%M%S")}_pythonlog.txt',
                               settings_path=r'C:\resources\settings_OTLMOW.json')

    kring = otl_facility.asset_factory.dynamic_create_instance_from_ns_and_name('onderdeel', 'Stroomkring')
    if not isinstance(kring, Stroomkring):
        return
    kring.naam = 'kring'
    kring.toestand = 'in-gebruik'
    kring.isActief = True

    print(kring)
    print(kring.info())
    print(kring.info_attr('toestand'))
    print(kring.info_attr_type('toestand'))


if __name__ == '__main__':
    main()

