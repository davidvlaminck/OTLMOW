from random import choice

from IPython.display import display, HTML
from pyvis import network as net

from OTLMOW.OTLModel.Classes.Bevestiging import Bevestiging
from OTLMOW.OTLModel.Classes.HoortBij import HoortBij
from OTLMOW.OTLModel.Classes.NietDirectioneleRelatie import NietDirectioneleRelatie
from OTLMOW.OTLModel.Classes.RelatieObject import RelatieObject
from OTLMOW.OTLModel.Classes.Sturing import Sturing
from OTLMOW.OTLModel.Classes.Voedt import Voedt
from OTLMOW.OTLModel.Classes.VoedtAangestuurd import VoedtAangestuurd


class Visualiser:
    def __init__(self):
        self.colorlist = ["#E5E5E5", "#CCCCCC", "#B2B2B2", "#999999", "#808080", "#666666", "#4D4D4D", "#333333", "#E8E3E3",
                          "#EBE0E0", "#EDDEDE", "#F0DBDB", "#F2D9D9", "#F5D6D6", "#F7D4D4", "#FAD1D1", "#FCCFCF", "#FFCCCC",
                          "#D1C7C7", "#D6C2C2", "#DBBDBD", "#E0B8B8", "#E6B3B3", "#EBADAD", "#F0A8A8", "#F5A3A3", "#FA9E9E",
                          "#FF9999", "#BAABAB", "#C2A3A3", "#C99C9C", "#D19494", "#D98C8C", "#E08585", "#E87D7D", "#F07575",
                          "#F76E6E", "#FF6666", "#A38F8F", "#AD8585", "#B87A7A", "#C27070", "#CC6666", "#D65C5C", "#E05252",
                          "#EB4747", "#F53D3D", "#FF3333", "#8C7373", "#996666", "#A65959", "#B24D4D", "#BF4040", "#CC3333",
                          "#D92626", "#E61919", "#F20D0D", "#FF0000", "#705C5C", "#7A5252", "#854747", "#8F3D3D", "#993333",
                          "#A32929", "#AD1F1F", "#B81414", "#C20A0A", "#CC0000", "#544545", "#5C3D3D", "#633636", "#6B2E2E",
                          "#732626", "#7A1F1F", "#821717", "#8A0F0F", "#910808", "#990000", "#382E2E", "#3D2929", "#422424",
                          "#471F1F", "#4D1919", "#521414", "#570F0F", "#5C0A0A", "#610505", "#660000", "#E8E6E3", "#EBE6E0",
                          "#EDE6DE", "#F0E6DB", "#F2E6D9", "#F5E6D6", "#F7E6D4", "#FAE6D1", "#FCE6CF", "#FFE6CC", "#D1CCC7",
                          "#D6CCC2", "#DBCCBD", "#E0CCB8", "#E6CCB3", "#EBCCAD", "#F0CCA8", "#F5CCA3", "#FACC9E", "#FFCC99",
                          "#BAB2AB", "#C2B2A3", "#C9B29C", "#D1B294", "#D9B28C", "#E0B285", "#E8B27D", "#F0B275", "#F7B26E",
                          "#FFB266", "#A3998F", "#AD9985", "#B8997A", "#C29970", "#CC9966", "#D6995C", "#E09952", "#EB9947",
                          "#F5993D", "#FF9933", "#8C8073", "#998066", "#A68059", "#B2804D", "#BF8040", "#CC8033", "#D98026",
                          "#E68019", "#F2800D", "#FF8000", "#70665C", "#7A6652", "#856647", "#8F663D", "#996633", "#A36629",
                          "#AD661F", "#B86614", "#C2660A", "#CC6600", "#544C45", "#5C4C3D", "#634C36", "#6B4C2E", "#734C26",
                          "#7A4C1F", "#824C17", "#8A4C0F", "#914C08", "#994C00", "#38332E", "#3D3329", "#423324", "#47331F",
                          "#4D3319", "#523314", "#57330F", "#5C330A", "#613305", "#663300", "#E8E8E3", "#EBEBE0", "#EDEDDE",
                          "#F0F0DB", "#F2F2D9", "#F5F5D6", "#F7F7D4", "#FAFAD1", "#FCFCCF", "#FFFFCC", "#D1D1C7", "#D6D6C2",
                          "#DBDBBD", "#E0E0B8", "#E6E6B3", "#EBEBAD", "#F0F0A8", "#F5F5A3", "#FAFA9E", "#FFFF99", "#BABAAB",
                          "#C2C2A3", "#C9C99C", "#D1D194", "#D9D98C", "#E0E085", "#E8E87D", "#F0F075", "#F7F76E", "#FFFF66",
                          "#A3A38F", "#ADAD85", "#B8B87A", "#C2C270", "#CCCC66", "#D6D65C", "#E0E052", "#EBEB47", "#F5F53D",
                          "#FFFF33", "#8C8C73", "#999966", "#A6A659", "#B2B24D", "#BFBF40", "#CCCC33", "#D9D926", "#E5E619",
                          "#F2F20D", "#FFFF00", "#70705C", "#7A7A52", "#858547", "#8F8F3D", "#999933", "#A3A329", "#ADAD1F",
                          "#B8B814", "#C2C20A", "#CCCC00", "#545445", "#5C5C3D", "#636336", "#6B6B2E", "#737326", "#7A7A1F",
                          "#828217", "#8A8A0F", "#919108", "#999900", "#38382E", "#3D3D29", "#424224", "#47471F", "#4C4D19",
                          "#525214", "#57570F", "#5C5C0A", "#616105", "#666600", "#E6E8E3", "#E6EBE0", "#E6EDDE", "#E6F0DB",
                          "#E6F2D9", "#E6F5D6", "#E6F7D4", "#E6FAD1", "#E6FCCF", "#E6FFCC", "#CCD1C7", "#CCD6C2", "#CCDBBD",
                          "#CCE0B8", "#CCE6B3", "#CCEBAD", "#CCF0A8", "#CCF5A3", "#CCFA9E", "#CCFF99", "#B2BAAB", "#B2C2A3",
                          "#B2C99C", "#B2D194", "#B3D98C", "#B3E085", "#B3E87D", "#B3F075", "#B3F76E", "#B3FF66", "#99A38F",
                          "#99AD85", "#99B87A", "#99C270", "#99CC66", "#99D65C", "#99E052", "#99EB47", "#99F53D", "#99FF33",
                          "#808C73", "#809966", "#80A659", "#80B24D", "#80BF40", "#80CC33", "#80D926", "#80E619", "#80F20D",
                          "#80FF00", "#66705C", "#667A52", "#668547", "#668F3D", "#669933", "#66A329", "#66AD1F", "#66B814",
                          "#66C20A", "#66CC00", "#4C5445", "#4C5C3D", "#4D6336", "#4D6B2E", "#4D7326", "#4D7A1F", "#4D8217",
                          "#4D8A0F", "#4D9108", "#4D9900", "#33382E", "#333D29", "#334224", "#33471F", "#334D19", "#335214",
                          "#33570F", "#335C0A", "#336105", "#336600", "#E3E8E3", "#E0EBE0", "#DEEDDE", "#DBF0DB", "#D9F2D9",
                          "#D6F5D6", "#D4F7D4", "#D1FAD1", "#CFFCCF", "#CCFFCC", "#C7D1C7", "#C2D6C2", "#BDDBBD", "#B8E0B8",
                          "#B3E6B3", "#ADEBAD", "#A8F0A8", "#A3F5A3", "#9EFA9E", "#99FF99", "#ABBAAB", "#A3C2A3", "#9CC99C",
                          "#94D194", "#8CD98C", "#85E085", "#7DE87D", "#75F075", "#6EF76E", "#66FF66", "#8FA38F", "#85AD85",
                          "#7AB87A", "#70C270", "#66CC66", "#5CD65C", "#52E052", "#47EB47", "#3DF53D", "#33FF33", "#738C73",
                          "#669966", "#59A659", "#4DB24D", "#40BF40", "#33CC33", "#26D926", "#19E619", "#0DF20D", "#00FF00",
                          "#5C705C", "#527A52", "#478547", "#3D8F3D", "#339933", "#29A329", "#1FAD1F", "#14B814", "#0AC20A",
                          "#00CC00", "#455445", "#3D5C3D", "#366336", "#2E6B2E", "#267326", "#1F7A1F", "#178217", "#0F8A0F",
                          "#089108", "#009900", "#2E382E", "#293D29", "#244224", "#1F471F", "#194D19", "#145214", "#0F570F",
                          "#0A5C0A", "#056105", "#006600", "#E3E8E6", "#E0EBE6", "#DEEDE6", "#DBF0E6", "#D9F2E6", "#D6F5E6",
                          "#D4F7E6", "#D1FAE6", "#CFFCE6", "#CCFFE6", "#C7D1CC", "#C2D6CC", "#BDDBCC", "#B8E0CC", "#B3E6CC",
                          "#ADEBCC", "#A8F0CC", "#A3F5CC", "#9EFACC", "#99FFCC", "#ABBAB2", "#A3C2B2", "#9CC9B2", "#94D1B2",
                          "#8CD9B3", "#85E0B3", "#7DE8B3", "#75F0B3", "#6EF7B3", "#66FFB3", "#8FA399", "#85AD99", "#7AB899",
                          "#70C299", "#66CC99", "#5CD699", "#52E099", "#47EB99", "#3DF599", "#33FF99", "#738C80", "#669980",
                          "#59A680", "#4DB280", "#40BF80", "#33CC80", "#26D980", "#19E680", "#0DF280", "#00FF80", "#5C7066",
                          "#527A66", "#478566", "#3D8F66", "#339966", "#29A366", "#1FAD66", "#14B866", "#0AC266", "#00CC66",
                          "#45544C", "#3D5C4C", "#36634D", "#2E6B4D", "#26734D", "#1F7A4D", "#17824D", "#0F8A4D", "#08914D",
                          "#00994D", "#2E3833", "#293D33", "#244233", "#1F4733", "#194D33", "#145233", "#0F5733", "#0A5C33",
                          "#056133", "#006633", "#E3E8E8", "#E0EBEB", "#DEEDED", "#DBF0F0", "#D9F2F2", "#D6F5F5", "#D4F7F7",
                          "#D1FAFA", "#CFFCFC", "#CCFFFF", "#C7D1D1", "#C2D6D6", "#BDDBDB", "#B8E0E0", "#B3E6E6", "#ADEBEB",
                          "#A8F0F0", "#A3F5F5", "#9EFAFA", "#99FFFF", "#ABBABA", "#A3C2C2", "#9CC9C9", "#94D1D1", "#8CD9D9",
                          "#85E0E0", "#7DE8E8", "#75F0F0", "#6EF7F7", "#66FFFF", "#8FA3A3", "#85ADAD", "#7AB8B8", "#70C2C2",
                          "#66CCCC", "#5CD6D6", "#52E0E0", "#47EBEB", "#3DF5F5", "#33FFFF", "#738C8C", "#669999", "#59A6A6",
                          "#4DB2B2", "#40BFBF", "#33CCCC", "#26D9D9", "#19E5E6", "#0DF2F2", "#00FFFF", "#5C7070", "#527A7A",
                          "#478585", "#3D8F8F", "#339999", "#29A3A3", "#1FADAD", "#14B8B8", "#0AC2C2", "#00CCCC", "#455454",
                          "#3D5C5C", "#366363", "#2E6B6B", "#267373", "#1F7A7A", "#178282", "#0F8A8A", "#089191", "#009999",
                          "#2E3838", "#293D3D", "#244242", "#1F4747", "#194C4D", "#145252", "#0F5757", "#0A5C5C", "#056161",
                          "#006666", "#E3E6E8", "#E0E6EB", "#DEE6ED", "#DBE6F0", "#D9E6F2", "#D6E6F5", "#D4E5F7", "#D1E5FA",
                          "#CFE5FC", "#CCE5FF", "#C7CCD1", "#C2CCD6", "#BDCCDB", "#B8CCE0", "#B3CCE6", "#ADCCEB", "#A8CCF0",
                          "#A3CCF5", "#9ECCFA", "#99CCFF", "#ABB2BA", "#A3B2C2", "#9CB2C9", "#94B2D1", "#8CB2D9", "#85B2E0",
                          "#7DB2E8", "#75B2F0", "#6EB2F7", "#66B2FF", "#8F99A3", "#8599AD", "#7A99B8", "#7099C2", "#6699CC",
                          "#5C99D6", "#5299E0", "#4799EB", "#3D99F5", "#3399FF", "#737F8C", "#667F99", "#597FA6", "#4D7FB2",
                          "#407FBF", "#337FCC", "#267FD9", "#197FE6", "#0D7FF2", "#007FFF", "#5C6670", "#52667A", "#476685",
                          "#3D668F", "#336699", "#2966A3", "#1F66AD", "#1466B8", "#0A66C2", "#0066CC", "#454C54", "#3D4C5C",
                          "#364C63", "#2E4C6B", "#264C73", "#1F4C7A", "#174C82", "#0F4C8A", "#084C91", "#004C99", "#2E3338",
                          "#29333D", "#243342", "#1F3347", "#19334D", "#143352", "#0F3357", "#0A335C", "#053361", "#003366",
                          "#E3E3E8", "#E0E0EB", "#DEDEED", "#DBDBF0", "#D9D9F2", "#D6D6F5", "#D4D4F7", "#D1D1FA", "#CFCFFC",
                          "#CCCCFF", "#C7C7D1", "#C2C2D6", "#BDBDDB", "#B8B8E0", "#B3B3E6", "#ADADEB", "#A8A8F0", "#A3A3F5",
                          "#9E9EFA", "#9999FF", "#ABABBA", "#A3A3C2", "#9C9CC9", "#9494D1", "#8C8CD9", "#8585E0", "#7D7DE8",
                          "#7575F0", "#6E6EF7", "#6666FF", "#8F8FA3", "#8585AD", "#7A7AB8", "#7070C2", "#6666CC", "#5C5CD6",
                          "#5252E0", "#4747EB", "#3D3DF5", "#3333FF", "#73738C", "#666699", "#5959A6", "#4D4DB2", "#4040BF",
                          "#3333CC", "#2626D9", "#1919E6", "#0D0DF2", "#0000FF", "#5C5C70", "#52527A", "#474785", "#3D3D8F",
                          "#333399", "#2929A3", "#1F1FAD", "#1414B8", "#0A0AC2", "#0000CC", "#454554", "#3D3D5C", "#363663",
                          "#2E2E6B", "#262673", "#1F1F7A", "#171782", "#0F0F8A", "#080891", "#000099", "#2E2E38", "#29293D",
                          "#242442", "#1F1F47", "#19194D", "#141452", "#0F0F57", "#0A0A5C", "#050561", "#000066", "#E6E3E8",
                          "#E6E0EB", "#E6DEED", "#E6DBF0", "#E6D9F2", "#E6D6F5", "#E5D4F7", "#E5D1FA", "#E5CFFC", "#E5CCFF",
                          "#CCC7D1", "#CCC2D6", "#CCBDDB", "#CCB8E0", "#CCB3E6", "#CCADEB", "#CCA8F0", "#CCA3F5", "#CC9EFA",
                          "#CC99FF", "#B2ABBA", "#B2A3C2", "#B29CC9", "#B294D1", "#B28CD9", "#B285E0", "#B27DE8", "#B275F0",
                          "#B26EF7", "#B266FF", "#998FA3", "#9985AD", "#997AB8", "#9970C2", "#9966CC", "#995CD6", "#9952E0",
                          "#9947EB", "#993DF5", "#9933FF", "#7F738C", "#7F6699", "#7F59A6", "#7F4DB2", "#7F40BF", "#7F33CC",
                          "#7F26D9", "#7F19E6", "#7F0DF2", "#7F00FF", "#665C70", "#66527A", "#664785", "#663D8F", "#663399",
                          "#6629A3", "#661FAD", "#6614B8", "#660AC2", "#6600CC", "#4C4554", "#4C3D5C", "#4C3663", "#4C2E6B",
                          "#4C2673", "#4C1F7A", "#4C1782", "#4C0F8A", "#4C0891", "#4C0099", "#332E38", "#33293D", "#332442",
                          "#331F47", "#33194D", "#331452", "#330F57", "#330A5C", "#330561", "#330066", "#E8E3E8", "#EBE0EB",
                          "#EDDEED", "#F0DBF0", "#F2D9F2", "#F5D6F5", "#F7D4F7", "#FAD1FA", "#FCCFFC", "#FFCCFF", "#D1C7D1",
                          "#D6C2D6", "#DBBDDB", "#E0B8E0", "#E6B3E6", "#EBADEB", "#F0A8F0", "#F5A3F5", "#FA9EFA", "#FF99FF",
                          "#BAABBA", "#C2A3C2", "#C99CC9", "#D194D1", "#D98CD9", "#E085E0", "#E87DE8", "#F075F0", "#F76EF7",
                          "#FF66FF", "#A38FA3", "#AD85AD", "#B87AB8", "#C270C2", "#CC66CC", "#D65CD6", "#E052E0", "#EB47EB",
                          "#F53DF5", "#FF33FF", "#8C738C", "#996699", "#A659A6", "#B24DB2", "#BF40BF", "#CC33CC", "#D926D9",
                          "#E619E5", "#F20DF2", "#FF00FF", "#705C70", "#7A527A", "#854785", "#8F3D8F", "#993399", "#A329A3",
                          "#AD1FAD", "#B814B8", "#C20AC2", "#CC00CC", "#544554", "#5C3D5C", "#633663", "#6B2E6B", "#732673",
                          "#7A1F7A", "#821782", "#8A0F8A", "#910891", "#990099", "#382E38", "#3D293D", "#422442", "#471F47",
                          "#4D194C", "#521452", "#570F57", "#5C0A5C", "#610561", "#660066", "#E8E3E6", "#EBE0E6", "#EDDEE6",
                          "#F0DBE6", "#F2D9E6", "#F5D6E6", "#F7D4E6", "#FAD1E6", "#FCCFE6", "#FFCCE6", "#D1C7CC", "#D6C2CC",
                          "#DBBDCC", "#E0B8CC", "#E6B3CC", "#EBADCC", "#F0A8CC", "#F5A3CC", "#FA9ECC", "#FF99CC", "#BAABB2",
                          "#C2A3B2", "#C99CB2", "#D194B2", "#D98CB3", "#E085B3", "#E87DB3", "#F075B3", "#F76EB3", "#FF66B3",
                          "#A38F99", "#AD8599", "#B87A99", "#C27099", "#CC6699", "#D65C99", "#E05299", "#EB4799", "#F53D99",
                          "#FF3399", "#8C7380", "#996680", "#A65980", "#B24D80", "#BF4080", "#CC3380", "#D92680", "#E61980",
                          "#F20D80", "#FF0080", "#705C66", "#7A5266", "#854766", "#8F3D66", "#993366", "#A32966", "#AD1F66",
                          "#B81466", "#C20A66", "#CC0066", "#54454C", "#5C3D4C", "#63364D", "#6B2E4D", "#73264D", "#7A1F4D",
                          "#82174D", "#8A0F4D", "#91084D", "#99004D", "#382E33", "#3D2933", "#422433", "#471F33", "#4D1933",
                          "#521433", "#570F33", "#5C0A33", "#610533", "#660033"]
        self.colorDict = {}

    def show(self, list_of_objects):
        g = net.Network(height='100%', width='100%', heading='', directed=True)
        self.create_nodes(g, list_of_objects)
        self.create_edges(g, list_of_objects)
        g.show('example.html')
        display(HTML('example.html'))

    def create_nodes(self, g, list_of_objects):
        otl_objects = list(filter(lambda o: not isinstance(o, RelatieObject), list_of_objects))
        for otl_object in otl_objects:
            naam = otl_object.__class__.__name__ + '_' + otl_object.assetId.identificator
            if hasattr(otl_object, 'naam'):
                naam = otl_object.naam
            selected_color = self.random_color_if_not_in_dict(otl_object.typeURI)

            tooltip = self.get_tooltip(otl_object)

            g.add_node(otl_object.assetId.identificator,
                       label=naam,
                       size=20,
                       color=selected_color,
                       title=tooltip)

    def create_edges(self, g, list_of_objects):
        relaties = list(filter(lambda o: isinstance(o, RelatieObject), list_of_objects))
        otl_assets = list(filter(lambda o: not isinstance(o, RelatieObject), list_of_objects))
        asset_ids = list(map(lambda x: x.assetId.identificator, otl_assets))
        for relatie in relaties:
            if relatie.bronAssetId.identificator in asset_ids and relatie.doelAssetId.identificator in asset_ids:  # only display relations between assets that are displayed
                g.add_edge(source=relatie.bronAssetId.identificator,
                           to=relatie.doelAssetId.identificator,
                           color=self.map_relation_to_color(relatie),
                           width=2,
                           arrowsize=0.5)
                if isinstance(relatie, NietDirectioneleRelatie):
                    g.add_edge(to=relatie.bronAssetId.identificator,
                               source=relatie.doelAssetId.identificator,
                               color=self.map_relation_to_color(relatie),
                               width=2, arrowsize=0.5)

    @staticmethod
    def map_relation_to_color(relatie) -> str:
        relatie_color_dict = {
            'red': Voedt,
            'black': Bevestiging,
            'green': Sturing,
            'orange': HoortBij,
            'purple': VoedtAangestuurd}

        for k, v in relatie_color_dict.items():
            if isinstance(relatie, v):
                return k
        return 'brown'

    def random_color_if_not_in_dict(self, typeURI):
        if typeURI not in self.colorDict.keys():
            randomColor = choice(self.colorlist)
            while randomColor in self.colorDict.values():
                randomColor = choice(self.colorlist)
            self.colorDict[typeURI] = randomColor
        return self.colorDict[typeURI]

    @staticmethod
    def get_tooltip(otl_object):
        html = otl_object.info().replace('\n', '<br/>').replace(' ', '&nbsp;')
        return '<div style="font-family: monospace;"</div>' + html
