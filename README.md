# OTLClassPython Project 
This project aims to implement the Flemish data standard OTL (https://wegenenverkeer.data.vlaanderen.be/) in Python.
Below is sample code that should be self-explanatory. It demonstrates the basic possibilities of this project.

## Installation and requirements
To install the OTL MOW project into your python project, use pip to install it
``` 
pip install OTLMOW
``` 
OTLMOW has dependencies on rdflib, pyvis and shapely. 
``` 
pip install rdflib
pip install pyvis
pip install shapely
``` 
If you're using Windows, use the following commands instead to install shapely
``` 
pip install pipwin
pipwin install shapely
``` 

## Creating the OTL datamodel using the OTL SQLite
With every OTL update, this piece of code will allow the creation of an updated Python datamodel. The generated classes are not backwards compatible.
```  
from src.OTLMOW.Facility.OTLFacility import OTLFacility
from src.OTLMOW.Loggers.TxtLogger import TxtLogger

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
Use the property 'waarde' to change the value of a property and to allow data validation.
```  
from src.OTLMOW.Facility.OTLFacility import OTLFacility
from src.OTLMOW.Loggers.TxtLogger import TxtLogger
from src.OTLMOW.OTLModel.Classes.DNBLaagspanning import DNBLaagspanning
from src.OTLMOW.OTLModel.Classes.EnergiemeterDNB import EnergiemeterDNB
from src.OTLMOW.OTLModel.Classes.Voedt import Voedt

# create the main facade class: OTLFacility
logger = TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt')
otl_facility = OTLFacility(logger)

# use the generated datamodel to create instances of OTL classes
dnb = DNBLaagspanning()
dnb.naam = 'A0024'
dnb.toestand = 'in-gebruik'
# dnb.toestand = 'foute toestand'  # raises ValueError because the value is not valid
dnb.assetId.identificator = 'eigen_Id_voor_A0024'
dnb.eanNummer = '541448860003995215'
dnb.adresVolgensDNB.gemeente = 'brasschaat'
dnb.adresVolgensDNB.postcode = '2930'
dnb.adresVolgensDNB.straatnaam = 'Bredabaan 90'

meter = EnergiemeterDNB()
meter.naam = '50004784'
meter.assetId.identificator = 'eigen_Id_voor_50004784'
meter.aantalTelwerken = 1
meter.geometry = 'POINT Z(157696.6 219065.5 0)'

voedingsrelatie = Voedt()
voedingsrelatie.assetId.identificator = "A0024-50004784"
voedingsrelatie.bronAssetId.identificator = 'eigen_Id_voor_A0024'
voedingsrelatie.doelAssetId.identificator = 'eigen_Id_voor_50004784'

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
        "naam": "A0024",
        "toestand": "in-gebruik",
        "typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBLaagspanning"
    },
    {
        "aantalTelwerken": 1,
        "assetId": {
            "identificator": "eigen_Id_voor_50004784"
        },
        "geometry": "POINT Z(157696.6 219065.5 0)",
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

