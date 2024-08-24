import sys


'''
checkgraph function
It checks the relationships between each node and its neighboring nodes to ensure there are no errors in the data. Specifically, it performs the folloing checks:

1. Node Existence Check: For every node in the graph, the function checks if each neighbor defined in the node's neighbor list is also present recciprocally in the neighbor list of those neighbor nodes.
   In other words, it verifies that bidirectional connections are properly defined. If node A lists B as a neighbor but node B does not list A as a neighbor, an error is raised.

2. Distance Value Validation: It checks if the distances(or weights) of the connections between nodes are negative. If a distance (or time) value is negative, it is physically impossible, and an error is raised.

3. Distance Value Consistency Check: It verifies whether the distance from node A to B is the same as from B to A. Since the graph is assumed to be undirected, distances should be the same in both directions. If they do not match, an error is raised.
'''
def checkgraph(graph):



    namelist = list(graph.keys()) #get the keys(the set of all stations)
    for node in namelist:
        for neighbor, distance in graph[node].items():
            #check whether the station exists
            if node not in list(graph[neighbor].keys()):
                raise ValueError("Node is not exist.")
                return

            #check whether it is a negative value
            if distance < 0:
                raise ValueError("Route value is negative.")
                return

            #check the value
            if distance != graph[neighbor][node]:
                print(node, neighbor, distance)
                raise ValueError("Route value is not equal.")
                return
            

    return

'''
dijkstra function
It takes a graph data structure and a starting node as arguments, and uses Dijkstra's algorithm to calculate the shortest paths and distances from the starting node to all other nodes in the graph.
The operation of this function can be described as follows:

1. Checklist Initialization: A checklist is created for all nodes in the graph, setting the distance to each node to infinity('sys.maxsize'). The distance to the starting node is set to 0.

2. Path Dictionary Initialization: A dictionary to store paths and distances from the starting node is initialized, with the distance for the starting node set to 0 and the path as an empty list.

3. Checklist Interation: As long as there are nodes left in the checklist, the node with the shortest distance is identified and set as the current node('checknode').

4. Neighbor Distance Update: For all neighboring nodes of the current node, a new distance ('ndistance') is calculated.
   This distance is the sum of the distance to the current node ('checkdistance') and the distance from the current node to the neighboring node ('distance').

5. Shortest Distance Update: If the newly calculated distance is shorter than the previously stored distance to the neighbor node in the checklist, this new distance and path are updated in the checklist and path dictionary.

6. Current Node Removal: The current node is removed from the checkist, and the process is repeated for the next node.

7. Path Return: Once all nodes have been removed from the checklist, the path dictionary containing the calculated paths is returned.
'''
def dijkstra(graph, start):
    

    #generate the set of untreated nodes
    checklist = {node: sys.maxsize for node in graph}

    #set the start point
    checklist[start] = 0
    path = {start:(0,[])}

    while checklist:

        #get connected nodes
        checknode = min(checklist,key = checklist.get)  
        checkdistance = checklist[checknode]

        #check and update the values, routes
        for neighbor, distance in  graph[checknode].items():
            if neighbor not in checklist:
                continue
            
            ndistance = distance + checkdistance
            if ndistance < checklist[neighbor]:
                checklist[neighbor] = ndistance
                path[neighbor] = (ndistance, path[checknode][1] + [checknode])

        #remove the node from untreated set
        checklist.pop(checknode)

    return path



'''
graph variable
It stores all the routes in a map into a dictionary format.

4 Graphs are defined here.

TestGraph1-3 are the testing maps.

TaskGraph is the railway system map.

'''

'''
#TestGraph1

graph = {
    'Paddington':{'Kings Cross':1,'Euston':6},
    'Waterloo':{'Euston':8},
    'Kings Cross':{'Euston':4,'Paddington':1},
    'Euston':{ 'Kings Cross':4,'Paddington':6,'Waterloo':8},
}
'''

