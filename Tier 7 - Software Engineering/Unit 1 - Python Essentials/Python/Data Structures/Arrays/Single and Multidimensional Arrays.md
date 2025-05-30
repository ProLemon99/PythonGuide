# **Single and Multi-Dimensional Arrays**

## **Single-Dimensional Arrays**
A **single-dimensional** array is a linear collection of elements, meaning it has only one row of data. Each element is accessed using a single index.

Think of it like a list of numbers in a straight line:

```python
[10, 20, 30, 40, 50]
```
Each item in this array is accessed using a single index.
![Image](/Tier%207%20-%20Software%20Engineering/Unit%201%20-%20Python%20Essentials/Python/Data%20Structures/Arrays/Images/Arrays.png)

### **Example Using Array Module**
```python
import array

# Creating a single-dimensional array of integers
numbers = array.array('i', [10, 20, 30, 40, 50])

# Accessing elements using their index
print(numbers[0])  # Output: 10
print(numbers[3])  # Output: 40
```

## **Multi-Dimensional Arrays**
A **multi-dimensional array** is an array containing other arrays inside it. The most common type is a **2D array**, which resembles a table with rows and columns.

For example, a **2D array** can be visualised as:

```python
[
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
]
```
Each element is accessed using two indices: one for the row and one for the column.

**2D Multidimensional Array Example**

![Image](/Tier%207%20-%20Software%20Engineering/Unit%201%20-%20Python%20Essentials/Python/Data%20Structures/Arrays/Images/Multidimensional.png)

### **Example Using NumPy Module**
Python’s built-in array module only supports single-dimensional arrays, so we use NumPy for multi-dimensional arrays.

```python
import numpy as np

# Creating a 2D array (3 rows, 3 columns)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Accessing elements using row and column indices
print(matrix[0][1])  # Output: 2 (row 0, column 1)
print(matrix[2][2])  # Output: 9 (row 2, column 2)
```

## **Key Differences**
| Feature | Single-Dimensional Array | Multi-Dimensional Array |
| --- | --- | --- |
| Structure | A single row of elements | A grid (rows and columns) |
| Indexing | Uses one index (e.g., ```arr[2]```) | Uses multiple indices (e.g., ```arr[1][2]```) |
| Usage | Used for simple lists of data | Used for tables, matrices, images, etc. |
| Library | Can use array module or lists | Requires numpy for efficient handling |