class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        if self.value is not None:
            return str(self.value) + ' -> '
        else:
            return ''

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head is None: # LinkedList is empty
            return 'Head -> Tail'
        else:
            a = self.head 
            print('Head -> ', end='')
            while a is not None:
                print(a, end='')
                a = a.next
            if a is not None:
                print(a, end='')
            return 'Tail'

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
            new.next = a
        else:
            index = 0
            b = a
            while a and index < position-1:
                index += 1
                b = a
                a = a.next
            if a is None: # insert at last
                b.next = new
                new.next = self.tail
            else:
                n = a.next 
                a.next = new
                new.next = n

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
                a.next = a.next.next

lst = [1,2,3,4,5,6]
LL = LinkedList()
for element in sorted(lst,reverse=True):
    LL.insert(element)
    print(LL)
LL.insert(1.5,1)
print(LL)

LL.search(2)

LL.insert(1000,7)
print(LL)

LL.delete(7)
print(LL)

LL.delete(1)
print(LL)