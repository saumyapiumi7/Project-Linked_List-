import Node


class DoublyLinkedList:
    def init(self):  # defining variable
        self.head = None  # initially first node is none
        self.tail = None  # initially last node is none
        self.length = 0  # initially doubly linked list length is zero

    # Doubly Linked List length size
    def doublyListLength(self):
        current = self.head  # create current as head node
        count = 0  # creating count as zero
        while current is not None:  # traversing until current node is none
            count += 1
            current = current.getNext()  # change next of current as current
        return count

    # this function print contend of all doubly linked
    def printForwardList(self):
        if self.head is None:  # checking head node is none
            print("Empty Doubly Linked List")
        else:
            current = self.head
            while current is not None:  # traversing until current node is none
                print(current.getData(), end=" ")  # print data of current node
                current = current.getNext()  # change next of current as current

    # this function print to reverse contend of all doubly linked
    def printBackwardList(self):
        if self.head is None:  # checking head node is none
            print("Empty Doubly Linked List")
        else:
            current = self.head
            while current.getNext() is not None:  # traversing until next of current is none
                current = current.getNext()  # change next of new node as current
            while current is not None:  # traversing until current is none
                print(current.getData(), end=" ")  # print data of current
                current = current.getPrev()  # change previous of current as current

    # add new node to the beginning
    def addNodeBeginning(self, data):
        newNode = Node(data)
        newNode.setData(data)
        if self.head is None:  # checking head Node is Node
            self.head = newNode  # create new node as head node
        else:
            newNode.setNext(self.head)  # create next of new node as head node
            self.head.setPrev(newNode)  # create previous of head node as newNode
            newNode.setPrev(None)  # create previous of new node as none
            self.head = newNode  # change new node as head node
        self.length += 1  # adding one to length

    # add new node to the end of the doubly linked list
    def addNodeEnd(self, data):
        newNode = Node(data)
        newNode.setData(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.getNext() is not None:  # traversing until next of current is none
                current = current.getNext()  # change next of current as current
            current.setNext(newNode)  # create next of current as new node
            newNode.setPrev(current)  # create previous of new node as current
            newNode.setNext(None)  # create next of new node as none
        self.length += 1

    # add new node to given position of the doubly linked list
    def addNodeInPos(self, pos, data):
        # checking position is greater than length mines one or position is less than zero
        if pos > self.length - 1 or pos < 0:
            return None
        elif pos == self.length - 1:  # checking position is equal to length mines one
            self.addNodeEnd(data)  # running addNodeEnd function
        elif pos == 0:  # checking position is equal to zero
            self.addNodeBeginning(data)  # running addNodeBeginning function
        else:
            newNode = Node(data)
            newNode.setData(data)
            current = self.head
            count = 0
            while count != pos - 1:  # traversing until the previous node before the position
                current = current.getNext()  # change next of current as current
                count += 1
            newNode.setPrev(current)  # create previous of new node as current
            newNode.setNext(current.getNext())  # create next of new node as next of current
            current.getNext().setPrev(newNode)  # create previous of next in current as new node
            current.setNext(newNode)  # create next of current as new node
        self.length += 1

    # delete first node of the doubly linked list
    def deleteFirstNode(self):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            self.head = self.head.getNext()  # change next of head as head
            self.head.setPrev(None)  # create previous of head as none
        self.length -= 1

    # delete last node of the doubly linked list
    def deleteLastNode(self):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            current = self.head
            previous = None  # create previous node as none
            while current.getNext() is not None:  # traversing until next of current is none
                previous = current  # change current as previous
                current = current.getNext()  # change next of current as current
            previous.setNext(None)  # create next of previous as none
        self.length -= 1

    # delete given position node
    def deleteNodeByPos(self, Pos):
        if self.head is None:
            print("Empty Doubly Linked List")
            return None
        if self.length > Pos > -1:  # checking length greater than position and one mines less than position
            if Pos == 0:  # checking position is equal to zero
                self.deleteFirstNode()  # running deleteFirstNode function
            elif Pos == self.length - 1:  # checking position is equal to length mines one
                self.deleteLastNode()  # running deleteLastNode function
            else:
                count = 0
                current = self.head
                while count != Pos - 1:  # traversing until the previous node before the position
                    count += 1
                    current = current.getNext()  # change next of current as current
                # create a deleteNode variable and next of current assign it
                deleteNode = current.getNext()
                current.setNext(deleteNode.getNext())  # create next of deleteNode as next of current
                current.getNext().setPrev(current)  # create previous of next in current as current
            self.length -= 1

    # search element of doubly linked list
    def searchValue(self, value):
        if self.head is None:
            print("Empty Doubly Linked List")
        else:
            current = self.head
            count = 0
            while current is not None:  # traversing until current node is none
                if current.getData() == value:  # checking search element equal to data of current node
                    print("This value Position is :", count)  # print count number

                    # printing next node and previous node to search value node

                    if current.getNext() is None:  # checking next of current node is none
                        # assign data of previous in current node to currentPrev variable
                        currentPrev = current.getPrev().getData()
                        currentNext = "None"  # assign "None" string to currentNext variable

                    elif current.getPrev() is None:  # checking previous of current node is none
                        currentPrev = "None"  # assign "None" string to currentPrev variable
                        # assign data of next in current node to currentNext variable
                        currentNext = current.getNext().getData()
                    else:
                        # assign data of previous in current node to currentPrev variable
                        currentPrev = current.getPrev().getData()
                        # assign data of next in current node to currentNext variable
                        currentNext = current.getNext().getData()

                    # print next and previous node
                    print("\nPrevious Node is\t: {} \nNext Node is\t\t: {}".format(currentPrev, currentNext))
                current = current.getNext()  # change next of current as current
                count += 1