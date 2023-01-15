class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        if self.value is not None:    
            return str(self.value) + ' <-> '
        else:
            return ''

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head is None: # DoublyLinkedList is empty
            return 'Head <-> Tail'
        else:
            a = self.head
            print('Head <-> ', end='')
            while a.next is not None:
                print(a, end='')
                a = a.next
            if a.value is not None:
                print(a, end='')
            return 'Tail'

    def reverseTraveral(self):
        if self.tail is None: # DoublyLinkedList is empty
            return 'Tail <-> Head'
        else:
            z = self.tail
            y = z
            print('Tail <-> ', end='')
            print(z, end='')
            while z.prev is not None:
                z = z.prev
                print(z, end = '')
            return 'Head'

    def search(self, value):
        a = self.head
        while a is not None: # Hoover through each element
            if a.value == value:
                print('Element Found')
                return True # if value is found
            a = a.next
        print('Element Not Found')
        return -1 # if value is not found

    def insert(self, value, position=0):
        a = self.head
        new = Node(value)
        if a is None: # LinkedList is empty
            self.head = new
            self.tail = new
        elif position == 0: # Default insert at position- 0 (Head)
            self.head = new
            a.prev = new
            new.next = a
        else:
            index = 0
            b = a
            while a and index < position-1:
                index += 1
                b = a
                a = a.next
            if a is None: # Insert at last
                new.next = self.tail
                b.next = new
                new.prev = b
            else:   
                n = a.next
                a.next = new
                new.prev = a
                new.next = n
                a.next.prev = new

    def delete(self, position=0):
        a = self.head
        if position == 0: # Default delete at position- 0 (Head)
            self.head = a.next
        else:
            index = 0
            b = a
            while a and index < position-1:
                index += 1
                b = a
                a = a.next
            if a is None: # position greater than LL
                b.value = None
            else: # delete element at specified position
                n = a.next.next
                a.next = n

lst = [1,2,3,4,5,6]
DLL = DoublyLinkedList()
for element in sorted(lst,reverse=True):
    DLL.insert(element)
    print(DLL)
DLL.insert(1.5,1)
print(DLL)

DLL.search(2)

DLL.insert(1000,7)
print(DLL)

DLL.delete(9)
print(DLL)

DLL.delete(1)
print(DLL)
print('reverse traverse')
print(DLL.reverseTraveral())
