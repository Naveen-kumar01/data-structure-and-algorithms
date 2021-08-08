class Node:
        def __init__(self, data):
                        self.data=data
                        self.next=None

class CLL:
        def __init__(self):
                self.head=None

        def push(self, data):
                ptr1 = Node(data)
                temp = self.head 
                ptr1.next = self.head
 
                if self.head is not None:
                        while(temp.next != self.head):
                                temp = temp.next
                        temp.next = ptr1
 
                else:
                        ptr1.next = ptr1
 
                self.head = ptr1

        def insertatend(self,data):
                temp=self.head
                ptr1=Node(data)
                ptr1.next=self.head

                while(temp.next != self.head):
                        temp=temp.next
                temp.next=ptr1

        def deleteatbeg(self):
                if(self.head==None):
                        print("linl list is empty")
                temp=self.head
                ptr=self.head
                while(temp.next!=self.head):
                        temp=temp.next
                self.head=ptr.next
                temp.next=ptr.next

        def deleteatend(self):
                                if self.head is None:
                                        print("linklist is empty")
                                        return
                                cur=self.head
                                prev=self.head
                                ptr=self.head
                                while(cur.next!=self.head):
                                                prev=cur
                                                cur=cur.next
                                prev.next=ptr
                
                
        def printList(self):
                temp = self.head
                print("\nTraversal in forward direction")
                if self.head is not None:
                        while(True):
                                print(temp.data,end="->")
                                temp = temp.next
                                if (temp == self.head):
                                        break

if __name__=='__main__':
        cl=CLL()
        cl.push(10)
        cl.push(20)
        cl.insertatend(50)
        cl.insertatend(90)
        cl.insertatend(100)
        cl.printList()
        cl.deleteatbeg()
        cl.printList()
        cl.deleteatend()
        cl.printList()
