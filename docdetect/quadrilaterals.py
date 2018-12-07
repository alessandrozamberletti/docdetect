# -*- coding: utf-8 -*-
import itertools


def find_quadrilaterals(intersections):
    graph = _build_graph(intersections)
    quadrilaterals = []
    for node in graph:
        _bounded_dfs(graph, node, quadrilaterals)
    return _quadrilaterals2coords(quadrilaterals, intersections)


def _quadrilaterals2coords(quadrilaterals, intersections):
    coords = []
    for quadrilateral in quadrilaterals:
        rect = []
        for node in quadrilateral:
            corner = next(corner['coords'] for corner in intersections if corner['id'] == node)
            rect.append(corner)
        coords.append(rect)
    return coords


def _build_graph(intersections):
    graph = {k['id']: [] for k in intersections}
    for i1, i2 in itertools.permutations(intersections, 2):
        if _common_line_exists(i1['lines'], i2['lines']):
            graph[i1['id']].append(i2['id'])
    return graph


def _common_line_exists(l1, l2):
    common_line = set(list(l1)) & set(list(l2))
    return True if common_line else False


def _bounded_dfs(neighbours, current_node, cycles, seen_nodes=[]):
    if current_node not in seen_nodes:
        seen_nodes.append(current_node)
        if len(seen_nodes) == 4:
            if seen_nodes[0] in neighbours[current_node]:
                cycles.append(seen_nodes.copy())
        else:
            for adj_node in neighbours[current_node]:
                _bounded_dfs(neighbours, adj_node, cycles, seen_nodes=seen_nodes)
        del seen_nodes[-1]