'''
#TestGraph2

graph = {
    'A':{'B':4,'D':2},
    'B':{'A':4,'C':4,'D':1},
    'C':{'B':4,'D':1,'E':3},
    'D':{ 'A':2,'B':1,'C':1,'E':7},
    'E':{ 'C':3,'D':7},
}
'''

'''
#TestGraph3

graph = {
    'A':{'B':12,'F':16,'G':14},
    'B':{'A':12,'C':10,'F':7},
    'C':{'B':10,'D':3,'E':5,'F':6},
    'D':{ 'C':3,'E':4},
    'E':{ 'C':5,'D':4,'F':2,'G':8},
    'F':{ 'A':16,'B':7,'C':6,'E':2,'G':9},
    'G':{ 'A':14,'E':8,'F':9},
    
}
'''


#TaskGraph

graph = {
    'Paddington':{'Baker Street':6,'Notting Hill Gate':4},
    'Notting Hill Gate':{'Paddington':4,'Bond Street':7,'South Kensington':7},
    'South Kensington':{ 'Notting Hill Gate':7,'Green Park':7,'Victoria':4},
    'Baker Street':{'Paddington':6,'Bond Street':2,'Oxford Circus':4,'Kings Cross':7},
    'Bond Street':{'Baker Street':2, 'Notting Hill Gate':7,'Green Park':2,'Oxford Circus':1},
    'Green Park':{'Bond Street':2,'Oxford Circus':2,'Piccadilly Circus':1,'Westminster':3,'Victoria':2,'South Kensington':7},
    'Victoria':{'Green Park':2,'Westminster':4,'South Kensington':4},
    'Oxford Circus':{'Baker Street':4,'Warren Street':2,'Tottenham Court Road':2,'Piccadilly Circus':2,'Green Park':2,'Bond Street':1},
    'Piccadilly Circus':{'Oxford Circus':2,'Leicester Square':2,'Charing Cross':2,'Green Park':1},
    'Westminster':{'Green Park':3,'Embankment':2,'Waterloo':2,'Victoria':4},
    'Warren Street':{'Kings Cross':3, 'Tottenham Court Road':3,'Oxford Circus':2},
    'Tottenham Court Road':{'Warren Street':3,'Holborn':2,'Leicester Square':1,'Oxford Circus':2},
    'Leicester Square':{'Tottenham Court Road':1,'Charing Cross':2,'Holborn':2,'Piccadilly Circus':2},
    'Charing Cross':{'Leicester Square':2,'Embankment':1,'Piccadilly Circus':2},
    'Embankment':{'Charing Cross':1,'Blackfriars':4,'Waterloo':2,'Westminster':2},
    'Waterloo':{'Embankment':2,'London Bridge':3,'Elephant and Castle':4,'Westminster':2},
    'Elephant and Castle':{'Waterloo':4,'London Bridge':3},
    'Holborn':{'Kings Cross':4,'Bank':5,'Leicester Square':2,'Tottenham Court Road':2},
    'Kings Cross':{'Baker Street':7,'Warren Street':3,'Holborn':4,'Moorgate':6,'Old Street':6},
    'Blackfriars':{'Bank':4,'Embankment':4},
    'Old Street':{'Kings Cross':6,'Moorgate':1},
    'Moorgate':{'Old Street':1,'Liverpool Street':2,'Bank':3,'Kings Cross':6},
    'Bank':{'Moorgate':3,'Liverpool Street':2,'Tower Hill':2,'London Bridge':2,'Blackfriars':4,'Holborn':5},
    'London Bridge':{'Bank':2,'Elephant and Castle':3,'Waterloo':3},
    'Liverpool Street':{'Moorgate':2,'Bank':2,'Tower Hill':6,'Aldgate East':4},
    'Tower Hill':{'Bank':2,'Liverpool Street':6,'Aldgate East':2},
    'Aldgate East':{ 'Liverpool Street':4, 'Tower Hill':2},
}


