#  Practice Set 2 - NumPy Data Types & Functions

# Section 1: Data Types in NumPy

# 1. Create an array  [1, 2, 3, 4, 5]  and check its  dtype  attribute.
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)          #[1 2 3 4 5]
print(arr.dtype)    #int64



# 2. Create an array  [10, 20, 30]  with  dtype='float32'  and print both the array and its dtype.

arr = np.array([10, 20, 30], dtype='float32')
print(arr)          #[10. 20. 30.]
print(arr.dtype)    #float32    


# 3. Create an integer array  [5, 10, 15]  and convert it to  float64  using  astype() .

arr = np.array([5, 10, 15])
arr_float = arr.astype('float64')
print(arr_float)    #[ 5. 10. 15.]
print(arr_float.dtype)  #float64


# 4. Create two arrays with the same values but different dtypes ( int32  and  int64 ). Compare their nbytes .

arr_int32 = np.array([1, 2, 3], dtype='int32')
arr_int64 = np.array([1, 2, 3], dtype='int64')
print(arr_int32.nbytes)  #12 bytes (3 elements * 4 bytes each)
print(arr_int64.nbytes)  #24 bytes (3 elements * 8 bytes each

# 5. Create an array with 100 elements of  float32 . Calculate how many bytes it uses and compare with  float64 .

arr_float32 = np.zeros(100, dtype='float32')
arr_float64 = np.zeros(100, dtype='float64')
print(arr_float32.nbytes)  #400 bytes (100 elements * 4 bytes each)
print(arr_float64.nbytes)  #800 bytes (100 elements * 8 bytes each


# 6. Create an array from  [1.5, 2.5, 3.5]  as  int32 . What values do you get and why?

arr = np.array([1.5, 2.5, 3.5], dtype='int32')
print(arr)  #[1 2 3]  #The decimal parts are truncated (not rounded) when converting to int32.


# 7. Create a float array  [1.9, 2.1, 3.7, 4.3]  and convert to  int32 . What happens to the decimal parts?

arr = np.array([1.9, 2.1, 3.7, 4.3], dtype='int32')
print(arr)  #[1 2 3 4]  #The decimal parts are truncated (not rounded) when converting to int32.



# 8. Create 4 different arrays with values  [10, 20, 30]  using dtypes:  int8 ,  int32 ,  float32 ,  float64 . Print dtype and nbytes for each.

arr1 = np.array([10,20,30],dtype='int8')
arr2 = np.array([10,20,30],dtype='int32')
arr3 = np.array([10,20,30],dtype='float32')
arr4 = np.array([10,20,30],dtype='float64')
print(arr1.dtype)
print(arr1.nbytes)
print(arr2.dtype)
print(arr2.nbytes)
print(arr3.dtype)
print(arr3.nbytes)
print(arr4.dtype)
print(arr4.nbytes)


# Section 2: Broadcasting

# 9. Create array  [1, 2, 3, 4, 5]  and add 10 to each element using broadcasting.
arr = np.array([1, 2, 3, 4, 5])
result = arr + 10
print(result)  #[11 12 13 14 15]



# 10. Subtract a 1D array  [1, 2, 3]  from a 2D array  [[10, 20, 30], [40, 50, 60]] .
arr_2d = np.array([[10, 20, 30], [40, 50, 60]])
arr_1d = np.array([1, 2, 3])
result = arr_2d - arr_1d
print(result)
# [[ 9 18 27]
#  [39 48 57]]  



# 11. Create a 3x3 matrix  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  and multiply every element by 5 using broadcasting.
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
result = matrix * 5
print(result)
# [[ 5 10 15]
#  [20 25 30]
#  [35 40 45]]



# 12. Create a dataset and normalize it using broadcasting: subtract the column mean and divide by column standard deviation.


# 13. Create a 2x4 array and a 1D array with 4 elements. Add them together using broadcasting.
arr_2d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr_1d = np.array([10, 20, 30, 40])
result = arr_2d + arr_1d
print(result)
# [[11 22 33 44]
#  [15 26 37 48]]



# 14. Create a column vector with shape  (3, 1)  and a row vector with shape  (1, 4) . Multiply them and print the result shape.
col_vector = np.array([[1], [2], [3]])  # Shape (3, 1)
row_vector = np.array([[10, 20, 30, 40]])  # Shape (1, 4)
result = col_vector * row_vector    
print(result)
# [[10 20 30 40]
#  [20 40 60 80]
#  [30 60 90 120]]


# 15. Create a random dataset with shape  (5, 3) . Center the data by subtracting the mean of each column.
data = np.random.rand(5, 3)  # Random dataset with shape (5, 3)
column_mean = np.mean(data, axis=0)  # Mean of each column
centered_data = data - column_mean  # Center the data
print(centered_data)  # Centered dataset with mean approximately 0 for each column

# [[ 0.1870718  -0.10519853  0.24449008]
# [-0.05926589  0.30621022 -0.2951291 ]
# [-0.17735954 -0.39947492  0.42528248]
# [ 0.38768164  0.08177833 -0.39941773]
# [-0.33812801  0.1166849   0.02477427]]




 , ccl,gr vc[sptrbpltt0yyyyoooooooooooooooppppovywCC2g65555xc v,l,l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥l̥ṣḍfcvvvvvvvvvvvvvv]