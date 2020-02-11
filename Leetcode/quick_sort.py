#quicksort python


def partition(input,start,end):
    pivot = input[end-1]
    i = start-1
    for j in range (start,end-1):
        if input[j] <= pivot:
            i+=1
            input[i],input[j]=input[j],input[i]
    input[i+1],input[end-1]=input[end-1],input[i+1] 
    return i+1

def sort(input,start,end):
    if start < end-1:
        ans=partition(input,start,end)
        sort(input,start,ans)
        sort(input,ans+1,end)
    

list = [1,5,1,14,6,1,6,8]
sort(list, 0, len(list))
print (list)    

