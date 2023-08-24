import math 
def prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    sqnum = round(math.sqrt(num))
    for i in range(3,sqnum+1,2):
        if num % i == 0:
            return False
    return True
def primeCheck(arr):
    count=0
    for num in arr:
        if prime(num):
            count+=1
    return count
        
if __name__ == "__main__" :
    print("Enter the elements in the array: \n")
    arr = list(map(int , input().split()))
    ans = primeCheck(arr)
    print("Number of prime numbers: ", ans)
