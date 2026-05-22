# Creating NumPy Arrays — 10 Simple Tasks

import numpy as np
from sqlalchemy import column

# 1. Create  a = np.array([0,1,2,3,4])  and print  a .
a=np.array([0,1,2,3,4])
print(a)    


# 2. Make  b = np.zeros((2,3))  and print  b .

b=np.zeros((2,3))
print(b)    


# 3. Make  c = np.ones((2,2))  and multiply by 5; print  c .

c=np.ones((2,2))*5
print(c)


# 4. Create  d = np.arange(0,10)  and print the last element using negative indexing.

d=np.arange(0,10)
print(d[-1])


# 5. Use  np.linspace(0,1,5)  and print the result.

e=np.linspace(0,1,5)
print(e)


# 6. Create  e = np.full((2,3), 9)  and print  e .

e=np.full((2,3),9)
print(e)


# 7. Create a 3×3 identity matrix with  np.eye(3)  and print it.

f=np.eye(3)
print(f)


# 8. Make a float array  f = np.array([1.2, 2.5, 3.7]) , convert to int with  astype , and print.

f=np.array([1.2, 2.5, 3.7])
f_int=f.astype(int)
print(f_int)


# 9. Create  g = np.arange(6)  and reshape to  (2,3) ; print  g .

g=np.arange(6).reshape(2,3)
print(g)


# 10. Create  h = np.arange(0,20,2)  and print its  dtype  and  shape 
h=np.arange(0,20,2)
print(h.dtype)



# Indexing and Slicing — 10 Simple Tasks

# 1. Create  arr = np.arange(12).reshape(4,3)  and print  arr .

arr=np.arange(12).reshape(4,3)
print(arr)



# 2. Flatten  arr  with  arr.flatten()  and print the flattened array.


flattened=arr.flatten()
print(flattened)


# 3. From the flattened array, print elements  3:6 .

arr = np.arange(12).reshape(4, 3)
flattened = arr.flatten()
print(flattened[3:6])



# 4. Make  b = arr[1]  and print the second row.

b=arr[1]
print(b)


# 5. Use negative indexing to print the last row ( arr[-1] ).

print(arr[-1])


# 6. Create  sel = arr[[0,2]]  to pick rows 0 and 2 and print  sel .

sel=arr[[0,2]]
print(sel)


# 7. Create a 1D array and show boolean indexing:  x = np.array([1,2,3,4]); print(x[x>2]) .

x=np.array([1,2,3,4])
print(x[x>2])


# 8. Use  np.where  to find indices where  x  is even.

x=np.array([1,2,3,4])
even_indices=np.where(x%2==0)
print(even_indices)


# 9. Copy a slice:  s = arr.flatten()[2:5].copy() ; change  s[0]  and show original unchanged.

arr = np.arange(12).reshape(4, 3)
s = arr.flatten()[2:5].copy()   
s[0] = 99
print("Modified slice:", s)
print("Original array:\n", arr)


# 10. Show slicing with step:  print(np.arange(10)[::2]) 
print(np.arange(10)[::2])



# Multidimensional Indexing and Axis — 10 Simple Tasks

# 1. Create  arr3D = np.arange(24).reshape(2,3,4)  and print  arr3D.shape .

arr3D=np.arange(24).reshape(2,3,4)
print(arr3D.shape)


# 2. Print  np.sum(arr3D, axis=0)  and its shape.

arr3D = np.array(
    [
        [
            [1, 2, 3], 
            [4, 5, 6]
        ],

      [
          [7, 8, 9], 
          [10, 11, 12]
      ]
    ]
) 
sum = np.sum(arr3D,axis=0)
print(arr3D)
print('============')
print(sum)
print(sum.shape)


# 3. Print  np.sum(arr3D, axis=1)  and its shape.

arr3D = np.array(
    [
        [
            [1, 2, 3], 
            [4, 5, 6]
        ],

      [
          [7, 8, 9], 
          [10, 11, 12]
      ]
    ]
)
sum = np.sum(arr3D,axis=1)
print(arr3D)
print('============')
print(sum)
print(sum.shape)


# 4. Set  arr3D[:,0,:] = 0  and print  arr3D .

arr3D = np.array(
    [
        [
            [1, 2, 3], 
            [4, 5, 6]
        ],

      [
          [7, 8, 9], 
          [10, 11, 12]
      ]
    ]
)
arr3D[:,0,:] = 0
print(arr3D)


# 5. Create  a2 = np.array([[1,2,3],[4,5,6]])  and add  [10,10,10]  to each row using broadcasting; print result.

a2 = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
    )    
a3 = [10,10,10]
sum  = a2+a3
print(sum)



# 6. Show  a2.T  (transpose) and print shapes before and after.

# '''
# Transpose ->    rows → columns
#                 columns → rows
# '''
a2 = np.array([[1,2,3],[4,5,6]])
print(a2.shape)
t = a2.transpose()
print(t)


# 7. Use  keepdims=True :  print(np.mean(a2, axis=1, keepdims=True).shape) .

# Create a 2D array
a2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# axis=1 means calculate mean row-wise
# keepdims=True keeps the result as 2D instead of converting to 1D
result = np.mean(a2, axis=1, keepdims=True)

# Print mean values
print(result)

# Print shape of result
print(result.shape)


# 8. Demonstrate assigning a compatible slice value:  arr3D[:,1,:] = np.ones((2,4))*5  and print arr3D .

arr3D = np.array(
    [
        [
            [1, 2, 3], 
            [4, 5, 6]
        ],

      [
          [7, 8, 9], 
          [10, 11, 12]
      ]
    ]
)
# Replace row index 1 in all blocks with 5s
'''
arr3D[:,1,:] = np.zeros((2,4))*5
'''
arr3D[:,1,:] = np.ones((2,3)) * 5
print(arr3D)

# 9. Reshape a 1D  ts = np.arange(20)  into  (5,4)  and compute per-row mean.

arr_1D = np.arange(20)
arr_1D = arr_1D.reshape(5,4)
x = np.mean(arr_1D,axis=1,keepdims=True)
print(x)

# 10. Given  data = np.arange(12).reshape(3,4) , standardize each column (feature) by subtracting column mean and dividing by column std; print result.

#     by subtracting column mean and dividing by column std; print result

data = np.arange(12)
data = data.reshape(3,4)
mean = np.mean(data, axis=0)
std = np.std(data,axis=0)
result  = (data - mean) / std
print(result)


# Create numbers from 0 to 11
data = np.arange(12)

# Convert into 3 rows and 4 columns
data = data.reshape(3,4)

# Find mean of each column
# axis=0 means column-wise
# axis=1 means row-wise
mean = np.mean(data, axis=0)

# Find standard deviation of each column
std = np.std(data, axis=0)

# Standardization formula
# (value - mean) / std
result = (data - mean) / std

print(result)