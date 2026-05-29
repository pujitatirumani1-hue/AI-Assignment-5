import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network
import pandas as pd
import os

os.makedirs("results", exist_ok=True)

students = pd.DataFrame([
    {"name": "Emma", "category": "Student"},
    {"name": "Liam", "category": "Student"},
    {"name": "Python", "category": "Skill"},
    {"name": "Machine Learning", "category": "Skill"},
    {"name": "Data Science", "category": "Domain"},
])

connections = pd.DataFrame([
    {"source": "Emma", "target": "Python", "relation": "learns"},
    {"source": "Liam", "target": "Machine Learning", "relation": "studies"},
    {"source": "Python", "target": "Data Science", "relation": "used_in"},
    {"source": "Machine Learning", "target": "Data Science", "relation": "applied_to"},
    {"source": "Emma", "target": "Liam", "relation": "collaborates_with"},
])

graph = nx.DiGraph()

for _, row in students.iterrows():
    graph.add_node(row["name"], category=row["category"])

for _, row in connections.iterrows():
    graph.add_edge(
        row["source"],
        row["target"],
        relation=row["relation"]
    )

print("Academic Knowledge Graph")
print("=" * 40)

print("\nEntities")
for node, data in graph.nodes(data=True):
    print(f"{node} ({data['category']})")

print("\nConnections")
for u, v, data in graph.edges(data=True):
    print(f"{u} --{data['relation']}--> {v}")

print("\nBetweenness Centrality")
centrality = nx.betweenness_centrality(graph)

for node, value in sorted(
    centrality.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(f"{node}: {value:.3f}")

nx.write_graphml(graph, "results/academic_graph.graphml")

colors = {
    "Student": "#66BB6A",
    "Skill": "#42A5F5",
    "Domain": "#FFA726"
}

node_colors = [
    colors.get(
        graph.nodes[n]["category"],
        "#BDBDBD"
    )
    for n in graph.nodes()
]

plt.figure(figsize=(9, 6))

pos = nx.kamada_kawai_layout(graph)

nx.draw(
    graph,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=2800,
    font_size=10,
    arrows=True
)

edge_labels = {
    (u, v): d["relation"]
    for u, v, d in graph.edges(data=True)
}

nx.draw_networkx_edge_labels(
    graph,
    pos,
    edge_labels=edge_labels
)

plt.title("Academic Knowledge Graph")
plt.savefig(
    "results/academic_graph.png",
    dpi=150
)
plt.close()

net = Network(
    height="700px",
    width="100%",
    directed=True
)

for node, data in graph.nodes(data=True):
    net.add_node(
        node,
        label=node,
        title=data["category"],
        color=colors.get(
            data["category"],
            "#BDBDBD"
        )
    )

for u, v, data in graph.edges(data=True):
    net.add_edge(
        u,
        v,
        label=data["relation"]
    )

net.write_html(
    "results/academic_graph.html"
)

print("\nFiles generated successfully!")
