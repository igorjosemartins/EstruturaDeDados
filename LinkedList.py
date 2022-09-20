from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.nextData = None 

class LinkedList:
    def __init__(self):
        self.head = None

    def atBegining(self, data):
        newData = Node(data)
        newData.nextData = self.head
        self.head = newData
    
    def printlist(self):
        printedNode = self.head
        while printedNode is not None:
            print(printedNode.data)
            printedNode = printedNode.nextData


list = LinkedList()
list.atBegining(10)
list.atBegining(5)
list.atBegining(1)
list.atBegining(3)

list.printlist()
