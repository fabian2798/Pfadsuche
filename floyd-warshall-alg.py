# Floyd-Warshall-Algorithmus

import numpy as np
#from pyvis.network import Network

# Anzahl der Knoten -> zum Navigieren
V = 26

# sehr große Zahl -> Knoten nicht verbunden oder bereits bekannte Kanten
INF = 99999

def floydWarshall(graph):

    dist = graph

    for k in range(V): # Iteration
        for i in range(V): # jeden Knoten als Startpunkt
            for j in range(V): # jeden Knoten als Ziel
                # dist[i][j]= aktuelle Kosten
                # dist[k][j]= Kosten vom Nachbarknoten zum Zielknoten
                # dist[i][k]= Kosten zum Nachfolger
                if dist[i][j] > dist[k][j] + dist[i][k]: # Abkürzung gefunden
                    dist[i][j] = dist[i][k] + dist[k][j] # Kostenänderung
                    p[i][j] = p[k][j] # Vorgänger ändern
    printSolution(dist)


def printSolution(dist):
    print("Matrix zeigt die geringsten Kosten jedem Startknoten zum entsprechenden Endknoten:")
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
    for x in alpha:
        print(x+'\t',end=' ')
        if x == 'Z':
            print('\n')
    for i in range(V): # Reihe
        for j in range(V): # Spalte
            if dist[i][j] == INF:
                print('INF', end=" ") # Nicht erreichbare Knoten
            else:
                print("%d\t" % (dist[i][j]), end=' ') # Ausgabe von Endkosten zum Zielpunkt
            if j == V - 1:
                print('\t'+alpha[i]) # Werte ausgehend vom Buchstaben, Buchstabe = Startpunkt

def ConstructPath(p, i, j):
    alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    i,j = int(i), int(j) # Integer Zuweisung aufgrund von numpy
    if i==j: # Startpunkt
        print (alpha[i],end='')
    elif p[i][j] == -INF: # Pfad nicht erreichbar
        print('Nicht erreichbar')
        print (i,'-',j)
    else: # kürzesten Weg vom Vorgänger
        ConstructPath(p, i, p[i][j])
        print(alpha[j],end='')

# A ,B ,C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z
graph = np.array([
         [0, 3, 3, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF], # A
         [3, 0, INF, 2, 2,  INF, INF, INF, INF, INF, INF, INF, INF, 8, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF], # B
         [3, INF, 0, INF, INF, 3, INF, INF,  2, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF], # C
         [INF, 2, INF, 0, 4, 5, 4, 8,  INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF], # D
         [INF, 2, INF, 4, 0, INF, 4, INF, INF, INF, INF, INF, INF, 8, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF], # E
         [INF, INF, 3, 5, INF, 0, INF, 6, 6, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF], # F
         [INF, INF, INF, 4, 4, INF, 0, 3, INF, INF, 3, 4, INF, 3, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF], # G
         [INF, INF, INF, 8, INF, 6, 3, 0, 3, 2, 5, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF], # H
         [INF, INF, 2, INF, INF, 6, INF, 3, 0, 3, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 8, INF, INF, INF, INF, INF], # I
         [INF, INF, INF, INF, INF, INF, INF, 2, 3, 0, 4, INF, INF, INF, INF, 5, INF, INF, INF, INF, 1, INF, INF, INF, INF,INF], # J
         [INF, INF, INF, INF, INF, INF, 3, 5, INF, 4, 0, 2, 8, INF, INF, 1, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF], # K
         [INF, INF, INF, INF, INF, INF, 4, INF, INF, INF, 2, 0, 2, 2, INF, INF, 6, 3, INF, INF, INF, INF, INF, INF, INF, INF], # L
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 8, 2, 0, INF, 1, 4, INF, 2, INF, INF, INF, INF, INF, INF, INF, INF], # M
         [INF, 8, INF, INF, 8, INF, 3, INF, INF, INF, INF, 2, INF, 0, INF, INF, 2, INF, 5, INF, INF, INF, INF, INF, INF, INF], # N
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 1, INF, 0, 5, INF, 2, INF, 5, INF, INF, 8, INF, INF, INF], # O
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, 5, 1, INF, 4, INF, 5, 0, INF, INF, INF, INF, 2, 3, 4, INF, INF, INF], # P
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 6, INF, 2, INF, INF, 0, 4, 3, INF, INF, INF, INF, 4, INF, INF], # Q
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, 2, INF, 2, 4, 0, INF, 2, INF, INF, INF, 3, INF, INF], # R
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 5, INF, INF, 3, INF, 0, INF, INF, INF, INF, 4, INF, INF], # S
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 5, INF, INF, 2, INF, 0, INF, INF, 6, 4, INF, 4], # T
         [INF, INF, INF, INF, INF, INF, INF, INF, 8, 1, INF, INF, INF, INF, INF, 2, INF, INF, INF, INF, 0, 3, INF, INF, INF, INF], # U
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, INF, INF, INF, INF, 3, 0, 3, INF, 3, INF], # V
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 8, 4, INF, INF, INF, 6, INF, 3, 0, INF, 5, 3], # W
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 4, 3, 4, 4, INF, INF, INF, 0, INF, 2], # X
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 3, 5, INF, 0, 6], # Y
         [INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, INF, 4, INF, INF, 3, 2, 6, 0] # Z
         ])

# Erstellung des Grundgerüstes

p = np.zeros(graph.shape)
for i in range(V): # Reihe
    for j in range(V): # Spalte
        p[i][j] = i
        if i != j and graph[i][j] == 0: # Sicherheit, falls mehrere Knotenkosten 0 erhalten haben
            p[i][j] = -INF
            graph[i][j] = INF

# main
floydWarshall(graph)
print(140*'-')
print('Folgendes zeigt den kürzesten Weg vom gewünschten Startpunkt zum Zielpunkt:')
ConstructPath(p,0,25)
#print(p)
# Visualisation Graph
"""
net = Network('1000px','1000px')
nodes = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
net.add_nodes(nodes)
edges = [
    ('M','O',1), ('U','J',1), ('P','K',1),
    ('B','D',2), ('C','I',2), ('N','L',2), ('L','K',2), ('U','P',2), ('O','R',2),
    ('R','T',2), ('X','Z',2), ('M','R',2), ('H','J',2), ('B','E',2), ('L','M',2), ('N','Q',2),
    ('A','B',3), ('A','C',3), ('C','F',3), ('I','J',3), ('S','Q',3), ('U','V',3), ('V','P',3), ('V','W',3), ('W','Z',3),
    ('V','Y',3), ('G','K',3), ('H','G',3), ('I','H',3), ('L','R',3),
    ('D','G',4), ('D','E',4), ('K','J',4), ('S','X',4), ('T','Z',4), ('Q','R',4), ('M','P',4), ('G','E',4), ('W','P',4),
    ('X','Q',4), ('X','T',4), ('L','G',4),
    ('D','F',5), ('H','F',5), ('J','P',5), ('N','S',5), ('P','O',5), ('W','Y',5), ('T','O',5),
    ('F','H',6), ('W','T',6), ('Y','Z',6),
    ('D','H',8), ('I','U',8), ('E','N',8), ('K','M',8), ('W','O',8), ('B','N',8)
]
net.add_edges(edges)
net.show('mygraph.html')
"""