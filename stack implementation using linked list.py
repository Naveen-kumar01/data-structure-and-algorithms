class Node:  
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 

class stack:  
	def __init__(self): 
		self.head = None

	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node  

	def pop(self):
		if self.head is None:
			print("linklist is empty")
		temp=self.head
		self.head=self.head.next
		print()
		print("stack after pop")
		
	def printstack(self): 
		temp = self.head 
		while (temp): 
			print(temp.data,end="->") 
			temp = temp.next

	def peek(self):
	    print()
	    print("the top element is ",self.head.data)

	def Count(self):
		temp=self.head
		c=0
		while(temp != None):
			temp=temp.next
			c+=1

		print()
		print("no. of element are ",c)

if __name__=='__main__':  
	l = stack()  
	l.push(7);  
	l.push(1); 
	l.push(4) 
	l.push(8)
	print('Created stack is:') 
	l.printstack()
	l.peek()
	l.pop()
	l.printstack()
	l.Count()
