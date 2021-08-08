class Node:  
    def __init__(self, data): 
	    self.data = data # Assign data 
	    self.next = None # Initialize next as null 

class LinkedList:  
    def __init__(self): 
	    self.head = None

    def push(self, new_data): 
	    new_node = Node(new_data) 
	    new_node.next = self.head 
	    self.head = new_node 

    def insertAfter(self, prev_node, new_data): 

	    if prev_node is None: 
		    print("The given previous node must in LinkedList.")
		    return
	    new_node = Node(new_data) 
	    new_node.next = prev_node.next
	    prev_node.next = new_node 

    def append(self, new_data): 
	    new_node = Node(new_data) 
	    if self.head is None: 
		    self.head = new_node 
		    return
	    last = self.head
	    while (last.next): 
		    last = last.next
	    last.next = new_node
			    
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

    def rotate(self, k):
        temp=self.head
        temp1=self.head
        temp2=self.head
        c=1
        while(c <k and temp is not None):
                temp=temp.next
                c+=1
        temp1= temp
        while(temp.next!=None):
            temp=temp.next
        temp2 = temp
        temp2.next= self.head
        self.head= temp1.next
        temp1.next=None

if __name__=='__main__': 
    l = LinkedList()
    l.append(6)
    l.push(7); 
    l.push(1); 
    l.append(4) 
    l.insertAfter(l.head.next, 8)
    l.printList()
    l.rotate(2)
    print('Created linked list is:',) 
    l.printList()
