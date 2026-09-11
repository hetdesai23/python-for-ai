import numpy as np
import pandas as pd


# Creating Series

country = ['India', 'Pakistan', 'USA', 'Nepal', 'Srilanka']
pd.Series(country)

runs = [13, 24, 56, 78, 100]
pd.Series(runs)

marks = [67, 57, 89, 100]
subjects = ['maths', 'english', 'science', 'hindi']

pd.Series(marks, index=subjects)
pd.Series(marks, index=subjects, name='Het marks')


# Series from Dictionary

marks = {
    'maths': 67,
    'english': 57,
    'science': 89,
    'hindi': 100
}

marks_series = pd.Series(marks)
marks_series
pd.Series(marks_series, name='Het marks')


# Series Attributes

marks_series.dtype
marks_series.size
marks_series.name
marks_series.is_unique

pd.Series([1, 1, 2, 3, 5, 6]).is_unique

marks_series.index
marks_series.values


# Series using read_csv

subs = pd.read_csv('subs.csv')
subs

vk = pd.read_csv('kohli_ipl.csv', index_col='match_no')
vk

movies = pd.read_csv('bollywood.csv', index_col='movie')
movies


# Series Methods

subs.head()

vk.head(3)
vk.tail(10)

movies.sample(5)

movies.value_counts()

vk.sort_values(ascending=False, by='runs').head(1).values[0]

vk.sort_values(inplace=True, by='runs')
vk

movies.sort_index(inplace=True)
movies


# Series Maths Methods

vk.count()

subs.sum()
subs.product()

subs.mean()
print(vk.median())
print(movies.mode())
print(subs.std())
print(vk.var())

subs.min()
subs.max()

vk.describe()
subs.describe()


# Series Indexing

x = pd.Series([12, 13, 14, 15, 35, 46, 57, 58, 79, 9])
x[1]

marks_series.iloc[-1]

vk[5:16]

vk[-5:]

movies[-5::2]

vk.loc[[1, 3, 4, 5]]

movies.loc['2 States (2014 film)']


# Editing Series

marks_series[1] = 100
marks_series

marks_series['evs'] = 100
marks_series

runs_ser = vk.runs

runs_ser[2:4] = [100, 100]
runs_ser

runs_ser.iloc[[0, 3, 4]] = [0, 0, 0]
runs_ser

movies['2 states (2014 film)'] = 'Alia Bhatt'
movies


# Series with Python Functionalities

print(len(subs))
print(type(subs))
print(dir(subs))
print(sorted(subs))
print(max(subs))
print(min(subs))

list(marks_series)

'2 states (2014 film)' in movies
'Alia Bhatt' in movies
'Alia Bhatt' in movies.values

for i in movies.index:
    print(i)


# Arithmetic Operators

100 - marks_series


# Relational Operators

vk >= 50


# Boolean Indexing on Series

vk[vk >= 50].size

vk[vk == 0].size

subs[subs > 200].size

num_movies = movies.value_counts()
num_movies[num_movies > 20]


# Plotting Graphs on Series

subs.plot()

movies.value_counts().head(20).plot(kind='bar')