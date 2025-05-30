# **Optimising Code**

It is important that when creating our code we are as efficient as possible. This not only saves time, but also saves storage and improves efficiency when running a program.

Look at the following for advice on how we can best optimise code - you may even find you come across functions you have not used before!

<table>
<tr>
<td> Code Practice </td> <td> Unoptimised </td> <td> Optimized </td>
</tr>
<tr>
<td> <b> Using List Comprehensions: </b> Instead of using loops to create or transform lists, use list comprehensions, which are more concise and often faster. </td>
<td>

```python
squares = [] 
for i in range(10): 
    squares.append(i * i)
```
</td>
<td>

```python
squares = [i * i for i in range(10)]
```
</td>
</tr>
<tr>
<td> <b> Using Generator Expressions for Large Data: </b> Generators are more memory-efficient than lists when dealing with large datasets because they generate items on the fly rather than storing them all in memory. </td>
<td>

```python
squares = [i * i for i in range(1000000)]
```
</td>
<td>

```python
squares = (i * i for i in range(1000000))
```
</td>
</tr>
<tr>
<td> <b> Using Built-In Functions: </b> Python's built-in functions are implemented in C and are highly optimised for performance. </td>
<td>

```python
total = 0 
for num in range(1, 1001): 
    total += num
```
</td>
<td>

```python
total = sum(range(1, 1001))
```
</td>
</tr>
<tr>
<td> <b> Avoiding Unnecessary List Copying: </b> When you slice a list, Python creates a new list object. To avoid unnecessary copying, work with the original list when possible. </td>
<td>

```python
new_list = my_list[:]
```
</td>
<td>

```python
new_list = my_list
```
</td>
</tr>
<tr>
<td> <b> Avoiding Global Variables: </b> Accessing global variables is slower than accessing local variables. It is often better to pass variables as arguments to functions instead of relying on global state. </td>
<td>

```python
x = 10 
def add_to_x(y): 
    return x + y
```
</td>
<td>

```python
def add_to_x(x, y): 
    return x + y
```
</td>
</tr>
<tr>
<td> <b> Using join() for String Concatenation: </b> Concatenating strings with + can be inefficient because it creates a new string object each time. Instead, use join() to concatenate a list of strings. </td>
<td>

```python
words = ["Hello", "world", "from", "Python"]
sentence = ""
for word in words:
    sentence += word + " "
```
</td>
<td>

```python
words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
```
</td>
</tr>
<tr>
<td> <b> Using enumerate() for Indexed Iteration: </b> This technique avoids manual index management. </td>
<td>

```python
i = 0
for item in my_list:
    print(i, item)
    i += 1
```
</td>
<td>

```python
for i, item in enumerate(my_list):
    print(i, item)
```
</td>
</tr>
<tr>
<td> <b> Minimising Function Calls in Loops: </b> Repeated function calls in loops can slow down performance. Instead, store function results in a variable if they are called multiple times. </td>
<td>

```python
for i in range(len(my_list)):
    print(len(my_list))
```
</td>
<td>

```python
list_length = len(my_list)
for i in range(list_length):
    print(list_length)
```
</td>
</tr>
<tr>
<td> <b> Using any() and all(): </b> These functions are useful for checking conditions in a collection and are faster than manually looping through each element. </td>
<td>

```python
found = False
for item in my_list:
    if item > 10:
        found = True
        break
```
</td>
<td>

```python
found = any(item > 10 for item in my_list)
```
</td>
</tr>
</table>