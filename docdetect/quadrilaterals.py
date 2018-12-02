# -*- coding: utf-8 -*-
from docdetect.line_utils import lines_are_same


def find_quadrilaterals(intersections):
    graph = _build_graph(intersections)
    quadrilaterals = []
    for node in graph:
            _partial_dfs(graph, node, quadrilaterals)
    return _quadrilaterals2coords(quadrilaterals, intersections)


def _quadrilaterals2coords(quadrilaterals, intersections):
    coordinates = []
    for quadrilateral in quadrilaterals:
        rect = []
        for node in quadrilateral:
            corner = next(corner['coords'] for corner in intersections if corner['id'] == node)
            rect.append(corner)
        coordinates.append(rect)
    return coordinates


def _build_graph(corners):
    graph = {}
    for corner in corners:
        line1, line2 = corner['lines']
        graph[corner['id']] = []
        for corner1 in corners:
            if corner['coords'] == corner1['coords']:
                continue
            line21, line22 = corner1['lines']
            if lines_are_same(line1, line21) or \
                    lines_are_same(line1, line22) or \
                    lines_are_same(line2, line21) or \
                    lines_are_same(line2, line22):
                graph[corner['id']].append(corner1['id'])
    return graph


def _partial_dfs(neighbours, current_node, cycles, seen_nodes=[], cycle_length=4):
    if current_node not in seen_nodes:
        seen_nodes.append(current_node)
        if len(seen_nodes) == cycle_length:
            if seen_nodes[0] in neighbours[current_node]:
                cycles.append(seen_nodes.copy())
        else:
            for adj_node in neighbours[current_node]:
                _partial_dfs(neighbours, adj_node, cycles, seen_nodes=seen_nodes)
        del seen_nodes[-1]
