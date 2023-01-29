class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.prev = None

    def __str__(self):
        if self.value is not None:
            return str(self.value) + ' <-> '
        else:
            return ''

class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        a = self.head 
        if a is None: # LinkedList is empty
            return 'Head <-> Head'
        else:
            print('Head <-> ', end='')
            while a.next != self.head:
                print(a, end='')
                a = a.next
                if a == a.next:
                    break    
            print(a, end='')
            return 'Head'

    def search(self, value):
        a = self.head
        while a.next != self.head: # Hoover through each element
            if a.value == value:
                print('Element Found')
                return True # if value is found
            a = a.next
            if a == self.head:
                break
        print('Element Not Found')
        return -1 # if value is not found

    def insert(self, value, position=0):
        a = self.head
        new = Node(value)
        if a is None: # LinkedList is empty
            self.head = new
            new.next = new
            new.prev = new
        elif position == 0: # Default insert at position- 0 (Head)
            p = a.prev
            self.head = new
            a.prev = self.head
            new.next = a
            new.prev = p
        else:
            index = 0
            b = a
            a = a.next
            while index < position-1:
                index += 1
                b = a
                a = a.next
                if a == self.head:  # position greater than last , insert at last
                    a.prev = new
                    b.next = new
                    new.prev = b
                    new.next = a
                    return
            b.next = new
            new.next = a
            a.prev = new
            new.prev = b

    def delete(self, position=0):
        a = self.head
        if a == a.next: # CLL contains only 1 element, delete head
            a.value = None
            return
        elif position == 0: # Default delete at position- 0 (Head)
            old_head = a
            self.head = a.next
            a = self.head
            b = a
            a = a.next
            while a != old_head:
                b = a
                a = a.next
            b.next = self.head
        else:
            index = 0
            old_head = a
            b = a
            while index < position-1:
                index += 1
                b = a
                a = a.next
                if a == old_head: # position greater than LL, delete last
                    b.value = None
            # delete element at specified position
            b.next = a.next
   
lst = [1,2,3,4,5,6]
DCLL = DoublyCircularLinkedList()
for element in sorted(lst,reverse=True):
    DCLL.insert(element)
    print(DCLL)

DCLL.insert(1.5,1)
print(DCLL)

DCLL.search(2)

DCLL.insert(1000,7)
print(DCLL)


# print('delete last')
# DCLL.delete(8)
# print(DCLL)

# DCLL.delete(1)
# print(DCLL)
# for i in range(len(lst)):
#     DCLL.delete()
#     print(DCLL)

