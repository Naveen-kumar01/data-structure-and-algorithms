class Stack(object):
    def __init__(self, limit=0):
        self.stk = limit*[None]
        self.limit = limit
    def isEmpty(self):
        if(len(self.stk)<=0):
            return
    def push(self, item):
        if(len(self.stk) >= self.limit):
            self.resize()
            self.stk.append(item)
            print('Stack after increase in array size and push is ',*self.stk,sep=" ")

    def pop(self):
        if(len(self.stk) <= 0):
            print('Stack Underflow!')
            return 0
        else:
            print("poped element is ")
            return self.stk.pop()
        
    def peek(self):
        if(len(self.stk)<0):
            print('Stack Underflow')
        else:
            print("top element is ")
            return self.stk[-1]
    def resize(self):
        newstk=list(self.stk)
        self.limit=2*self.limit
        self.stk=newstk
            
    def size(self):
        print("length of stack is ")
        return len(self.stk)
if __name__=="__main__":
    s=Stack()
    s.push("1")
    s.push("2")
    s.push("14")
    s.push("31")
    s.push("19")
    s.push("3")
    s.push("99")
    s.push("9")
    print(s.peek())
    print(s.pop())
    print(s.peek())
    print(s.pop())
    print(s.size())
