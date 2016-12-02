class Node:                           #Class to create node
  def __init__(self, value):
    self.value=value


class Graph:                           #stored here in dict
  def __init__(self):
    self.dict = {}                    #dict

  def addnode(self, value):           #function to addnode
  	node = Node(value)                #node=node value

  	self.dict[node.value] = []             #dict node value =[]
  
  def addedge(self, value, neighbour):         #function to add edges 
  	self.dict[value].append(neighbour)         #dict value append to neighbour
  	self.dict[neighbour].append(value)         #do the reverse so theyre both linked if a linked with c c must be linked to a
  def printValues(self):                       #print value function
  	print(self.dict)


Create_node = Graph()
Create_node.addnode('A')                  #add nodes
Create_node.addnode('B')
Create_node.addnode('C')
Create_node.addnode('D')
Create_node.addnode('E')
Create_node.addnode('F')
Create_node.addnode('G')
Create_node.addnode('H')
Create_node.addnode('I')
Create_node.addnode('J')


Create_node.addedge('A', 'C')                               #addedges
Create_node.addedge('B', 'C')
Create_node.addedge('D', 'C')
Create_node.addedge('E', 'C')
Create_node.addedge('A', 'B')
Create_node.addedge('A', 'D')
Create_node.addedge('H', 'I')
Create_node.addedge('I', 'C')

Create_node.printValues()
