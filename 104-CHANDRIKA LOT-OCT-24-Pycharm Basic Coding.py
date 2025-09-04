from lib2to3.pygram import python_grammar_no_print_statement

import numpy as np
x = range(20)
m1=np.reshape(x,(4,5))
print(m1)

x=[[22,25,30,11],[20,17,18,24],[35,19,28,33]]
print("type of x:",type(x))
m2=np.array(x)
print(m2)

m3=np.zeros((3,3))
print("m3=\n",m3)

m3=np.ones((3,3),dtype=int)
print("m3=\n",m3)

m3=np.random.random((3,3))
print("m3=\n",m3)

x = [[22,10,17,16],[7,9,15,18],[5,10,23,21]]
print("Type of X =",type(x))
# 4 columns and 3 rows
m2 = np.array(x)
print(m2)

print(m2[0,0], m2[-1,-2])

print(m2[0])

print(m2[1])

print(m2[2])

print(m2[-1])

print(m2[1:3,2:])

import numpy as np
x = [[22,10,17,16],[7,9,15,18],[5,10,23,21]]
m1 = np.array(x)
print(m1)
print("Shape of Matrice 1 (rows, columns) = ",m1.shape)
y = [[12,20,27,36],[17,19,35,18],[15,30,13,11]]
m2 = np.array(y)
print(m2)
print("Shape of Matrice 2 (rows, columns) = ",m2.shape)

print("Addition: ")
print(m1 + m2)
print(np.add(m1,m2))

print("Subtraction: ")
print(m1 - m2)
print(np.subtract(m1,m2))

print("Element Multiplication: ")
print(m1 * m2)
print(np.multiply(m1,m2))

print("Division: ")
print(m1 / m2)
print(np.divide(m1,m2))

m3=m2.transpose()
print(m3)
m4=np.matmul(m1,m3)
print(m1@m3)
print(m4)

#Histogram
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=np.random.random(5000)
plt.hist(data)
plt.title("Histogram Graph")
plt.xlabel("Marks")
plt.ylabel("Student")
plt.show()

#Boxplot
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data=np.random.random(5000)
np.random.seed(50)
data1=np.random.normal(50,600,70)
data2=np.random.normal(50,600,70)
data3=np.random.normal(50,600,70)
data4=np.random.normal(50,600,70)
plt.boxplot([data1,data2,data3,data4])
plt.show()

# BARPLOT
import matplotlib.pyplot as plt
marks = [55,79,58,65,87]
subjects = ["Maths","Python","Data Science","SQL","Tableau"]
abc="green"
plt.bar(subjects,marks, color=abc)
for idx, val in enumerate(marks):
    plt.text(idx, val,val, ha='center')
plt.title("My Marks in Class X board")
plt.suptitle("Bar Graph")
plt.xlabel("Marks Obtained")
plt.ylabel("Subjects Appeared")
#plt.savefig()
plt.show()

# STACKED BAR PLOT
import matplotlib.pyplot as plt
import numpy as np
term1_marks = [55,79,58,65,77]
term2_marks = [75,89,48,69,87]
term3_marks = [73,79,58,68,97]
term4_marks = [65,69,80,67,67]
subjects = ["Maths","Python","Data Science","SQL","Tableau"]
pos=[0,1,2,3,4]
plt.bar(pos,term1_marks,color="green")
plt.bar(pos,term2_marks,bottom=term1_marks,color="red")
bottom_2=np.add(term1_marks,term2_marks).tolist()
plt.bar(pos,term3_marks,bottom=bottom_2,color="blue")
bottom_3=np.add(bottom_2,term3_marks).tolist()
plt.bar(pos,term4_marks,bottom=bottom_3,color="yellow")
plt.title("stacked bar plot")
plt.xlabel("Subjects Appeared")
plt.ylabel("Marks Obtained")
plt.show()

#scatterplot
import numpy as np
import matplotlib.pyplot as plt
marks=[55,79,58,65,77]
hours=[5,7,8,9,6]
plt.scatter(hours,marks)
plt.title("My Marks in Class X board")
plt.suptitle("Scatter Graph")
plt.xlabel("Hours studied")
plt.ylabel("Total Marks Obtained")
#plt.savefig()
plt.show()

# PIE PLOT
import matplotlib.pyplot as plt
import numpy
marks = [55,79,58,65,77]
subjects = ["Maths","Python","Data Science","SQL","Tableau"]
sizes = numpy.array(marks)
p,tx,autotexts = plt.pie(sizes, labels=subjects, autopct="")
for i,v in enumerate(autotexts):
    v.set_text(sizes[i])
plt.title("My Marks in Class X board")
plt.suptitle("Pie Graph")
#plt.savefig()
plt.show()

link="https://raw.githubusercontent.com/swapnilsaurav/Dataset/refs/heads/master/Iris.csv"
import pandas as pd
df = pd.read_csv(link)
print(df)
print("First 5 rows only:\n",df.head()) # by default display 5 rows
print("Last 6 rows only:\n",df.tail(6)) # by default display 5 rows
print("Shape (rows, columns) of dataset: ",df.shape)

# basic statistics
print("Generate Statistics :\n",df.describe())

# checking for missing values
print("Checking for missing values:\n", df.isnull().sum())

# removing duplicate values
df_species = df.drop_duplicates(subset="Species")
print(df_species)

# Balanced dataset
# In this case, if the number of rows for each unique species are same - data is balanced
# otherwise data is not balanced
print("Checking if dataset is balanced or not:\n",df.value_counts("Species"))
'''
Iris-setosa        50
Iris-versicolor    50
Iris-virginica     50
Dataset is balanced in this case
'''
# accessing values : iloc (reference - number not name) or loc (name)
print(df['SepalLengthCm'])
print("LOC: \n", df.loc[:10, 'SepalLengthCm']) #(rows, cols)
print("ILOC: \n", df.iloc[:10, 1]) #(rows, cols)
print("LOC: \n", df.loc[[0,2,5,8], 'SepalLengthCm']) #(rows, cols)

# performing query on the dataset
# lets check if specific set of Species are in the dataset or not
print("1. Checking for Species: \n",df[df['Species'].isin(['Iris-versicolor',
                                    'Iris-Persica','Iris-Latifolia'])])
print("2. Calculate average of Sepal length: \n",df['SepalLengthCm'].mean())

print("3. Calculate average of Sepal length for each species: \n",
      df.groupby('Species').mean())

# delete a perticular ID
# drop is used to remove both row(axis=0) and col (axis=1)
df_4 = df.drop([2,5,8],axis=0)
print("4. After removing ID=3, 6, 9: \n",df_4.head(10))

df_4 = df.drop(['PetalLengthCm'],axis=1)
print("4. After removing PetalLengthCm: \n",df_4.head(10))

'''
Github link for datasets:

https://github.com/swapnilsaurav/Dataset

Dataset: iris.csv
'''
link="https://raw.githubusercontent.com/swapnilsaurav/Dataset/refs/heads/master/Iris.csv"
import pandas as pd
df = pd.read_csv(link)
print(df)
import matplotlib.pyplot as plt
import seaborn as sns

#pairplot - with Histogram & Scatter plot
sns.pairplot(df.drop(['Id'], axis=1), hue="Species")
plt.show()

sns.violinplot(y="Species",x="SepalLengthCm", data=df)
plt.show()

sns.lineplot(x="Id", y="SepalLengthCm", data=df)
plt.show()


