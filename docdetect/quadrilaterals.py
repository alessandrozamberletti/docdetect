# -*- coding: utf-8 -*-
import itertools


def find_quadrilaterals(intersections):
    graph = _build_graph(intersections)
    cycles = []
    [_bounded_dfs(graph, node, cycles) for node in graph]
    return _cycles2coords(cycles, intersections)


def _cycles2coords(cycles, intersections):
    return [[_node2coords(node, intersections) for node in quadrilateral] for quadrilateral in cycles]


def _node2coords(node, intersections):
    return next(corner['coords'] for corner in intersections if corner['id'] == node)


def _build_graph(intersections):
    graph = {k['id']: [] for k in intersections}
    for i1, i2 in itertools.permutations(intersections, 2):
        if _common_line_exists(i1['lines'], i2['lines']):
            graph[i1['id']].append(i2['id'])
    return graph


def _common_line_exists(l1, l2):
    common_line = set(list(l1)) & set(list(l2))
    return True if common_line else False


def _bounded_dfs(neighbours, current, cycles, seen=[]):
    if current in seen:
        return
    seen.append(current)
    if len(seen) == 4:
        _add_cycle(current, neighbours, seen, cycles)
    else:
        [_bounded_dfs(neighbours, neighbour, cycles, seen=seen) for neighbour in neighbours[current]]
    del seen[-1]


def _add_cycle(current, neighbours, seen, cycles):
    if seen[0] in neighbours[current]:
        cycles.append(seen.copy())
