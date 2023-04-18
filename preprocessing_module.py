import pandas as pd
import numpy as np

# Boolean function, returns true if the number is a float 
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


#### This function takes as input the data frame containing data, cleans it from epmty and non-numeric entries,
      # and returns the dataset matrix of features X, and the vector of labels y #####
def Preprocessing(df):
  # Check which row contains empty cells
  empty_rows = np.where(df.isna().any(axis=1))[0]
  print(empty_rows)
  for x in empty_rows:
    print(df.loc[x])

  # Drop the rows with empty cells (without returning row index)
  df = df.dropna()

  # Reset the indexes
  df = df.reset_index(drop = True)

  X = df.iloc[:,1:29] # feature vectors are the first two columns in the dataset
  y = df.iloc[:,0]    # labels are in the last column of the dataset
  X = X.values
  y = y.values

  # Check for non numerical values:
  # Array of rows with errors
  faulty_rows = []

  # Iterate over X
  row_num = 0
  for i in X:
    row_num += 1
    col_num = 0
    for j in i:
      col_num += 1
      if not isfloat(j):
        faulty_rows.append(row_num-1)
        print(j, row_num, col_num)
        print(faulty_rows)

  # Drop the rows with errors
  df = df.drop(faulty_rows)
  df = df.reset_index(drop = True)

  # Same for the matrix
  X = np.delete(X, faulty_rows, axis = 0)
  y = np.delete(y, faulty_rows, axis = 0)

  return X,y