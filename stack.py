class Stack:
    def __init__(self) -> None:
        self.arr = []

    def __str__(self):
        print('top','^',sep='\n')
        for i in self.arr[::-1]:
            print(str(i),'^',sep='\n')
        return 'bottom'

    def isEmpty(self):
        return len(self.arr) == 0
    
    def push(self,ele):
        self.arr.append(ele)

    def pop(self):
        if self.isEmpty():
            print('Empty Stack')
            return -1
        else:
            return self.arr.pop()
    
    def size(self):
        return len(self.arr)

S = Stack()
L = [1,2,3,4]
for i in L:
    S.push(i)
print(S)

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def __str__(self):
        print('top','^',sep='\n')
        a = self.top
        while a:
            print(a.value,'^',sep='\n')
            a = a.next
        return 'bottom'

    def isEmpty(self):
        if self.top.value is None:
            return True
        else:
            return False
    
    def push(self,ele):
            new = Node(ele)
            new.next = self.top
            self.top = new
        
    def pop(self):
        if self.isEmpty():
            print('Empty Stack')
            return -1
        else:
            removed = self.top
            self.top = self.top.next
            return removed

    def size(self):
        c = 0
        a = self.top
        if a is None:
            return c
        while a:
            c += 1
            a = a.next
        return c

S = Stack()
L = [1,2,3,4]
for i in L:
    S.push(i)
print(S)

print(S.size())
