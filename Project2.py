import re

goal_state=[[1,2,3],[8,0,4],[7,6,5]]

class Node:

    def __init__(self, map, f_value, path):
        self.state=map
        self.f_cost=f_value
        self.p_cost=path

    def create_frontier(self):
        #initialize point that will represent where the 0 position is at
        p_x=0
        p_y=0

        
        #find the zero position in the puzzle
        for x in range(len(self.state)):
            for y in range(len(self.state[x])):
                if int(self.state[x][y]) == 0:
                    p_x=x
                    p_y=y

        container=[[p_x,p_y-1], [p_x,p_y+1], [p_x+1,p_y], [p_x-1,p_y]] # hold a list that represent the moved set a key can have
        frontier=[]  # hold list of children to current node

        #loop through the number of action a key can do.
        for x in range(len(container)):

            test,cost=self.create_state(container[x][0],container[x][1], p_x, p_y, self.state)

            #statement check if wether or not the method create_state has a valid action to branch to another state
            if test is not None:
                
                child_state=Node(test, 0,cost)
                frontier.append(child_state)

        return frontier

    #Function create and return a new state based on the move action and its cost of moving it
    def create_state(self, x2, y2, x1, y1 , data):

        #checks wether the position in in x2, x2 is within the boundary of the list in data
        if x2 >= 0 and x2 < len(data) and y2 >= 0 and y2 < len(data):

            #cost to reach this state
            cost=int(data[x2][y2]) + self.p_cost

            temp= self.copy_state(data)#create copy of state given to a temporary variable
            hold=temp[x2][y2]  # hold temporaly the value at position to switch for
    
            temp[x2][y2]=temp[x1][y1] #switch key with 0 key 
            temp[x1][y1]=hold #return original key  back to position

            return temp, cost
        else:
            return None, None #return a none value when the points x2, y2 are an invalid number in data
    
    #takes a list that contain a then copy it to a new list and return back a whole new copy
    def copy_state(self, data1):
        temp=[]
        for x in data1:
            cont= []
            for y in x:
                cont.append(y)
            temp.append(cont)
        return temp
    
    
class Puzzle_solver:

    def __init__(self):
        self.open=[] #list that hold unexplored node state 
        self.closed=[] #list that hold explored node state

    #find the total value cost by combining the heuristic and path cost
    def f_find(self, current_state):
        return self.h_find(current_state)+ current_state.f_cost
    
    #Function that will search inside the closed list varibale wether the current state in data exist in it or not
    def check_list(self, data):

        for x in range(len(self.closed)):
            if self.closed[x].state == data.state:
                return True

        return False   


    #find the heuristic value from giving node
    def h_find(self, node_v):
        hit=0
        for x in range(len(node_v.state)):
            for y in range(len(node_v.state[x])):
                if int(node_v.state[x][y]) != goal_state[x][y]:
                    hit+=1
        return hit

    #start to search solution by a* algotrithm
    def solve_puzzle(self, state):
        
        count=0 #variable to use to saved the total travel cost
        node_start=Node(state, 0,0) # Create the initial node
        node_start.f_cost=self.f_find(node_start) #combine the cost of travel and herustic value on the initial node
        self.open.append(node_start) #add node to the open list variable
        
        while True:
            # get the first the first index for which it is the least cost value in the list
            current_n = self.open[0]

            # check if current node is at the goal state
            if self.h_find(current_n)==0:
                count=current_n.p_cost
                break
            
            #checks wether or not the state had already been explore and discovered
            if self.check_list(current_n) is True:
                del self.open[0]
                self.open.sort(key = lambda x:x.f_cost,reverse=False)

            else:
                #loop through the frontier at current node
                for x in current_n.create_frontier():
                    x.f_cost=self.f_find(x)
                    self.open.append(x)

                # add the current node to the closed list
                self.closed.append(current_n)

                #remove node from open list as it has alreay been explore in it
                del self.open[0]
                self.open.sort(key = lambda x:x.f_cost,reverse=False)

        return count  

def main():

    print("Enter text name file here")
    file_name= input()

    file_content=open(file_name,"r")

    #find and saved the initial stated for the puzzle
    map=[]
    for x in file_content:
        value=x.split()
        map.append(value)
    
    print("Goal State")
    for x in goal_state:
        print(x)
    print()
    
    #create and start searching solution through A* algorithm
    puzzle=Puzzle_solver()
    total=puzzle.solve_puzzle(map)

    #print solution
    print("Initial State")
    for x in map:
        print(x)
    print("Total cost for solution: ", total)
    
    file_content.close()
    return

main()
