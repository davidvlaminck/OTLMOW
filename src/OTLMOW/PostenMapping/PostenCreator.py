import os
from datetime import datetime

from OTLMOW.Loggers.AbstractLogger import AbstractLogger
from OTLMOW.Loggers.LogType import LogType
from OTLMOW.ModelGenerator.StringHelper import wrap_in_quotes
from OTLMOW.PostenMapping.PostenCollector import PostenCollector
from OTLMOW.PostenMapping.StandaardPost import StandaardPost


class PostenCreator:
    def __init__(self, logger: AbstractLogger, postenCollector: PostenCollector):
        self.logger = logger
        self.postenCollector = postenCollector
        self.logger.log("Created an instance of PostenCreator", LogType.INFO)
        self.datablock_lijst_import = []
        self.datablock_lijst = []

    def create_all_mappings(self):
        self.logger.log('started creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"), logType=LogType.INFO)
        self.postenCollector.collect()
        self.combine_mappings_and_posten()
        self.create_standaardposten()
        self.logger.log('finished creating model at ' + datetime.now().strftime("%d/%m/%Y %H:%M:%S"), logType=LogType.INFO)

    def create_standaardposten(self):
        for post in self.postenCollector.standaardposten:
            try:
                dataToWrite = self.create_datablock_from_post(post)
                if dataToWrite is None:
                    self.logger.log(f"Could not create a class for {post.nummer}", LogType.INFO)
                    pass
                if len(dataToWrite) == 0:
                    self.logger.log(f"Could not create a class for {post.nummer}", LogType.INFO)
                    pass
                self.writeToFile(post, dataToWrite)
                self.logger.log(f"Created a class for {post.nummer}", LogType.INFO)
                self.add_to_lijst(post)
            except BaseException as e:
                self.logger.log(str(e), LogType.ERROR)
                self.logger.log(f"Could not create a class for {post.nummer}", LogType.ERROR)
        self.create_lijst()

    def combine_mappings_and_posten(self):
        for post in self.postenCollector.standaardposten:
            mappings = self.postenCollector.find_mappings_by_postnummer(post.nummer)
            post.mappings = mappings

    def create_datablock_from_post(self, post: StandaardPost) -> [str]:
        datablock = ['# coding=utf-8',
                     "from OTLMOW.PostenMapping.StandaardPost import StandaardPost",
                     "from OTLMOW.PostenMapping.StandaardPostMapping import StandaardPostMapping",
                     "", "",
                     '# Generated with PostenCreator. To modify: extend, do not edit',
                     f"class Post{post.nummer.replace('.', '')}(StandaardPost):",
                     "    def __init__(self):",
                     "        super().__init__(",
                     f"            nummer='{post.nummer}',",
                     f"            beschrijving={wrap_in_quotes(post.beschrijving)},",
                     f"            meetstaateenheid='{post.meetstaateenheid}',",
                     "            mappings=[StandaardPostMapping("]

        for mapping in post.mappings:
            datablock.append(f"                typeURI={wrap_in_quotes(mapping.typeURI)},")
            datablock.append(f"                attribuutURI={wrap_in_quotes(mapping.attribuutURI)},")
            datablock.append(f"                dotnotatie={wrap_in_quotes(mapping.dotnotatie)},")
            datablock.append(f"                defaultWaarde={wrap_in_quotes(mapping.defaultWaarde)},")
            datablock.append(f"                range={wrap_in_quotes(mapping.range)},")
            datablock.append(f"                usagenote={wrap_in_quotes(mapping.usagenote)},")
            datablock.append(f"                isMeetstaatAttr={mapping.isMeetstaatAttr},")
            datablock.append(f"                isAltijdInTeVullen={mapping.isAltijdInTeVullen},")
            datablock.append(f"                isBasisMapping={mapping.isBasisMapping},")
            datablock.append(f"                mappingStatus={wrap_in_quotes(mapping.mappingStatus)},")
            datablock.append(f"                mappingOpmerking={wrap_in_quotes(mapping.mappingOpmerking)},")
            datablock.append(f"                standaardpostnummer='{mapping.standaardpostnummer}')")
            datablock.append(f'                , StandaardPostMapping(')

        datablock.pop(-1)
        datablock[-1] = datablock[-1] + '])'

        return datablock

    @staticmethod
    def writeToFile(post: StandaardPost, dataToWrite: [str]):
        base_dir = os.path.dirname(os.path.realpath(__file__))
        path = f"{base_dir}/../PostenMapping/Model/Post{post.nummer.replace('.', '')}.py"

        with open(path, "w", encoding='utf-8') as file:
            for line in dataToWrite:
                file.write(line + "\n")

    def add_to_lijst(self, post: StandaardPost):
        self.datablock_lijst_import.append(
            f"from OTLMOW.PostenMapping.Model.Post{post.nummer.replace('.', '')} import Post{post.nummer.replace('.', '')}")
        self.datablock_lijst.append(f"            '{post.nummer}': Post{post.nummer.replace('.', '')}(),")

    def create_lijst(self):
        datablock = []
        datablock.extend(self.datablock_lijst_import)
        datablock.append("")
        datablock.append("")
        datablock.append("class PostenLijst:")
        datablock.append("    def __init__(self):")
        datablock.append("        self.lijst = {")
        datablock.extend(self.datablock_lijst)
        datablock[-1] = datablock[-1][:-1]
        datablock.append("        }")

        base_dir = os.path.dirname(os.path.realpath(__file__))
        path = f"{base_dir}/../PostenMapping/PostenLijst.py"

        with open(path, "w", encoding='utf-8') as file:
            for line in datablock:
                file.write(line + "\n")
