# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 20:22:32 2017

@author: fang2
"""


#demonstrates 234 tree

class DataItem:

	def __init__(self, data):	
		self.data = data

	def displayItem(self):	#format " /27"
		print ('/'+str(self.data))
#end class DataItem

class Node:

	minimumdegree = 4
	def __init__(self):
		self.numItems = 0
		self.parent = None
		self.childArray = [None for i in range(4)]	
		self.itemArray = [None for i in range(3)]	


			
	def connectChild(self, childNum, pChild):
		self.childArray[childNum] = pChild
		if pChild:
			pChild.parent = self

			
	def disconnectChild(self, childNum):
		pTempNode = self.childArray[childNum]
		self.childArray[childNum] = None
		return pTempNode

	def getChild(self, childNum):
		return self.childArray[childNum]

	def getParent(self):
		return self.parent

	def isLeaf(self):
		return not self.childArray[0]

	def getNumItems(self):
		return self.numItems

	def getItem(self, index):	
		return self.itemArray[index]

	def isFull(self):
		return self.numItems==self.minimumdegree - 1

	def findItem(self, key):	
		for j in range(self.minimumdegree-1):	
			if not self.itemArray[j]:	
				break	
			elif self.itemArray[j].data == key:	
				return j
		return -1
	

	def insertItem(self, pNewItem):
		
		self.numItems += 1
		newKey = pNewItem.data	

		for j in reversed(range(self.minimumdegree-1)):	#start on right,	#examine items
			if self.itemArray[j] == None:	#if item null,
				pass	#go left one cell
			else:	#not null,
				itsKey = self.itemArray[j].data	#get its key
				if newKey < itsKey:	#if it's bigger
					self.itemArray[j+1] = self.itemArray[j]	#shift it right
				else:
					self.itemArray[j+1] = pNewItem	#insert new item
					return j+1#return index to new item
			#end else (not null)
		#end for 	#shifted all items,
		self.itemArray[0] = pNewItem	#insert new item
		return 0
	#end insertItem()

	def removeItem(self):	#remove largest item
		#assumes node not empty
		pTemp = self.itemArray[self.numItems-1]	#save item
		self.itemArray[self.numItems-1] = None	#disconnect it
		self.numItems -= 1#one less item
		return pTemp#return item

	def displayNode(self):	#format "/24/56/74"
		for j in range(self.numItems):
			self.itemArray[j].displayItem()	#format "/56"
		print ('/')	#final "/"

#end class Node

class Tree234:
	#as private instance variables don't exist in Python,
	#hence using a convention: name prefixed with an underscore, to treat them as non-public part
	def __init__(self):
		self._pRoot = Node()	#root node

	def find(self, key):
		pCurNode = self._pRoot	#start at root
		while True:
			childNumber=pCurNode.findItem(key)
			if childNumber != -1:
				return childNumber	#found it
			elif pCurNode.isLeaf():
				return -1#can't find it
			else:	#search deeper
				pCurNode = self.getNextChild(pCurNode, key)
		#end while

	def insert(self, dValue):	#insert a DataItem
		pCurNode = self._pRoot
		pTempItem = DataItem(dValue)

		while True:
			if pCurNode.isFull():	#if node full,
				self.split(pCurNode)	#split it
				pCurNode = pCurNode.getParent()	#back up
					#search once
				pCurNode = self.getNextChild(pCurNode, dValue)
			#end if(node is full)

			elif pCurNode.isLeaf():	#if node is leaf,
				break	#go insert
			#node is not full, not a leaf; so go to lower level
			else:
				pCurNode = self.getNextChild(pCurNode, dValue)
		#end while
		pCurNode.insertItem(pTempItem)	#insert new item
	#end insert()

	def split(self, pThisNode):	#split the node
		#assumes node is full
		
		pItemC = pThisNode.removeItem()	#remove items from
		pItemB = pThisNode.removeItem()	#this node
		pChild2 = pThisNode.disconnectChild(2)	#remove children
		pChild3 = pThisNode.disconnectChild(3)	#from this node

		pNewRight = Node()	#make new node

		if pThisNode == self._pRoot:	#if this is the root,
			self._pRoot = Node()	#make new root
			parent = self._pRoot	#root is our parent
			self._pRoot.connectChild(0, pThisNode)	#connect to parent
		else:	#this node not the root
			parent = pThisNode.getParent()	#get parent

		#deal with parent
		itemIndex = parent.insertItem(pItemB)	#item B to parent
		n = parent.getNumItems()	#total items?

		j = n-1#move parent's
		while j > itemIndex:	#connections
			pTemp = parent.disconnectChild(j)	#one child
			parent.connectChild(j+1, pTemp)	#to the right
			j -= 1
				#connect newRight to parent
		parent.connectChild(itemIndex+1, pNewRight)

		#deal with newRight
		pNewRight.insertItem(pItemC)	#item C to newRight
		pNewRight.connectChild(0, pChild2)	#connect to 0 and 1
		pNewRight.connectChild(1, pChild3)	#on newRight
	#end split()

	#gets appropriate child of node during search of value
	def getNextChild(self, pNode, theValue):
		#assumes node is not empty, not full, not a leaf
		numItems = pNode.getNumItems()
		
		for j in range(numItems):	#for each item in node
			if theValue < pNode.getItem(j).data:	#are we less?
				return pNode.getChild(j)	#return left child
		else:	#end for 	#we're greater, so
			return pNode.getChild(j + 1)	#return right child

	def displayTree(self):
		self.recDisplayTree(self._pRoot, 0, 0)

	def recDisplayTree(self, pThisNode, level, childNumber):
         print ('level='+str(level)+' child= ', str(childNumber))
         print("----------------------------------------------")
         pThisNode.displayNode()	#display this node

		#call ourselves for each child of this node
         numItems = pThisNode.getNumItems()
         for j in range(numItems+1):
             pNextNode = pThisNode.getChild(j)
             if pNextNode:
                 self.recDisplayTree(pNextNode, level+1,childNumber)
        
			return
	#end recDisplayTree()
#end class Tree234

pTree = Tree234()
pTree.insert(50)
pTree.insert(40)
pTree.insert(60)
pTree.insert(30)
pTree.insert(70)
pTree.displayTree()

##as Python doesn't support switch, simulating the same with dictionary and functions
#def show():
#	pTree.displayTree()
#
#def insert():
#	value = int(raw_input('Enter value to insert: '))
#	pTree.insert(value)
#
#def find():
#	value = int(raw_input('Enter value to find: '))
#	found = pTree.find(value)
#	if found != -1:
#		print 'Found', value
#	else:
#		print 'Could not find', value
#
#case = { 's' : show,
#	'i' : insert,
#	'f' : find}
##switch simulation completed
#
#while True:
#	print
#	choice = raw_input('Enter first letter of show, insert, or find: ')
#	if case.get(choice, None):
#		case[choice]()
#	else:
#		print 'Invalid entry'
##end while
#del pTree
##end