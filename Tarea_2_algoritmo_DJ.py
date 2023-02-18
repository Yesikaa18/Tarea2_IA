import matplotlib.pyplot as plt
import sys
import time

inicio = time.time()

# Código a medir
time.sleep(1)


def shortestpath(graph,start,end,visited=[],distances={},predecessors={}):
    """Find the shortest path between start and end nodes in a graph"""
    # we've found our end node, now find the path to it, and return
    if start==end:
        path=[]
        while end != None:
            path.append(end)
            end=predecessors.get(end,None)
        return distances[start], path[::-1]
    # detect if it's the first time through, set current distance to zero
    if not visited: distances[start]=0
    # process neighbors as per algorithm, keep track of predecessors
    for neighbor in graph[start]:
        if neighbor not in visited:
            neighbordist = distances.get(neighbor,sys.maxsize)
            tentativedist = distances[start] + graph[start][neighbor]
            if tentativedist < neighbordist:
                distances[neighbor] = tentativedist
                predecessors[neighbor]=start
    # neighbors processed, now mark the current node as visited
    visited.append(start)
    # finds the closest unvisited node to the start
    unvisiteds = dict((k, distances.get(k,sys.maxsize)) for k in graph if k not in visited)
    closestnode = min(unvisiteds, key=unvisiteds.get)
    # now we can take the closest node and recurse, making it current
    return shortestpath(graph,closestnode,end,visited,distances,predecessors)

if __name__ == "__main__":

    graph = {

            'a': {'c': 14, 'e': 7, 'b': 9, 'B': 28, 'C': 31},
            'b': {'f': 9, 'd': 6, 'K':17},
            'c': {'b': 14, 'a': 9, 'd': 2, 'G': 12, 'F': 29},
            'd': {'c': 7, 'e': 10, 'f': 15, 'O': 15},
            'e': {'a': 9, 'd': 2, 'g': 10, 'c': 11, 'F': 8},
            'f': {'h': 6, 'j': 15, 'e': 11, 'E': 11},
            'g': {'b': 3, 'j': 6, 'U': 18},
            'h': {'a': 14, 'i': 9, 'f': 2, 'L': 18},
            'i': {'c': 7, 'q': 10, 'f': 15, 'P': 26},
            'j': {'e': 9, 'h': 2, 'k': 11, 'K': 10},
            'k': {'l': 9, 'P': 19},
            'l': {'b': 14, 'u': 9, 'x': 2, 'a': 12},
            'm': {'c': 7, 's': 10, 't': 15, 'C': 19},
            'n': {'g': 9, 'm': 2,'c': 11, 'C': 12, 'B': 20, 'I': 15},
            'o': {'e': 9, 's': 6, 'D': 3, 'H': 7},
            'p': {'u': 14, 'a': 9, 'w': 2},
            'q': {'o': 7, 'e': 10, 'k': 15},
            'r': {'w': 9, 'x': 10},
            's': {'c': 9, 'i': 6},
            't': {'c': 14, 'a': 9},
            'u': {'z': 7, 'q': 10, 'v': 0},
            'v': {'e': 9, 'b': 2, 'x': 10, 'c': 11},
            'w': {'a': 9, 'd': 6},
            'x': {'g': 14, 'r': 9, 's': 2},
            'y': {'e': 7, 'm': 10, 'l': 15},
            'z': {'a': 9, 'd': 2, 'f': 10, 'B': 11},
            'A': {'a': 12, 'x': 2, 'g': 10},
            'B': {'c': 2, 'u': 6, 'h': 1, 'J': 23},
            'C': {'a': 7, 'z': 11},
            'D': {'C': 3, 'e':9, 'r': 4 },
            'E': {'A':1, 'C':4, 'h': 12, '5': 79},
            'F': {'D':6, 'a':13},
            'G': {'y':4, 'w':8, ' s': 5, 'C': 7, 'L': 29},
            'H': {'A':1 , 'a':14, 'G': 12 },
            'I': {'E':12, 'u':7, 'W': 12},
            'J': {'I':2, 'H':6, 'b': 15},
            'K': {'J':4, 'c':10, 'z':4, 'F': 10, '1': 45},
            'L': {'K':12 , 'B':3, 'c': 6, 'M': 13 },
            'M': {'J':1, 'j':5},
            'N': {'K':3, 'u':13, 'D': 45},
            'O': {'t':3, 'u':12},
            'P': {'K':4 , 'G':8 },
            'Q': {'P':12, 'O':5, 'L': 9},
            'R': {'Q':1, 'h':3, 'x': 8},
            'S': {'B':5, 'D':4},
            'T': {'R':12, 'o':11},
            'U': {'T': 10, 'a':2},
            'V': {'U':9, 'S':12},
            'W': {'U': 10, 'i':3 },
            'X': {'D':3, 'a':9, 'A': 19},
            'Y': {'W':6, 'V':7},
            'Z': {'X':11, 'H':2, 'X': 7},


            '1': {'a': 14, '5': 7, '2': 9, '4': 28},
            '2': {'6': 9, '4': 6, 'K':17},
            '3': {'2': 14, '1': 9, '4': 2, '7': 12},
            '4': {'3': 7, '5': 10, '6': 15, 'O': 15},
            '5': {'1': 9, '4': 2, '7': 10, '3': 11, '6': 8},
            '6': {'8': 6, '10': 15, '5': 11, '5': 11},
            '7': {'2': 3, '10': 6, 'U': 18},
            '8': {'1': 14, '9': 9, '6': 2, 'L': 18},
            '9': {'3': 7, 'q': 10, '6': 15, 'P': 26},
            '10': {'5': 9, '8': 2, 'k': 11, 'K': 10}

             }


print (shortestpath(graph,'a','10')) #aquí se modifica el recorrido que queremos llevar a cabo, en este caso de a - 10

fin = time.time()
print("Tiempo de ejecución del programa: ", fin-inicio)
intento = 1
#--------------------------
fig, ax = plt.subplots()
ax.set_ylabel('Tiempo')
ax.set_title('Tiempo de ejecución')
plt.bar(intento, fin-inicio)
plt.show()
