import numpy as np
import pandas as pd


def separator_line():
    print(20*"-")


print("######## Creation of Pandas objects (Series, DataFrame) #########")

# data frame is a colletion of series

# data frame column has one data type

# TODO: Define a pandas series 's' with the elements 1, 3, 5, np.nan, 6 and 8

pandas_series = pd.Series([1, 3, 5, np.nan, 6, 8]) # series only has one data type
print(pandas_series) # indices are also printed

separator_line()

# TODO: Create a pandas dataframe 'df' from a dictionary

df = pd.DataFrame({'A': [-1, -0.5, 0, 3],
                   'B': pd.Timestamp('20130102'),
                   'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                   'D': np.array([1, 2, 3, 4], dtype='int32'),
                   'E': pd.Categorical(["test", "train", "test", "train"]),
                   'F': 'foo'})

# TODO: Print out the data types of 'df''s columns

print(df.dtypes)

separator_line()

print("######## Viewing data #########")

# TODO: Print out the first two rows of 'df'

print(df.head(2))

separator_line()

# TODO: Print out the last three rows of 'df'

print(df.tail(3))

separator_line()

# TODO: Print out the column names of 'df'

col = df.columns.values
print(type(col))
print(col)

separator_line()

# TODO: Retrieve data of 'df' as numpy array

numpy_data = df.to_numpy()
print(numpy_data)

separator_line()

# TODO: Display a statistic summary of data

print(df.describe())

separator_line()

# header column labels
# indices row labels

# TODO: Transpose the pandas dataframe 'df'

print(df.transpose())

separator_line()

# TODO: Sort in ascending order the rows of 'df' by column 'D'

df1 = df.sort_values(by=['D'])
print(df1)

separator_line()

print("######## Selection #########")

# TODO: Select column 'D' of 'df' by column label

df2 = df[['D']]
print(df2)

separator_line()

# TODO: Select the first three rows of 'df' by slicing

print(df.iloc[:3])

separator_line()

# TODO: Select columns 'A' and 'B' from 'df' by column label

df3 = df[['A', 'B']]
print(df3)

separator_line()

# TODO: Find out what what happens if you select a column which does not exist

# df4 = df[['R']]
# print(df4)

separator_line()

# TODO: Select row at index 3 from 'df' by position

print(df.iloc[3,:])

separator_line()

# TODO: Select rows with indices 2 and 3 and columns with indices 0 and 1 from 'df'

print(df.iloc[2,:])
print(df.iloc[3,:])

print(df.iloc[:,0])
print(df.iloc[:,1])

separator_line()

# TODO: Get the rows of 'df' whose value in column 'A' not equal to zero

print(df.loc[df['A'] != 0])

separator_line()

# TODO: Create a deep copy of 'df' and assign it to variable 'df5'

df5 = df.copy(deep=True)
print(df5)