class Node:
    #constructor
    def init(self,data):
        self.item = data
        self.next = None
        self.prev = None

    # set data of the Node
    def setData(self, data):
        self.data = data

    # get data of this Node
    def getData(self):
        return self.data

    # get data of this Node
    def getNext(self):
        return self.next

    # set next data of the Node
    def setNext(self, ind1):
        self.next = ind1

    # get previous data of the Node
    def getPrev(self):
        return self.prev

    # set previous data of the Node
    def setPrev(self, ind2):
        self.prev = ind2

    # get if it has a Next
    def hasNext(self):
        return self.next is not None

    # get if it has a Previous
    def hasPrev(self):
        return self.prev is not None
