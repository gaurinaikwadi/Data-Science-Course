# Pandas Coding Questions

# Core Data Structures


# 1. Create a Pandas Series containing the values  10, 20, 30, 40  using the default index.
import pandas as pd
series1 = pd.Series([10, 20, 30, 40])
print(series1)            # Output: 0    10
                          #         1    20
                          #         2    30
                          #         3    40


# 2. Create a Pandas Series containing the values 100, 200, 300 with custom index labels a , b , and c .
series2 = pd.Series([100, 200, 300], index=['a', 'b', 'c'])
print(series2)            # Output: a    100
                          #         b    200
                          #         c    300



# 3. Create a DataFrame with columns Name and Age using a dictionary.
data = {
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age': [25, 30, 35]
    }

df = pd.DataFrame(data) 
print(df)                 # Output:            Name   Age
                          #           0        Alice   25
                          #           1          Bob   30
                          #           2      Charlie   35


# 4. Given a DataFrame df , display its row index, column names, and shape.
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age': [25, 30, 35]
    })

print(df.index)          # Output: RangeIndex(start=0, stop=3, step=1)  
print(df.columns)        # Output: Index(['Name', 'Age'], dtype='object')
print(df.shape)          # Output: (3, 2)




# Creating DataFrames


# 5. Create a DataFrame from the following list of lists and assign appropriate column names:
[
["Amit", 21],
["Riya", 22],
["John", 23]
]

data = [
    ["Amit", 21],
    ["Riya", 22],
    ["John", 23]
]

df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)                 # Output:                 Name   Age
                          #               0         Amit   21
                          #               1         Riya   22
                          #               2         John   23



# 6. Create a DataFrame from a NumPy array containing student marks and assign column names.
import numpy as np
marks_array = np.array([[85, 90], [78, 88], [92, 95]])
df = pd.DataFrame(marks_array, columns=['Math', 'Science'])
print(df)                 # Output:          Math    Science
                          #               0    85       90
                          #               1    78       88
                          #               2    92       95




# 7. Read a CSV file named student.csv into a Pandas DataFrame.
import pandas as pd
df = pd.read_csv('students.csv')
print(df)                                      # Output: (Contents of student.csv will be displayed)



# 8. Read a JSON file named students.json into a Pandas DataFrame.
import pandas as pd
df = pd.read_json('students.json')
print(df)                                      # Output: (Contents of students.json will be displayed)



# 9. Display the first 5 rows, last 5 rows, DataFrame information, and column names of a DataFrame.
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'], 
    'Age': [25, 30, 35, 40, 45, 50]
    })

print(df.head())         # Output:          Name  Age
                        #             0    Alice   25
                        #             1      Bob   30
                        #             2  Charlie   35


print(df.tail())         # Output:          Name  Age
                        #             1      Bob   30
                        #             2  Charlie   35
                        #             3    David   40
                        #             4      Eve   45
                        #             5    Frank   50


print(df.info())         # Output: <class 'pandas.core.frame.DataFrame'>
                        #         RangeIndex: 6 entries, 0 to 5
                        #         Data columns (total 2 columns):

                        #          #   Column  Non-Null Count  Dtype 
                        #         ---  ------  --------------  ----- 
                        #          0   Name    6 non-null      object
                        #          1   Age     6 non-null      int64 
                        #         dtypes: int64(1), object(1)
                        #         memory usage: 224.0+ bytes


print(df.columns)      # Output: Index(['Name', 'Age'], dtype='object')




# 10. Find the number of rows and columns present in a DataFrame.
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'], 
    'Age': [25, 30, 35, 40, 45]
    })

print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")                  # Output: Number of rows: 5
                                                            #         Number of columns: 2




# Data Selection & Filtering

# 11. Select the Name column from a DataFrame and check its type.
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age': [25, 30, 35]
    })

name_column = df['Name']
print(name_column)          # Output: 0      Alice
print(type(name_column))    # Output: <class 'pandas.core.series.Series'>  



# 12. Select the Name and Age columns from a DataFrame.
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age':  [25, 30, 35]
    })

