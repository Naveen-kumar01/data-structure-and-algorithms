s="ababbc"
l=[]
dict={}
dict1={}
res = [s[i: j] for i in range(len(s)) 
          for j in range(i + 1, len(s) + 1)]
for i in res:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)
for i in dict:
    if(len(i)>1 and dict[i]>=2):
        l.append(i)
max=0
ans=""
for i in l:
    if(len(i)>max):
        max=len(i)
        ans=i
print(ans)
   
