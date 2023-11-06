graph = {
    'a':{'b':3, 'c':3},
    'b':{'d':2, 'n':8, 'e':2, 'a':3},
    'c':{'f':3, 'i':2, 'a':3},
    'd':{'e':4, 'f':5, 'g':4, 'h':8, 'b':2},
    'e':{'n':8, 'g':4, 'b':2, 'd':4},
    'f':{'h':6, 'i':6, 'd':5, 'c':3},
    'g':{'k':3, 'h':3, 'n':3, 'l':4, 'd':4, 'e':4},
    'h':{'k':5, 'j':2, 'i':3, 'd':8, 'g':3, 'f':6},
    'i':{'u':8, 'j':3, 'c':2, 'f':6, 'h':3},
    'j':{'p':5, 'u':1, 'k':4, 'h':2, 'i':3},
    'k':{'m':8, 'p':1, 'l':2, 'j':4, 'h':5, 'g':3},
    'l':{'q':6, 'r':3, 'm':2, 'n':2, 'k':2, 'g':4},
    'm':{'p':4, 'r':2, 'o':1, 'k':8, 'l':2},
    'n':{'q':2, 's':5, 'b':8, 'e':8, 'g':3, 'l':2},
    'o':{'r':2, 't':5, 'p':5, 'w':8, 'm':1},
    'p':{'w':4, 'u':2, 'v':3, 'j':5, 'k':1, 'm':4, 'o':5},
    'q':{'r':4, 's':3, 'x':4, 'l':6, 'n':2},
    'r':{'t':2, 'x':3, 'o':2, 'm':2, 'l':3, 'q':4},
    's':{'x':4, 'n':5, 'q':3},
    't':{'z':4, 'x':4, 'w':6, 'o':5, 'r':2},
    'u':{'v':3, 'i':8, 'j':1, 'p':2},
    'v':{'w':3, 'y':3, 'p':3, 'u':3},
    'w':{'y':5, 'z':3, 't':6, 'o':8, 'p':4, 'v':3},
    'x':{'z':2, 't':4, 'r':3, 'q':4, 's':4},
    'y':{'z':6, 'w':5, 'v':3},
    'z':{'t':4, 'w':3, 'y':6, 'x':2}
}

def dijkstra(graph, start, goal):
    shortest_distance = {} # benötigte kosten bis zu diesem knoten
    track_predecessor = {} # pfad der bisher zu diesem knoten genommen wurde
    unseenNodes = graph # um durch die knoten zu navigieren
    infinity = 999999 # eine sehr große zahl, alternativ float('inf')
    track_path = [] # optimale route

    for node in unseenNodes:
        shortest_distance[node] = infinity # Knotenkosten unidentifiziert, deshalb infinity
    shortest_distance[start] = 0 # Startpunkt benötigt keine Kosten

    while unseenNodes: # läuft bis alles identifiziert ist == dict = leer
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node # erstes Element aus Graphen
            elif shortest_distance[node] < shortest_distance[min_distance_node]: # momentane Knotenkosten mit nachfolge Knotenkosten prüfen
                min_distance_node = node

        path_options = graph[min_distance_node].items() # kanten, kosten

        for child_node, cost in path_options:
            if cost + shortest_distance[min_distance_node] < shortest_distance[child_node]: # optimaleren pfad gefunden
                shortest_distance[child_node] = cost + shortest_distance[min_distance_node] # Kosten der Route anpassen
                track_predecessor[child_node] = min_distance_node # Vorgänger ändern
# predecessor = Vorgänger
        unseenNodes.pop(min_distance_node) # Knoten abgeschlossen, muss nicht mehr besucht werden

    current_node = goal

    while current_node != start: # rekursiver vorgang, vorgänger werden ausgegeben (start hat keinen)
        try:
            track_path.insert(0, current_node) # setzt vorgänger an erste Stelle der Liste andere Elemente werden eine Position nach hinten verschoben
            current_node = track_predecessor[current_node]

        except KeyError: # falls kein pfad gefunden werden kann (keine Verbindung von start zu ziel)
            print('Pfad nicht erreichbar')
            break

    track_path.insert(0, start)

    if shortest_distance[goal] != infinity: # ein pfad wurde gefunden
        print('kürzeste Route: ' + str(shortest_distance[goal]))
        print('optimaler Pfad ' + str(track_path))

# main programm

if __name__ == '__main__':
    dijkstra(graph, 'a', 'z')