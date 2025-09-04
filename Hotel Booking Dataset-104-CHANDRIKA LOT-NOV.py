
#https://github.com/swapnilsaurav/Dataset
#hotel_bookings.csv

link="https://raw.githubusercontent.com/swapnilsaurav/Dataset/refs/heads/master/hotel_bookings.csv"
import pandas as pd
df=pd.read_csv(link)
print(df.shape)#calculate columns and rows
print(df.dtypes)

df.isnull().sum()

import seaborn as sns
import matplotlib.pyplot as plt
cols=df.columns[:30]
colors=('Yellow','pink')
sns.heatmap(df[cols].isnull(),cmap='YlGnBu')
plt.show()

import numpy as np
for col in df.columns:
    pct_missing = np.mean(df[col].isnull()) * 100
    # 1 0 1 1 0 0 0 0 0 1 = 4/10 = 0.4 * 100 = 40%
    print(col, "  :  ",pct_missing,"%")

import seaborn as sns
import matplotlib.pyplot as plt
cols = df.columns[:30]
colors = ['#348feb','#eb4034']
sns.heatmap(df[cols].isnull(), cmap=sns.color_palette(colors))
plt.show()

df_cols_drop = []
print("Columns with more than 80% missing values:")
for col in df.columns:
    pct_missing = np.mean(df[col].isnull()) * 100
    if pct_missing > 80:
        print(col, "  :  ",pct_missing,"%")
        df_cols_drop.append(col)
# drop all the cols
df = df.drop(df_cols_drop,axis=1) # axis = 1 for column
print("2: SHAPE: ",df.shape) # rows & columns after drop

# checking how many missing values in each row
print("Creating missing indicators")
for col in df.columns:
    missing = df[col].isnull()
    num_missing = np.sum(df[col].isnull())
    if num_missing > 0:
        print(f"{col}  to  {col}_ismissing")
        # add a new column
        df[f"{col}_ismissing"] = missing

print("3: SHAPE: ",df.shape) # rows & columns after adding _ismissing cols
# create histogram
ismissing_cols = [col for col in df.columns if '_ismissing' in col]
df['num_missing'] = df[ismissing_cols].sum(axis=1)

df['num_missing'].value_counts().sort_index().plot.bar(x='index', y='num_missing')
plt.show()

# check for rows with more than 20 missing values and delete them later
# get the index (row number) with more than 20 missing values
ind_missing =df[df['num_missing']>=20].index
print("Indices with more than 20 missing values=",ind_missing)

df = df.drop(ind_missing,axis=0) #deleting rows with these missing values
print("4: SHAPE: ",df.shape) # after deleting rows
print("Strategy 1: Deleting missing rows and columns done")
print("Performing Strategy 2: Replace with specific values")
for col in df.columns:
    pct_missing = np.mean(df[col].isnull()) * 100
    if pct_missing > 0:
        print(col, "  :  ",pct_missing,"%")

print("Performing Strategy 3: Replace with mean and mode values")
for col in df.columns:
    pct_missing = np.mean(df[col].isnull()) * 100
    if pct_missing >0:
        print(col, "  :  ",pct_missing,"%")

num_cols = df.select_dtypes(include=[np.number])
for col in num_cols:
    pct_missing = np.mean(df[col].isnull()) * 100
    if pct_missing > 0:
        avg = df[col].mean()
        df[col] = df[col].fillna(avg)

# mode for non-numeric
non_num_cols = df.select_dtypes(exclude=[np.number])
for col in non_num_cols:
    pct_missing = np.mean(df[col].isnull()) * 100
    if pct_missing > 0:
        avg = df[col].describe()['top'] #calculate mode
        df[col] = df[col].fillna(avg)


print("Checking if any more missing values")
for col in df.columns:
    pct_missing = np.mean(df[col].isnull()) * 100
    if pct_missing >0:
        print(col, "  :  ",pct_missing,"%")

print("5: SHAPE: ",df.shape)  # before dropping missing values
ismissing_cols = [col for col in df.columns if '_ismissing' in col]
#df['num_missing']
ismissing_cols.append('num_missing')
df = df.drop(ismissing_cols,axis=1)
print("6: SHAPE: ",df.shape)  # after dropping missing values


