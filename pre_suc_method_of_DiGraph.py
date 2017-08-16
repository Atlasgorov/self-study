import networkx as nx
import matplotlib.pyplot as plt
DG = nx.DiGraph()
DG.add_edges_from([(0,1),(1,0),(0,2),(2,3),(1,2)])
plt.ion()
nx.draw_networkx(DG)
plt.show()

print(list(nx.strongly_connected_components(DG)))
print('节点2的入度节点是：', DG.predecessors(2)）
print('节点1的出度节点是：', DG.successors(1))
