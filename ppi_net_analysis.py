import csv
import networkx as nx
import warnings

ppi_data = open(,"r")
ppi_csv = csv.reader(ppi_data)
ppi_net = nx.Graph()

for row in ppi_csv:
    ppi_net.add_edge(row[0], row[2])


def operable():
    '''
    finds out if the condition can be used with the current data
    '''
def cond_satified():
    '''
    finds out if the attr matches the condition'''

def subset_network(subset_edges):
    '''
    returns a sub setted network with the given edges
    @subset_edges needs to be a list of with pairlist (or pairtuple) as elements
    '''
    new_g = nx.Graph()
    for edge in subset_edges:
        new_g.add_edge(*edge)
    return new_g

def get_nodes_with_attr(graph, attr, condition, value):
    '''
    returns all node meeting the condition and attr
    '''
    node_attr_dict = nx.get_nodes_attributes(graph)
    #find the key attr type
    attr_type = type(dict.keys()[1])
    node_list = []

    if operable( attr_type, condition):
        for node, attr in node_attr_dict:
            if cond_satified(attr, condition, value):
                node_list.append(node)
    else:
        warnings.warn("Incompatible condition and attr")
        
        
def degree_greater_than(greater_degree):
    '''
    returns all nodes greater than greater_degree
    '''
    return [(node,degree) for node, degree in ppi_net.degree().items() if degree\
        > greater_degree]

def degree_greater_than(lesser_degree):
 '''
    returns all nodes lesser than lesser_degree
    '''
    return [(node,degree) for node, degree in ppi_net.degree().items() if degree\
        > lesser_degree]

def degree_equal_to(equal_degree):
     '''
    returns all nodes equal to equal_degree 
    '''
    return [(node,degree) for node, degree in ppi_net.degree().items() if degree\
        > equal_degree]