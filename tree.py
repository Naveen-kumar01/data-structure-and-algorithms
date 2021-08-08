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
        print( self.data)
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

    
    def Max(self,root):
        res=[]
        if(root):
            res.append(root.data)
            res = res + self.PreOrderTraversal(root.left)
            res = res + self.PreOrderTraversal(root.right)
        return max(res)

    def LevelOrderTraversal(self,root):
        max = 0
        if root is None:
            return
        queue = []
        queue.append(root)
        while(len(queue) > 0):
            tree = queue.pop(0)
            if(tree.data>max):
                max=tree.data
            if tree.left is not None:
                queue.append(tree.left)
            if tree.right is not None:
                queue.append(tree.right)
        print("largest number is ") 
        print(max,end=" ")
    
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
    print(root.Max(root))
    root.LevelOrderTraversal(root)
        










    
        
        
        
