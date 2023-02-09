class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,capacity):
        self.capacity = capacity
        self.front = None
        self.rear = None
        self.size = 0

    def __str__(self):
        print('<<<- front <- ',end='')
        a = self.front
        while a:
            print(a.value,'<- ',end='')
            a = a.next
        return 'rear <<<-'

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

    def enqueue(self,val):
        temp = Node(val)
        if self.isFull():
            print('Queue is Full')
            return
        if self.front is None:
            self.rear = self.front = temp
            self.front.next = self.rear
        else:
            self.rear.next = temp
            self.rear = temp
        self.size += 1
        
    def dequeue(self):
        if self.isEmpty():
            return 
        else:
            temp = self.front.next
            self.front = temp
            self.size -= 1
        if self.isEmpty():
            self.rear = None
            self.front = None
        
    
    def getfront(self):
        if self.isEmpty():
            return 'Queue is Empty'
        else:
            return self.front.value
        
    def getrear(self):
        if self.isEmpty():
            return 'Queue is Empty'
        else:
            return self.rear.value
        


Q = Queue(10)
print(Q.isEmpty())
L = [0,1,2,3,4,5,6,7,8,9,10]
for i in L:
    Q.enqueue(i)
print(Q)
Q.dequeue()
print(Q)
print(Q.getfront())

print(Q.getrear())

print(Q.isFull())