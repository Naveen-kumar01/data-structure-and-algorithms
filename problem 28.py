def nextGreatest(list):
    size=len(list)
    max_from_right=list[size-1]
    list[size-1]=-1
    for i in range(size-2,-1,-1):
        temp = list[i] 
        list[i] = max_from_right
        if(max_from_right < temp):
            max_from_right = temp
def printArray(arr): 
    for i in range(0,len(list)): 
        print(list[i],end=" ") 
  
# Driver function to test above function 
list=[16, 17, 4, 3, 5, 2] 
nextGreatest(list) 
print("Modified array is ")
printArray(list)
