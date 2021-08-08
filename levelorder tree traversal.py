class tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def insert(self,data):
        if(self.data):
            if(data<self.data):
                if(self.left is None):
                    self.left=tree(data)
                else:
                    self.left.insert(data)
            elif(data>self.data):
                if(self.right is None):
                    self.right=tree(data)
                else:
                    self.right.insert(data)
            else:
                self.data=data

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


    def InOrderTraversal(self,root):
        res=[]
        if(root):
            res=self.InOrderTraversal(root.left)
            res.append(root.data)
            res=res + self.InOrderTraversal(root.right)
        return res

    def PreOrderTraversal(self,root):
        res=[]
        if(root):
            res.append(root.data)
            res = res + self.PreOrderTraversal(root.left)
            res = res + self.PreOrderTraversal(root.right)
        return res

    def PostOrderTraversal(self,root):
        res=[]
        if(root):
            res=self.PostOrderTraversal(root.left)
            res=res + self.PostOrderTraversal(root.right)
            res.append(root.data)
        return res

    def LevelOrderTraversal(self,root):
        if root is None:
            return
        queue = []
        queue.append(root)
        while(len(queue) > 0):
            print(queue[0].data,end="-->")
            tree = queue.pop(0)
            if tree.left is not None:
                queue.append(tree.left)
            if tree.right is not None:
                queue.append(tree.right)
                
    def Search(self,root,num):
        queue = []
        queue.append(root)
        while(len(queue) > 0):
            tree = queue.pop(0)
            if(num==tree.data):
                print("found num ",num)
            if tree.left is not None:
                queue.append(tree.left)
            if tree.right is not None:
                queue.append(tree.right)

if __name__=="__main__":
    root = tree(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print(root.InOrderTraversal(root))
    print(root.PostOrderTraversal(root))
    print(root.PreOrderTraversal(root))
    print(root.LevelOrderTraversal(root))
    print(root.Search(root,10))
        










    
        
        
        




