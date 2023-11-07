from __future__ import annotations
from typing import Any


# ex1: Write a Python class that simulates a Stack. The class should implement methods like push, pop, peek (the last
# two methods should return None if no element is present in the stack).

class Stack:
    def __init__(self) -> None:
        self.items = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        if not (len(self.items) == 0):
            last_item = self.items[-1]
            self.items = self.items[:-1]
            return last_item
        else:
            return None

    def peek(self) -> Any:
        if not (len(self.items) == 0):
            return self.items[-1]
        else:
            return None


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Stack:", stack.items)
print("Peek:", stack.peek())

popped_item = stack.pop()
print("Popped item:", popped_item)

print("Stack items:", stack.items)


# ex2: Write a Python class that simulates a Queue. The class should implement methods like push, pop, peek (the last
# two methods should return None if no element is present in the queue).

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item: Any) -> None:
        self.items.append(item)

    def pop(self) -> Any:
        if not (len(self.items) == 0):
            first_item = self.items[0]
            self.items = self.items[1:]
            return first_item
        else:
            return None

    def peek(self) -> Any:
        if not (len(self.items) == 0):
            return self.items[0]
        else:
            return None


queue = Queue()

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)

print("Queue:", queue.items)
print("Peek:", queue.peek())

popped_item = queue.pop()
print("Popped item:", popped_item)

print("Queue items:", queue.items)


# ex3: Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. The class
# should provide methods to access elements (get and set methods) and some mathematical functions such as transpose,
# matrix multiplication and a method that allows iterating through all elements form a matrix an apply a
# transformation over them (via a lambda function).

class Matrix:
    def __init__(self, n: int, m: int) -> None:
        self.n = n
        self.m = m
        self.matrix = [[0 for _ in range(m)] for _ in range(n)]

    def get(self, i: int, j: int) -> int:
        return self.matrix[i][j]

    def set(self, i: int, j: int, value: int) -> None:
        if 0 <= i < self.n and 0 <= j < self.m:
            self.matrix[i][j] = value
        else:
            raise IndexError("Index out of bounds")

    def transpose(self) -> Matrix:
        transposed = Matrix(self.m, self.n)
        for i in range(self.n):
            for j in range(self.m):
                transposed.matrix[j][i] = self.matrix[i][j]
        return transposed

    def multiply(self, other: Matrix) -> Matrix:
        if self.m != other.n:
            raise ValueError("Can't multiply matrices")
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                for k in range(self.m):
                    result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return result

    def apply(self, function: callable) -> Any:
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j] = function(self.matrix[i][j])


matrix1 = Matrix(3, 2)

matrix1.set(0, 0, 1)
matrix1.set(0, 1, 2)
matrix1.set(1, 0, 3)
matrix1.set(1, 1, 4)
matrix1.set(2, 0, 5)
matrix1.set(2, 1, 6)

print("Original Matrix:")
for row in matrix1.matrix:
    print(row)
transposed_matrix = matrix1.transpose()

matrix2 = Matrix(2, 3)
matrix2.set(0, 0, 7)
matrix2.set(0, 1, 8)
matrix2.set(0, 2, 9)
matrix2.set(1, 0, 10)
matrix2.set(1, 1, 11)
matrix2.set(1, 2, 12)

result_matrix = matrix1.multiply(matrix2)


def square(x):
    return x * x


matrix1.apply(square)

print("Squared Matrix:")
for row in matrix1.matrix:
    print(row)

print("Transposed Matrix:")
for row in transposed_matrix.matrix:
    print(row)

print("Multiplied Matrix:")
for row in result_matrix.matrix:
    print(row)
