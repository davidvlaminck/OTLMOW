# OTLClassPython Project 
demo code
```  
from Facility.OTLFacility import OTLFacility
from Loggers.TxtLogger import TxtLogger
from OTLModel.Classes.DNBLaagspanning import DNBLaagspanning

# create the main facade class: OTLFacility
logger = TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt')
otl_facility = OTLFacility(logger)

# create a datamodel based on the OTL SQLite database and ttl files stored on the github
otl_file_location = 'InputFiles/OTL.db'
otl_facility.init_otl_model_creator(otl_file_location)
otl_facility.create_otl_datamodel()

# use the generated datamodel to create instances of OTL classes
dnb = DNBLaagspanning()
dnb.naam.waarde = 'A0024'
dnb.toestand.set_value_by_label('in gebruik')
dnb.assetId.identificator.waarde = 'eigen_Id_voor_A0024'
dnb.eanNummer.waarde = '541448860003995215'
dnb.adresVolgensDNB.gemeente.set_value_by_label('brasschaat')
# dnb.adresVolgensDNB.gemeente.set_value_by_label('Brasschaat') # this raises a ValueError because it has an incorrect value
dnb.adresVolgensDNB.postcode.waarde = '2930'
dnb.adresVolgensDNB.straatnaam.waarde = 'Bredabaan 90'

# encode to a json representation
encoded_json = otl_facility.encoder.encode(dnb)
print(encoded_json)
```
output:
```
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
    "toestand": "in-gebruik"
}
```

