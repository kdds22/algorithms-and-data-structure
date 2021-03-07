
def insertion_sort_asc(A):
    for item in range(len(A)):
        key = A[item]
        index = item - 1
        while index >= 0 and A[index] > key:
            A[index+1] = A[index]
            index = index - 1
        A[index+1] = key
    print("Asc: ",A)

def insertion_sort_desc(A):
    for item in range(len(A)):
        key = A[item]
        index = item - 1
        while index >= 0 and A[index] < key:
            A[index+1] = A[index]
            index = index - 1
        A[index+1] = key
    print("Desc: ", A)
        
        
        
A = [22,30,12,15,89,2,1,55,3,90,8]
print("Original: ", A)
insertion_sort_asc(A) #[1, 2, 3, 8, 12, 15, 22, 30, 55, 89, 90]
B = [22,30,12,15,89,2,1,55,3,90,8]
insertion_sort_desc(B) #[90, 89, 55, 30, 22, 15, 12, 8, 3, 2, 1]

