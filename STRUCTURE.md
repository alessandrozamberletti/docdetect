```python
import docdetect

rects = docdetect.find(im, use_mser=True)
```

```python
edges = detect_edges(im, use_mser=True) # threshold1, threshold2
lines = detect_lines(edges) # rho, theta, threshold
corners = find_corners(lines) # min_angle
graph = build_graph(corners)
quadrilaterals = dfs(graph) 

return quadrilaterals
```
