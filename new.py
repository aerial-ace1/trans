import networkx as nx
import matplotlib.pyplot as plt


G=nx.Graph()
i=1
G.add_node(1,pos=(i,i),state = "Ram")
G.add_node(2,pos=(2,2))
G.add_node(3,pos=(1,0))
G.add_edge(1,2,weight="Shyam")
G.add_edge(1,3,weight=9.8)
pos=nx.get_node_attributes(G,'pos')
options = {
    'node_size': 5000,
    'width': 3,
}


nx.draw(G,pos, font_weight='bold',**options)
node_labels = nx.get_node_attributes(G,'state')
nx.draw_networkx_labels(G, pos labels = node_labels)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,edge_labels=labels)
plt.show()