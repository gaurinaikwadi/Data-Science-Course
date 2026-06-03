# 1. How do you check the total number of missing (null) values in each column of a pandas DataFrame?

print(df.isnull().sum())


# 2. What is the difference between calling df.dropna() and df.dropna(axis=1) ?

# Drop rows with *any* missing values
df.dropna()

# Drop columns with missing values
df.dropna(axis=1)


# 3. Write a pandas statement to fill all missing values in an "Age" column with the mean of that column.

df["Age"].fillna(df["Age"].mean())
df.fillna(method="ffill")
df.fillna(method="bfill")


# 5. What method is used to identify duplicate rows in a DataFrame, and how do you remove them entirely?

df.duplicated() # True for duplicates
df.drop_duplicates() # Remove duplicate rows


# 6. How do you drop duplicates based only on a specific subset of columns, for instance, "Name" andm"Age" ? 
df.duplicated(subset=["Name", "Age"])


# 7. Write the code to convert all text in the "Name" column of a DataFrame to lowercase
df['Name'].str.lower()


# 8.  How can you check if the "City" column contains the substring "delhi" , while making the search case-insensitive?
df['City'].str.contains('delhi', case=False)

# 9. Given an "Email" column containing complete email addresses, how would you split the strings
into two parts at the "@" symbol?
df['Email'].str.split('@')

df2 = df.dropna().copy()
df2['Age'] = df2['Age'].astype(int)

# 10.  How do you convert the data type of an "Age" column from float or string to integer?
df.info()
df2.info()

# 12. Why is it recommended to use .copy() when assigning a filtered DataFrame to a new variable
(e.g., df2 = df.dropna().copy() )?

df2 = df.dropna().copy()

# 13. Write the code to create a new column "Age Group" using a lambda function with apply() , where anyone with an Age >= 25 is marked as "Adult" and others as "Minor" .
df["Age Group"] = df["Age"].apply(lambda x : 'Adult' if x >= 25 else 'Minor')

# 15.  How can you systematically change values in a "Gender" column from "M" , "F" , "O" to "Male" , "Female" , "Other" using the .map() method?
gender_map = {"M": "Male", "F": "Female", "O": "Other"}
df2["Gender"] = df2["Gender"].map(gender_map)

# 16. How do you use the .replace() method to change the value "Delhi" to "New Delhi" and "Mumbai" to "New Mumbai" in the "City" column?
df2["City"] = df2["City"].replace({
    'del':'Delhi',
    'mum':'New Mumbai',
})

# 17. Write the code to sort a DataFrame by the "Age" column in descending order.
df.sort_values("Age")

# 18. How can you sort a DataFrame based on multiple columns, for example, first by "City" and then by "Age" ?
df2.sort_values(["City", "Age"])
 
# 19. After sorting or filtering a DataFrame, the index can become out of order. What method and parameters do you use to reset the index to standard sequential integers and drop the old index?
df2.reset_index(drop=True, inplace=True)

# 20.
df2.sort_index()

# 21.
b = df2['Age Rank'] = df2['Age'].rank(method='dense', ascending=False)

# 22.
df2 = df[["City", "Name", "Age"]] 

# 23.
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Math': [85, 78, 92],
    'Science': [90, 82, 89],
    'English': [88, 85, 94]
}
dfx = pd.DataFrame(data)

# 24.
dfx_melted = pd.melt(
    dfx,
    id_vars=['Name'],
    value_vars=['Math', 'Science', 'English'],
    var_name='Subject',
    value_name='Score'
)

# 25.
dfx_pivoted = dfx_melted.pivot(
    index='Name',
    columns='Subject',
    values='Score'
)