import networkx as nx
from pyvis import network as net
from IPython.core.display import display, HTML
import dash

from OTLModel.Classes.Bevestiging import Bevestiging
from OTLModel.Classes.RelatieObject import RelatieObject
from OTLModel.Classes.Sturing import Sturing
from OTLModel.Classes.Voedt import Voedt


class Visualiser:
    def show(self, list_of_objects):
        g = net.Network(height='550px', width='100%', heading='')
        self.create_nodes(g, list_of_objects)
        self.create_edges(g, list_of_objects)
        g.show('example.html')
        # self.add_to_html(g)
        display(HTML('example.html'))

    def create_nodes(self, g, list_of_objects):
        otl_objects = list(filter(lambda o: not isinstance(o, RelatieObject), list_of_objects))
        for otl_object in otl_objects:
            g.add_node(otl_object.assetId.identificator, label=otl_object.naam)

    def create_edges(self, g, list_of_objects):
        relaties = list(filter(lambda o: isinstance(o, RelatieObject), list_of_objects))
        for relatie in relaties:

            g.add_edge(source=relatie.bronAssetId.identificator,
                       to=relatie.doelAssetId.identificator,
                       color=self.map_relation_to_color(relatie))

    def map_relation_to_color(self, relatie):
        if isinstance(relatie, Voedt):
            return 'red'
        if isinstance(relatie, Bevestiging):
            return 'black'
        if isinstance(relatie, Sturing):
            return 'green'
        if isinstance(relatie, HoortBij):
            return 'orange'

    def add_to_html(self, g):
        f = g.html.find('"interaction": {')
        insert_text='"click":{"event":console.log("working")},'
        g.html = g.html[:f] + insert_text + g.html[f:]
