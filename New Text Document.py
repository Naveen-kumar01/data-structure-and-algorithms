class Queue(object):
    def __init__ (self, c):
        self.Q = []
        self.front = self.rear = 0
        self.size = c

    def isEmpty(self):
        return self.size < 0

    def enqueue(self, data):
        if(self.rear == self.size):
            print('Queue is full')
            return
        else:
            self.Q.append(data)
            self.rear+=1

    def dequeue(self):
        if(self.rear== self.front):
            print("queue is empty")
        else:
            x=self.Q.pop(0)
            self.rear-=1

    def display(self):
        if(self.front==self.rear):
            print("queue is empty")
        for i in range(0,len(self.Q)):
            print(self.Q[i],"<--",end=" ")

    def queueFront(self):   
        if(self.front == self.rear): 
            print("\nQueue is Empty")
        else:
            print("\nFront Element is:",  
              self.Q[self.front])

if __name__=="__main__":
    q=Queue(4)
    q.display()  
    q.enqueue(20) 
    q.enqueue(30) 
    q.enqueue(40) 
    q.enqueue(50)
    q.display()  
    q.enqueue(60)
    q.display() 
    q.dequeue() 
    q.dequeue() 
    print("\n\nafter two node deletion\n")
    q.display()
    q.queueFront() 

