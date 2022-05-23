from pprint import pprint
from typing import List, Dict, Tuple, Any
from dataclasses import dataclass


@dataclass
class Edge:  # like a hallway
    node1: int  # id of first node
    node2: int  # id of second node
    length: int


def add_edge(edges, id1, id2, len):
    edge = Edge(id1, id2, len)
    edges[(id1, id2)] = edge
    edges[(id2, id1)] = edge


@dataclass
class Node:
    id: int
    paths: Dict[int, Tuple[
        List[Any], int]]  # PATHs and Total Lengths: map of node ID to tuple of (NODEs list and total length)
    edges: List[Edge]


def graph1():
    nodes = {}  # nodes by id

    # create nodes
    for id in range(1, 7):
        nodes[id] = Node(id, {}, [])

    # create edges (by node1, node2 ids)
    edges = {}
    add_edge(edges, 1, 2, 7)
    add_edge(edges, 1, 3, 9)
    add_edge(edges, 1, 6, 14)
    add_edge(edges, 2, 3, 10)
    add_edge(edges, 2, 4, 15)
    add_edge(edges, 3, 4, 11)
    add_edge(edges, 3, 6, 2)
    add_edge(edges, 4, 5, 6)
    add_edge(edges, 5, 6, 9)

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


def graph2():
    nodes = {}  # nodes by id

    # create nodes
    for id in range(1, 4):
        nodes[id] = Node(id, {}, [])

    # create edges (by node1, node2 ids)
    edges = {}
    add_edge(edges, 1, 2, 5)
    add_edge(edges, 1, 3, 2)
    add_edge(edges, 2, 3, 1)

    # create edges/links
    nodes[1].edges.append(edges[(1, 2)])
    nodes[1].edges.append(edges[(1, 3)])

    nodes[2].edges.append(edges[(2, 1)])
    nodes[2].edges.append(edges[(2, 3)])

    nodes[3].edges.append(edges[(3, 1)])
    nodes[3].edges.append(edges[(3, 2)])

    return nodes


def update_lengths(all_nodes, cur_path, edge, total_len):
    cur_node_id = cur_path[-1].id
    origin_node_id = cur_path[0].id

    target_node_id = edge.node1
    if target_node_id == cur_node_id:
        target_node_id = edge.node2
    target_node = all_nodes[target_node_id]

    total_len = total_len + edge.length
    print(f'update_lengths origin:{origin_node_id} current:{cur_node_id} targ:{target_node_id} total:{total_len}')
    if origin_node_id in target_node.paths and target_node.paths[origin_node_id][1] < total_len:
        return  # better path already found

    # store best path and continue...
    cur_path.append(target_node)
    path_ids = tuple(n.id for n in cur_path)
    target_node.paths[origin_node_id] = (path_ids, total_len)
    for e in target_node.edges:
        if e.node1 not in (cur_node_id, origin_node_id) and e.node2 not in (cur_node_id, origin_node_id):
            update_lengths(all_nodes, cur_path, e, total_len)

    cur_path.pop()


def dijkstra(all_nodes):
    for id in all_nodes:  # nodes by id
        for e in all_nodes[id].edges:
            update_lengths(all_nodes, [all_nodes[id]], e, 0)
            # update path n.id, edge


if __name__ == '__main__':
    g = graph1()
    dijkstra(g)
    pprint(g)
