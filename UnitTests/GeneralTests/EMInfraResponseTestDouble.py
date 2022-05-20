class ResponseTestDouble():
    single_response = """{
  "@graph": [
{
  "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring",
  "@id": "https://data.awvvlaanderen.be/id/asset/000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n",
  "loc:Locatie.geometrie": "POINT Z(101489.3 190526.6 0)",
  "loc:Locatie.omschrijving": "",
  "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
  "loc:Locatie.puntlocatie": {
    "loc:DtcPuntlocatie.precisie": "",
    "loc:DtcPuntlocatie.weglocatie": {
      "loc:DtcWeglocatie.straatnaam": "",
      "loc:DtcWeglocatie.ident8": "A0100002",
      "loc:DtcWeglocatie.gemeente": "Gent",
      "loc:DtcWeglocatie.referentiepaalOpschrift": 47.4,
      "loc:DtcWeglocatie.ident2": "A10",
      "loc:DtcWeglocatie.referentiepaalAfstand": -9
    },
    "loc:DtcPuntlocatie.bron": "",
    "loc:3Dpunt.puntgeometrie": {
      "loc:DtcCoord.lambert72": {
        "loc:DtcCoordLambert72.ycoordinaat": 190526.6,
        "loc:DtcCoordLambert72.xcoordinaat": 101489.3,
        "loc:DtcCoordLambert72.zcoordinaat": 0
      }
    },
    "loc:DtcPuntlocatie.adres": {
      "loc:DtcAdres.straat": "Luchthavenlaan",
      "loc:DtcAdres.bus": "",
      "loc:DtcAdres.gemeente": "Gent",
      "loc:DtcAdres.postcode": "9051",
      "loc:DtcAdres.nummer": "35",
      "loc:DtcAdres.provincie": "Oost-Vlaanderen"
    }
  },
  "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring",
  "AIMDBStatus.isActief": true,
  "AIMNaamObject.naam": "A10N47.4.K_stroomkring",
  "AIMObject.notitie": "",
  "AIMObject.assetId": {
    "DtcIdentificator.identificator": "000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n",
    "DtcIdentificator.toegekendDoor": "AWV"
  },
  "geo:Geometrie.log": [
    {
      "geo:DtcLog.overerving": [
        {
          "geo:DtcOvererving.erflaatId": {
            "DtcIdentificator.identificator": "b59f3b37-fe77-4677-9e7c-e5491319e759-b25kZXJkZWVsI0xhYWdzcGFubmluZ3Nib3Jk",
            "DtcIdentificator.toegekendDoor": "AWV"
          },
          "geo:DtcOvererving.erfgenaamId": {
            "DtcIdentificator.identificator": "000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n",
            "DtcIdentificator.toegekendDoor": "AWV"
          },
          "geo:DtcOvererving.relatieId": {
            "DtcIdentificator.identificator": "b80e2ca4-123c-46ac-b747-4b6e8075bf78-b25kZXJkZWVsI0JldmVzdGlnaW5n",
            "DtcIdentificator.toegekendDoor": "AWV"
          }
        }
      ],
      "geo:DtcLog.gaVersie": "GA_2.2.0",
      "geo:DtcLog.geometrie": {
        "geo:DtuGeometrie.punt": "POINT Z(101489.3 190526.6 0)"
      },
      "geo:DtcLog.bron": "https://geo.data.wegenenverkeer.be/id/concept/KlLogBron/overerving",
      "geo:DtcLog.nauwkeurigheid": "",
      "geo:DtcLog.niveau": "https://geo.data.wegenenverkeer.be/id/concept/KlLogNiveau/-1"
    }
  ]
}]}"""

    response = """{
  "@graph": [
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer",
      "@id": "https://data.awvvlaanderen.be/id/asset/0005bafb-838f-47e0-a4e2-20dd120ede6b-b25kZXJkZWVsI09tdm9ybWVy",
      "AIMObject.notitie": "",
      "Omvormer.type": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlOmvormerType/Encoder",
      "AIMDBStatus.isActief": true,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "Omvormer.ipAdres": "10.216.10.33",
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Omvormer",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0005bafb-838f-47e0-a4e2-20dd120ede6b-b25kZXJkZWVsI09tdm9ybWVy"
      },
      "AIMNaamObject.naam": "ENCA0469"
    },    
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
      "@id": "https://data.awvvlaanderen.be/id/asset/000a35d5-c4a5-4a36-8620-62c99e053ba0-b25kZXJkZWVsI05ldHdlcmtwb29ydA",
      "AIMObject.notitie": "",
      "Netwerkpoort.nNILANCapaciteit": 155,
      "AIMDBStatus.isActief": true,
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
      "Netwerkpoort.technologie": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/SDH",
      "loc:Locatie.puntlocatie": "",
      "AIMNaamObject.naam": "Poort_2625",
      "Netwerkpoort.merk": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/NOKIA",
      "loc:Locatie.geometrie": "",
      "loc:Locatie.omschrijving": "",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000a35d5-c4a5-4a36-8620-62c99e053ba0-b25kZXJkZWVsI05ldHdlcmtwb29ydA"
      },
      "Netwerkpoort.golflengte": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortGolflengte/NULL",
      "Netwerkpoort.config": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/STM-1",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp"
    },    
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
      "@id": "https://data.awvvlaanderen.be/id/asset/000be0f8-b9a1-408b-b9a3-919c8cfed383-b25kZXJkZWVsI05ldHdlcmtwb29ydA",
      "AIMObject.notitie": "",
      "loc:Locatie.omschrijving": "",
      "Netwerkpoort.nNILANCapaciteit": 155,
      "AIMObject.assetId": {
        "DtcIdentificator.identificator": "000be0f8-b9a1-408b-b9a3-919c8cfed383-b25kZXJkZWVsI05ldHdlcmtwb29ydA",
        "DtcIdentificator.toegekendDoor": "AWV"
      },
      "Netwerkpoort.golflengte": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortGolflengte/C1310",
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
      "Netwerkpoort.technologie": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/SDH",
      "AIMNaamObject.naam": "Poort_2488",
      "Netwerkpoort.merk": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/NOKIA",
      "loc:Locatie.geometrie": "",
      "AIMDBStatus.isActief": true,
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 67997.6,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.ycoordinaat": 206750.1
          }
        },
        "loc:DtcPuntlocatie.bron": "",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "293",
          "loc:DtcAdres.gemeente": "Brugge",
          "loc:DtcAdres.straat": "Koning Albert I-laan",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.postcode": "8200",
          "loc:DtcAdres.provincie": "West-Vlaanderen"
        },
        "loc:DtcPuntlocatie.weglocatie": ""
      },
      "Netwerkpoort.config": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/STM-1",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#Mpt",
      "@id": "https://data.awvvlaanderen.be/id/asset/000c4eee-bc07-45b5-8c58-686faf912c86-bGdjOmluc3RhbGxhdGllI01wdA",
      "AIMObject.notitie": "",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "hellinko",
        "tz:DtcToezichter.voornaam": "Koen",
        "tz:DtcToezichter.naam": "Hellinckx",
        "tz:DtcToezichter.email": "koen.hellinckx@mow.vlaanderen.be"
      },
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#Mpt",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalOpschrift": 62.8,
          "loc:DtcWeglocatie.referentiepaalAfstand": 44,
          "loc:DtcWeglocatie.gemeente": "Beersel",
          "loc:DtcWeglocatie.ident2": "R0",
          "loc:DtcWeglocatie.straatnaam": "R0000001",
          "loc:DtcWeglocatie.ident8": "R0000001"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.postcode": "1651",
          "loc:DtcAdres.gemeente": "Beersel",
          "loc:DtcAdres.provincie": "Vlaams-Brabant",
          "loc:DtcAdres.straat": "Klarissenbos",
          "loc:DtcAdres.nummer": "37",
          "loc:DtcAdres.bus": ""
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 144406.4,
            "loc:DtcCoordLambert72.ycoordinaat": 161173.7,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        }
      },
      "lgc:Mpt.meetpost": 113901,
      "AIMDBStatus.isActief": true,
      "lgc:Mpt.rijstrook": "3",
      "lgc:Mpt.gekoppeld": false,
      "loc:Locatie.geometrie": "",
      "loc:Locatie.omschrijving": "R0 - COMPLEX BEERSEL - MIV139",
      "lgc:Mpt.formaat": "Standaard",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "District Vilvoorde-autosnelwegen",
        "tz:DtcBeheerder.referentie": "212"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_VHS",
        "tz:DtcToezichtGroep.naam": "EMT_VHS"
      },
      "NaampadObject.naampad": "R0X62.5/R0P62.5.K/MIV139/1722",
      "AIMNaamObject.naam": "1722",
      "AIMObject.assetId": {
        "DtcIdentificator.identificator": "000c4eee-bc07-45b5-8c58-686faf912c86-bGdjOmluc3RhbGxhdGllI01wdA",
        "DtcIdentificator.toegekendDoor": "AWV"
      }
    },
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera",
      "@id": "https://data.awvvlaanderen.be/id/asset/000c960e-b694-4f96-bf56-51872325c714-b25kZXJkZWVsI0NhbWVyYQ",
      "loc:Locatie.omschrijving": "",
      "loc:Locatie.geometrie": "POINT Z (151063.4 209792.6 0)",
      "AIMDBStatus.isActief": true,
      "Camera.heeftAid": false,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMObject.notitie": "voorzorgsmaatregel: AID 6",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000c960e-b694-4f96-bf56-51872325c714-b25kZXJkZWVsI0NhbWVyYQ"
      },
      "AIMNaamObject.naam": "CAMA0006",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalAfstand": -21,
          "loc:DtcWeglocatie.ident2": "R1",
          "loc:DtcWeglocatie.gemeente": "Antwerpen",
          "loc:DtcWeglocatie.ident8": "R0011122",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 0.9,
          "loc:DtcWeglocatie.straatnaam": "R0011121"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 151063.4,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.ycoordinaat": 209792.6
          }
        },
        "loc:DtcPuntlocatie.precisie": "",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.provincie": "Antwerpen",
          "loc:DtcAdres.gemeente": "Antwerpen",
          "loc:DtcAdres.straat": "Generaal Armstrongweg",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.postcode": "2020",
          "loc:DtcAdres.nummer": "1"
        },
        "loc:DtcPuntlocatie.bron": ""
      },
      "Camera.isPtz": false,
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Camera",
      "Camera.heeftSpitsstrook": false
    },
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
      "@id": "https://data.awvvlaanderen.be/id/asset/000cbd26-eef7-421f-9b81-a88f5210f44a-b25kZXJkZWVsI05ldHdlcmtwb29ydA",
      "loc:Locatie.omschrijving": "",
      "Netwerkpoort.config": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/10GE",
      "Netwerkpoort.golflengte": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortGolflengte/C1310",
      "AIMDBStatus.isActief": true,
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000cbd26-eef7-421f-9b81-a88f5210f44a-b25kZXJkZWVsI05ldHdlcmtwb29ydA"
      },
      "loc:Locatie.puntlocatie": {
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 213332.2,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.xcoordinaat": 153214.4
          }
        },
        "loc:DtcPuntlocatie.precisie": "",
        "loc:DtcPuntlocatie.bron": "",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.straat": "Ellermanstraat",
          "loc:DtcAdres.postcode": "2060",
          "loc:DtcAdres.provincie": "Antwerpen",
          "loc:DtcAdres.gemeente": "Antwerpen",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.nummer": "14"
        },
        "loc:DtcPuntlocatie.weglocatie": ""
      },
      "Netwerkpoort.nNILANCapaciteit": 10000,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp",
      "Netwerkpoort.merk": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Ciena",
      "Netwerkpoort.technologie": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/CEN",
      "loc:Locatie.geometrie": "",
      "AIMObject.notitie": "",
      "AIMNaamObject.naam": "Poort_2289"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#Bus",
      "@id": "https://data.awvvlaanderen.be/id/asset/000d0d0e-f1b2-4cdd-87ef-7bf193fbf665-bGdjOmluc3RhbGxhdGllI0J1cw",
      "AIMObject.notitie": "",
      "NaampadObject.naampad": "WW0256/BUS",
      "loc:Locatie.omschrijving": "N368 (Sint-Andreaslaan) met N370 (Stationstraat) WS256",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#Bus",
      "AIMNaamObject.naam": "BUS",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "District Brugge",
        "tz:DtcBeheerder.referentie": "311"
      },
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.email": "david.seynaeve@mow.vlaanderen.be",
        "tz:DtcToezichter.naam": "Seynaeve",
        "tz:DtcToezichter.gebruikersnaam": "seynaeda",
        "tz:DtcToezichter.voornaam": "David"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_WV",
        "tz:DtcToezichtGroep.naam": "AWV_EW_WV"
      },
      "AIMDBStatus.isActief": true,
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 202882.1,
            "loc:DtcCoordLambert72.xcoordinaat": 77402.3,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.straat": "Sint-Andreaslaan",
          "loc:DtcAdres.postcode": "8730",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "West-Vlaanderen",
          "loc:DtcAdres.nummer": "2",
          "loc:DtcAdres.gemeente": "Beernem"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident2": "N368",
          "loc:DtcWeglocatie.gemeente": "Beernem",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 6.4,
          "loc:DtcWeglocatie.straatnaam": "Sint-Andreaslaan",
          "loc:DtcWeglocatie.referentiepaalAfstand": -14,
          "loc:DtcWeglocatie.ident8": "N3680002"
        }
      },
      "loc:Locatie.geometrie": "",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000d0d0e-f1b2-4cdd-87ef-7bf193fbf665-bGdjOmluc3RhbGxhdGllI0J1cw"
      }
    },
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
      "@id": "https://data.awvvlaanderen.be/id/asset/000d0d69-e1fc-40e3-9f45-99ac8e6aa341-b25kZXJkZWVsI05ldHdlcmtwb29ydA",
      "AIMObject.notitie": "",
      "AIMNaamObject.naam": "VMSA17-AS1.Fa1.2",
      "AIMDBStatus.isActief": true,
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000d0d69-e1fc-40e3-9f45-99ac8e6aa341-b25kZXJkZWVsI05ldHdlcmtwb29ydA"
      },
      "Netwerkpoort.type": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortType/UNI"
    },
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring",
      "@id": "https://data.awvvlaanderen.be/id/asset/000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n",
      "AIMObject.notitie": "",
      "AIMNaamObject.naam": "A10N47.4.K_stroomkring",
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Stroomkring",
      "AIMDBStatus.isActief": true,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000d3091-deca-4714-8f82-d95aace9ea90-b25kZXJkZWVsI1N0cm9vbWtyaW5n"
      }
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/000d450f-157a-42b6-acb2-a303a3226110-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "loc:Locatie.omschrijving": "",
      "lgc:VPLMast.datumLichtmastVernieuwd": "1900-01-01",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.vsaSperfilter": false,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "lgc:EMObject.vsaType": "elektromagnetisch",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.email": "robin.lux@mow.vlaanderen.be",
        "tz:DtcToezichter.gebruikersnaam": "luxro",
        "tz:DtcToezichter.voornaam": "Robin",
        "tz:DtcToezichter.naam": "Lux"
      },
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.lichtmastType": "RM - Rechte metalen paal",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000d450f-157a-42b6-acb2-a303a3226110-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ond:EMObject.aantalLampenVervangen": 0,
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "lgc:VPLMast.datumLichtmastGeschilderd": "1900-01-01",
      "lgc:VPLMast.aantalArmen": "0 - geen armen",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 300,
      "lgc:EMObject.verlichtingstype": "opafrit",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_LB",
        "tz:DtcToezichtGroep.naam": "AWV_EW_LB"
      },
      "lgc:VPLMast.paalhoogte": "12,00",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.postcode": "3560",
          "loc:DtcAdres.gemeente": "Lummen",
          "loc:DtcAdres.straat": "Dellestraat",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Limburg",
          "loc:DtcAdres.nummer": "44"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 211035.5,
            "loc:DtcCoordLambert72.ycoordinaat": 186097.8,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "A0131621",
          "loc:DtcWeglocatie.gemeente": "Lummen",
          "loc:DtcWeglocatie.ident2": "A13",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 0,
          "loc:DtcWeglocatie.straatnaam": "A0131621",
          "loc:DtcWeglocatie.referentiepaalAfstand": 79
        }
      },
      "ond:EMObject.aantalVsaVervangen": 0,
      "lgc:EMObject.lampType": "NaHP-T-250",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "720",
        "tz:DtcBeheerder.naam": "District Centraal - Limburg"
      },
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Schreder Syntra",
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "NaampadObject.naampad": "G0574/G0574.WV/414",
      "lgc:EMObject.ledVerlichting": false,
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ond:EMObject.aantalStartersVervangen": 0,
      "AIMNaamObject.naam": "414",
      "lgc:EMObject.armatuurkleur": "7038",
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "lgc:VPLMast.armlengte": [
        "niet van toepassing - Indien lichtmast type niet gelijk is aan 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ],
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/000d64ff-3b36-4f7b-9138-5e904c5fe21d-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Schreder Z2",
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.lampType": "MHHP-T-250",
      "lgc:VPLMast.paalhoogte": "10,00",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMNaamObject.naam": "043",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_AN",
        "tz:DtcToezichtGroep.naam": "AWV_EW_AN"
      },
      "lgc:EMObject.aantalVerlichtingstoestellen": 2,
      "NaampadObject.naampad": "A3299/A3299.WV/043",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "N0499012",
          "loc:DtcWeglocatie.referentiepaalAfstand": -34,
          "loc:DtcWeglocatie.straatnaam": "Charles de Costerlaan",
          "loc:DtcWeglocatie.gemeente": "Antwerpen",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 2.1,
          "loc:DtcWeglocatie.ident2": "N49"
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 150897.6,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.ycoordinaat": 213045.7
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.provincie": "Antwerpen",
          "loc:DtcAdres.gemeente": "Antwerpen",
          "loc:DtcAdres.postcode": "2050",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.straat": "Julius Vuylstekelaan",
          "loc:DtcAdres.nummer": "16"
        }
      },
      "lgc:VPLMast.lichtmastType": "RM - Rechte metalen paal",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Van Alboom",
        "tz:DtcToezichter.gebruikersnaam": "vanalbma",
        "tz:DtcToezichter.email": "matthias.vanalboom@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Matthias"
      },
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "T-stuk",
      "lgc:EMObject.geschilderd": true,
      "lgc:VPLMast.aantalArmen": "0 - geen armen",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 300,
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "121",
        "tz:DtcBeheerder.naam": "District Antwerpen"
      },
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "loc:Locatie.omschrijving": "N49A - CH. DE COSTERLAAN - WAASLANDTUNNEL LO - VOORPLEIN",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000d64ff-3b36-4f7b-9138-5e904c5fe21d-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.armlengte": [
        "niet van toepassing - Indien lichtmast type niet gelijk is aan 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ]
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#LS",
      "@id": "https://data.awvvlaanderen.be/id/asset/000d72f2-9ca0-4ebe-83c5-1999bbfdecb3-bGdjOmluc3RhbGxhdGllI0xT",
      "AIMObject.notitie": "",
      "loc:Locatie.omschrijving": "",
      "ins:EMObject.datumLaatsteKeuring": "2020-10-09",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Els",
        "tz:DtcToezichter.email": "els.geysen@mow.vlaanderen.be",
        "tz:DtcToezichter.naam": "Geysen",
        "tz:DtcToezichter.gebruikersnaam": "geysenel"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_WV",
        "tz:DtcToezichtGroep.naam": "AWV_EW_WV"
      },
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#LS",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "ins:EMObject.resultaatKeuring": "niet-conform met inbreuken",
      "AIMNaamObject.naam": "LS",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.gemeente": "Oostkamp",
          "loc:DtcAdres.postcode": "8020",
          "loc:DtcAdres.straat": "Sijslostraat",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.nummer": "123",
          "loc:DtcAdres.provincie": "West-Vlaanderen"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident2": "N368",
          "loc:DtcWeglocatie.referentiepaalAfstand": 52,
          "loc:DtcWeglocatie.referentiepaalOpschrift": 18.1,
          "loc:DtcWeglocatie.gemeente": "Oostkamp",
          "loc:DtcWeglocatie.straatnaam": "Sijslostraat",
          "loc:DtcWeglocatie.ident8": "N3680002"
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 199677.5,
            "loc:DtcCoordLambert72.xcoordinaat": 67514.8,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        }
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "District Brugge",
        "tz:DtcBeheerder.referentie": "311"
      },
      "loc:Locatie.geometrie": "",
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.installatieverantwConformArt266Arei": "geysenel",
      "NaampadObject.naampad": "WW0873/KAST/LS",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000d72f2-9ca0-4ebe-83c5-1999bbfdecb3-bGdjOmluc3RhbGxhdGllI0xT"
      }
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#RLCPaal",
      "@id": "https://data.awvvlaanderen.be/id/asset/000e1b42-2aec-4641-90b9-21ac05a930cf-bGdjOmluc3RhbGxhdGllI1JMQ1BhYWw",
      "AIMObject.notitie": "",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000e1b42-2aec-4641-90b9-21ac05a930cf-bGdjOmluc3RhbGxhdGllI1JMQ1BhYWw"
      },
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#RLCPaal",
      "NaampadObject.naampad": "N80X1.3/496G9/7",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "loc:Locatie.omschrijving": "R71-N80",
      "loc:Locatie.puntlocatie": {
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 217324.9,
            "loc:DtcCoordLambert72.ycoordinaat": 178926.8,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.straatnaam": "Sint-Truidersteenweg",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 1.4,
          "loc:DtcWeglocatie.gemeente": "Hasselt",
          "loc:DtcWeglocatie.referentiepaalAfstand": -36,
          "loc:DtcWeglocatie.ident2": "N80",
          "loc:DtcWeglocatie.ident8": "N0800002"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "1",
          "loc:DtcAdres.postcode": "3500",
          "loc:DtcAdres.straat": "Helstraat",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.gemeente": "Hasselt",
          "loc:DtcAdres.provincie": "Limburg"
        }
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "720",
        "tz:DtcBeheerder.naam": "District Centraal - Limburg"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_VHS",
        "tz:DtcToezichtGroep.naam": "EMT_VHS"
      },
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.email": "joris.vandenbosch@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Joris",
        "tz:DtcToezichter.gebruikersnaam": "vdboscjo",
        "tz:DtcToezichter.naam": "Vandenbosch"
      },
      "loc:Locatie.geometrie": "",
      "AIMDBStatus.isActief": true,
      "AIMNaamObject.naam": "7"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/000e5aa3-a971-4105-88e1-a5aec0dc88bf-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "loc:Locatie.omschrijving": "",
      "ins:EMObject.interneRoestvorming": "OK",
      "lgc:EMObject.overhangLed": "niet gekend",
      "lgc:VPLMast.lichtmastType": "M - Metalen paal met arm",
      "lgc:EMObject.verlichtingsniveauLed": "niet gekend",
      "lgc:EMObject.vsaType": "elektronisch",
      "lgc:EMObject.vsaSperfilter": false,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_LB",
        "tz:DtcToezichtGroep.naam": "AWV_EW_LB"
      },
      "lgc:VPLMast.ralKleurVplmast": "7038",
      "AIMObject.notitie": "",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "lgc:EMObject.geschilderd": true,
      "ins:EMObject.directGevaar": false,
      "lgc:VPLMast.paalhoogte": "12,50 - niet voor type lichtmast 'K' en 'KS'",
      "lgc:EMObject.contractnummerLeveringLed": "MDN58",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.merkEnTypeLed": "Schreder Ampera",
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 63,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "vanottjo",
        "tz:DtcToezichter.naam": "Van Otterdijk",
        "tz:DtcToezichter.email": "jos.vanotterdijk@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Jos"
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "719",
        "tz:DtcBeheerder.naam": "District Zuid - Limburg"
      },
      "NaampadObject.naampad": "G1597/G1597.WV/249",
      "AIMDBStatus.isActief": true,
      "lgc:VPLMast.armlengte": [
        "2 - Enkel voor lichtmast types 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ],
      "ins:VPLMast.toestandPaal": "OK",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "lgc:VPLMast.aantalArmen": "1 - alleen mogelijk voor lichtmast 'M', 'MS', 'B', 'BS', 'K' of 'KS'",
      "ond:EMObject.aantalLampenVervangen": 1,
      "lgc:EMObject.inclinatiehoekLed": 5,
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "lgc:EMObject.datumInstallatieLed": "2021-05-10",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000e5aa3-a971-4105-88e1-a5aec0dc88bf-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ond:EMObject.aantalVsaVervangen": 0,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "lgc:VPLMast.leverancier": "PetitJean",
      "AIMNaamObject.naam": "249",
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "ins:EMObject.externeRoestvorming": "OK",
      "lgc:VPLMast.nummerVoedingskring": "2",
      "ins:VPLMast.toestandBouten": "OK",
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "lgc:EMObject.aantalTeVerlichtenRijvakkenLed": "niet gekend",
      "ins:EMObject.toestandVerlichtingstoestellen": "OK",
      "ins:VPLMast.toestandFunderingVplmast": "OK",
      "ond:EMObject.aantalStartersVervangen": 0,
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.gemeente": "Borgloon",
          "loc:DtcWeglocatie.referentiepaalAfstand": -1,
          "loc:DtcWeglocatie.straatnaam": "Tongersesteenweg",
          "loc:DtcWeglocatie.ident2": "N79",
          "loc:DtcWeglocatie.ident8": "N0790002",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 13.6
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 220983,
            "loc:DtcCoordLambert72.ycoordinaat": 165197.4,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.postcode": "3840",
          "loc:DtcAdres.straat": "Tongersesteenweg",
          "loc:DtcAdres.nummer": "301",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.gemeente": "Borgloon",
          "loc:DtcAdres.provincie": "Limburg"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter"
      },
      "ins:VPLMast.toestandDeurtje": "OK",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Schreder Ampera",
      "lgc:EMObject.kleurtemperatuurLed": "K3000",
      "lgc:EMObject.ledVerlichting": true,
      "lgc:EMObject.armatuurkleur": "7038",
      "ins:EMObject.nummerLeesbaar": "Ja",
      "ond:VPLMast.deurtjeVervangen": false,
      "lgc:EMObject.lampType": "LED",
      "lgc:VPLMast.optiekLed": "5136",
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "lgc:EMObject.brandurenLed": 60000,
      "lgc:EMObject.lumenPakketLed": 7500
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#GebouwLegacy",
      "@id": "https://data.awvvlaanderen.be/id/asset/000e89f6-d580-4492-8f03-25548957703c-bGdjOmluc3RhbGxhdGllI0dlYm91d0xlZ2FjeQ",
      "AIMObject.notitie": "",
      "loc:Locatie.omschrijving": "A11 TUNNELS",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalAfstand": -19,
          "loc:DtcWeglocatie.referentiepaalOpschrift": 145.9,
          "loc:DtcWeglocatie.ident8": "A0110001",
          "loc:DtcWeglocatie.straatnaam": "A0110001",
          "loc:DtcWeglocatie.ident2": "A11",
          "loc:DtcWeglocatie.gemeente": "Knokke-Heist"
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.gemeente": "Knokke-Heist",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.nummer": "41",
          "loc:DtcAdres.provincie": "West-Vlaanderen",
          "loc:DtcAdres.postcode": "8300",
          "loc:DtcAdres.straat": "Dudzelestraat"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 75141.6,
            "loc:DtcCoordLambert72.ycoordinaat": 222304,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        }
      },
      "AIMNaamObject.naam": "MIN.1",
      "AIMDBStatus.isActief": true,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#GebouwLegacy",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "viaeneya",
        "tz:DtcToezichter.email": "yarno.viaene@mow.vlaanderen.be",
        "tz:DtcToezichter.naam": "Viaene",
        "tz:DtcToezichter.voornaam": "Yarno"
      },
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "TOV",
        "tz:DtcToezichtGroep.naam": "Tunnel Organ. VL."
      },
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000e89f6-d580-4492-8f03-25548957703c-bGdjOmluc3RhbGxhdGllI0dlYm91d0xlZ2FjeQ"
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "THV_BRUGGE",
        "tz:DtcBeheerder.naam": "THV Via Brugge"
      },
      "loc:Locatie.geometrie": "",
      "NaampadObject.naampad": "A11.PPS/A11.TUNNEL/K052.ZUID/MIN.1"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#RSSGroep",
      "@id": "https://data.awvvlaanderen.be/id/asset/000f8d16-8ed9-4294-a6f2-3c3cedf9b0f3-bGdjOmluc3RhbGxhdGllI1JTU0dyb2Vw",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#RSSGroep",
      "NaampadObject.naampad": "A11X65.7/A11N65.7.S/Z62",
      "AIMDBStatus.isActief": true,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000f8d16-8ed9-4294-a6f2-3c3cedf9b0f3-bGdjOmluc3RhbGxhdGllI1JTU0dyb2Vw"
      },
      "AIMNaamObject.naam": "Z62",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "BAM NV",
        "tz:DtcBeheerder.referentie": "BAM"
      },
      "AIMObject.notitie": "",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-opbouw",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Smet",
        "tz:DtcToezichter.email": "kristof.smet@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Kristof",
        "tz:DtcToezichter.gebruikersnaam": "smetkr"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.naam": "LANTIS",
        "tz:DtcToezichtGroep.referentie": "LANTIS"
      }
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/000fea80-886b-40b9-b1d9-7ef28a3e9e98-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.lichtmastType": "M - Metalen paal met arm",
      "lgc:EMObject.lumenPakketLed": 0,
      "lgc:EMObject.inclinatiehoekLed": 0,
      "lgc:EMObject.aantalDriversPerToestel": 0,
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "000fea80-886b-40b9-b1d9-7ef28a3e9e98-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "ond:EMObject.aantalStartersVervangen": 0,
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.nummerVoedingskring": "A",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:VPLMast.paalhoogte": "12,50 - niet voor type lichtmast 'K' en 'KS'",
      "ond:EMObject.aantalLampenVervangen": 0,
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "District Aalst",
        "tz:DtcBeheerder.referentie": "415"
      },
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "AIMDBStatus.isActief": true,
      "lgc:VPLMast.armlengte": [
        "2 - Enkel voor lichtmast types 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ],
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.naam": "AWV_EW_OV",
        "tz:DtcToezichtGroep.referentie": "AWV_EW_OV"
      },
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:EMObject.lampType": "NaLP131",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "lgc:VPLMast.aantalArmen": "1 - alleen mogelijk voor lichtmast 'M', 'MS', 'B', 'BS', 'K' of 'KS'",
      "ond:EMObject.aantalVsaVervangen": 0,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Jacob",
        "tz:DtcToezichter.gebruikersnaam": "daemja",
        "tz:DtcToezichter.email": "jacob.daem@mow.vlaanderen.be",
        "tz:DtcToezichter.naam": "Daem"
      },
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Schreder GSM",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 157,
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident2": "N8",
          "loc:DtcWeglocatie.straatnaam": "Brusselsesteenweg",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 19.9,
          "loc:DtcWeglocatie.ident8": "N0080001",
          "loc:DtcWeglocatie.gemeente": "Ninove",
          "loc:DtcWeglocatie.referentiepaalAfstand": -36
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 128143.5,
            "loc:DtcCoordLambert72.ycoordinaat": 168894.6,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.postcode": "9402",
          "loc:DtcAdres.gemeente": "Ninove",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.nummer": "504",
          "loc:DtcAdres.provincie": "Oost-Vlaanderen",
          "loc:DtcAdres.straat": "Brusselsesteenweg"
        }
      },
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "lgc:EMObject.vsaType": "elektromagnetisch",
      "lgc:EMObject.brandurenLed": 0,
      "AIMNaamObject.naam": "A51",
      "loc:Locatie.omschrijving": "N28 - N8 (Brusselseteenweg thv 248)",
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "NaampadObject.naampad": "WO2075/WO2075.WV/A51",
      "lgc:EMObject.ledVerlichting": false,
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "lgc:EMObject.lichtpunthoogteTovRijweg": 0,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/001006b3-6a29-4191-bc87-514016404f4e-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Bulens",
        "tz:DtcToezichter.gebruikersnaam": "bulenswi",
        "tz:DtcToezichter.email": "wim.bulens@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Wim"
      },
      "lgc:EMObject.lampType": "NaHP-T-150",
      "AIMNaamObject.naam": "009",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 177364.1,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.xcoordinaat": 153455.3
          }
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "2",
          "loc:DtcAdres.gemeente": "Machelen",
          "loc:DtcAdres.straat": "Generaal Lemanlaan",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.postcode": "1830",
          "loc:DtcAdres.provincie": "Vlaams-Brabant"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "N0019042",
          "loc:DtcWeglocatie.ident2": "N1",
          "loc:DtcWeglocatie.straatnaam": "Emmanuellaan",
          "loc:DtcWeglocatie.referentiepaalAfstand": 2,
          "loc:DtcWeglocatie.referentiepaalOpschrift": 0.3,
          "loc:DtcWeglocatie.gemeente": "Machelen"
        }
      },
      "lgc:VPLMast.armlengte": [
        "1,5"
      ],
      "loc:Locatie.omschrijving": "",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "001006b3-6a29-4191-bc87-514016404f4e-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "AIMDBStatus.isActief": true,
      "NaampadObject.naampad": "C2544/C2544.WV/009",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "District Vilvoorde-autosnelwegen",
        "tz:DtcBeheerder.referentie": "212"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_VB",
        "tz:DtcToezichtGroep.naam": "AWV_EW_VB"
      },
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "loc:Locatie.geometrie": "",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 180
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00102476-9342-4c7d-9e27-350fc2fbc6f7-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.vsaSperfilter": false,
      "NaampadObject.naampad": "WW0115/WW0115.WV/D07",
      "lgc:EMObject.vsaType": "elektromagnetisch",
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "ond:EMObject.aantalStartersVervangen": 0,
      "lgc:EMObject.lampType": "LED",
      "lgc:VPLMast.ralKleurVplmast": "7038",
      "AIMObject.notitie": "",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.lichtmastType": "RM - Rechte metalen paal",
      "AIMNaamObject.naam": "D07",
      "lgc:VPLMast.leverancier": "niet gekend",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalOpschrift": 0.1,
          "loc:DtcWeglocatie.referentiepaalAfstand": -34,
          "loc:DtcWeglocatie.gemeente": "Kortrijk",
          "loc:DtcWeglocatie.ident2": "R8",
          "loc:DtcWeglocatie.ident8": "R0080111",
          "loc:DtcWeglocatie.straatnaam": "R0080111"
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 69247.1,
            "loc:DtcCoordLambert72.ycoordinaat": 168608,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.postcode": "8501",
          "loc:DtcAdres.nummer": "4",
          "loc:DtcAdres.gemeente": "Kortrijk",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.straat": "Tuinwijklaan",
          "loc:DtcAdres.provincie": "West-Vlaanderen"
        }
      },
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "lgc:EMObject.geschilderd": true,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Geert",
        "tz:DtcToezichter.email": "geert.deglas@mow.vlaanderen.be",
        "tz:DtcToezichter.gebruikersnaam": "deglasge",
        "tz:DtcToezichter.naam": "Deglas"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_WV",
        "tz:DtcToezichtGroep.naam": "AWV_EW_WV"
      },
      "lgc:EMObject.merkEnTypeLed": "Philips Luma",
      "ins:EMObject.directGevaar": false,
      "lgc:EMObject.contractnummerLeveringLed": "MDN58",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "ond:EMObject.aantalLampenVervangen": 0,
      "loc:Locatie.omschrijving": "weg: R008; ident8: R0080111; kilometerpunt: 0,000; zijde weg: Rechts",
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "lgc:VPLMast.nummerVoedingskring": "D",
      "lgc:VPLMast.aantalArmen": "1",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Schreder Corus",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "lgc:EMObject.lichtpunthoogteTovRijweg": 5,
      "lgc:EMObject.datumInstallatieLed": "2018-04-30",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "312",
        "tz:DtcBeheerder.naam": "District Kortrijk"
      },
      "lgc:VPLMast.armlengte": [
        "0,5 - voor ledtoestellen op middenberm"
      ],
      "ond:EMObject.aantalVsaVervangen": 0,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "lgc:EMObject.kleurtemperatuurLed": "K4000",
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "lgc:EMObject.lumenPakketLed": 5000,
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "lgc:VPLMast.paalhoogte": "5,00 - niet voor type lichtmast 'K' en 'KS'",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "lgc:EMObject.aantalDriversPerToestel": 1,
      "lgc:EMObject.inclinatiehoekLed": -10,
      "lgc:EMObject.ledVerlichting": true,
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00102476-9342-4c7d-9e27-350fc2fbc6f7-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      }
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00107c4a-dc4f-46bf-af13-77d116b481c9-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00107c4a-dc4f-46bf-af13-77d116b481c9-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "vanottjo",
        "tz:DtcToezichter.naam": "Van Otterdijk",
        "tz:DtcToezichter.email": "jos.vanotterdijk@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Jos"
      },
      "AIMDBStatus.isActief": true,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_LB",
        "tz:DtcToezichtGroep.naam": "AWV_EW_LB"
      },
      "lgc:EMObject.inclinatiehoekLed": 5,
      "lgc:EMObject.kleurtemperatuurLed": "K4000",
      "lgc:VPLMast.armlengte": [
        "niet van toepassing"
      ],
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Schreder Ampera",
      "lgc:EMObject.ledVerlichting": true,
      "lgc:EMObject.armatuurkleur": "7038",
      "lgc:EMObject.lampType": "LED",
      "NaampadObject.naampad": "G3692/G3692.WV/216",
      "loc:Locatie.omschrijving": "",
      "AIMNaamObject.naam": "216",
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.lichtmastType": "RM - Rechte metalen paal",
      "lgc:EMObject.contractnummerLeveringLed": "MDN58",
      "lgc:EMObject.geschilderd": false,
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 83,
      "lgc:VPLMast.paalhoogte": "8,00",
      "lgc:EMObject.merkEnTypeLed": "Schreder Ampera",
      "lgc:EMObject.vsaType": "elektronisch",
      "lgc:EMObject.datumInstallatieLed": "2019-06-05",
      "ins:EMObject.nummerLeesbaar": "ja",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "717",
        "tz:DtcBeheerder.naam": "District West - Limburg"
      },
      "lgc:EMObject.lumenPakketLed": 10000,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "17",
          "loc:DtcAdres.postcode": "3560",
          "loc:DtcAdres.gemeente": "Lummen",
          "loc:DtcAdres.straat": "Thiewinkelstraat",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Limburg"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 209201.3,
            "loc:DtcCoordLambert72.ycoordinaat": 185641.6,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident2": "N725",
          "loc:DtcWeglocatie.ident8": "N7250001",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 4.5,
          "loc:DtcWeglocatie.gemeente": "Lummen",
          "loc:DtcWeglocatie.referentiepaalAfstand": -31,
          "loc:DtcWeglocatie.straatnaam": "Thiewinkelstraat"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel"
      },
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "lgc:VPLMast.nummerVoedingskring": "2",
      "lgc:VPLMast.optiekLed": "5137",
      "loc:Locatie.geometrie": "",
      "lgc:EMObject.brandurenLed": 60000
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#PTZ",
      "@id": "https://data.awvvlaanderen.be/id/asset/00109bfd-08ac-4a6b-b8b6-a0e5ef7c1215-bGdjOmluc3RhbGxhdGllI1BUWg",
      "loc:Locatie.omschrijving": "",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00109bfd-08ac-4a6b-b8b6-a0e5ef7c1215-bGdjOmluc3RhbGxhdGllI1BUWg"
      },
      "AIMNaamObject.naam": "CAMA0449",
      "AIMDBStatus.isActief": true,
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.gemeente": "Wommelgem",
          "loc:DtcAdres.provincie": "Antwerpen",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.postcode": "2160",
          "loc:DtcAdres.straat": "Oude Baan",
          "loc:DtcAdres.nummer": "75"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 211273.1,
            "loc:DtcCoordLambert72.xcoordinaat": 158693.3,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident2": "A13",
          "loc:DtcWeglocatie.referentiepaalAfstand": -40,
          "loc:DtcWeglocatie.ident8": "A0130001",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 3.6,
          "loc:DtcWeglocatie.gemeente": "Wommelgem",
          "loc:DtcWeglocatie.straatnaam": "A0130001"
        }
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "121",
        "tz:DtcBeheerder.naam": "District Antwerpen"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_VHS",
        "tz:DtcToezichtGroep.naam": "EMT_VHS"
      },
      "NaampadObject.naampad": "A2287/A2287.WV/240/A13P034/CAMA0449",
      "loc:Locatie.geometrie": "",
      "AIMObject.notitie": "",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-opbouw",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#PTZ",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Tom",
        "tz:DtcToezichter.naam": "Verboven",
        "tz:DtcToezichter.gebruikersnaam": "verbovto",
        "tz:DtcToezichter.email": "tom.verboven@mow.vlaanderen.be"
      }
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#LS",
      "@id": "https://data.awvvlaanderen.be/id/asset/00114756-9f8b-4c8c-b905-93da6c0b26cd-bGdjOmluc3RhbGxhdGllI0xT",
      "AIMObject.notitie": "",
      "loc:Locatie.omschrijving": "",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "AWV-WV",
        "tz:DtcBeheerder.naam": "AFDELING WEGEN WEST-VLAANDEREN"
      },
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#LS",
      "AIMDBStatus.isActief": true,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "loc:Locatie.puntlocatie": {
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 55310.7,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.ycoordinaat": 171814.4
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.straat": "Beselarestraat",
          "loc:DtcAdres.gemeente": "Zonnebeke",
          "loc:DtcAdres.postcode": "8980",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.nummer": "320",
          "loc:DtcAdres.provincie": "West-Vlaanderen"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalAfstand": 43,
          "loc:DtcWeglocatie.referentiepaalOpschrift": 8.3,
          "loc:DtcWeglocatie.gemeente": "Zonnebeke",
          "loc:DtcWeglocatie.straatnaam": "Beselarestraat",
          "loc:DtcWeglocatie.ident8": "N3030001",
          "loc:DtcWeglocatie.ident2": "N303"
        }
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_VHS",
        "tz:DtcToezichtGroep.naam": "EMT_VHS"
      },
      "NaampadObject.naampad": "N303X8.1/WZ1221/LS-C",
      "AIMNaamObject.naam": "LS-C",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "vdkerklu",
        "tz:DtcToezichter.naam": "Vande Kerkhove",
        "tz:DtcToezichter.email": "luc.vandekerkhove@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Luc"
      },
      "loc:Locatie.geometrie": "",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00114756-9f8b-4c8c-b905-93da6c0b26cd-bGdjOmluc3RhbGxhdGllI0xT"
      }
    },
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBLaagspanning",
      "@id": "https://data.awvvlaanderen.be/id/asset/001164ee-ae3d-4dd9-89b5-3e13ee97adb6-b25kZXJkZWVsI0ROQkxhYWdzcGFubmluZw",
      "AIMObject.notitie": "",
      "loc:Locatie.omschrijving": "",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "001164ee-ae3d-4dd9-89b5-3e13ee97adb6-b25kZXJkZWVsI0ROQkxhYWdzcGFubmluZw"
      },
      "DNB.adresVolgensDNB": {
        "DtcAdres.straatnaam": "Westkerkestraat n368kmpt32",
        "DtcAdres.gemeente": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAlgGemeente/ichtegem",
        "DtcAdres.postcode": "8480"
      },
      "AIMDBStatus.isActief": true,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMNaamObject.naam": "KW0176",
      "DNB.eanNummer": "541448860001876882",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.gemeente": "Brugge",
          "loc:DtcAdres.postcode": "8380",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "West-Vlaanderen",
          "loc:DtcAdres.straat": "Rederskaai",
          "loc:DtcAdres.nummer": "50"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 225739.2,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.xcoordinaat": 69084.5
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.weglocatie": ""
      },
      "AIMObject.datumOprichtingObject": "2016-09-01",
      "DNB.referentieDNB": "- WVL/TI/onbekend -",
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#DNBLaagspanning"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#AB",
      "@id": "https://data.awvvlaanderen.be/id/asset/001183f1-52b1-4c83-9678-77ffab31adec-bGdjOmluc3RhbGxhdGllI0FC",
      "AIMObject.notitie": "",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Johan",
        "tz:DtcToezichter.gebruikersnaam": "vanhecjo",
        "tz:DtcToezichter.email": "Johan.VanHecke@vlaamsewaterweg.be",
        "tz:DtcToezichter.naam": "Van Hecke"
      },
      "AIMNaamObject.naam": "AB",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "001183f1-52b1-4c83-9678-77ffab31adec-bGdjOmluc3RhbGxhdGllI0FC"
      },
      "AIMDBStatus.isActief": false,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#AB",
      "NaampadObject.naampad": "OM0220/AB",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_BMI",
        "tz:DtcToezichtGroep.naam": "EMT_BMI"
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "VLAAMSE MILIEUMAATSCHAPPIJ",
        "tz:DtcBeheerder.referentie": "VMMO"
      },
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#SeinSch",
      "@id": "https://data.awvvlaanderen.be/id/asset/0011c5ad-086b-4eb9-b8b3-52cc25a7d261-bGdjOmluc3RhbGxhdGllI1NlaW5TY2g",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "WATERWEGEN EN ZEEKANAAL NV",
        "tz:DtcBeheerder.referentie": "W&Z_ABS_D1"
      },
      "NaampadObject.naampad": "KO0021/SEIN.SCH/OPW.LO2",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_WHG",
        "tz:DtcToezichtGroep.naam": "EMT_WHG"
      },
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMNaamObject.naam": "OPW.LO2",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Aäron",
        "tz:DtcToezichter.naam": "Meirlaen",
        "tz:DtcToezichter.email": "aaron.meirlaen@vlaamsewaterweg.be",
        "tz:DtcToezichter.gebruikersnaam": "meirlaaa"
      },
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "1",
          "loc:DtcAdres.straat": "Sluisweg",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.gemeente": "Merelbeke",
          "loc:DtcAdres.provincie": "Oost-Vlaanderen",
          "loc:DtcAdres.postcode": "9820"
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalOpschrift": 30.3,
          "loc:DtcWeglocatie.ident8": "R0040001",
          "loc:DtcWeglocatie.straatnaam": "R0040001",
          "loc:DtcWeglocatie.ident2": "R4",
          "loc:DtcWeglocatie.gemeente": "Merelbeke",
          "loc:DtcWeglocatie.referentiepaalAfstand": 27
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 188941.7,
            "loc:DtcCoordLambert72.xcoordinaat": 106453.1,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter"
      },
      "AIMObject.notitie": "Waarborg liep tot 24/05/2020",
      "loc:Locatie.omschrijving": "SLUIS OW006",
      "AIMDBStatus.isActief": true,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0011c5ad-086b-4eb9-b8b3-52cc25a7d261-bGdjOmluc3RhbGxhdGllI1NlaW5TY2g"
      },
      "loc:Locatie.geometrie": "",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#SeinSch"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/0011d522-9281-4c20-ac87-7fbfa3177f10-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "lgc:VPLMast.lichtmastType": "RM - Rechte metalen paal",
      "NaampadObject.naampad": "A1641/A1641.WV/227",
      "lgc:VPLMast.aantalArmen": "0 - geen armen",
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.lampType": "NaLP131",
      "lgc:VPLMast.paalhoogte": "16,00 - niet voor type lichtmast 'K' en 'KS'",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "AIMNaamObject.naam": "227",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "BAM NV",
        "tz:DtcBeheerder.referentie": "BAM"
      },
      "lgc:EMObject.aantalVerlichtingstoestellen": 2,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Smet",
        "tz:DtcToezichter.email": "kristof.smet@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Kristof",
        "tz:DtcToezichter.gebruikersnaam": "smetkr"
      },
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "T-stuk",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.naam": "LANTIS",
        "tz:DtcToezichtGroep.referentie": "LANTIS"
      },
      "lgc:EMObject.geschilderd": true,
      "loc:Locatie.omschrijving": "AANSLUITINGSWISSELAAR N49 (A11) - R1 CHARLES DE COSTERLAAN - DWARSLAAN - KMP 0 tot 1 - CABINE LS",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.gemeente": "Zwijndrecht",
          "loc:DtcWeglocatie.ident8": "A0110001",
          "loc:DtcWeglocatie.straatnaam": "A0110001",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 65.4,
          "loc:DtcWeglocatie.referentiepaalAfstand": 37,
          "loc:DtcWeglocatie.ident2": "A11"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 147602,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.ycoordinaat": 213131.7
          }
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "12C",
          "loc:DtcAdres.straat": "Neerstraat",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.gemeente": "Zwijndrecht",
          "loc:DtcAdres.postcode": "2070",
          "loc:DtcAdres.provincie": "Antwerpen"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter"
      },
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 157,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/overgedragen",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Rombalux",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0011d522-9281-4c20-ac87-7fbfa3177f10-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "lgc:EMObject.verlichtingstype": "hoofdbaan",
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.armlengte": [
        "niet van toepassing - Indien lichtmast type niet gelijk is aan 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ]
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00120ca1-cfdb-4a82-af59-1cf7df1a8fd0-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "ins:EMObject.interneRoestvorming": "OK",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00120ca1-cfdb-4a82-af59-1cf7df1a8fd0-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "NaampadObject.naampad": "WO0590/WO0590.WV/590B12",
      "lgc:EMObject.contractnummerLeveringLed": "niet gekend",
      "lgc:EMObject.vsaType": "elektromagnetisch",
      "ins:VPLMast.toestandBouten": "OK",
      "ond:EMObject.andereOnderhoudsacties": "15m kabel",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet gekend",
      "lgc:EMObject.overhangLed": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "ins:EMObject.opmerkingToestandVerlichtingstoestel": "Vernieuwd",
      "loc:Locatie.puntlocatie": {
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 89580.6,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.ycoordinaat": 184193.9
          }
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "N0430002",
          "loc:DtcWeglocatie.ident2": "N43",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 18.6,
          "loc:DtcWeglocatie.gemeente": "Deinze",
          "loc:DtcWeglocatie.straatnaam": "Kortrijksesteenweg",
          "loc:DtcWeglocatie.referentiepaalAfstand": -35
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.provincie": "Oost-Vlaanderen",
          "loc:DtcAdres.nummer": "41",
          "loc:DtcAdres.gemeente": "Deinze",
          "loc:DtcAdres.straat": "Torenstraat",
          "loc:DtcAdres.postcode": "9800",
          "loc:DtcAdres.bus": ""
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel"
      },
      "lgc:VPLMast.lichtmastType": "B - Betonnen paal",
      "lgc:EMObject.verlichtingsniveauLed": "niet gekend",
      "lgc:EMObject.kleurtemperatuurLed": "niet gekend",
      "AIMNaamObject.naam": "590B12",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:VPLMast.paalhoogte": "12,50 - niet voor type lichtmast 'K' en 'KS'",
      "lgc:VPLMast.nummerVoedingskring": "Kring B",
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "AIMDBStatus.isActief": true,
      "lgc:VPLMast.armlengte": [
        "2 - Enkel voor lichtmast types 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ],
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.naam": "AWV_EW_OV",
        "tz:DtcToezichtGroep.referentie": "AWV_EW_OV"
      },
      "ins:VPLMast.toestandPaal": "OK",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Taildeman",
        "tz:DtcToezichter.email": "alain.taildeman@mow.vlaanderen.be",
        "tz:DtcToezichter.gebruikersnaam": "taildeal",
        "tz:DtcToezichter.voornaam": "Alain"
      },
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:EMObject.lampType": "NaLP131",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "lgc:VPLMast.aantalArmen": "1 - alleen mogelijk voor lichtmast 'M', 'MS', 'B', 'BS', 'K' of 'KS'",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "413",
        "tz:DtcBeheerder.naam": "District Eeklo"
      },
      "ond:EMObject.aantalLampenVervangen": 1,
      "lgc:EMObject.opmerkingInventarisVerlichtingstoestel": "Vernieuwd",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ond:EMObject.aantalVsaVervangen": 0,
      "lgc:EMObject.verlichtingstoestelMerkEnType": "niet gekend",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 157,
      "loc:Locatie.omschrijving": "weg: ; ident8: N0430002; kilometerpunt: ; zijde weg:",
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "ins:EMObject.externeRoestvorming": "OK",
      "lgc:EMObject.aantalTeVerlichtenRijvakkenLed": "niet gekend",
      "lgc:EMObject.ledVerlichting": false,
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ins:EMObject.toestandVerlichtingstoestellen": "OK",
      "ins:VPLMast.toestandFunderingVplmast": "OK",
      "ond:EMObject.aantalStartersVervangen": 0,
      "ins:VPLMast.toestandDeurtje": "OK",
      "ins:EMObject.nummerLeesbaar": "Ja",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00122e61-d9fb-40ac-be43-4c79d35e7019-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "loc:Locatie.omschrijving": "",
      "lgc:EMObject.contractnummerLeveringLed": "MDN58",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "vanottjo",
        "tz:DtcToezichter.naam": "Van Otterdijk",
        "tz:DtcToezichter.email": "jos.vanotterdijk@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Jos"
      },
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.inclinatiehoekLed": 5,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "loc:Locatie.puntlocatie": {
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 235740.5,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.ycoordinaat": 188272.1
          }
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.straat": "Maastrichterstraat",
          "loc:DtcAdres.gemeente": "As",
          "loc:DtcAdres.postcode": "3665",
          "loc:DtcAdres.provincie": "Limburg",
          "loc:DtcAdres.nummer": "59",
          "loc:DtcAdres.bus": ""
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "N0750001",
          "loc:DtcWeglocatie.referentiepaalAfstand": -11,
          "loc:DtcWeglocatie.straatnaam": "N0750001",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 19.1,
          "loc:DtcWeglocatie.ident2": "N75",
          "loc:DtcWeglocatie.gemeente": "As"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter"
      },
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Schreder Ampera",
      "lgc:VPLMast.ralKleurVplmast": "7038",
      "AIMObject.notitie": "",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "718",
        "tz:DtcBeheerder.naam": "District Oost - Limburg"
      },
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00122e61-d9fb-40ac-be43-4c79d35e7019-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.lichtmastType": "RM - Rechte metalen paal",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "lgc:EMObject.geschilderd": true,
      "lgc:EMObject.merkEnTypeLed": "Schreder Ampera",
      "lgc:EMObject.lumenPakketLed": 12500,
      "lgc:VPLMast.aantalArmen": "0 - geen armen",
      "lgc:EMObject.vsaType": "elektronisch",
      "NaampadObject.naampad": "G1006/G1006.WV/337",
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:EMObject.datumInstallatieLed": "2021-05-26",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_LB",
        "tz:DtcToezichtGroep.naam": "AWV_EW_LB"
      },
      "lgc:VPLMast.paalhoogte": "16,00 - niet voor type lichtmast 'K' en 'KS'",
      "lgc:VPLMast.nummerVoedingskring": "3",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "lgc:VPLMast.leverancier": "PetitJean",
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 110,
      "lgc:EMObject.kleurtemperatuurLed": "K3000",
      "lgc:EMObject.ledVerlichting": true,
      "lgc:EMObject.armatuurkleur": "7038",
      "AIMNaamObject.naam": "337",
      "lgc:EMObject.lampType": "LED",
      "lgc:VPLMast.optiekLed": "5136",
      "loc:Locatie.geometrie": "",
      "lgc:EMObject.brandurenLed": 60000,
      "lgc:VPLMast.armlengte": [
        "niet van toepassing - Indien lichtmast type niet gelijk is aan 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ]
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00124b81-f52a-4e46-be2d-8936b7972a36-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "loc:Locatie.omschrijving": "",
      "lgc:VPLMast.opmerkingInventarisPaal": "paal is verwijderd",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.lumenPakketLed": 0,
      "lgc:EMObject.inclinatiehoekLed": 0,
      "NaampadObject.naampad": "WO0307/WO0307.WV/B05.weg",
      "AIMDBStatus.isActief": false,
      "lgc:EMObject.aantalDriversPerToestel": 0,
      "lgc:EMObject.brandurenLed": 0,
      "lgc:EMObject.lichtpunthoogteTovRijweg": 0,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd",
      "AIMObject.notitie": "",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "andere",
      "ond:EMObject.aantalLampenVervangen": 0,
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "loc:Locatie.puntlocatie": "",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ond:EMObject.aantalVsaVervangen": 0,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00124b81-f52a-4e46-be2d-8936b7972a36-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ond:EMObject.aantalStartersVervangen": 0,
      "lgc:VPLMast.lichtmastBuitenGebruik": true,
      "AIMNaamObject.naam": "B05.weg",
      "loc:Locatie.geometrie": "",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 0
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#Z30Paal",
      "@id": "https://data.awvvlaanderen.be/id/asset/0012526f-3e61-458d-abd2-87173c5c6afa-bGdjOmluc3RhbGxhdGllI1ozMFBhYWw",
      "AIMObject.notitie": "",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0012526f-3e61-458d-abd2-87173c5c6afa-bGdjOmluc3RhbGxhdGllI1ozMFBhYWw"
      },
      "AIMDBStatus.isActief": false,
      "NaampadObject.naampad": "723G2/Z30/D",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "717",
        "tz:DtcBeheerder.naam": "District West - Limburg"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_VHS",
        "tz:DtcToezichtGroep.naam": "EMT_VHS"
      },
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.email": "joris.vandenbosch@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Joris",
        "tz:DtcToezichter.gebruikersnaam": "vdboscjo",
        "tz:DtcToezichter.naam": "Vandenbosch"
      },
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#Z30Paal",
      "AIMNaamObject.naam": "D"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#CamGroep",
      "@id": "https://data.awvvlaanderen.be/id/asset/00127162-1f3b-4d56-9167-208dc34c3589-bGdjOmluc3RhbGxhdGllI0NhbUdyb2Vw",
      "AIMObject.notitie": "",
      "NaampadObject.naampad": "A11.PPS/K101.TUNNEL/A11P143.45.P/P143.45.CAM",
      "loc:Locatie.omschrijving": "AS44 - U-bak (rijrichting Brugge - zijde Antwerpen) (A1)",
      "AIMDBStatus.isActief": true,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "viaeneya",
        "tz:DtcToezichter.email": "yarno.viaene@mow.vlaanderen.be",
        "tz:DtcToezichter.naam": "Viaene",
        "tz:DtcToezichter.voornaam": "Yarno"
      },
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#CamGroep",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "THV_BRUGGE",
        "tz:DtcBeheerder.naam": "THV Via Brugge"
      },
      "AIMNaamObject.naam": "P143.45.CAM",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00127162-1f3b-4d56-9167-208dc34c3589-bGdjOmluc3RhbGxhdGllI0NhbUdyb2Vw"
      },
      "loc:Locatie.geometrie": "",
      "loc:Locatie.puntlocatie": "",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "TOV",
        "tz:DtcToezichtGroep.naam": "Tunnel Organ. VL."
      }
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00127b82-d1f9-4cd8-ae94-9acf5482f3c1-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "lgc:VPLMast.aantalArmen": "niet gekend",
      "lgc:VPLMast.lichtmastType": "niet gekend",
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:VPLMast.paalhoogte": "niet gekend",
      "lgc:VPLMast.armlengte": [
        "niet gekend"
      ],
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_AN",
        "tz:DtcToezichtGroep.naam": "AWV_EW_AN"
      },
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ond:EMObject.aantalStartersVervangen": 0,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "loc:Locatie.omschrijving": "WEG: ; IDENT8: N0490001; KILOMETERPUNT: ; ZIJDE WEG:",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Van Alboom",
        "tz:DtcToezichter.gebruikersnaam": "vanalbma",
        "tz:DtcToezichter.email": "matthias.vanalboom@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Matthias"
      },
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:EMObject.vsaType": "niet gekend",
      "ond:EMObject.aantalLampenVervangen": 0,
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.postcode": "9120",
          "loc:DtcAdres.gemeente": "Beveren",
          "loc:DtcAdres.nummer": "80X",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Oost-Vlaanderen",
          "loc:DtcAdres.straat": "Melseledijk"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalOpschrift": 70.3,
          "loc:DtcWeglocatie.ident8": "A0110001",
          "loc:DtcWeglocatie.gemeente": "Beveren",
          "loc:DtcWeglocatie.referentiepaalAfstand": 26,
          "loc:DtcWeglocatie.straatnaam": "Expressweg - N49",
          "loc:DtcWeglocatie.ident2": "A11"
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 142973.1,
            "loc:DtcCoordLambert72.ycoordinaat": 214635.4,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        }
      },
      "AIMDBStatus.isActief": false,
      "AIMNaamObject.naam": "98301",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ond:EMObject.aantalVsaVervangen": 0,
      "NaampadObject.naampad": "WO0098/WV/98301",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "niet gekend",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "lgc:EMObject.lampType": "niet gekend",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "121",
        "tz:DtcBeheerder.naam": "District Antwerpen"
      },
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00127b82-d1f9-4cd8-ae94-9acf5482f3c1-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "lgc:EMObject.verlichtingstype": "niet gekend",
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/0012a0f2-d22e-4376-bbd2-3911ba59397e-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 300,
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "414",
        "tz:DtcBeheerder.naam": "District St-Niklaas"
      },
      "lgc:EMObject.contractnummerLeveringLed": "niet gekend",
      "AIMNaamObject.naam": "K16",
      "lgc:VPLMast.paalhoogte": "12,50",
      "NaampadObject.naampad": "WO0176/WO0176.WV/K16",
      "AIMObject.notitie": "",
      "ins:EMObject.interneRoestvorming": "OK",
      "lgc:VPLMast.aantalArmen": "niet gekend",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.lichtmastType": "RK - Kreukelpaal",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet gekend",
      "lgc:EMObject.overhangLed": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:EMObject.verlichtingsniveauLed": "niet gekend",
      "lgc:EMObject.kleurtemperatuurLed": "niet gekend",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:EMObject.vsaType": "niet gekend",
      "ins:VPLMast.toestandBouten": "niet van toepassing",
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "AIMDBStatus.isActief": true,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.naam": "AWV_EW_OV",
        "tz:DtcToezichtGroep.referentie": "AWV_EW_OV"
      },
      "ins:VPLMast.toestandPaal": "OK",
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:EMObject.lampType": "MHHP-T-250",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "ond:EMObject.aantalLampenVervangen": 1,
      "loc:Locatie.puntlocatie": "",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ond:EMObject.aantalVsaVervangen": 0,
      "loc:Locatie.omschrijving": "WEG: ; IDENT8: N0410002; KILOMETERPUNT: ; ZIJDE WEG: Z44-MDN60",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "niet gekend",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "ins:EMObject.externeRoestvorming": "OK",
      "lgc:EMObject.aantalTeVerlichtenRijvakkenLed": "niet gekend",
      "lgc:VPLMast.armlengte": [
        "niet van toepassing"
      ],
      "lgc:EMObject.ledVerlichting": false,
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ins:EMObject.toestandVerlichtingstoestellen": "OK",
      "ins:VPLMast.toestandFunderingVplmast": "OK",
      "ond:EMObject.aantalStartersVervangen": 0,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Kaya",
        "tz:DtcToezichter.voornaam": "Cenk",
        "tz:DtcToezichter.gebruikersnaam": "kayace",
        "tz:DtcToezichter.email": "cenkhan.kaya@mow.vlaanderen.be"
      },
      "ins:VPLMast.toestandDeurtje": "OK",
      "AIMObject.assetId": {
        "DtcIdentificator.identificator": "0012a0f2-d22e-4376-bbd2-3911ba59397e-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
        "DtcIdentificator.toegekendDoor": "AWV"
      },
      "ins:EMObject.nummerLeesbaar": "Ja",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false
    },
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software",
      "@id": "https://data.awvvlaanderen.be/id/asset/00138f22-dbef-45e3-8605-a28cd6d01c94-b25kZXJkZWVsI1NvZnR3YXJl",
      "AIMObject.notitie": "",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00138f22-dbef-45e3-8605-a28cd6d01c94-b25kZXJkZWVsI1NvZnR3YXJl"
      },
      "AIMDBStatus.isActief": true,
      "Software.versie": "3.6.15",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Software",
      "AIMObject.datumOprichtingObject": "2021-05-04",
      "Software.poortenconfiguratie": [
        {
          "DtcSoftwarePoortconfiguratie.poortnummer": 27017,
          "DtcSoftwarePoortconfiguratie.richting": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlPoortconfiguratieRichting/ingaand",
          "DtcSoftwarePoortconfiguratie.service": "TCP"
        }
      ],
      "AIMNaamObject.naam": "DIZV-MongoDB1"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#AB",
      "@id": "https://data.awvvlaanderen.be/id/asset/0013a2e1-3260-4b9a-b353-afbc6267fc82-bGdjOmluc3RhbGxhdGllI0FC",
      "loc:Locatie.puntlocatie": {
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 155329.5,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.ycoordinaat": 197139.5
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.straatnaam": "A0011211",
          "loc:DtcWeglocatie.gemeente": "Rumst",
          "loc:DtcWeglocatie.ident2": "A1",
          "loc:DtcWeglocatie.referentiepaalAfstand": 380,
          "loc:DtcWeglocatie.referentiepaalOpschrift": 0,
          "loc:DtcWeglocatie.ident8": "A0011211"
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "1",
          "loc:DtcAdres.provincie": "Antwerpen",
          "loc:DtcAdres.postcode": "2840",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.gemeente": "Rumst",
          "loc:DtcAdres.straat": "Bussestraat"
        }
      },
      "loc:Locatie.omschrijving": "E19 - COMPLEX - KMPNT 22,3 TOT 23,25 -  + VOETGANGERSTUNNEL   CABINE HS",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Duchateau",
        "tz:DtcToezichter.email": "lieven.duchateau@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Lieven",
        "tz:DtcToezichter.gebruikersnaam": "duchatli"
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "112",
        "tz:DtcBeheerder.naam": "District Puurs"
      },
      "AIMDBStatus.isActief": false,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0013a2e1-3260-4b9a-b353-afbc6267fc82-bGdjOmluc3RhbGxhdGllI0FC"
      },
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#AB",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd",
      "loc:Locatie.geometrie": "",
      "AIMObject.notitie": "",
      "AIMNaamObject.naam": "TCWVA17",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_BMI",
        "tz:DtcToezichtGroep.naam": "EMT_BMI"
      },
      "NaampadObject.naampad": "A0092/TCWVA17"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/0013e6ce-d93c-4a9a-bd1c-4b4ec6e42f9b-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.lichtmastType": "M - Metalen paal met arm",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "lgc:EMObject.lumenPakketLed": 0,
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:EMObject.aantalDriversPerToestel": 0,
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "loc:Locatie.omschrijving": "N255",
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "ond:EMObject.aantalStartersVervangen": 0,
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "AIMObject.notitie": "",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Philips Iridium",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "ond:EMObject.aantalLampenVervangen": 0,
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "District Aalst",
        "tz:DtcBeheerder.referentie": "415"
      },
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "AIMNaamObject.naam": "E21",
      "lgc:EMObject.inclinatiehoekLed": 0,
      "lgc:EMObject.lampType": "NaHP-T-150",
      "AIMDBStatus.isActief": true,
      "lgc:VPLMast.armlengte": [
        "2 - Enkel voor lichtmast types 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ],
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.naam": "AWV_EW_OV",
        "tz:DtcToezichtGroep.referentie": "AWV_EW_OV"
      },
      "lgc:VPLMast.paalhoogte": "10,00",
      "NaampadObject.naampad": "WO0327/WO0327.WV/E21",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "lgc:VPLMast.aantalArmen": "1 - alleen mogelijk voor lichtmast 'M', 'MS', 'B', 'BS', 'K' of 'KS'",
      "ond:EMObject.aantalVsaVervangen": 0,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0013e6ce-d93c-4a9a-bd1c-4b4ec6e42f9b-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Jacob",
        "tz:DtcToezichter.gebruikersnaam": "daemja",
        "tz:DtcToezichter.email": "jacob.daem@mow.vlaanderen.be",
        "tz:DtcToezichter.naam": "Daem"
      },
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "lgc:EMObject.vsaType": "elektromagnetisch",
      "lgc:EMObject.brandurenLed": 0,
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "ond:EMObject.vermoedenSokkelAsbesthoudend": false,
      "lgc:VPLMast.nummerVoedingskring": "E",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "lgc:EMObject.ledVerlichting": false,
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "N2550001",
          "loc:DtcWeglocatie.ident2": "N255",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 12.7,
          "loc:DtcWeglocatie.referentiepaalAfstand": 49,
          "loc:DtcWeglocatie.straatnaam": "Edingsesteenweg",
          "loc:DtcWeglocatie.gemeente": "Ninove"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.ycoordinaat": 166135,
            "loc:DtcCoordLambert72.xcoordinaat": 125653.2
          }
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.straat": "Edingsesteenweg",
          "loc:DtcAdres.gemeente": "Ninove",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Oost-Vlaanderen",
          "loc:DtcAdres.postcode": "9400",
          "loc:DtcAdres.nummer": "278"
        }
      },
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "lgc:EMObject.lichtpunthoogteTovRijweg": 0,
      "loc:Locatie.geometrie": "",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 180,
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link",
      "@id": "https://data.awvvlaanderen.be/id/asset/0013f300-a54a-4dfa-9633-b6ab75ef4bc1-aW5zdGFsbGF0aWUjTGluaw",
      "AIMNaamObject.naam": "Link_1350",
      "AIMDBStatus.isActief": false,
      "Link.geleidingsgroepTnummer": 0,
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/installatie#Link",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0013f300-a54a-4dfa-9633-b6ab75ef4bc1-aW5zdGFsbGF0aWUjTGluaw"
      },
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp",
      "AIMObject.notitie": "",
      "NaampadObject.naampad": "OTN.LINK/Link_1350"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/0014335a-b2a0-4c4c-b6f3-f19073ca81e3-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "NaampadObject.naampad": "C1678/C1678.WV/026",
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:VPLMast.armlengte": [
        "niet gekend"
      ],
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ond:EMObject.aantalStartersVervangen": 0,
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "loc:Locatie.omschrijving": "weg: N275; ident8: N2750001; kilometerpunt: 9999,000; zijde weg: Rechts",
      "lgc:VPLMast.aantalArmen": "niet gekend",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 155384.2,
            "loc:DtcCoordLambert72.ycoordinaat": 161809,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.gemeente": "Hoeilaart",
          "loc:DtcAdres.postcode": "1560",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.straat": "Groenendaalsesteenweg",
          "loc:DtcAdres.nummer": "149",
          "loc:DtcAdres.provincie": "Vlaams-Brabant"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.straatnaam": "Terhulpsesteenweg",
          "loc:DtcWeglocatie.ident8": "N2750001",
          "loc:DtcWeglocatie.gemeente": "Hoeilaart",
          "loc:DtcWeglocatie.referentiepaalAfstand": 11,
          "loc:DtcWeglocatie.ident2": "N275",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 4.3
        }
      },
      "lgc:VPLMast.lichtmastType": "niet gekend",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:EMObject.vsaType": "niet gekend",
      "ond:EMObject.aantalLampenVervangen": 0,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Bulens",
        "tz:DtcToezichter.gebruikersnaam": "bulenswi",
        "tz:DtcToezichter.email": "wim.bulens@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Wim"
      },
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0014335a-b2a0-4c4c-b6f3-f19073ca81e3-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "lgc:VPLMast.paalhoogte": "niet gekend",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "District Vilvoorde-autosnelwegen",
        "tz:DtcBeheerder.referentie": "212"
      },
      "AIMNaamObject.naam": "026",
      "ond:EMObject.aantalVsaVervangen": 0,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_VB",
        "tz:DtcToezichtGroep.naam": "AWV_EW_VB"
      },
      "lgc:EMObject.verlichtingstoestelMerkEnType": "niet gekend",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "lgc:EMObject.lampType": "niet gekend",
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "lgc:EMObject.verlichtingstype": "niet gekend",
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#LS",
      "@id": "https://data.awvvlaanderen.be/id/asset/00143e33-a365-4792-b5fb-1e4fc94c5ac4-bGdjOmluc3RhbGxhdGllI0xT",
      "AIMObject.notitie": "",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "213",
        "tz:DtcBeheerder.naam": "District Leuven"
      },
      "loc:Locatie.omschrijving": "A2 COMPLEX MET N2 - KMP 83.1 - CABINE LS - kmp 81.368 tot kmp 83.15",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#LS",
      "AIMDBStatus.isActief": true,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Tom",
        "tz:DtcToezichter.email": "tom.witters@mow.vlaanderen.be",
        "tz:DtcToezichter.naam": "Witters",
        "tz:DtcToezichter.gebruikersnaam": "witterto"
      },
      "AIMNaamObject.naam": "LS",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_VB",
        "tz:DtcToezichtGroep.naam": "AWV_EW_VB"
      },
      "NaampadObject.naampad": "C1383/KAST/LS",
      "ins:EMObject.datumLaatsteKeuring": "2020-10-27",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00143e33-a365-4792-b5fb-1e4fc94c5ac4-bGdjOmluc3RhbGxhdGllI0xT"
      },
      "loc:Locatie.geometrie": "",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "4",
          "loc:DtcAdres.gemeente": "Herent",
          "loc:DtcAdres.postcode": "3020",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Vlaams-Brabant",
          "loc:DtcAdres.straat": "Brusselsesteenweg"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "A0020001",
          "loc:DtcWeglocatie.referentiepaalAfstand": 33,
          "loc:DtcWeglocatie.ident2": "A2",
          "loc:DtcWeglocatie.gemeente": "Leuven",
          "loc:DtcWeglocatie.straatnaam": "A0020001",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 83.1
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.xcoordinaat": 171418,
            "loc:DtcCoordLambert72.ycoordinaat": 175067.2
          }
        }
      },
      "ins:EMObject.resultaatKeuring": "conform met opmerkingen"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00150ce7-ecd3-4165-9930-0bc42857b392-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "loc:Locatie.omschrijving": "",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 99,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "vanottjo",
        "tz:DtcToezichter.naam": "Van Otterdijk",
        "tz:DtcToezichter.email": "jos.vanotterdijk@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Jos"
      },
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.vsaSperfilter": false,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_LB",
        "tz:DtcToezichtGroep.naam": "AWV_EW_LB"
      },
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMNaamObject.naam": "717",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 236702.2,
            "loc:DtcCoordLambert72.ycoordinaat": 189026,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "126",
          "loc:DtcAdres.gemeente": "As",
          "loc:DtcAdres.postcode": "3665",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.straat": "Stationsstraat",
          "loc:DtcAdres.provincie": "Limburg"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "N0750961",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 0,
          "loc:DtcWeglocatie.ident2": "N75",
          "loc:DtcWeglocatie.straatnaam": "N0750961",
          "loc:DtcWeglocatie.gemeente": "Maasmechelen",
          "loc:DtcWeglocatie.referentiepaalAfstand": 119
        }
      },
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "lgc:EMObject.ledVerlichting": false,
      "lgc:EMObject.armatuurkleur": "7038",
      "AIMObject.notitie": "",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "718",
        "tz:DtcBeheerder.naam": "District Oost - Limburg"
      },
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.lichtmastType": "RM - Rechte metalen paal",
      "lgc:VPLMast.nummerVoedingskring": "7",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00150ce7-ecd3-4165-9930-0bc42857b392-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "lgc:EMObject.geschilderd": false,
      "lgc:VPLMast.paalhoogte": "8,00",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Schreder Safir",
      "lgc:VPLMast.aantalArmen": "0 - geen armen",
      "lgc:EMObject.vsaType": "elektronisch",
      "lgc:EMObject.lampType": "MHHP-T-90 lv. PGZ12",
      "NaampadObject.naampad": "G1006/G1006.WV/717",
      "lgc:VPLMast.leverancier": "PetitJean",
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.armlengte": [
        "niet van toepassing - Indien lichtmast type niet gelijk is aan 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ]
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#OTN",
      "@id": "https://data.awvvlaanderen.be/id/asset/00152093-251e-4d92-9089-2a3835f01677-bGdjOmluc3RhbGxhdGllI09UTg",
      "ond:EMObject.klimatiseringLocatieOk": true,
      "ond:EMObject.beschrijvingInterventie": " Voeding module opgebrand",
      "NaampadObject.naampad": "XTMSA/XTMSA/MSA1.OTN",
      "ond:EMObject.apparatuurGereinigd": true,
      "ond:EMObject.fotoSApparatuurGemaakt": true,
      "ond:OTN.eindeOtn1": "2020-09-16T18:30:00",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_TELE",
        "tz:DtcToezichtGroep.naam": "EMT_TELE"
      },
      "ond:EMObject.glasvezelOkBevestigingLabels": true,
      "ond:EMObject.locatieBereikbaar": true,
      "ond:EMObject.apparatuurFiltersVervangen": true,
      "AIMNaamObject.naam": "MSA1.OTN",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd",
      "loc:Locatie.geometrie": "",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "EMT",
        "tz:DtcBeheerder.naam": "AGENTSCHAP WEGEN EN VERKEER"
      },
      "AIMObject.notitie": "",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#OTN",
      "ond:EMObject.apparatuurVrijVanAlarmen": true,
      "ond:EMObject.batterijVervangen": false,
      "ond:EMObject.abbameldaInstallatieOk": true,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Vandegoor",
        "tz:DtcToezichter.voornaam": "Peter",
        "tz:DtcToezichter.gebruikersnaam": "vandegpe",
        "tz:DtcToezichter.email": "peter.vandegoor@mow.vlaanderen.be"
      },
      "ond:OTN.startOtn1": "2020-09-16T17:30:00",
      "AIMDBStatus.isActief": false,
      "ond:EMObject.algemeneToestandLocatieOk": true,
      "ond:EMObject.glasvezelConnectorsOkOud": "ja",
      "ond:EMObject.koperkabelOkBevestigingLabels": true,
      "ond:EMObject.verlichtingLocatieOk": true,
      "loc:Locatie.omschrijving": "ALPHACLOUD MECHELEN DATACENTRUM",
      "ond:EMObject.elektrischPlanInstallatieOk": true,
      "ond:EMObject.ventilatieLocatieOk": false,
      "ond:EMObject.voedingsstekkersOk": true,
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.provincie": "Antwerpen",
          "loc:DtcAdres.straat": "Smisstraat",
          "loc:DtcAdres.postcode": "2800",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.nummer": "36",
          "loc:DtcAdres.gemeente": "Mechelen"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 158936.3,
            "loc:DtcCoordLambert72.ycoordinaat": 189860.8,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.weglocatie": ""
      },
      "ond:OTN.startOtn": "2018-08-17T13:11:00",
      "ond:OTN.eindeOtn": "2018-08-17T13:11:00",
      "ond:EMObject.DubbeleVoedingOk": "ja",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00152093-251e-4d92-9089-2a3835f01677-bGdjOmluc3RhbGxhdGllI09UTg"
      },
      "ond:EMObject.labelInstallatieNrApparatuurOk": true,
      "ond:EMObject.glasvezelOkSelectielijst": "ja",
      "ond:EMObject.upsOk": "Geen UPS",
      "ond:EMObject.voedingskabelsOk": true,
      "ond:EMObject.apparatuurVentilatieOk": true,
      "ond:EMObject.glasvezelConnectorsOk": true,
      "ond:EMObject.koperkabelOkSelectielijst": "ja",
      "ond:EMObject.labelContactInfoApparatuurOk": true,
      "ins:EMObject.abbameldaOperoepGemaakt": false
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#Mpt",
      "@id": "https://data.awvvlaanderen.be/id/asset/0015a1af-521f-4151-a98f-381fe5fc8eb6-bGdjOmluc3RhbGxhdGllI01wdA",
      "AIMObject.notitie": "",
      "NaampadObject.naampad": "A14X79.8/A14P79.8.K/MIV334/2552",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "hellinko",
        "tz:DtcToezichter.voornaam": "Koen",
        "tz:DtcToezichter.naam": "Hellinckx",
        "tz:DtcToezichter.email": "koen.hellinckx@mow.vlaanderen.be"
      },
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#Mpt",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0015a1af-521f-4151-a98f-381fe5fc8eb6-bGdjOmluc3RhbGxhdGllI01wdA"
      },
      "lgc:Mpt.rijstrook": "2",
      "AIMNaamObject.naam": "2552",
      "loc:Locatie.omschrijving": "VOETPADKAST E17 KMP 79,9  SNEDE",
      "AIMDBStatus.isActief": true,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_VHS",
        "tz:DtcToezichtGroep.naam": "EMT_VHS"
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "411",
        "tz:DtcBeheerder.naam": "District Gent"
      },
      "lgc:Mpt.gekoppeld": false,
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.straat": "Bosstraat",
          "loc:DtcAdres.gemeente": "Waasmunster",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Oost-Vlaanderen",
          "loc:DtcAdres.nummer": "26",
          "loc:DtcAdres.postcode": "9250"
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 131189.5,
            "loc:DtcCoordLambert72.ycoordinaat": 202267,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "A0140002",
          "loc:DtcWeglocatie.referentiepaalAfstand": -13,
          "loc:DtcWeglocatie.referentiepaalOpschrift": 79.9,
          "loc:DtcWeglocatie.straatnaam": "A0140002",
          "loc:DtcWeglocatie.gemeente": "Waasmunster",
          "loc:DtcWeglocatie.ident2": "A14"
        }
      },
      "loc:Locatie.geometrie": "",
      "lgc:Mpt.meetpost": 133401,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/0015d19e-c18b-41ee-8e17-676409515284-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.lichtmastType": "M - Metalen paal met arm",
      "lgc:EMObject.vsaType": "elektromagnetisch",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "ond:EMObject.aantalStartersVervangen": 0,
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "lgc:VPLMast.ralKleurVplmast": "7038",
      "AIMObject.notitie": "",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:EMObject.opmerkingInventarisVerlichtingstoestel": "plan 17 maart 1999",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "lgc:EMObject.geschilderd": true,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Geert",
        "tz:DtcToezichter.email": "geert.deglas@mow.vlaanderen.be",
        "tz:DtcToezichter.gebruikersnaam": "deglasge",
        "tz:DtcToezichter.naam": "Deglas"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_WV",
        "tz:DtcToezichtGroep.naam": "AWV_EW_WV"
      },
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "ins:EMObject.directGevaar": false,
      "lgc:VPLMast.paalhoogte": "12,50 - niet voor type lichtmast 'K' en 'KS'",
      "ond:EMObject.aantalLampenVervangen": 0,
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "AIMDBStatus.isActief": true,
      "lgc:VPLMast.armlengte": [
        "2 - Enkel voor lichtmast types 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ],
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:VPLMast.opmerkingInventarisPaal": "plan 17 maart 1999",
      "loc:Locatie.omschrijving": "weg: A019; ident8: A0190311; kilometerpunt: 0,000; zijde weg: Rechts",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Schreder GZM",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "lgc:VPLMast.aantalArmen": "1 - alleen mogelijk voor lichtmast 'M', 'MS', 'B', 'BS', 'K' of 'KS'",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "42",
          "loc:DtcAdres.postcode": "8560",
          "loc:DtcAdres.straat": "Tombroekdreef",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.gemeente": "Wevelgem",
          "loc:DtcAdres.provincie": "West-Vlaanderen"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalOpschrift": 0.3,
          "loc:DtcWeglocatie.ident8": "A0190311",
          "loc:DtcWeglocatie.ident2": "A19",
          "loc:DtcWeglocatie.straatnaam": "A0190311",
          "loc:DtcWeglocatie.referentiepaalAfstand": 42,
          "loc:DtcWeglocatie.gemeente": "Wevelgem"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 169502,
            "loc:DtcCoordLambert72.xcoordinaat": 67652,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        }
      },
      "lgc:VPLMast.nummerVoedingskring": "B",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "312",
        "tz:DtcBeheerder.naam": "District Kortrijk"
      },
      "NaampadObject.naampad": "WW0093/WW0093.WV/B11",
      "ond:EMObject.aantalVsaVervangen": 0,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "lgc:EMObject.lampType": "niet gekend",
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "AIMNaamObject.naam": "B11",
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0015d19e-c18b-41ee-8e17-676409515284-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/0016338a-50b6-4e88-94fd-5cb0685bc738-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "lgc:VPLMast.aantalArmen": "niet gekend",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalAfstand": -47,
          "loc:DtcWeglocatie.referentiepaalOpschrift": 45.3,
          "loc:DtcWeglocatie.ident2": "R4",
          "loc:DtcWeglocatie.gemeente": "Gent",
          "loc:DtcWeglocatie.ident8": "R0040001",
          "loc:DtcWeglocatie.straatnaam": "Industrieweg"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 103338.1,
            "loc:DtcCoordLambert72.ycoordinaat": 198494.2,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "50",
          "loc:DtcAdres.postcode": "9032",
          "loc:DtcAdres.gemeente": "Gent",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.straat": "Industrieweg",
          "loc:DtcAdres.provincie": "Oost-Vlaanderen"
        }
      },
      "lgc:VPLMast.lichtmastType": "niet gekend",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "NaampadObject.naampad": "WO0139/WO0139.WV/B23",
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "ond:EMObject.aantalStartersVervangen": 0,
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0016338a-50b6-4e88-94fd-5cb0685bc738-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:EMObject.vsaType": "niet gekend",
      "ond:EMObject.aantalLampenVervangen": 0,
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "AIMDBStatus.isActief": true,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.naam": "AWV_EW_OV",
        "tz:DtcToezichtGroep.referentie": "AWV_EW_OV"
      },
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:EMObject.lampType": "NaLP131",
      "lgc:VPLMast.paalhoogte": "niet gekend",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "loc:Locatie.omschrijving": "WEG: ; IDENT8: R0040002; KILOMETERPUNT: ; ZIJDE WEG: Z43-MDN60",
      "lgc:VPLMast.armlengte": [
        "niet gekend"
      ],
      "ond:EMObject.aantalVsaVervangen": 0,
      "lgc:EMObject.verlichtingstoestelMerkEnType": "niet gekend",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 157,
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "AIMNaamObject.naam": "B23",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "desmetjg",
        "tz:DtcToezichter.email": "jeanpaul.desmet@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Jean-Paul",
        "tz:DtcToezichter.naam": "De Smet"
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "411",
        "tz:DtcBeheerder.naam": "District Gent"
      },
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "lgc:EMObject.verlichtingstype": "niet gekend",
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
      "@id": "https://data.awvvlaanderen.be/id/asset/001769c7-5487-46d7-b565-06e896d89098-b25kZXJkZWVsI05ldHdlcmtwb29ydA",
      "AIMObject.notitie": "",
      "loc:Locatie.omschrijving": "",
      "Netwerkpoort.technologie": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkTechnologie/NULL",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "001769c7-5487-46d7-b565-06e896d89098-b25kZXJkZWVsI05ldHdlcmtwb29ydA"
      },
      "AIMDBStatus.isActief": true,
      "Netwerkpoort.nNILANCapaciteit": 100,
      "AIMObject.typeURI": "https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Netwerkpoort",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 191011.5,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.xcoordinaat": 102874.8
          }
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "1",
          "loc:DtcAdres.postcode": "9051",
          "loc:DtcAdres.gemeente": "Gent",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Oost-Vlaanderen",
          "loc:DtcAdres.straat": "Raymonde de Larochelaan"
        },
        "loc:DtcPuntlocatie.bron": "",
        "loc:DtcPuntlocatie.weglocatie": ""
      },
      "Netwerkpoort.merk": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkMerk/Ciena",
      "Netwerkpoort.config": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortConfig/FE",
      "loc:Locatie.geometrie": "",
      "Netwerkpoort.golflengte": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlNetwerkpoortGolflengte/NULL",
      "AIMNaamObject.naam": "Poort_3718",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-ontwerp"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00181a47-8235-4623-8571-cdb2b81c9564-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "AIMDBStatus.isActief": true,
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "ond:EMObject.aantalStartersVervangen": 0,
      "lgc:EMObject.lampType": "LED",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "andere",
      "AIMObject.notitie": "",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.lichtmastType": "RM - Rechte metalen paal",
      "AIMNaamObject.naam": "C31",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_WV",
        "tz:DtcToezichtGroep.naam": "AWV_EW_WV"
      },
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "ond:EMObject.aantalLampenVervangen": 0,
      "NaampadObject.naampad": "WW0019/WW0019.WV/C31",
      "lgc:EMObject.merkEnTypeLed": "Schreder Ampera",
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "lgc:VPLMast.aantalArmen": "0 - geen armen",
      "lgc:EMObject.vsaType": "elektronisch",
      "lgc:EMObject.vsaSperfilter": false,
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "District Ieper",
        "tz:DtcBeheerder.referentie": "313"
      },
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "N0340001",
          "loc:DtcWeglocatie.referentiepaalAfstand": 42,
          "loc:DtcWeglocatie.referentiepaalOpschrift": 65,
          "loc:DtcWeglocatie.straatnaam": "Duinkerkelaan",
          "loc:DtcWeglocatie.gemeente": "De Panne",
          "loc:DtcWeglocatie.ident2": "N34"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 25478.6,
            "loc:DtcCoordLambert72.ycoordinaat": 200678.5,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "202",
          "loc:DtcAdres.straat": "Zeelaan",
          "loc:DtcAdres.postcode": "8660",
          "loc:DtcAdres.provincie": "West-Vlaanderen",
          "loc:DtcAdres.gemeente": "De Panne",
          "loc:DtcAdres.bus": ""
        }
      },
      "lgc:EMObject.contractnummerLeveringLed": "MDN31",
      "lgc:EMObject.lumenPakketLed": 15000,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00181a47-8235-4623-8571-cdb2b81c9564-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ond:EMObject.aantalVsaVervangen": 0,
      "lgc:EMObject.datumInstallatieLed": "2015-06-26",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "lgc:EMObject.kleurtemperatuurLed": "K4000",
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "loc:Locatie.omschrijving": "weg: N034; ident8: N0340001; kilometerpunt: 0,000; zijde weg: Rechts",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.gebruikersnaam": "callewal",
        "tz:DtcToezichter.voornaam": "Alan",
        "tz:DtcToezichter.email": "alan.callewaert@mow.vlaanderen.be",
        "tz:DtcToezichter.naam": "Callewaert"
      },
      "lgc:EMObject.aantalDriversPerToestel": 1,
      "lgc:EMObject.ledVerlichting": true,
      "lgc:VPLMast.paalhoogte": "12,50",
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "lgc:VPLMast.nummerVoedingskring": "C",
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "lgc:EMObject.lichtpunthoogteTovRijweg": 12.5,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "lgc:VPLMast.armlengte": [
        "niet van toepassing - Indien lichtmast type niet gelijk is aan 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ],
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00189e9e-0f02-4bb8-8c4d-a2be2c7f8bd1-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "lgc:VPLMast.aantalArmen": "niet gekend",
      "lgc:VPLMast.lichtmastType": "M - Metalen paal met arm",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "lgc:EMObject.contractnummerLeveringLed": "niet gekend",
      "loc:Locatie.omschrijving": "weg: N031; ident8: N0310001; kilometerpunt: 0,000; zijde weg: Rechts",
      "lgc:EMObject.lampType": "NaHP-T-100",
      "AIMObject.notitie": "",
      "AIMNaamObject.naam": "C06",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Philips Iridium",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "ins:EMObject.externeRoestvorming": "lichte roestvorming",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet gekend",
      "lgc:EMObject.overhangLed": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Els",
        "tz:DtcToezichter.email": "els.geysen@mow.vlaanderen.be",
        "tz:DtcToezichter.naam": "Geysen",
        "tz:DtcToezichter.gebruikersnaam": "geysenel"
      },
      "lgc:EMObject.verlichtingsniveauLed": "niet gekend",
      "lgc:EMObject.kleurtemperatuurLed": "niet gekend",
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_WV",
        "tz:DtcToezichtGroep.naam": "AWV_EW_WV"
      },
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "9",
          "loc:DtcAdres.straat": "Zeelaan",
          "loc:DtcAdres.gemeente": "Brugge",
          "loc:DtcAdres.postcode": "8380",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "West-Vlaanderen"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 219746.9,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.xcoordinaat": 68115.4
          }
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident2": "N31",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 13.9,
          "loc:DtcWeglocatie.straatnaam": "Zeelaan",
          "loc:DtcWeglocatie.ident8": "N0310001",
          "loc:DtcWeglocatie.gemeente": "Brugge",
          "loc:DtcWeglocatie.referentiepaalAfstand": -39
        }
      },
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:VPLMast.paalhoogte": "12,50 - niet voor type lichtmast 'K' en 'KS'",
      "lgc:EMObject.vsaType": "niet gekend",
      "ins:EMObject.interneRoestvorming": "lichte roestvorming",
      "ins:VPLMast.toestandBouten": "niet van toepassing",
      "ond:EMObject.aantalLampenVervangen": 0,
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "AIMDBStatus.isActief": true,
      "lgc:VPLMast.armlengte": [
        "2 - Enkel voor lichtmast types 'M', 'MS', 'B', 'BS', 'K' of 'KS'"
      ],
      "ins:VPLMast.toestandPaal": "OK",
      "lgc:EMObject.vsaSperfilter": false,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00189e9e-0f02-4bb8-8c4d-a2be2c7f8bd1-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "NaampadObject.naampad": "WW0078/WW0078.WV/C06",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ond:EMObject.aantalVsaVervangen": 0,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "lgc:EMObject.aantalTeVerlichtenRijvakkenLed": "niet gekend",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "District Brugge",
        "tz:DtcBeheerder.referentie": "311"
      },
      "lgc:EMObject.ledVerlichting": false,
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ins:EMObject.toestandVerlichtingstoestellen": "OK",
      "ins:VPLMast.toestandFunderingVplmast": "OK",
      "ond:EMObject.aantalStartersVervangen": 0,
      "ins:VPLMast.toestandDeurtje": "OK",
      "ins:EMObject.nummerLeesbaar": "Ja",
      "lgc:EMObject.verlichtingstype": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "lgc:VPLMast.risicovollePaal": false,
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 120,
      "loc:Locatie.geometrie": ""
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VOT",
      "@id": "https://data.awvvlaanderen.be/id/asset/0018bba6-a2a7-4540-b91e-df2a1f043555-bGdjOmluc3RhbGxhdGllI1ZPVA",
      "AIMObject.notitie": "",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VOT",
      "AIMDBStatus.isActief": false,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Ceyssens",
        "tz:DtcToezichter.email": "Christian.Ceyssens@vlaamsewaterweg.be",
        "tz:DtcToezichter.voornaam": "Christian",
        "tz:DtcToezichter.gebruikersnaam": "ceyssech"
      },
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0018bba6-a2a7-4540-b91e-df2a1f043555-bGdjOmluc3RhbGxhdGllI1ZPVA"
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "720",
        "tz:DtcBeheerder.naam": "District Centraal - Limburg"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.naam": "EMT_WHM",
        "tz:DtcToezichtGroep.referentie": "EMT_WHM"
      },
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/verwijderd",
      "NaampadObject.naampad": "LUM1B25/VOT",
      "AIMNaamObject.naam": "VOT"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/0019049c-ba27-4d4e-ad14-d4bafb9c6254-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "lgc:VPLMast.aantalArmen": "niet gekend",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Lefranc",
        "tz:DtcToezichter.email": "philippe.lefranc@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Philippe",
        "tz:DtcToezichter.gebruikersnaam": "lefranpi"
      },
      "lgc:VPLMast.lichtmastType": "niet gekend",
      "lgc:EMObject.lampType": "NaHP-T-150",
      "lgc:EMObject.vsaSperfilter": false,
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "1",
          "loc:DtcAdres.straat": "Sluisweg",
          "loc:DtcAdres.postcode": "9000",
          "loc:DtcAdres.gemeente": "Gent",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Oost-Vlaanderen"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 189371.9,
            "loc:DtcCoordLambert72.xcoordinaat": 105542.4,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.straatnaam": "R0040001",
          "loc:DtcWeglocatie.ident2": "R4",
          "loc:DtcWeglocatie.gemeente": "Gent",
          "loc:DtcWeglocatie.referentiepaalAfstand": 43,
          "loc:DtcWeglocatie.referentiepaalOpschrift": 31.3,
          "loc:DtcWeglocatie.ident8": "R0040001"
        }
      },
      "lgc:VPLMast.armlengte": [
        "niet gekend"
      ],
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "ond:EMObject.aantalStartersVervangen": 0,
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "loc:Locatie.omschrijving": "WEG: ; IDENT8: R0041132; KILOMETERPUNT: ; ZIJDE WEG:",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0019049c-ba27-4d4e-ad14-d4bafb9c6254-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "AIMNaamObject.naam": "A23",
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:EMObject.vsaType": "niet gekend",
      "ond:EMObject.aantalLampenVervangen": 0,
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "AIMDBStatus.isActief": true,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.naam": "AWV_EW_OV",
        "tz:DtcToezichtGroep.referentie": "AWV_EW_OV"
      },
      "lgc:VPLMast.paalhoogte": "niet gekend",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "ond:EMObject.aantalVsaVervangen": 0,
      "NaampadObject.naampad": "WO0976/WO0976.WV/A23",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "niet gekend",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "411",
        "tz:DtcBeheerder.naam": "District Gent"
      },
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 180,
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00193c46-5abe-4b36-8be9-ba88bcaa269c-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "lgc:VPLMast.aantalArmen": "niet gekend",
      "lgc:VPLMast.lichtmastType": "niet gekend",
      "loc:Locatie.omschrijving": "R6-(VAN OVERHEIDE TOT WALEM)-KABINE KOUTERDREEF-RING - KMPNT 19,85 TOT 21,93 - CABINE HS",
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:VPLMast.armlengte": [
        "niet gekend"
      ],
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_AN",
        "tz:DtcToezichtGroep.naam": "AWV_EW_AN"
      },
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ond:EMObject.aantalStartersVervangen": 0,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00193c46-5abe-4b36-8be9-ba88bcaa269c-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Van Alboom",
        "tz:DtcToezichter.gebruikersnaam": "vanalbma",
        "tz:DtcToezichter.email": "matthias.vanalboom@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Matthias"
      },
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:EMObject.vsaType": "niet gekend",
      "ond:EMObject.aantalLampenVervangen": 0,
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "112",
        "tz:DtcBeheerder.naam": "District Puurs"
      },
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "lgc:VPLMast.paalhoogte": "niet gekend",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "AIMNaamObject.naam": "086",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ond:EMObject.aantalVsaVervangen": 0,
      "lgc:EMObject.verlichtingstoestelMerkEnType": "niet gekend",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "lgc:EMObject.lampType": "niet gekend",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.provincie": "Antwerpen",
          "loc:DtcAdres.nummer": "256",
          "loc:DtcAdres.postcode": "2800",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.straat": "Oude Antwerpsebaan",
          "loc:DtcAdres.gemeente": "Mechelen"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalAfstand": -8,
          "loc:DtcWeglocatie.gemeente": "Mechelen",
          "loc:DtcWeglocatie.ident2": "A1",
          "loc:DtcWeglocatie.straatnaam": "A0010001",
          "loc:DtcWeglocatie.ident8": "A0010001",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 18.4
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 193023.8,
            "loc:DtcCoordLambert72.xcoordinaat": 156020,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        }
      },
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "lgc:EMObject.verlichtingstype": "hoofdbaan",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "NaampadObject.naampad": "A0673/A0673.WV/086",
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VL",
      "@id": "https://data.awvvlaanderen.be/id/asset/00197b0d-b858-498e-be3c-e185886df51c-bGdjOmluc3RhbGxhdGllI1ZM",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VL",
      "AIMNaamObject.naam": "VL",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Cornu",
        "tz:DtcToezichter.gebruikersnaam": "cornusv",
        "tz:DtcToezichter.voornaam": "Sven",
        "tz:DtcToezichter.email": "Sven.Cornu@mow.vlaanderen.be"
      },
      "AIMDBStatus.isActief": true,
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00197b0d-b858-498e-be3c-e185886df51c-bGdjOmluc3RhbGxhdGllI1ZM"
      },
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "loc:Locatie.omschrijving": "N180 NOORDERLAAN- N129 GROENENDAALLAAN                   K031",
      "NaampadObject.naampad": "915A3/VL",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "121",
        "tz:DtcBeheerder.naam": "District Antwerpen"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_AN",
        "tz:DtcToezichtGroep.naam": "AWV_EW_AN"
      },
      "loc:Locatie.geometrie": "",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.provincie": "Antwerpen",
          "loc:DtcAdres.gemeente": "Antwerpen",
          "loc:DtcAdres.straat": "Groenendaallaan",
          "loc:DtcAdres.postcode": "2030",
          "loc:DtcAdres.nummer": "391",
          "loc:DtcAdres.bus": ""
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 153605.3,
            "loc:DtcCoordLambert72.ycoordinaat": 214981,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalAfstand": 93,
          "loc:DtcWeglocatie.straatnaam": "Groenendaallaan",
          "loc:DtcWeglocatie.ident2": "N129",
          "loc:DtcWeglocatie.gemeente": "Antwerpen",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 2.5,
          "loc:DtcWeglocatie.ident8": "N1290002"
        }
      },
      "AIMObject.notitie": ""
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/00198bb5-f955-4580-a3b7-fb9d75711620-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "loc:Locatie.omschrijving": "",
      "lgc:VPLMast.aantalArmen": "niet gekend",
      "lgc:VPLMast.lichtmastType": "niet gekend",
      "AIMNaamObject.naam": "045",
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:VPLMast.armlengte": [
        "niet gekend"
      ],
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ond:EMObject.aantalStartersVervangen": 0,
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.straat": "Berkenlaan",
          "loc:DtcAdres.gemeente": "Machelen",
          "loc:DtcAdres.postcode": "1831",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Vlaams-Brabant",
          "loc:DtcAdres.nummer": "5"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.gemeente": "Machelen",
          "loc:DtcWeglocatie.straatnaam": "A2010002",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 1.8,
          "loc:DtcWeglocatie.ident8": "A2010002",
          "loc:DtcWeglocatie.ident2": "A201",
          "loc:DtcWeglocatie.referentiepaalAfstand": -38
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 174790.1,
            "loc:DtcCoordLambert72.xcoordinaat": 155340.2,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel"
      },
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:EMObject.vsaType": "niet gekend",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Bulens",
        "tz:DtcToezichter.gebruikersnaam": "bulenswi",
        "tz:DtcToezichter.email": "wim.bulens@mow.vlaanderen.be",
        "tz:DtcToezichter.voornaam": "Wim"
      },
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "00198bb5-f955-4580-a3b7-fb9d75711620-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "ond:EMObject.aantalLampenVervangen": 0,
      "NaampadObject.naampad": "C1827/C1827.WV/045",
      "lgc:VPLMast.paalhoogte": "niet gekend",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.naam": "District Vilvoorde-autosnelwegen",
        "tz:DtcBeheerder.referentie": "212"
      },
      "ond:EMObject.aantalVsaVervangen": 0,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_VB",
        "tz:DtcToezichtGroep.naam": "AWV_EW_VB"
      },
      "lgc:EMObject.verlichtingstoestelMerkEnType": "niet gekend",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "lgc:EMObject.lampType": "niet gekend",
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "lgc:EMObject.verlichtingstype": "niet gekend",
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#SDH",
      "@id": "https://data.awvvlaanderen.be/id/asset/0019a155-ae64-4703-8058-feb461c504fb-bGdjOmluc3RhbGxhdGllI1NESA",
      "AIMObject.notitie": "",
      "loc:Locatie.omschrijving": "",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Vandegoor",
        "tz:DtcToezichter.voornaam": "Peter",
        "tz:DtcToezichter.gebruikersnaam": "vandegpe",
        "tz:DtcToezichter.email": "peter.vandegoor@mow.vlaanderen.be"
      },
      "AIMDBStatus.isActief": true,
      "loc:Locatie.puntlocatie": {
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 172055.5,
            "loc:DtcCoordLambert72.xcoordinaat": 149198.6,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/manueel",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.gemeente": "Sint-Joost-ten-Node",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Brussel",
          "loc:DtcAdres.nummer": "19",
          "loc:DtcAdres.postcode": "1210",
          "loc:DtcAdres.straat": "Koning Albert II laan"
        },
        "loc:DtcPuntlocatie.weglocatie": ""
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "EMT_TELE",
        "tz:DtcToezichtGroep.naam": "EMT_TELE"
      },
      "ond:SDH.startSdh": "2021-08-09T10:00:00",
      "ond:EMObject.beschrijvingInterventie": "swap asc105",
      "loc:Locatie.geometrie": "",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0019a155-ae64-4703-8058-feb461c504fb-bGdjOmluc3RhbGxhdGllI1NESA"
      },
      "AIMNaamObject.naam": "CONa",
      "ond:SDH.startSdh1": "2021-11-17T12:00:00",
      "NaampadObject.naampad": "XTCON/XTCON/CONa",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "ond:SDH.eindeSdh1": "2021-11-17T13:00:00",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#SDH"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/0019c98d-5beb-45fe-bb3e-0043e0fbc37c-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "lgc:EMObject.aantalVerlichtingstoestellen": 1,
      "lgc:VPLMast.lichtmastType": "M - Metalen paal met arm",
      "lgc:VPLMast.optiekLed": "206_403892_7500.ldt",
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "312",
        "tz:DtcBeheerder.naam": "District Kortrijk"
      },
      "lgc:VPLMast.merkEnTypeArmatuurcontroller2": "Smartnodes - SLC-G3",
      "lgc:VPLMast.opmerkingInventarisPaal": "plan van 7 januari 2008",
      "lgc:EMObject.lampType": "LED",
      "lgc:VPLMast.ralKleurVplmast": "7038",
      "AIMObject.notitie": "",
      "AIMNaamObject.naam": "D63",
      "lgc:VPLMast.merkEnTypeArmatuurcontroller1": "Smartnodes - SLC-G3",
      "ins:EMObject.interneRoestvorming": "OK",
      "lgc:VPLMast.aantalArmen": "niet gekend",
      "lgc:EMObject.overhangLed": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:EMObject.contractnummerLeveringLed": "MDN73",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet van toepassing",
      "lgc:EMObject.verlichtingsniveauLed": "niet gekend",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.ident8": "A0140002",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 4.5,
          "loc:DtcWeglocatie.referentiepaalAfstand": -9,
          "loc:DtcWeglocatie.gemeente": "Kortrijk",
          "loc:DtcWeglocatie.ident2": "A14",
          "loc:DtcWeglocatie.straatnaam": "A0140002"
        },
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/meter",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.postcode": "8511",
          "loc:DtcAdres.nummer": "66",
          "loc:DtcAdres.gemeente": "Kortrijk",
          "loc:DtcAdres.straat": "Kapelhoekstraat",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "West-Vlaanderen"
        },
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 69201.6,
            "loc:DtcCoordLambert72.zcoordinaat": 0,
            "loc:DtcCoordLambert72.ycoordinaat": 164477.1
          }
        }
      },
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.voornaam": "Geert",
        "tz:DtcToezichter.email": "geert.deglas@mow.vlaanderen.be",
        "tz:DtcToezichter.gebruikersnaam": "deglasge",
        "tz:DtcToezichter.naam": "Deglas"
      },
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_WV",
        "tz:DtcToezichtGroep.naam": "AWV_EW_WV"
      },
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "lgc:EMObject.opmerkingInventarisVerlichtingstoestel": "plan van 7 januari 2008",
      "ins:VPLMast.toestandBouten": "niet van toepassing",
      "lgc:VPLMast.armlengte": [
        "2"
      ],
      "lgc:EMObject.inclinatiehoekLed": 0,
      "lgc:EMObject.vsaType": "elektronisch",
      "lgc:EMObject.aantalTeVerlichtenRijvakkenLed": "R2",
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.merkEnTypeLed": "AMPERA 5234 4000K 7500LM 48W",
      "ins:VPLMast.toestandPaal": "OK",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 48,
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:VPLMast.nummerVoedingskring": "D",
      "lgc:EMObject.verlichtingstype": "opafrit",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "NaampadObject.naampad": "WW0051/WW0051.WV/D63",
      "ond:EMObject.aantalLampenVervangen": 1,
      "lgc:VPLMast.serienummerArmatuurcontroller1": "SLC-G3-2020-889",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0019c98d-5beb-45fe-bb3e-0043e0fbc37c-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "loc:Locatie.omschrijving": "WEG: A014; IDENT8: A0140002; KILOMETERPUNT: 0,000; ZIJDE WEG: RECHTS",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 1,
      "ond:EMObject.aantalLamphoudersVervangen": 1,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ond:EMObject.aantalVsaVervangen": 1,
      "lgc:EMObject.kleurtemperatuurLed": "K4000",
      "lgc:EMObject.datumInstallatieLed": "2021-03-26",
      "ins:EMObject.externeRoestvorming": "OK",
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "lgc:EMObject.aantalDriversPerToestel": 1,
      "ins:EMObject.toestandVerlichtingstoestellen": "OK",
      "ins:VPLMast.toestandFunderingVplmast": "OK",
      "ins:VPLMast.toestandDeurtje": "OK",
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Schreder Ampera",
      "lgc:EMObject.ledVerlichting": true,
      "lgc:VPLMast.paalhoogte": "12,50",
      "ins:EMObject.nummerLeesbaar": "Ja",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false,
      "lgc:EMObject.brandurenLed": 60000,
      "lgc:EMObject.lumenPakketLed": 7500
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/0019eec3-4efa-42e8-9a93-d2ea9bacf165-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.email": "bert.groven@mow.vlaanderen.be",
        "tz:DtcToezichter.naam": "Groven",
        "tz:DtcToezichter.gebruikersnaam": "grovenbe",
        "tz:DtcToezichter.voornaam": "Bert"
      },
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:VPLMast.lichtmastType": "niet gekend",
      "AIMDBStatus.isActief": true,
      "AIMNaamObject.naam": "711",
      "lgc:VPLMast.armlengte": [
        "niet gekend"
      ],
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "ins:VPLMast.toestandDeurtje": "niet gekend",
      "ins:EMObject.externeRoestvorming": "niet gekend",
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ond:EMObject.aantalStartersVervangen": 0,
      "ins:EMObject.interneRoestvorming": "niet gekend",
      "AIMObject.notitie": "",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.ycoordinaat": 175500.1,
            "loc:DtcCoordLambert72.xcoordinaat": 170143.4,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.gemeente": "Herent",
          "loc:DtcAdres.nummer": "99",
          "loc:DtcAdres.postcode": "3020",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Vlaams-Brabant",
          "loc:DtcAdres.straat": "Brusselsesteenweg"
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.straatnaam": "Brusselsesteenweg",
          "loc:DtcWeglocatie.gemeente": "Herent",
          "loc:DtcWeglocatie.ident8": "N0020001",
          "loc:DtcWeglocatie.referentiepaalOpschrift": 21.2,
          "loc:DtcWeglocatie.ident2": "N2",
          "loc:DtcWeglocatie.referentiepaalAfstand": -37
        }
      },
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "213",
        "tz:DtcBeheerder.naam": "District Leuven"
      },
      "lgc:VPLMast.aantalArmen": "niet gekend",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "niet gekend",
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "ins:EMObject.directGevaar": false,
      "lgc:EMObject.vsaType": "niet gekend",
      "ond:EMObject.aantalLampenVervangen": 0,
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "lgc:VPLMast.paalhoogte": "niet gekend",
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "ond:EMObject.aantalVsaVervangen": 0,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.referentie": "AWV_EW_VB",
        "tz:DtcToezichtGroep.naam": "AWV_EW_VB"
      },
      "lgc:EMObject.verlichtingstoestelMerkEnType": "niet gekend",
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "ins:EMObject.toestandVerlichtingstoestellen": "niet gekend",
      "lgc:EMObject.lampType": "niet gekend",
      "NaampadObject.naampad": "C0462/C0462.WV/711",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "0019eec3-4efa-42e8-9a93-d2ea9bacf165-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "ins:VPLMast.toestandFunderingVplmast": "niet gekend",
      "ins:VPLMast.toestandPaal": "niet gekend",
      "lgc:EMObject.verlichtingstype": "niet gekend",
      "ins:VPLMast.toestandBouten": "niet gekend",
      "ond:VPLMast.deurtjeVervangen": false,
      "loc:Locatie.geometrie": "",
      "loc:Locatie.omschrijving": "weg: N002; ident8: N0020001; kilometerpunt: 9999,000; zijde weg: Links",
      "lgc:VPLMast.risicovollePaal": false,
      "ins:EMObject.nummerLeesbaar": "niet gekend"
    },
    {
      "@type": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "@id": "https://data.awvvlaanderen.be/id/asset/001a7434-0700-42e3-8adf-ae1c96520842-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q",
      "AIMObject.notitie": "",
      "lgc:VPLMast.bevestigingswijzeMeerdereToestellen": "mediaanbalk H",
      "lgc:EMObject.lumenPakketLed": 0,
      "AIMToestand.toestand": "https://wegenenverkeer.data.vlaanderen.be/id/concept/KlAIMToestand/in-gebruik",
      "ond:EMObject.aantalKlemmenblokkenVervangen": 0,
      "NaampadObject.naampad": "WO0179/WO0179.WV/C03",
      "ond:EMObject.vermoedenSokkelAsbesthoudend": false,
      "lgc:EMObject.verlichtingstoestelMerkEnType": "Rombalux",
      "lgc:VPLMast.nummerVoedingskring": "C",
      "ond:VPLMast.deurtjeVervangen": false,
      "ond:EMObject.aantalLamphoudersVervangen": 0,
      "lgc:VPLMast.lichtmastType": "RM - Rechte metalen paal",
      "lgc:EMObject.aantalVerlichtingstoestellen": 4,
      "lgc:VPLMast.leverancier": "niet gekend",
      "lgc:VPLMast.redenLichtmastBuitenGebruik": "niet van toepassing",
      "lgc:EMObject.geschilderd": false,
      "ins:EMObject.directGevaar": false,
      "ond:EMObject.aantalLampenVervangen": 0,
      "ond:EMObject.aantalZekeringenVervangen": 0,
      "lgc:EMObject.inclinatiehoekLed": 0,
      "lgc:VPLMast.aantalArmen": "0 - geen armen",
      "loc:Locatie.puntlocatie": {
        "loc:DtcPuntlocatie.precisie": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatiePrecisie/plus_meter",
        "loc:DtcPuntlocatie.adres": {
          "loc:DtcAdres.nummer": "132",
          "loc:DtcAdres.postcode": "9140",
          "loc:DtcAdres.bus": "",
          "loc:DtcAdres.provincie": "Oost-Vlaanderen",
          "loc:DtcAdres.straat": "Steendonkstraat",
          "loc:DtcAdres.gemeente": "Temse"
        },
        "loc:DtcPuntlocatie.bron": "https://loc.data.wegenenverkeer.be/id/concept/KlLocatieBron/meettoestel",
        "loc:3Dpunt.puntgeometrie": {
          "loc:DtcCoord.lambert72": {
            "loc:DtcCoordLambert72.xcoordinaat": 140178,
            "loc:DtcCoordLambert72.ycoordinaat": 205308.1,
            "loc:DtcCoordLambert72.zcoordinaat": 0
          }
        },
        "loc:DtcPuntlocatie.weglocatie": {
          "loc:DtcWeglocatie.referentiepaalAfstand": -47,
          "loc:DtcWeglocatie.referentiepaalOpschrift": 89.5,
          "loc:DtcWeglocatie.ident2": "A14",
          "loc:DtcWeglocatie.gemeente": "Temse",
          "loc:DtcWeglocatie.straatnaam": "A0140001",
          "loc:DtcWeglocatie.ident8": "A0140001"
        }
      },
      "AIMNaamObject.naam": "C03",
      "AIMDBStatus.isActief": true,
      "lgc:EMObject.lichtpunthoogteTovRijweg": 20,
      "tz:Toezicht.toezichtgroep": {
        "tz:DtcToezichtGroep.naam": "AWV_EW_OV",
        "tz:DtcToezichtGroep.referentie": "AWV_EW_OV"
      },
      "loc:Locatie.omschrijving": "E17 - N485 (Complex Haasdonk)",
      "lgc:EMObject.vsaSperfilter": false,
      "lgc:EMObject.lampType": "NaLP131",
      "AIMObject.assetId": {
        "DtcIdentificator.toegekendDoor": "AWV",
        "DtcIdentificator.identificator": "001a7434-0700-42e3-8adf-ae1c96520842-bGdjOmluc3RhbGxhdGllI1ZQTE1hc3Q"
      },
      "lgc:EMObject.aantalDriversPerToestel": 0,
      "lgc:VPLMast.paalhoogte": "20,00 - niet voor type lichtmast 'K' en 'KS'",
      "ond:EMObject.aantalVsaVervangen": 0,
      "AIMObject.typeURI": "https://lgc.data.wegenenverkeer.be/ns/installatie#VPLMast",
      "lgc:EMObject.verlichtingstoestelSysteemvermogen": 157,
      "lgc:EMObject.verlichtingstype": "doorlopende straatverlichting",
      "lgc:EMObject.vsaType": "elektromagnetisch",
      "lgc:EMObject.brandurenLed": 0,
      "lgc:VPLMast.armlengte": [
        "niet van toepassing"
      ],
      "lgc:EMObject.ledVerlichting": false,
      "tz:Schadebeheerder.schadebeheerder": {
        "tz:DtcBeheerder.referentie": "411",
        "tz:DtcBeheerder.naam": "District Gent"
      },
      "lgc:VPLMast.lichtmastBuitenGebruik": false,
      "ond:EMObject.aantalStartersVervangen": 0,
      "tz:Toezicht.toezichter": {
        "tz:DtcToezichter.naam": "Kaya",
        "tz:DtcToezichter.voornaam": "Cenk",
        "tz:DtcToezichter.gebruikersnaam": "kayace",
        "tz:DtcToezichter.email": "cenkhan.kaya@mow.vlaanderen.be"
      },
      "loc:Locatie.geometrie": "",
      "lgc:VPLMast.risicovollePaal": false
    }
  ]
}"""