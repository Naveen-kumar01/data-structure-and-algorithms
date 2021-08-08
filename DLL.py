class Node:
        def __init__(self,data):
                        self.data=data
                        self.next=None
                        self.prev=None

class DLL:
        def __init__(self):
                        self.head=None

        def push(self,new_data):
                        new_node=Node(new_data)
                        new_node.next=self.head
                        new_node.prev=None
                        if(self.head is not None):
                                        self.head.prev=new_node
                        self.head=new_node

        def insertAfter(self,new_data,pos):
                        new_node = Node(new_data)
                        if(pos<1):
                                        print("no such position available in linklist")
                        elif(pos==1):
                                        newNode.next = self.head;
                                        self.head.prev = newNode;
                                        self.head = newNode;
                        else:
                                        temp = self.head 
                                        for i in range(1,pos-1):
                                                        if(temp!=None):
                                                                        temp=temp.next
                        if(temp!=None):
                                        new_node.next = temp.next
                                        new_node.prev = temp
                                        temp.next = new_node
                        if (new_node.next is not None):
                                        new_node.next.prev = new_node
                        else:
                                        print("\nThe previous node is null.")

        def pushatend(self,new_data):
                        new_node=Node(new_data)
                        temp=self.head
                        while(temp.next!=None):
                                        temp=temp.next
                        new_node.prev = temp
                        temp.next=new_node
                        new_node.next=None

        def deleteathead(self):
                        if(self.head is None):
                                        print("list is empty")
                        temp=self.head
                        temp1=self.head.next
                        self.head = temp1
                        temp1.prev = None

        def deleteatpos(self, key, pos):
                temp=self.head
                prev=self.head
                if(pos==1 and temp.data==key):
                        self.head=temp.next
                        temp.next.prev=None
                elif(self.head is None):
                        print("list is empty")
                else:
                        while(temp.next!=None):
                                if(temp.data==key):
                                        break
                                prev=temp
                                temp=temp.next
                                prev.next=temp.next
                                temp.next.prev=temp.prev
        def deleteatend(self):
                temp=self.head
                while temp.next is not None:
                        temp=temp.next
                temp.prev.next=None

        def printList(self, node):

                        print("\nTraversal in forward direction")
                        while(node is not None):
                                        print(node.data,end="->")
                                        node = node.next

if __name__=='__main__': 
        l = DLL() 
        l.push(6)
        l.push(8)
        l.push(21)
        l.push(1)
        l.insertAfter(29,4)
        l.pushatend(50)
        l.printList(l.head)
        l.deleteathead()
        l.printList(l.head)
        l.deleteatpos(8,2)
        l.printList(l.head)
        l.deleteatend()
        l.printList(l.head)
                        
        
