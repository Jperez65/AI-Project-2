# Assingment 2: Problem 2

## Compiling the program

To compile file you must have python 3.8.5 ver installed in your system environment or use any other IDE programs. 
After that you must go to the directory where the program is located and write 

'''bash 
python Project2.py
'''

to your console terminal

## Running the program

Before running the program you must have a text file in the same directory folder with the program before running it. The text file content must follow the format of 8-puzzle layout. Example:

'''text
1 2 3
8 0 4
7 6 5
'''
After running the program it will output a message to enter the name of the txt file. Ex: 

'''text
Enter text name file here
sample.txt
'''

Next it will output the total numbers of move set cost needed to solve the 8-puzzle from initial state to goal state. Example:

'''text
Goal State
[1, 2, 3]
[8, 0, 4]
[7, 6, 5]

Initial State
['1', '3', '4']
['8', '0', '6']
['7', '5', '2']
Total cost for solution:  30
'''

## classes and function

The file has two classes that recreates the graph traversal of A* alorithm:
### Class Node
The class node represent a single node in the tree where it posses the state at such node, the path cost in getting to the node, and the final cost that combines the heuristic and path cost.

##### create_frontier
Function that produces a list nodes that represent the frontier or "children" from one node. 

##### create_state
Function create and return a new state based on the move action and its cost of moving it

##### copy_state
Takes a list that contain a then copy it to a new list and return back a whole new copy

### class Puzzle_solver

The class Puzzle_solver contains the main working for a* algorithm

##### f_find
Function finds the total value cost by combining the heuristic and path cost from node given in its parameter

##### check_list
Function that will search inside the closed list varibale whether the current state giving exist or not.

##### h_find 
Function finds the heuristic value from giving node

##### solve_puzzle
Primary function that initiates to solve the 8-puzzle by a* algorithm


### Author
Josue Perez

