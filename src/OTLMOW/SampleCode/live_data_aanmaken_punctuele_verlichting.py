from OTLMOW.Facility.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.Armatuurcontroller import Armatuurcontroller
from OTLMOW.OTLModel.Classes.Bevestiging import Bevestiging
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.LEDDriver import LEDDriver
from OTLMOW.OTLModel.Classes.PunctueleVerlichtingsmast import PunctueleVerlichtingsmast
from OTLMOW.OTLModel.Classes.Sturing import Sturing
from OTLMOW.OTLModel.Classes.VerlichtingstoestelLED import VerlichtingstoestelLED
from OTLMOW.OTLModel.Classes.Voedt import Voedt
from OTLMOW.OTLModel.Classes.VoedtAangestuurd import VoedtAangestuurd

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger)

    # add EM-Infra assets through API
    input_uuids = ['e8b4022a-00d6-4b01-9766-0e50ecfda150', '63b832e0-16be-4edb-a6ac-2fe8ff3f786b']

    cert_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.crt'
    key_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.key'
    importer = EMInfraImporter(cert_path=cert_path, key_path=key_path)

    # fetch assets, based on a list of uuids
    assets = importer.import_assets_from_webservice_by_uuids(input_uuids)

    # use the generated datamodel to create instances of OTL classes
    mast = PunctueleVerlichtingsmast()
    mast.naam = '031C9.T01'
    mast.toestand = 'in-gebruik'
    mast.assetId.identificator = '031C9.T01'
    mast.assetId.toegekendDoor = 'OTLMOW'
    mast.aantalArmen = '1'  # TODO getal, voor rekenen?
    mast.bevestigingToestellen.standaardMethode = 'paaltop-60mm'
    mast.leverancier = 'metalogalva'
    mast.dwarsdoorsnede = 'vierkant'
    mast.armlengte = '2'
    mast.masttype = 'MT'
    mast.isDraaibaar = False
    mast.masthoogte = 6
    mast.geometry = 'POINT Z (144094.1 165007.7 0)'

    hoortbij_mast1 = HoortBij()
    hoortbij_mast1.assetId.identificator = '031C9.T01-legacy'
    hoortbij_mast1.bronAssetId.identificator = '031C9.T01'
    hoortbij_mast1.doelAssetId.identificator = 'e8b4022a-00d6-4b01-9766-0e50ecfda150-bGdjOmluc3RhbGxhdGllI1ZWT1A'

    mast2 = PunctueleVerlichtingsmast()
    mast2.naam = '031C9.T02'
    mast2.toestand = 'in-gebruik'
    mast2.assetId.identificator = '031C9.T02'
    mast2.assetId.toegekendDoor = 'OTLMOW'
    mast2.aantalArmen = '1'  # TODO getal, voor rekenen?
    mast2.bevestigingToestellen.standaardMethode = 'paaltop-60mm'
    mast2.leverancier = 'metalogalva'
    mast2.dwarsdoorsnede = 'vierkant'
    mast2.armlengte = '3.2'
    mast2.masttype = 'MT'
    mast2.isDraaibaar = False
    mast2.masthoogte = 6
    mast2.geometry = 'POINT Z (144081.9 165015.4 0)'

    hoortbij_mast2 = HoortBij()  # TODO HoortBij kenmerk toevoegen
    hoortbij_mast2.assetId.identificator = '031C9.T02-legacy'
    hoortbij_mast2.bronAssetId.identificator = '031C9.T02'
    hoortbij_mast2.doelAssetId.identificator = '63b832e0-16be-4edb-a6ac-2fe8ff3f786b-bGdjOmluc3RhbGxhdGllI1ZWT1A'

    led1 = VerlichtingstoestelLED()
    led1.aantalTeVerlichtenRijstroken = 'R2'
    led1.lichtkleur = 'wit'
    led1.armatuurkleur = 'RAL 1023'
    led1.kleurTemperatuur = '4000'
    led1.verlichtingsNiveau = 'zr3'
    led1.heeftAntiVandalisme = False
    led1.lichtpuntHoogte = 'H06'
    led1.overhang = 'o+0.5'
    led1.isFaunavriendelijk = False
    led1.protector = 'vlak-glas'
    led1.verlichtGebied = 'punctuele-verlichting'
    led1.merk = 'Schreder'
    led1.modelnaam = 'andere'
    led1.systeemvermogen.waarde = 134
    led1.naam = '031C9.T01.LED'
    led1.toestand = 'in-gebruik'
    led1.assetId.identificator = '031C9.T01.LED'
    led1.assetId.toegekendDoor = 'OTLMOW'

    bevestigingsrelatie_led_mast1 = Bevestiging()
    bevestigingsrelatie_led_mast1.assetId.identificator = "031C9.T01-031C9.T01.LED"
    bevestigingsrelatie_led_mast1.bronAssetId.identificator = '031C9.T01'
    bevestigingsrelatie_led_mast1.doelAssetId.identificator = '031C9.T01.LED'

    led2 = VerlichtingstoestelLED()
    led2.aantalTeVerlichtenRijstroken = 'R2'
    led2.lichtkleur = 'wit'
    led2.armatuurkleur = 'RAL 1023'
    led2.kleurTemperatuur = '4000'
    led2.verlichtingsNiveau = 'zr3'
    led2.heeftAntiVandalisme = False
    led2.lichtpuntHoogte = 'H06'
    led2.overhang = 'o+0.5'
    led2.isFaunavriendelijk = False
    led2.protector = 'vlak-glas'
    led2.verlichtGebied = 'punctuele-verlichting'
    led2.merk = 'Schreder'
    led2.modelnaam = 'andere'
    led2.systeemvermogen.waarde = 134
    led2.naam = '031C9.T02.LED'
    led2.toestand = 'in-gebruik'
    led2.assetId.identificator = '031C9.T02.LED'
    led2.assetId.toegekendDoor = 'OTLMOW'

    bevestigingsrelatie_led_mast2 = Bevestiging()
    bevestigingsrelatie_led_mast2.assetId.identificator = "031C9.T02-031C9.T02.LED"
    bevestigingsrelatie_led_mast2.bronAssetId.identificator = '031C9.T02'
    bevestigingsrelatie_led_mast2.doelAssetId.identificator = '031C9.T02.LED'

    armatuurcontroller1 = Armatuurcontroller()
    armatuurcontroller1.merk = 'Dummydot'  # TODO extra attribuut
    armatuurcontroller1.naam = '031C9.T01.AMC'
    armatuurcontroller1.toestand = 'in-gebruik'
    armatuurcontroller1.assetId.identificator = '031C9.T01.AMC'
    armatuurcontroller1.assetId.toegekendDoor = 'OTLMOW'

    bevestigingsrelatie_led_amc1 = Bevestiging()
    bevestigingsrelatie_led_amc1.assetId.identificator = "031C9.T01.LED-031C9.T01.AMC"
    bevestigingsrelatie_led_amc1.bronAssetId.identificator = '031C9.T01.LED'
    bevestigingsrelatie_led_amc1.doelAssetId.identificator = '031C9.T01.AMC'

    armatuurcontroller2 = Armatuurcontroller()
    armatuurcontroller2.merk = 'Dummydot'  # TODO extra attribuut
    armatuurcontroller2.naam = '031C9.T02.AMC'
    armatuurcontroller2.toestand = 'in-gebruik'
    armatuurcontroller2.assetId.identificator = '031C9.T02.AMC'
    armatuurcontroller2.assetId.toegekendDoor = 'OTLMOW'

    bevestigingsrelatie_led_amc2 = Bevestiging()
    bevestigingsrelatie_led_amc2.assetId.identificator = "031C9.T02.LED-031C9.T02.AMC"
    bevestigingsrelatie_led_amc2.bronAssetId.identificator = '031C9.T02.LED'
    bevestigingsrelatie_led_amc2.doelAssetId.identificator = '031C9.T02.AMC'

    led_driver1 = LEDDriver()
    led_driver1.toestand = 'in-gebruik'
    led_driver1.assetId.identificator = '031C9.T01.leddriver'
    led_driver1.assetId.toegekendDoor = 'OTLMOW'

    sturingsrelatie_led_driver_led1 = Sturing()
    sturingsrelatie_led_driver_led1.assetId.identificator = '031C9.T01.LED-031C9.T01.leddriver-sturing'
    sturingsrelatie_led_driver_led1.bronAssetId.identificator = '031C9.T01.LED'
    sturingsrelatie_led_driver_led1.doelAssetId.identificator = '031C9.T01.leddriver'

    bevestigingsrelatie_led_driver_led1 = Bevestiging()
    bevestigingsrelatie_led_driver_led1.assetId.identificator = '031C9.T01.LED-031C9.T01.leddriver'
    bevestigingsrelatie_led_driver_led1.bronAssetId.identificator = '031C9.T01.LED'
    bevestigingsrelatie_led_driver_led1.doelAssetId.identificator = '031C9.T01.leddriver'

    led_driver2 = LEDDriver()
    led_driver2.toestand = 'in-gebruik'
    led_driver2.assetId.identificator = '031C9.T02.leddriver'
    led_driver2.assetId.toegekendDoor = 'OTLMOW'

    bevestigingsrelatie_led_driver_led2 = Bevestiging()
    bevestigingsrelatie_led_driver_led2.assetId.identificator = '031C9.T02.LED-031C9.T02.leddriver-sturing'
    bevestigingsrelatie_led_driver_led2.bronAssetId.identificator = '031C9.T02.LED'
    bevestigingsrelatie_led_driver_led2.doelAssetId.identificator = '031C9.T02.leddriver'

    sturingsrelatie_led_driver_led2 = Sturing()
    sturingsrelatie_led_driver_led2.assetId.identificator = '031C9.T02.LED-031C9.T02.leddriver'
    sturingsrelatie_led_driver_led2.bronAssetId.identificator = '031C9.T02.LED'
    sturingsrelatie_led_driver_led2.doelAssetId.identificator = '031C9.T02.leddriver'

    voedtaangestuurd_led_driver1_amc_1 = VoedtAangestuurd()
    voedtaangestuurd_led_driver1_amc_1.assetId.identificator = '031C9.T01.AMC-031C9.T01.leddriver'
    voedtaangestuurd_led_driver1_amc_1.bronAssetId.identificator = '031C9.T01.AMC'
    voedtaangestuurd_led_driver1_amc_1.doelAssetId.identificator = '031C9.T01.leddriver'

    voedtaangestuurd_led_driver2_amc_2 = VoedtAangestuurd()
    voedtaangestuurd_led_driver2_amc_2.assetId.identificator = '031C9.T02.AMC-031C9.T02.leddriver'
    voedtaangestuurd_led_driver2_amc_2.bronAssetId.identificator = '031C9.T02.AMC'
    voedtaangestuurd_led_driver2_amc_2.doelAssetId.identificator = '031C9.T02.leddriver'

    # vanuit stroomkring voedt aangestuurd gebruiken via montagekast

    lijst_otl_objecten = [mast, mast2, led1, led2, armatuurcontroller1, armatuurcontroller2, bevestigingsrelatie_led_mast1,
                          bevestigingsrelatie_led_mast2, bevestigingsrelatie_led_amc1, bevestigingsrelatie_led_amc2,
                          hoortbij_mast1, hoortbij_mast2, led_driver1, led_driver2, sturingsrelatie_led_driver_led1,
                          sturingsrelatie_led_driver_led2, bevestigingsrelatie_led_driver_led1,
                          bevestigingsrelatie_led_driver_led2, voedtaangestuurd_led_driver2_amc_2,
                          voedtaangestuurd_led_driver1_amc_1]
    lijst_otl_objecten.extend(assets)

    otl_facility.visualiser.show(lijst_otl_objecten)
