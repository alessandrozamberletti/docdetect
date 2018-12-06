# -*- coding: utf-8 -*-
from docdetect.line_utils import lines_are_same


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
    graph = {}
    for intersection1 in intersections:
        line1, line2 = intersection1['lines']
        graph[intersection1['id']] = []
        for intersection2 in intersections:
            if intersection1['coords'] == intersection2['coords']:
                continue
            line21, line22 = intersection2['lines']
            if lines_are_same(line1, line21) or \
                    lines_are_same(line1, line22) or \
                    lines_are_same(line2, line21) or \
                    lines_are_same(line2, line22):
                graph[intersection1['id']].append(intersection2['id'])
    return graph


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
