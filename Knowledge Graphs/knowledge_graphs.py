import networkx as nx
import matplotlib.pyplot as plt

kg = nx.DiGraph()

kg.add_node("Alice")
kg.add_node("Python")
kg.add_node("Knowledge Graph")

kg.add_edge("Alice", "Python", relation="learns")
kg.add_edge("Python", "Knowledge Graph", relation="used_for")

for u, v, data in kg.edges(data=True):
    print(f"{u} --{data['relation']}--> {v}")

pos = nx.spring_layout(kg)
nx.draw(kg, pos, with_labels=True, node_size=3000)

edge_labels = nx.get_edge_attributes(kg, "relation")
nx.draw_networkx_edge_labels(kg, pos, edge_labels=edge_labels)

plt.show()
