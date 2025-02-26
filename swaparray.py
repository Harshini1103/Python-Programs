def swap_array(arr1,arr2):
    arr1,arr2=arr2,arr1
    return arr1,arr2
arr1=[1,2,3]    
arr2=[4,5,6]
print("Before swapping:")
print("Array 1",arr1)
print("Array 2",arr2)
arr1,arr2=swap_array(arr1,arr2)
print("\n After swapping:")
print("Array 1",arr1)
print("Array 2",arr2)
# output:
# Before swapping:
# Array 1 [1, 2, 3]
# Array 2 [4, 5, 6]

#  After swapping:
# Array 1 [4, 5, 6]
# Array 2 [1, 2, 3]