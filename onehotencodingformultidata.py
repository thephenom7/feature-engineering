#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:46:25 2020

@author: akshayaksh
"""

for col in data.columns:
    print(col, ': ', len(data[col].unique()), ' labels')
    # let's examine how many columns we will obtain after one hot encoding these variables
pd.get_dummies(data, drop_first=True).shape

# let's find the top 10 most frequent categories for the variable X2

data.X2.value_counts().sort_values(ascending=False).head(10)

In [5]:

# let's make a list with the most frequent categories of the variable

top_10 = [x for x in data.X2.value_counts().sort_values(ascending=False).head(10).index]

top_10


# and now we make the 10 binary variables

for label in top_10:
    data[label] = np.where(data['X2']==label, 1, 0)

data[['X2']+top_10].head(10)

# get whole set of dummy variables, for all the categorical variables

def one_hot_top_x(df, variable, top_x_labels):
    # function to create the dummy variables for the most frequent labels
    # we can vary the number of most frequent labels that we encode
    
    for label in top_x_labels:
        df[variable+'_'+label] = np.where(data[variable]==label, 1, 0)

# read the data again
data = pd.read_csv('mercedesbenz.csv', usecols=['X1', 'X2', 'X3', 'X4', 'X5', 'X6'])

# encode X2 into the 10 most frequent categories
one_hot_top_x(data, 'X2', top_10)
data.head()

# find the 10 most frequent categories for X1
top_10 = [x for x in data.X1.value_counts().sort_values(ascending=False).head(10).index]

# now create the 10 most frequent dummy variables for X1
one_hot_top_x(data, 'X1', top_10)
data.head()
