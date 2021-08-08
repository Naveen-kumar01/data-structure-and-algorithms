class queue:
    def __init__(self):
        self.item=[]
    def isempty(self):
        if(self.item==[]):
            return self.item==[]
    def add(self,data):
        self.item.append(data)
    def pop(self):
        return self.item.pop(0)
    def front(self):
        return self.item[0]
    def print(self):
        print(*self.item,sep="->")

def reverse(q):
    if(q.isempty()):
        return
    x=q.front()
    q.pop()
    reverse(q)
    q.add(x)
    
if __name__=="__main__":
    q = queue() 
    q.add(56) 
    q.add(27) 
    q.add(30) 
    q.add(45) 
    q.add(85) 
    q.add(92) 
    q.add(58) 
    q.add(80) 
    q.add(90) 
    q.add(100) 
    reverse(q) 
    q.print() 
