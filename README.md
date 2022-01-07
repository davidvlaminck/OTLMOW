# OTLClassPython Project 
This project aims to implement the Flemish data standard OTL (https://wegenenverkeer.data.vlaanderen.be/) in Python.
Below is sample code that should be self-explanatory. It demonstrates the basic possibilities of this project.

## Creating the OTL datamodel using the OTL SQLite
With every OTL update, this piece of code will create an updated Python datamodel. This is not backwards compatible.
```  
from Facility.OTLFacility import OTLFacility
from Loggers.TxtLogger import TxtLogger

# create the main facade class: OTLFacility
logger = TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt')
otl_facility = OTLFacility(logger)

# create a datamodel based on the OTL SQLite database and ttl files stored on the github
otl_file_location = 'InputFiles/OTL.db'
otl_facility.init_otl_model_creator(otl_file_location)
otl_facility.create_otl_datamodel()
```
## Using the OTL Datamodel instances to create objects and encode them in JSON
The datamodel generates classes, allowing the properties to be filled with data.
Use the property 'waarde' to change the value of a property to allow data validation.
```  
from Facility.OTLFacility import OTLFacility
from Loggers.TxtLogger import TxtLogger
from OTLModel.Classes.DNBLaagspanning import DNBLaagspanning

# create the main facade class: OTLFacility
logger = TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt')
otl_facility = OTLFacility(logger)

# instantiate an OTL class and fill it with data
dnb = DNBLaagspanning()
dnb.naam.waarde = 'A0024'
# dnb.naam.waarde = 24  # this raises a ValueError because it has an incorrect value
dnb.toestand.set_value_by_label('in gebruik')
dnb.assetId.identificator.waarde = 'eigen_Id_voor_A0024'
dnb.eanNummer.waarde = '541448860003995215'
dnb.adresVolgensDNB.gemeente.set_value_by_label('brasschaat')
# dnb.adresVolgensDNB.gemeente.set_value_by_label('Brasschaat')  # this raises a ValueError because it has an incorrect value
dnb.adresVolgensDNB.postcode.waarde = '2930'
dnb.adresVolgensDNB.straatnaam.waarde = 'Bredabaan 90'
dnb.geometry = 'POINT Z(157696.6 219065.5 0)'

meter = EnergiemeterDNB()
meter.naam = '50004784'
meter.assetId.identificator.waarde = 'eigen_Id_voor_50004784'
meter.aantalTelwerken.waarde = 1

voedingsrelatie = Voedt()
voedingsrelatie.assetId.identificator.waarde = "A0024-50004784"
voedingsrelatie.bronAssetId.identificator.waarde = 'eigen_Id_voor_A0024'
voedingsrelatie.doelAssetId.identificator.waarde = 'eigen_Id_voor_50004784'

lijst_otl_objecten = [dnb, meter, voedingsrelatie]

# encode to a json representation
encoded_json = otl_facility.encoder.encode(lijst_otl_objecten)
print(encoded_json)

# write the json file
path = f'{datetime.now().strftime("%Y%m%d%H%M%S")}_export.json'
otl_facility.encoder.write_json_to_file(encoded_json, path)
```
output:
```
[
    {
        "adresVolgensDNB": {
            "gemeente": "brasschaat",
            "postcode": "2930",
            "straatnaam": "Bredabaan 90"
        },
        "assetId": {
            "identificator": "eigen_Id_voor_A0024"
        },
        "eanNummer": "541448860003995215",
        "geometry": "POINT Z(157696.6 219065.5 0)",
        "naam": "A0024",
        "toestand": "in-gebruik",
        "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBLaagspanning"
    },
    {
        "aantalTelwerken": 1,
        "assetId": {
            "identificator": "eigen_Id_voor_50004784"
        },
        "naam": "50004784",
        "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#EnergiemeterDNB"
    },
    {
        "assetId": {
            "identificator": "A0024-50004784"
        },
        "bronAssetId": {
            "identificator": "eigen_Id_voor_A0024"
        },
        "doelAssetId": {
            "identificator": "eigen_Id_voor_50004784"
        },
        "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Voedt"
    }
]
```

