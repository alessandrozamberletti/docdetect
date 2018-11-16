# -*- coding: utf-8 -*-
def find_quadrilaterals(corners):
    graph = build_graph(corners)
    quadrilaterals = []
    if len(graph) != 0:
        dfs_partial(graph, 0, quadrilaterals)
    return cycle2coords(quadrilaterals, corners)


def cycle2coords(cycles, corners):
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


def build_graph(corners):
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


def dfs(neighbours, current_node, cycles, seen_nodes=[], cycle_length=4):
    if current_node in seen_nodes:
        if len(seen_nodes) - seen_nodes.index(current_node) == cycle_length:
            cycles.append(seen_nodes[seen_nodes.index(current_node):].copy())
        return
    seen_nodes.append(current_node)
    for adj_node in neighbours[current_node]:
        dfs(neighbours, adj_node, cycles, seen_nodes=seen_nodes)
    del seen_nodes[-1]


def dfs_partial(neighbours, current_node, cycles, seen_nodes=[], cycle_length=4):
    if current_node not in seen_nodes:
        seen_nodes.append(current_node)
        if len(seen_nodes) == cycle_length:
            if seen_nodes[0] in neighbours[current_node]:
                cycles.append(seen_nodes.copy())
        else:
            for adj_node in neighbours[current_node]:
                dfs_partial(neighbours, adj_node, cycles, seen_nodes=seen_nodes)
        del seen_nodes[-1]


def lines_are_same(line1, line2):
    return line1 == line2
