from OTLMOW.Facility.EMInfraImporter import EMInfraImporter
from OTLMOW.Facility.OTLFacility import OTLFacility
from OTLMOW.Loggers.ConsoleLogger import ConsoleLogger
from OTLMOW.Loggers.LoggerCollection import LoggerCollection
from OTLMOW.Loggers.TxtLogger import TxtLogger
from OTLMOW.OTLModel.Classes.Armatuurcontroller import Armatuurcontroller
from OTLMOW.OTLModel.Classes.Bevestiging import Bevestiging
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.LEDDriver import LEDDriver
from OTLMOW.OTLModel.Classes.Laagspanningsbord import Laagspanningsbord
from OTLMOW.OTLModel.Classes.Montagekast import Montagekast
from OTLMOW.OTLModel.Classes.PunctueleVerlichtingsmast import PunctueleVerlichtingsmast
from OTLMOW.OTLModel.Classes.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from OTLMOW.OTLModel.Classes.Stroomkring import Stroomkring
from OTLMOW.OTLModel.Classes.Sturing import Sturing
from OTLMOW.OTLModel.Classes.VerlichtingstoestelLED import VerlichtingstoestelLED
from OTLMOW.OTLModel.Classes.Voedt import Voedt
from OTLMOW.OTLModel.Classes.VoedtAangestuurd import VoedtAangestuurd
from OTLMOW.OTLModel.Classes.Wegkantkast import Wegkantkast
from OTLMOW.OTLModel.Datatypes.DtcAdres import DtcAdresWaarden
from OTLMOW.OTLModel.Datatypes.DtcDocument import DtcDocumentWaarden, DtcDocument

