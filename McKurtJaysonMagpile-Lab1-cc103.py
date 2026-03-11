class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node('This song by Conan gray')
print(node1.data)

def insertNodeAtTheBeginning(data):
    global head
    newNode = Node(data)

    if(head == None):
        head == newNode
    else:
        newNode.next = head
        head = newNode

node1 = Node('This song by conan gray ')
head = node1

insertNodeAtTheBeginning('kanelang mata by cup of joe')


def traverseLinkedList():
    current = head
    while(current):
        print(current.data, end=" -> ")
        current = current.next



def insertNodeAtTheEnd(data):
    global head
    newNode = Node(data)
    

    if(head == None):
        head = newNode
    else:
        current = head
        while(current.next != None):
            current = current.next
        current.next = newNode

def insertNodeAfterGivenNode(data, node):
    newNode = Node(data)
    global head

    if(head == None):
        head == newNode
    else:
        current = head
        prev = head

        while(prev.data != Node):
            prev = current.next
            current = current.next

            if(current == None):
                print('The node does not exist')
                return
            
    newNode.next = current
    prev.next = newNode

insertNodeAtTheBeginning('wine by cup of joe')
traverseLinkedList()
insertNodeAtTheBeginning('mag isa muli by cup of joe')
traverseLinkedList()
insertNodeAtTheBeginning('saan by maki')
traverseLinkedList()
insertNodeAtTheBeginning('bakit by maki')
traverseLinkedList()
insertNodeAtTheEnd('null')
traverseLinkedList


