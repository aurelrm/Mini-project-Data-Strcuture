import random
import networkx as nx 
import matplotlib.pyplot as plt

def file_to_data(file_name):
    my_file = open(file_name, "r")
    mat = my_file.readline().split(";")
    my_file.close()

    data = []
    for element in mat:
        data.append(element.split())

    
    return data

def display_graph(data):

    G = nx.Graph()
    print(data)
    for element in data:
       
        G.add_edge(element[0], element[1], weight = element[2])
    
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
    nx.draw(G,pos,with_labels= True)
    plt.show()

def prims_algo(data):

    # on initialise toutes les liste que l'on va utiliser pour cette algorithme
    node_not_in = []
    node_in = []
    edges_in = []
    edges_not_in = data
    current_edge = [0,0,1000000]

    # initialisation de la list node_not_in 
    # ajoute dans cette matrice tout les noeuds qui devront être présent dans le graph
    for each in edges_not_in:
        if each[0] not in node_not_in:
            node_not_in.append(each[0])
        if each[1] not in node_not_in:
            node_not_in.append(each[1])
    
    #on choici ici au hazard un noeud
    #on le supprime de la liste des noeuds pas encore présent et on l'ajoute dans la liste des noeud présent
    node_not_in.sort()
    x = random.choice(node_not_in)
    node_in.append(x)
    node_not_in.remove(x)

    # tant que tout les noeuds ne sont pas connecté, on va chercher de nouveaux liens
    while(len(node_not_in) != 0):
        
        for edge in edges_not_in:
                
            # je trouve ici le meuilleur lien parmis tous les lien encore possible   
            if((edge[0] in node_in and not edge[1] in node_in) or (edge[1] in node_in and not edge[0] in node_in)):
                if(float(edge[2]) < float(current_edge[2])):
                    current_edge = edge
              
        # je met a jour toutes mes listes   
        edges_not_in.remove(current_edge)
        edges_in.append(current_edge)
        if(current_edge[0] not in node_in):
            node_in.append(current_edge[0])
            node_not_in.remove(current_edge[0])
        if(current_edge[1] not in node_in):
            node_in.append(current_edge[1])
            node_not_in.remove(current_edge[1])
        current_edge = [0,0,100000]

    # je retourne tous les liens 
    return edges_in

def read_csv(file_name):
    data = []
    my_file = open(file_name, "r")
    for line in my_file:
        
        data.append(line.replace("\n","").split(";"))
    return data

def exo1():
    my_data = read_csv("./distances.csv")
    display_graph(my_data)  
    my_data = prims_algo(my_data)
    display_graph(my_data)

if __name__ == "__main__":
    exo1()
    input("Appuyer sur une touche pour quitter...")
