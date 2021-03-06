
def insertion_sort(A):
    for item in range(len(A)):
        key = A[item]
        index = item - 1
        while index >= 0 and A[index] > key:
            A[index+1] = A[index]
            index = index - 1
        A[index+1] = key
        
        
A = [22,30,12,15,89,2,1,55,3,90,8]
insertion_sort(A)
print(A)