selected_columns = df[['Name', 'Age']]
print(selected_columns)     # Output:          Name   Age
                            #             0    Alice   25
                            #             1      Bob   30
                            #             2  Charlie   35


# 13. Retrieve a row using its label with loc .
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age':  [25, 30, 35]
    }, index=['a', 'b', 'c'])

row_b = df.loc['b']
print(row_b)               # Output: Name    Bob
                            #         Age     30
                            #         Name: b, 
                            #         dtype: object    



# 14. Retrieve the third row of a DataFrame using iloc.
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age':  [25, 30, 35]
    })

third_row = df.iloc[2]
print(third_row)           # Output:  Name    Charlie
                            #         Age     35
                            #         Name:    2, 
                            #         dtype:  object 



# 15. Access a specific cell value using row label and column name.
import pandas as pd
df = pd.DataFrame({     
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age':  [25, 30, 35]
    }, index=['a', 'b', 'c'])

cell_value = df.loc['b', 'Age']
print(cell_value)         # Output: 30



# 16. Access a specific cell value using row and column positions
import pandas as pd
df = pd.DataFrame({     
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age':  [25, 30, 35]
    }, index=['a', 'b', 'c'])

cell_value = df.iloc[1,1] 
print(cell_value)          # Output: 30 




# 17. Select a range of rows and specific columns using loc .
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 40, 45, 50]
}, index=['a', 'b', 'c', 'd', 'e', 'f'])

selected_data = df.loc['b':'e', 'Name':'Age']
print(selected_data)                               # Output:             Name  Age
                                                    #              b      Bob   30
                                                    #              c  Charlie   35
                                                    #              d    David   40
                                                    #              e      Eve   45



# 18. Select a range of rows and columns using iloc .
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [25, 30, 35, 40, 45, 50]
})

selected_data = df.iloc[1:5, 0:2]
print(selected_data)                               # Output:            Name  Age 
                                                    #             1      Bob   30
                                                    #             2  Charlie   35
                                                    #             3    David   40
                                                    #             4      Eve   45  
                                                    #             5    Frank   50
                                                    #             (Note: The last row with index 5 is not included in the output due to slicing)     



# 19. Access a single value from a DataFrame using at .

import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age':  [25, 30, 35]
}, index=['a', 'b', 'c'])

cell_value = df.at['b', 'Age']
print(cell_value)                  # Output: 30



# 20. Access a single value from a DataFrame using iat .
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'], 
    'Age':  [25, 30, 35]
}, index=['a', 'b', 'c'])

cell_value = df.iat[1, 1]
print(cell_value)                  # Output: 30



# 21. Filter all movies with an IMDb rating greater than 8.
import pandas as pd
df=pd.read_csv("data.csv")
filtered_movies = df[df['IMDb'] > 8][['Film', 'IMDb']]
print(filtered_movies)
                                


# 22. Filter all movies where the IMDb rating is greater than 8 OR the year is greater than 2020.
import pandas as pd
df = pd.read_csv("data.csv")
filtered_movies = df[(df['IMDb'] > 8) | (df['Year'] > 2020)] 
print(filtered_movies)



# 24. Filter all movies with an IMDb rating greater than 8 using the query() method.
import pandas as pd
df = pd.read_csv("data.csv")
filtered_movies = df.query('IMDb > 8')
print(filtered_movies)                



# 24. Create a copy of selected columns from a DataFrame and modify one value without affecting the original DataFrame.
import pandas as pd
df = pd.read_csv("data.csv")
selected_columns = df[['Film', 'IMDb']].copy()
selected_columns.loc[0, 'IMDb'] = 10.0
print(selected_columns)                                     # Output                  Film  IMDb
                                                            # 0                    Pathaan  10.0
                                                            # 1            Tiger Zinda Hai   6.0
                                                            # 2                     Dangal   8.4
                                                            # 3                 Brahmastra   5.6
                                                            # 4                  Padmaavat   7.0
                                                            # 5                  Andhadhun   8.3
                                                            # 6                      Stree   7.5
                                                            # 7                        War   6.5
                                                            # 8                 Good Newwz   7.0
                                                            # 9          Bhool Bhulaiyaa 2   5.9
                                                            # 10     Badrinath Ki Dulhania   6.1
                                                            # 11  Uri: The Surgical Strike   8.2       

 
