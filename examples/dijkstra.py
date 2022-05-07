from typing import List
from typing import Dict
from dataclasses import dataclass


@dataclass
class Edge:         # like a hallway
    node1: int      # id of first node
    node2: int      # id of second node
    length: int

def add_edge(edges, id1, id2, len):
    edge = Edge(id1, id2, len)
    edges[(id1, id2)] = edge
    edges[(id2, id1)] = edge

@dataclass
class Node:
    id: int
    lengths: Dict[int, int]       # map of node ID to shortest length so far
    edges: List[Edge]

def graph1(): 
    nodes = {}      # nodes by id

    # create nodes
    for id in range(1, 7):
        nodes[id] = Node(id, {}, [])

    # create edges (by node1, node2 ids)
    edges = {}
    add_edge(edges, 1, 2, 7)
    add_edge(edges,1, 3, 9)
    add_edge(edges,1, 6, 14)
    add_edge(edges,2, 3, 10)
    add_edge(edges,2, 4, 15)
    add_edge(edges,3, 4, 11)
    add_edge(edges,3, 6, 2)
    add_edge(edges,4, 5, 6)
    add_edge(edges,5, 6, 9)
    
    # create edges/links
    nodes[1].edges.append(edges[(1, 2)])
    nodes[1].edges.append(edges[(1, 3)])
    nodes[1].edges.append(edges[(1, 6)])

    nodes[2].edges.append(edges[(2, 1)])
    nodes[2].edges.append(edges[(2, 3)])
    nodes[2].edges.append(edges[(2, 4)])

    nodes[3].edges.append(edges[(3, 1)])
    nodes[3].edges.append(edges[(3, 2)])
    nodes[3].edges.append(edges[(3, 4)])
    nodes[3].edges.append(edges[(3, 6)])

    nodes[4].edges.append(edges[(4, 2)])
    nodes[4].edges.append(edges[(4, 3)])
    nodes[4].edges.append(edges[(4, 5)])

    nodes[5].edges.append(edges[(5, 4)])
    nodes[5].edges.append(edges[(5, 6)])

    nodes[6].edges.append(edges[(6, 1)])
    nodes[6].edges.append(edges[(6, 3)])
    nodes[6].edges.append(edges[(6, 5)])

    return nodes

def update_lengths (nodes, origin_node_id, cur_node_id, edge, total_len):
    total_len = total_len + edge.length
    target_node_id = edge.node1
    if target_node_id == cur_node_id: 
        target_node_id = edge.node2

    target_node = nodes[target_node_id]
    if origin_node_id in target_node.lengths and target_node.lengths[origin_node_id] < total_len:
        return  # better path already found

    # store best path and continue...
    target_node.lengths[origin_node_id] = total_len
    for e in target_node.edges:
        update_lengths(nodes, origin_node_id, target_node.id, e, total_len)


def dijkstra (nodes): 
    for id in nodes:        # nodes by id
        for e in nodes[id].edges:
            update_lengths(nodes, id, id, e, 0)
            # update path n.id, edge

if __name__ == '__main__':
    g = graph1()
    dijkstra(g)
    print(g)
        