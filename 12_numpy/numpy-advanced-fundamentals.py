import numpy as np
import time
import matplotlib.pyplot as plt


# SPEED COMPARISON - LIST

a = [i for i in range(10000000)]
b = [i for i in range(10000000, 20000000)]

c = []

start = time.time()

for i in range(len(a)):
    c.append(a[i] + b[i])

print("List time:", time.time() - start)


# SPEED COMPARISON - NUMPY

a = np.arange(10000000)
b = np.arange(10000000, 20000000)

start = time.time()

c = a + b

print("NumPy time:", time.time() - start)


# FANCY INDEXING

a = np.arange(12).reshape(4, 3)

print(a)

print(a[[0, 2, 3]])


a = np.random.randint(1, 100, 24).reshape(6, 4)

print(a)

print(a[[0, 2, 3, 5]])

print(a[:, [0, 2, 3]])


# BOOLEAN INDEXING

a = np.random.randint(1, 100, 24).reshape(6, 4)

print(a)

print(a > 50)

print(a[a > 50])


# FIND EVEN NUMBERS

print(a % 2 == 0)

print(a[a % 2 == 0])


# NUMBERS GREATER THAN 50 AND EVEN

print(a[(a > 50) & (a % 2 == 0)])


# NUMBERS DIVISIBLE BY 7

print(a[a % 7 == 0])


# BROADCASTING

a = np.arange(6).reshape(2, 3)
b = np.arange(6, 12).reshape(2, 3)

print(a)
print(b)
print(a + b)


a = np.arange(6).reshape(2, 3)
b = np.arange(3).reshape(1, 3)

print(a)
print(b)
print(a + b)


a = np.arange(3).reshape(1, 3)
b = np.arange(3).reshape(3, 1)

print(a)
print(b)
print(a + b)


a = np.arange(3).reshape(1, 3)
b = np.arange(4).reshape(4, 1)

print(a)
print(b)
print(a + b)


a = np.array([1])
b = np.arange(4).reshape(2, 2)

print(a)
print(b)
print(a + b)


# WORKING WITH MATHEMATICAL FORMULAS

a = np.arange(18)

print(np.sum(a))

print(np.sin(a))


# SIGMOID

def sigmoid(array):
    return 1 / (1 + np.exp(-array))


a = np.arange(10)

print(sigmoid(a))


# MEAN SQUARED ERROR

actual = np.random.randint(1, 50, 25)
predicted = np.random.randint(1, 50, 25)


def mse(actual, predicted):
    return np.mean((actual - predicted) ** 2)


print(mse(actual, predicted))

print(np.mean((actual - predicted) ** 2))


# BINARY CROSS ENTROPY

actual = np.random.randint(0, 2, 25)
predicted = np.random.random(25)


def bce(actual, predicted):
    return -np.mean(
        actual * np.log(predicted)
        + (1 - actual) * np.log(1 - predicted)
    )


print(bce(actual, predicted))


# WORKING WITH MISSING VALUES

a = np.array([1, 2, 3, 4, np.nan, 6])

print(a)

print(np.isnan(a))

print(a[~np.isnan(a)])


# PLOTTING GRAPHS

# y = x

x = np.linspace(-10, 10, 100)

y = x

plt.plot(x, y)
plt.title("y = x")
plt.show()


# y = x^2

x = np.linspace(-10, 10, 100)

y = x ** 2

plt.plot(x, y)
plt.title("y = x^2")
plt.show()


# y = sin(x)

x = np.linspace(-10, 10, 100)

y = np.sin(x)

plt.plot(x, y)
plt.title("y = sin(x)")
plt.show()


# y = x log(x)

x = np.linspace(1, 10, 100)

y = x * np.log(x)

plt.plot(x, y)
plt.title("y = x log(x)")
plt.show()


# SIGMOID GRAPH

x = np.linspace(-10, 10, 100)

y = 1 / (1 + np.exp(-x))

plt.plot(x, y)
plt.title("Sigmoid Function")
plt.show()