if __name__ == '__main__':
    logger = LoggerCollection([
        TxtLogger(r'C:\temp\pythonLogging\pythonlog.txt'),
        ConsoleLogger()])
    otl_facility = OTLFacility(logger, enable_relation_features=True)

    # add EM-Infra assets through API
    input_uuids = ['e8b4022a-00d6-4b01-9766-0e50ecfda150', '63b832e0-16be-4edb-a6ac-2fe8ff3f786b',
                   '0a1d21eb-f0d7-4d6d-8778-67d38167c10b']

    cert_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.crt'
    key_path = r'C:\resources\datamanager_eminfra_prd.awv.vlaanderen.be.key'
    importer = EMInfraImporter(cert_path=cert_path, key_path=key_path)

    # fetch assets, based on a list of uuids
    assets = importer.import_assets_from_webservice_by_uuids(input_uuids)

    hoortbij_legacy_VVOPgroep1 = otl_facility.relatie_creator.create_relation(
        bron=next(a for a in assets if a.assetId.identificator[0:36] == 'e8b4022a-00d6-4b01-9766-0e50ecfda150'),
        doel=next(a for a in assets if a.assetId.identificator[0:36] == '0a1d21eb-f0d7-4d6d-8778-67d38167c10b'),
        relatie=HoortBij)

    hoortbij_legacy_VVOPgroep2 = otl_facility.relatie_creator.create_relation(
        bron=next(a for a in assets if a.assetId.identificator[
                                       0:36] == '63b832e0-16be-4edb-a6ac-2fe8ff3f786b'),
        doel=next(a for a in assets if a.assetId.identificator[
                                       0:36] == '0a1d21eb-f0d7-4d6d-8778-67d38167c10b'),
        relatie=HoortBij)

    # use the generated datamodel to create instances of OTL classes
    mast = PunctueleVerlichtingsmast()
    mast.naam = '031C9.T01'
    mast.toestand = 'in-gebruik'
    mast.assetId.identificator = '031C9.T01'
    mast.assetId.toegekendDoor = 'OTLMOW'
    mast.aantalArmen = '1'  # TODO getal, voor rekenen?
    mast.bevestigingToestellen[0].standaardMethode = 'paaltop-60mm'
    mast.leverancier = 'metalogalva'
    mast.dwarsdoorsnede = 'vierkant'
    mast.armlengte = '2'
    mast.masttype = 'MT'
    mast.isDraaibaar = False
    mast.masthoogte = 6
    mast.geometry = 'POINT Z (144094.1 165007.7 0)'

    hoortbij_mast1 = otl_facility.relatie_creator.create_relation(bron=mast,
                                                                  doel=next(a for a in assets if a.assetId.identificator[
                                                                                                 0:36] == 'e8b4022a-00d6-4b01-9766-0e50ecfda150'),
                                                                  relatie=HoortBij)

    mast2 = PunctueleVerlichtingsmast()
    mast2.naam = '031C9.T02'
    mast2.toestand = 'in-gebruik'
    mast2.assetId.identificator = '031C9.T02'
    mast2.assetId.toegekendDoor = 'OTLMOW'
    mast2.aantalArmen = '1'  # TODO getal, voor rekenen?
    mast2.bevestigingToestellen[0].standaardMethode = 'paaltop-60mm'
    mast2.leverancier = 'metalogalva'
    mast2.dwarsdoorsnede = 'vierkant'
    mast2.armlengte = '3.2'
    mast2.masttype = 'MT'
    mast2.isDraaibaar = False
    mast2.masthoogte = 6
    mast2.geometry = 'POINT Z (144081.9 165015.4 0)'

    # TODO HoortBij kenmerk toevoegen
    hoortbij_mast2 = otl_facility.relatie_creator.create_relation(bron=mast2,
                                                                  doel=next(a for a in assets if a.assetId.identificator[
                                                                                                 0:36] == '63b832e0-16be-4edb-a6ac-2fe8ff3f786b'),
                                                                  relatie=HoortBij)

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

    bevestiging_led_mast1 = otl_facility.relatie_creator.create_relation(bron=mast, doel=led1, relatie=Bevestiging)

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

    bevestiging_led_mast2 = otl_facility.relatie_creator.create_relation(bron=mast2, doel=led2, relatie=Bevestiging)

    armatuurcontroller1 = Armatuurcontroller()
    armatuurcontroller1.merk = 'Dummydot'  # TODO extra attribuut
    armatuurcontroller1.naam = '031C9.T01.AMC'
    armatuurcontroller1.toestand = 'in-gebruik'
    armatuurcontroller1.assetId.identificator = '031C9.T01.AMC'
    armatuurcontroller1.assetId.toegekendDoor = 'OTLMOW'

    bevestiging_led_amc1 = otl_facility.relatie_creator.create_relation(bron=led1, doel=armatuurcontroller1, relatie=Bevestiging)

    armatuurcontroller2 = Armatuurcontroller()
    armatuurcontroller2.merk = 'Dummydot'  # TODO extra attribuut
    armatuurcontroller2.naam = '031C9.T02.AMC'
    armatuurcontroller2.toestand = 'in-gebruik'
    armatuurcontroller2.assetId.identificator = '031C9.T02.AMC'
    armatuurcontroller2.assetId.toegekendDoor = 'OTLMOW'

    bevestiging_led_amc2 = otl_facility.relatie_creator.create_relation(bron=led2, doel=armatuurcontroller2, relatie=Bevestiging)

    led_driver1 = LEDDriver()
    led_driver1.toestand = 'in-gebruik'
    led_driver1.assetId.identificator = '031C9.T01.leddriver'
    led_driver1.assetId.toegekendDoor = 'OTLMOW'

    sturingsrelatie_led_driver_led1 = otl_facility.relatie_creator.create_relation(bron=led_driver1, doel=led1, relatie=Sturing)

    bevestiging_led_driver_led1 = otl_facility.relatie_creator.create_relation(bron=led_driver1, doel=led1, relatie=Bevestiging)

    led_driver2 = LEDDriver()
    led_driver2.toestand = 'in-gebruik'
    led_driver2.assetId.identificator = '031C9.T02.leddriver'
    led_driver2.assetId.toegekendDoor = 'OTLMOW'

    sturingsrelatie_led_driver_led2 = otl_facility.relatie_creator.create_relation(bron=led_driver2, doel=led2, relatie=Sturing)

    bevestiging_led_driver_led2 = otl_facility.relatie_creator.create_relation(bron=led_driver2, doel=led2, relatie=Bevestiging)

    voedtaangestuurd_led_driver1_amc_1 = otl_facility.relatie_creator.create_relation(bron=armatuurcontroller1, doel=led_driver1,
                                                                                      relatie=VoedtAangestuurd)

    voedtaangestuurd_led_driver2_amc_2 = otl_facility.relatie_creator.create_relation(bron=armatuurcontroller2, doel=led_driver2,
                                                                                      relatie=VoedtAangestuurd)

    montagekast1 = Montagekast()
    montagekast1.toestand = 'in-gebruik'
    montagekast1.opstelhoogte = 0.5
    montagekast1.assetId.identificator = '031C9.T01.mkast'
    montagekast1.assetId.toegekendDoor = 'OTLMOW'

    montagekast2 = Montagekast()
    montagekast2.toestand = 'in-gebruik'
    montagekast2.opstelhoogte = 0.5
    montagekast2.assetId.identificator = '031C9.T02.mkast'
    montagekast2.assetId.toegekendDoor = 'OTLMOW'

    # bevestiging_montagekast2_mast2 = otl_facility.relatie_creator.create_relation(bron=mast2, doel=montagekast2, relatie=Bevestiging)  TODO niet mogelijk in huidige model

    # TODO dit moet VoedtAangestuurd worden?
    voedt_montagekast1_amc1 = otl_facility.relatie_creator.create_relation(bron=montagekast1, doel=armatuurcontroller1,
                                                                           relatie=Voedt)

    voedt_montagekast2_amc2 = otl_facility.relatie_creator.create_relation(bron=montagekast2, doel=armatuurcontroller2,
                                                                           relatie=Voedt)

    str = Stroomkring()
    str.toestand = 'in-gebruik'
    str.assetId.identificator = '031C9.str'
    str.assetId.toegekendDoor = 'OTLMOW'

    voedt_str_montagekast1 = otl_facility.relatie_creator.create_relation(bron=str, doel=montagekast1, relatie=Voedt)
    voedt_str_montagekast2 = otl_facility.relatie_creator.create_relation(bron=str, doel=montagekast2, relatie=Voedt)

    lsb = Laagspanningsbord()
    lsb.toestand = 'in-gebruik'
    lsb.assetId.identificator = '031C9.lsb'
    lsb.assetId.toegekendDoor = 'OTLMOW'
    lsb.vermogen.waarde = 40

    bevestiging_lsb_str = otl_facility.relatie_creator.create_relation(bron=lsb, doel=str, relatie=Bevestiging)

    kast = Wegkantkast()
    kast.toestand = 'in-gebruik'
    kast.assetId.identificator = '031C9.kast'
    kast.assetId.toegekendDoor = 'OTLMOW'
    kast.adres.postcode = "1600"
    kast.adres.gemeente = 'sint-Pieters-Leeuw'
    kast.adres.straatnaam = 'Bergensesteenweg'
    kast.adres.huisnummer = '206'

    bevestiging_kast_lsb = otl_facility.relatie_creator.create_relation(bron=kast, doel=lsb, relatie=Bevestiging)

    verkeersbord11 = RetroreflecterendVerkeersbord()
    verkeersbord11.toestand = 'in-gebruik'
    verkeersbord11.assetId.identificator = '031C9.T01.bord1'
    verkeersbord11.assetId.toegekendDoor = 'OTLMOW'
    # verkeersbord11.merk = 'Trafiroad' TODO keuzelijst heeft geen merken
    verkeersbord11.oppervlakte = 0.5
    verkeersbord11.opstelhoogte = 2.5
    verkeersbord11.afmeting.vierhoekig.breedte.waarde = 70
    verkeersbord11.afmeting.vierhoekig.hoogte.waarde = 70
    verkeersbord11.grootteorde = 'klein'
    verkeersbord11.afwerkingsgraad = 'volledig-afgewerkt'
    verkeersbord11.kleurAchterkant.waarde = '7043'
    verkeersbord11.afbeelding[0].uri = 'https://wegcode.be/images/stories/verkeerstekens/F/F49.png'

    verkeersbord12 = RetroreflecterendVerkeersbord()
    verkeersbord12.toestand = 'in-gebruik'
    verkeersbord12.assetId.identificator = '031C9.T01.bord2'
    verkeersbord12.assetId.toegekendDoor = 'OTLMOW'
    verkeersbord12.oppervlakte = 0.5
    verkeersbord12.opstelhoogte = 6
    verkeersbord12.afmeting.vierhoekig.breedte.waarde = 70
    verkeersbord12.afmeting.vierhoekig.hoogte.waarde = 70
    verkeersbord12.grootteorde = 'klein'
    verkeersbord12.afwerkingsgraad = 'volledig-afgewerkt'
    verkeersbord12.kleurAchterkant.waarde = '7043'
    verkeersbord12.afbeelding[0].uri = 'https://wegcode.be/images/stories/verkeerstekens/F/F49.png'
    
    verkeersbord21 = RetroreflecterendVerkeersbord()
    verkeersbord21.toestand = 'in-gebruik'
    verkeersbord21.assetId.identificator = '031C9.T02.bord1'
    verkeersbord21.assetId.toegekendDoor = 'OTLMOW'
    verkeersbord21.oppervlakte = 0.5
    verkeersbord21.opstelhoogte = 2.5
    verkeersbord21.afmeting.vierhoekig.breedte.waarde = 70
    verkeersbord21.afmeting.vierhoekig.hoogte.waarde = 70
    verkeersbord21.grootteorde = 'klein'
    verkeersbord21.afwerkingsgraad = 'volledig-afgewerkt'
    verkeersbord21.kleurAchterkant.waarde = '7043'
    verkeersbord21.afbeelding[0].uri = 'https://wegcode.be/images/stories/verkeerstekens/F/F49.png'
    
    verkeersbord22 = RetroreflecterendVerkeersbord()
    verkeersbord22.toestand = 'in-gebruik'
    verkeersbord22.assetId.identificator = '031C9.T02.bord2'
    verkeersbord22.assetId.toegekendDoor = 'OTLMOW'
    verkeersbord22.oppervlakte = 0.5
    verkeersbord22.opstelhoogte = 6
    verkeersbord22.afmeting.vierhoekig.breedte.waarde = 70
    verkeersbord22.afmeting.vierhoekig.hoogte.waarde = 70
    verkeersbord22.grootteorde = 'klein'
    verkeersbord22.afwerkingsgraad = 'volledig-afgewerkt'
    verkeersbord22.kleurAchterkant.waarde = '7043'
    verkeersbord22.afbeelding[0].uri = 'https://wegcode.be/images/stories/verkeerstekens/F/F49.png'

    bevestiging_mast_bord11 = otl_facility.relatie_creator.create_relation(bron=mast, doel=verkeersbord11, relatie=Bevestiging)
    bevestiging_mast_bord12 = otl_facility.relatie_creator.create_relation(bron=mast, doel=verkeersbord12, relatie=Bevestiging)
    bevestiging_mast_bord21 = otl_facility.relatie_creator.create_relation(bron=mast2, doel=verkeersbord21, relatie=Bevestiging)
    bevestiging_mast_bord22 = otl_facility.relatie_creator.create_relation(bron=mast2, doel=verkeersbord22, relatie=Bevestiging)

    lijst_otl_objecten = [mast, mast2, led1, led2, armatuurcontroller1, armatuurcontroller2, bevestiging_led_mast1,
                          bevestiging_led_mast2, bevestiging_led_amc1, bevestiging_led_amc2,
                          hoortbij_mast1, hoortbij_mast2, led_driver1, led_driver2, sturingsrelatie_led_driver_led1,
                          sturingsrelatie_led_driver_led2, bevestiging_led_driver_led1,
                          bevestiging_led_driver_led2, voedtaangestuurd_led_driver2_amc_2,
                          voedtaangestuurd_led_driver1_amc_1, hoortbij_legacy_VVOPgroep1, hoortbij_legacy_VVOPgroep2,
                          montagekast1, montagekast2, voedt_montagekast1_amc1, voedt_montagekast2_amc2, str,
                          voedt_str_montagekast1, voedt_str_montagekast2, lsb, bevestiging_lsb_str, kast, bevestiging_kast_lsb,
                          verkeersbord11, verkeersbord12, verkeersbord21, verkeersbord22,
                          bevestiging_mast_bord11, bevestiging_mast_bord12, bevestiging_mast_bord21, bevestiging_mast_bord22]
    lijst_otl_objecten.extend(assets)

    otl_facility.visualiser.show(lijst_otl_objecten)
