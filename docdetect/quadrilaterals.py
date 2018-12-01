# -*- coding: utf-8 -*-
from docdetect.line_utils import lines_are_same


def find_quadrilaterals(corners):
    graph = _build_graph(corners)
    quadrilaterals = []
    for node in graph:
            _partial_dfs(graph, node, quadrilaterals)
    return _cycle2coords(quadrilaterals, corners)


def _cycle2coords(cycles, corners):
    coords = []
    for k1 in cycles:
        rect = []
        for node in k1:
            for intersection in corners:
                if intersection[0] == node:
                    x0 = intersection[-2]
                    y0 = intersection[-1]
                    rect.append((x0, y0))
        coords.append(rect)
    return coords


def _build_graph(corners):
    graph = {}
    for corner in corners:
        line1 = corner[-4]
        line2 = corner[-3]
        x0 = corner[-2]
        y0 = corner[-1]
        graph[corner[0]] = []
        for corner1 in corners:
            if x0 == corner1[-2] and y0 == corner1[-1]:
                continue
            line21 = corner1[-4]
            line22 = corner1[-3]
            if lines_are_same(line1, line21) or \
                    lines_are_same(line1, line22) or \
                    lines_are_same(line2, line21) or \
                    lines_are_same(line2, line22):
                graph[corner[0]].append(corner1[0])
    return graph


def _partial_dfs(neighbours, current_node, cycles, seen_nodes=[], cycle_length=4):
    if current_node not in seen_nodes:
        seen_nodes.append(current_node)
        if len(seen_nodes) == cycle_length and seen_nodes[0] in neighbours[current_node]:
                cycles.append(seen_nodes.copy())
        else:
            for adj_node in neighbours[current_node]:
                _partial_dfs(neighbours, adj_node, cycles, seen_nodes=seen_nodes)
        del seen_nodes[-1]
