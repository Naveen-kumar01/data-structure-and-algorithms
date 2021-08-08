class Node:  
	def __init__(self, data): 
		self.data = data  
		self.next = None 

class LinkedList:  
	def __init__(self): 
		self.head = None

	def push(self, new_data): 
		new_node = Node(new_data) 
		new_node.next = self.head 
		self.head = new_node 

	def insertAfter(self, key, pos, new_data):
		new_node=Node(new_data)
		temp=self.head
		if(pos<1):
			print("no such position available in linklist")
		elif(pos==1):
			new_node.next = self.head
			self.head = new_node
		else:
			while(temp.data!=key):
				temp=temp.next
			new_node.next=temp.next
			temp.next=new_node
 
	def append(self, new_data): 
		new_node = Node(new_data) 
		if self.head is None: 
			self.head = new_node 
			return
		last = self.head
		while (last.next): 
			last = last.next
		last.next = new_node

	def deletefrombeginning(self):
		if self.head is None:
			print("linklist is empty")
		temp=self.head
		self.head=self.head.next

	def deleteFromEnd(self):
		if self.head is None:
			print("linklist is empty")
			return
		cur=self.head
		prev=self.head
		while(cur.next!=None):
			prev=cur
			cur=cur.next
		prev.next=None

	def deletefrompos(self,key):
		if (self.head is None):
			print("linklist is empty")
			return
		temp=self.head
		while(temp!= None):
			if(temp.data==key):
				break
			prev=temp
			temp=temp.next
		prev.next=temp.next
		temp=None
				
		
		
	def printList(self): 
		temp = self.head 
		while (temp): 
			print(temp.data,end="->") 
			temp = temp.next

	def Count(self):
		temp=self.head
		c=0
		while(temp != None):
			temp=temp.next
			c+=1

		print()
		print("no. of element are ",c)

if __name__=='__main__': 

	# Start with the empty list 
	l = LinkedList() 

	# Insert 6. So linked list becomes 6->None 
	l.append(6) 

	# Insert 7 at the beginning. So linked list becomes 7->6->None 
	l.push(7); 

	# Insert 1 at the beginning. So linked list becomes 1->7->6->None 
	l.push(1); 

	# Insert 4 at the end. So linked list becomes 1->7->6->4->None 
	l.append(4) 

	# Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None 
	l.insertAfter(6,3, 8)
	l.printList()

	l.deletefrompos(8)

	print('Created linked list is:') 
	l.printList()
	l.Count()
