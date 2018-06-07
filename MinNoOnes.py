def MinNoOnes(a,low,high):
    if low>high:
        return -1
    else:
        mid=int((low+high)/2)
        if(a[low]==1):
            return low
        if a[mid]==0:
            return MinNoOnes(a,mid+1,high)
        else:
            return MinNoOnes(a,low,mid)
#
# a=[0,1,1,1,1,1,1,1,1]
# n=len(a)-1
# val=MinNoOnes(a,0,n)
# num=n-val+1
# print(num)

list=[[0,0,1],[0,0,1,1,1,1,1],[0,0,1]]
minimum=[]
def findones(list):
    for i in range(0,len(list)):
        n=len(list[i])-1
        index=MinNoOnes(list[i],0,n)
        if(index!=-1):
            num=n-index+1
            minimum.append(num)
        else:
            minimum.append(-1)
findones(list)
val=minimum.index(min(minimum))
print(val)
# for i,ele in enumerate(min):
