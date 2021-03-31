import heapq

#class will posses the component of a single vertex node where it contains: all connected edges, letter or title of the node,
# weight of the node, node that is connect to it from uniform-cost search, and flag whether it has been already explore
class node:
    
    def __init__(self, node):

        self.letter=node  
        self.neighbor={}
        self.visited=False
        self.weight= 100000
        self.previous_state=None

    #function help fill the dictionary with edges conected to it
    def add_neighbor(self, target, weight_value=0):

        self.neighbor[int(target)]= int(weight_value)
    
    #return dictionary that list all connected edges with their cost value
    def get_neighbor(self):
        
        return self.neighbor

    #return the cost of traversing a specific edge
    def get_cost(self, target):

        return self.neighbor[int(target)]

    #eliminate one of the connected edges on the vertex
    def remove_neighbor(self, target):

        del self.neighbor[int(target)]

    #store the found weight value during uniform-cost traversal
    def set_distance(self, value):

        self.weight = value

    #return node value weight saved from the path function     
    def node_travesal(self):
        return self.weight

    #set the node that it has been already explore and pass through
    def node_visit(self):
        self.visited=True
    
    #return if node has been visited or not
    def check_visit(self):
        return self.visited
    
    #sets what was the previous node connect to it when finding the distance in path function
    def set_prev_state(self, state):
        self.previous_state=state
    
    #return previous node connect to it
    def get_state(self):
        return self.previous_state
    
    #return node 
    def get_node(self):
        return self.letter

    

class Node_graph:

    def __init__(self):

        self.graph_vert={}
        self.num_vertices= 0

    # Function will add a single vertex to the graph#
    def add_vertex(self, target):

        if target in self.graph_vert:
            return

        self.num_vertices=+1
        sample=node(target)
        self.graph_vert[target]=sample
    
    #return the vertex chosen pick by the parameter on graph_vector dictionary
    def get_vertex(self, id):
        return self.graph_vert[str(id)]

    #established an edge based on designate paramter in the function. 
    # Target: node that would be connected by the vertex
    # Home: main vertex being connect from
    # cost: the weight cost of traversing from this edge to the target 
    def add_edge(self, target, home, cost=0):
        
        self.graph_vert[home].add_neighbor(target, cost)
    
    #check whether two choosen vertices exist in the dictionary graph_vect
    def check_vertex(self, v1, v2):

        if self.graph_vert.get(str(v1)) and self.graph_vert.get(str(v2)):
            return True
        print("Graph does not have one of the vertex you inputed")
        return False

    #Implement a uniform-cost search
    def find_path(self, home, goal):
        
        explore_path=[] # container to saved any already explore path
        unexplore_path=[]

        self.graph_vert[str(home)].set_distance(0) #have the starting node with the lowest possible value
        
        unexplore_path=[(self.graph_vert[i].node_travesal(), i) for i in self.graph_vert] #fill list with a tuple:(Node_cost, node)
        heapq.heapify(unexplore_path) # creating a priority queue 

        
        # checks if the starting node has any outgoing frontier 
        if not bool(self.graph_vert[str(home)].get_neighbor()):
            print("Initial vertex has no outgoing edge")
            print("Total cost: 0")
            return False
        
        #loop through the lenght from the priority queue
        while len(unexplore_path):

            current_node=heapq.heappop(unexplore_path)
            point = current_node[1]  # indicate the current node we are in now
            self.graph_vert[point].node_visit()
            explore_path.append(current_node)

            #If the goal node has been reach break from the loop
            if str(point) == str(goal):
                break
            
            #loop through the edges conect to the vertex
            for node in self.graph_vert[str(point)].get_neighbor():

                # check wether the node has already been visited
                if self.graph_vert[str(node)].check_visit():
                    continue

                #add up current node value to the weight of its neighbor
                distance = self.graph_vert[str(point)].node_travesal() + self.graph_vert[str(point)].get_cost(node)

                #compare the distance value with the neighbor current distance value
                if distance < self.graph_vert[str(node)].node_travesal():
                    self.graph_vert[str(node)].set_distance(distance)
                    self.graph_vert[str(node)].set_prev_state(point)

            #clear the queue and refill it with updated distance
            unexplore_path.clear()
            unexplore_path=[(self.graph_vert[i].node_travesal(), i) for i in self.graph_vert if not self.graph_vert[i].check_visit()]
            heapq.heapify(unexplore_path)
        
        #Condition to check wether loop found a connected edges to the goal node 
        check_node=self.graph_vert[str(explore_path[-1][1])].get_state()
        if check_node == None:
            print("Goal vertex does not have an in going edges")

            return False

        return True

def ret_path(target, trail, trail_cost ,graph):

    if target.get_state() != None:
        trail.append( graph.get_vertex( target.get_state() ).get_node())
        target=graph.get_vertex(target.get_state())
        trail_cost.append(target.node_travesal())
        ret_path(target, trail, trail_cost, graph)
    return


file_sample = open("sample.txt","r")

graph_node = Node_graph()

for x in file_sample:
    frm ,trg ,value = x.split()
    graph_node.add_vertex(frm)
    graph_node.add_edge(trg,frm,value)

start= input("Starting vertex: ")
end= input("Ending vertex: ")

# condition will check first wether both vertex exist in the graph and begin to contruct and find if their is a path between the two vertex
if graph_node.check_vertex(start, end) and graph_node.find_path( start, end):

    point=graph_node.get_vertex(end)
    cost= point.node_travesal()


    path=[point.get_node()]
    path_cost=[cost]
    ret_path(point, path, path_cost, graph_node) 

    for x in range((len(path)-1), -1, -1):
        if x == 0:
            break
        print("vertex {0} to vertex {1}, cost {2}".format(path[x], path[x-1], ( path_cost[x-1]- path_cost[x]) ) )

    print("Total cost: {0}".format(cost))
print("Ending program")
file_sample.close()