'''
Reusability of the algorithm

1. Algorithm's Universal Applicability: the 'checkgraph' and 'dijkstra' functions operate independently of the specific input format, working with the graph data that is passed to them.
   This means that the logic of the algorithm is not dependent on specific network data and can be applied to a wide range of problems.

2. Flexibility of Parameterization: The code is designed to accommodate external data through parameterization.
   The graph structure is defined externally, and the functions accept this as input.
   This ensures that new network data can be easily integrated and the code can be reused.

3. Ease of Code Modification: To apply a new network, all that is needed is a change in the graph data. This allows for the determination of the shortest paths for various types of networks.
   Additionally, the code is structured to be easily understandable and modifiable by other developers. This is an important factor in enhancing reusability.
'''




'''
##
This code performs the process of finding the shortest path between stations in the London railway network by taking input from the user for the start and end points. Each part of the code functions as follows:

1. Graph Validation: In the 'try'blcok, the 'checkgraph' function is called to validate the input graph.
   This function checks if each node(station) in the graph is correctly connected to others, ensures that distance values are not negative, and verifies that the distances of bidirectional connections match.
   If the graph is invalid, a 'ValueError' exception is raised and an error message is displayed.

2. User Input: Two 'while' loops are used to take user input for the start station('start') and end station ('end').
   If the input station does not exist in the graph's keys(list of stations), a message "Station not exist." is displayed and it prompts for input again.

3. Shortest Path Calculation: The 'dijkstra' function is called to calculate the shortest path and time from the start station to the end station.
   This function takes the graph and start station as inputs and returns the shortest paths and distances to all stations.

4. Result Output: The calculated shortest path and time are displayed.
   The output format includes the start station, end station, total time, and the path(list of stations), with the path being delineated by arrows('->')
'''

try:
    checkgraph(graph)
except ValueError as e:
    print("Error:", e)


#4 Example Routes
#Bank -> Aldgate East
result=dijkstra(graph, "Bank")["Aldgate East"]

print("Example 1:")
print("Start station: ","Bank")
print("Destination station: ","Aldgate East")
print("Time:",result[0])
print("Route:")
for i in result[1]:
    print(i, end='->')

print("Aldgate East")
print()

#Paddington -> Oxford Circus
result=dijkstra(graph, "Paddington")["Oxford Circus"]

print("Example 2:")
print("Start station: ","Paddington")
print("Destination station: ","Oxford Circus")
print("Time:",result[0])
print("Route:")
for i in result[1]:
    print(i, end='->')

print("Oxford Circus")
print()

#Elephant and Castle –> Bank
result=dijkstra(graph, "Elephant and Castle")["Bank"]

print("Example 3:")
print("Start station: ","Elephant and Castle")
print("Destination station: ","Bank")
print("Time:",result[0])
print("Route:")
for i in result[1]:
    print(i, end='->')

print("Bank")
print()

#Baker Street –> Warren Street
result=dijkstra(graph, "Baker Street")["Warren Street"]

print("Example 4:")
print("Start station: ","Baker Street")
print("Destination station: ","Warren Street")
print("Time:",result[0])
print("Route:")
for i in result[1]:
    print(i, end='->')

print("Warren Street")
print()

#Input to check for the Map
#set mark of input
stf = True
edf = True

#Use While-Loop to keep reading until getting the correct input
while(stf):
    start = input("Input the Start Point:")
    if start not in list(graph.keys()):
        print("Station not exist.")

    else:
        stf = False

while(edf):
    end = input("Input the End Point:")
    if end not in list(graph.keys()):
        print("Station not exist.")
    else:
        edf = False
        
#use the function
result=dijkstra(graph, start)[end]

#print the routes
print("Start station: ",start)
print("Destination station: ",end)
print("Time:",result[0])
print("Route:")
for i in result[1]:
    print(i, end='->')

print(end)

