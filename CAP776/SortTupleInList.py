def middle(n):
    return n[1]
if __name__=="__main__":
    arr = [(2,5),(1,2),(4,4),(2,3),(2,1)]
    min = arr[0][1]
    sorted(arr,key=middle)
            
    print(arr)
