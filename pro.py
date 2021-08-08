class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def show(self):
        print(*self.items,sep="")
    
s = Stack()
text = input('Please enter the string: ') 
for character in text:
    if(s.is_empty()):
        s.push(character)
    elif(s.peek()==character):
        s.pop()
    else:
        s.push(character)
print(s.show())
