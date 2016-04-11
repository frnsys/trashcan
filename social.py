import networkx as nx
from enum import IntEnum


class Relation(IntEnum):
    familial = 0
    friend = 1
    enemy = 2
    professional = 3
    romantic = 4


class Social():
    """a social network between people.
    consists of two components:
    an undirected relationship graph and
    a directed influence graph
    """
    def __init__(self):
        self.relations = nx.Graph()
        self.influence = nx.DiGraph()

    def relate(self, person_a, person_b, relationship):
        self.relations.add_nodes_from([person_a, person_b])
        data = self.relations.get_edge_data(person_a, person_b)
        if data is None:
            data = {'relations': set()}
        data['relations'].add(relationship)
        self.relations.add_edge(person_a, person_b, **data)

    def influence(self, person_a, person_b, influence):
        self.influence.add_nodes_from([person_a, person_b])
        self.influence.add_edge(person_a, person_b, influence=influence)