print(df)            

#               Actor                      Film  Year            Genre  \     
# 0       Shah Rukh Khan                   Pathaan  2023           Action   
# 1          Salman Khan           Tiger Zinda Hai  2017           Action   
# 2           Aamir Khan                    Dangal  2016        Biography   
# 3        Ranbir Kapoor                Brahmastra  2022          Fantasy   
# 4        Ranveer Singh                 Padmaavat  2018       Historical   
# 5   Ayushmann Khurrana                 Andhadhun  2018         Thriller   
# 6        Rajkummar Rao                     Stree  2018    Horror Comedy   
# 7       Hrithik Roshan                       War  2019           Action   
# 8         Akshay Kumar                Good Newwz  2019           Comedy   
# 9        Kartik Aaryan         Bhool Bhulaiyaa 2  2022    Horror Comedy   
# 10        Varun Dhawan     Badrinath Ki Dulhania  2017  Romantic Comedy   
# 11       Vicky Kaushal  Uri: The Surgical Strike  2019           Action   

#     BoxOffice(INR Crore)  IMDb  
# 0                   1050   7.2  
# 1                    565   6.0  
# 2                   2024   8.4  
# 3                    431   5.6  
# 4                    585   7.0  
# 5                    111   8.3  
# 6                    180   7.5  
# 7                    475   6.5  
# 8                    318   7.0  
# 9                    266   5.9  
# 10                   201   6.1  
# 11                   342   8.2  





# 25. Demonstrate the difference between a view and a copy in Pandas.
import pandas as pd

# Read the dataset
df = pd.read_csv("data.csv")

# Subset without .copy() (view/reference)
view_subset = df[['Film', 'IMDb']]

# Subset with .copy()
copy_subset = df[['Film', 'IMDb']].copy()

# Modify values
view_subset.loc[0, 'IMDb'] = 9.5
copy_subset.loc[1, 'IMDb'] = 8.8

# Display results
print("Original DataFrame:")
print(df[['Film', 'IMDb']])

print("\nSubset without .copy():")
print(view_subset)

print("\nSubset with .copy():")
print(copy_subset)

# Output:

# Original DataFrame:
#                  Film  IMDb
# 0            Pathaan   9.5
# 1    Tiger Zinda Hai   6.0
# 2             Dangal   8.4
# 3         Brahmastra   5.6
# 4          Padmaavat   7.0
# 5          Andhadhun   8.3
# 6              Stree   7.5
# 7                War   6.5
# 8         Good Newwz   7.0
# 9  Bhool Bhulaiyaa 2   5.9
# 10 Badrinath Ki Dulhania   6.1
# 11 Uri: The Surgical Strike   8.2

# Subset without .copy():
#                  Film  IMDb
# 0            Pathaan   9.5
# 1    Tiger Zinda Hai   6.0
# 2             Dangal   8.4
# 3         Brahmastra   5.6
# 4          Padmaavat   7.0
# 5          Andhadhun   8.3
# 6              Stree   7.5
# 7                War   6.5
# 8         Good Newwz   7.0
# 9  Bhool Bhulaiyaa 2   5.9
# 10 Badrinath Ki Dulhania   6.1
# 11 Uri: The Surgical Strike   8.2

# Subset with .copy():
#                  Film  IMDb
# 0            Pathaan   7.2
# 1    Tiger Zinda Hai   8.8
# 2             Dangal   8.4
# 3         Brahmastra   5.6
# 4          Padmaavat   7.0
# 5          Andhadhun   8.3
# 6              Stree   7.5
# 7                War   6.5
# 8         Good Newwz   7.0
# 9  Bhool Bhulaiyaa 2   5.9
# 10 Badrinath Ki Dulhania   6.1
# 11 Uri: The Surgical Strike   8.2
