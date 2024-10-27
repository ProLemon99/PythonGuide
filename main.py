# Swaroop - A Byte Of Python - Code Learning Session
# By Lemon

# Module 1: First Steps
print("hi")

lemon = "hi"
print(lemon)

# Module 2: Basics
name = 'lemon'
age = 12

print('{0} is {1} years old as of Jan 2022'.format(name, age))
print(f'{name} is {str(age)} years old as of Jan 2022') # Note these 2 are the same, f string came out as of Py 3.6
print(name + ' is ' + str(age) + ' years old as of Jan 2022') # This works too

# Module 3: Operators and Expressions
a = 2
a = a * 3
print(a)

a = 2
a *= 3
print(a) # These 2 are the same

# Notice that var = var operation expression becomes var operation= expression

# lambda = Lambda Expression
# if - else: Conditional Expression
# or - BOOLEAN or
# and - BOOLEAN and
# not x : Boolean NOT
# in, not in, is, is not, <, <=, >, >=, !=, == : Comparisons, including membership tests and identity tests 
# | : Bitwise OR
# ^ : Bitwise XOR
# & : Bitwise AND
# <<, >> : Shifts
# +, - : Addition and subtraction
# *, /, //, % : Multiplication, Division, Floor Division and Remainder
# +x, -x, ~x : Positive, Negative, bitwise NOT
# ** : Exponentiation
# x[index], x[index:index], x(arguments...), x.attribute : Subscription, slicing, call, attribute reference
# (expressions...), [expressions...], {key: value...}, {expressions...} : Binding or tuple display, list display, dictionary display, set display

# You can specify multi-line strings using triple quotes - (""" or '''). You can use single quotes and double quotes freely within the triple quotes. An example is:

'''This is a multi-line string. 
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
'''

# What Python does in the format method is that it substitutes each argument value into the place of the specification. There can be more detailed specifications such as:

# decimal (.) precision of 3 for float '0.333'
print('{0:.3f}'.format(1.0/3))
# fill with underscores (_) with the text centered
# (^) to 11 width '___hello___'
print('{0:_^11}'.format('hello'))
# keyword-based 'Swaroop wrote A Byte of Python'
print('{name} plays {book}'.format(name='pixel', book='roblox'))

# Since we are discussing formatting, note that print always ends with an invisible "new line" character (\n) so that repeated calls to print will all print on a separate line each. To prevent this newline character from being printed, you can specify that it should end with a blank:

print('a', end='')
print('b', end='')
# Or end with space
print('a', end=' ')
print('b', end=' ')
print('c')

# Strings
s = 'This is a string. \
This continues the string.'
print(s)
# is the same as:
s = 'This is a string. This continues the string.'
print(s)

# Indentations:

# Whitespace is important in Python. Actually, whitespace at the beginning of the line is important. This is called indentation. Leading whitespace (spaces and tabs) at the beginning of the logical line is used to determine the indentation level of the logical line, which in turn is used to determine the grouping of statements. This means that statements which go together must have the same indentation. Each such set of statements is called a block. We will see examples of how blocks are important in later chapters.

# Error below! Notice a single space at the start of the line

# i = 5
 # print('Value is', i)
# print('I repeat, the value is', i)

#  File "whitespace.py", line 3
#    print('Value is', i)
#    ^
#IndentationError: unexpected indent

# Notice that there is a single space at the beginning of the second line. The error indicated by Python tells us that the syntax of the program is invalid i.e. the program was not properly written. What this means to you is that you cannot arbitrarily start new blocks of statements (except for the default main block which you have been using all along, of course). Cases where you can use new blocks will be detailed in later chapters such as the control flow.

# strings, intergers, floats and booleans
string_data = str(input("type a string here: "))
integer_data = int(input("type an integer here: "))
float_data = float(input("type a float here: "))
boolean_data = bool(input("type a boolean here: "))
databool = True

print("strings are anything that involves letters, grammar and text")
print(f"integers are whole numbers that can be manipulated using math functions {integer_data + 12/3}")
print(f"floats are any number, floats can be decimals, negatives and whole numbers {float_data/3.2*17.23+-3}")
if boolean_data and databool == True:
    print(f"boolean is true, false, and, or and not {boolean_data}")
else:
    print(f"boolean is true, false, and, or and not {databool}")

#functions allow you to compress pieces of code that may need to be used multiple times
def do_smth():
    print("this did something")
do_smth()

#functions can have parameters that can be called on as a variable when writing the code within the function and will be defined when called
def data_show(number, kind):
    print(f"{kind} has {number} instances")
dat_show(7, "water")

#variables*
x = "this is a variable"

#print command*
print("this with send a message")

#inputs*
x = input("this is where you can get the user to type stuff: ")

#if, elif and else*
if x == "this is a variable":
    print("try changing the variable and see the result")
elif x == "something":
    print("this will only happen when both the if is false and the elif is true")
else:
    print("this will happen when both the if and elif are false")

#functions*
def define():
    print("defining something will shorten code and make things easier by making a section of code one line")
define()

#dictionaries
mydictionary = {
    "a dictionary":1,
    "assigns a key": "and a value",
    "and act": "as extended variables"
}
print(mydictionary["a dictionary"])

#while loop*
while x == "while":
    print("while loops will continue to loop until the condition is false")
    x = input("this is where you can get the user to type stuff: ")

#for in range loop*
for n in range(6):
    print(n)

#lists
mylist = ["this","is","a","list"]
print(mylist[0])
mylist.append(1)
print(mylist)

#classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

try:
    print(error_maker)
except:
    print("error!")
else:
    print("nothing's wrong")

#tuples
mytuple = ("apple", "banana", "cherry")
for i in mytuple:
  print(i)

#counting
x = "this will output the number of items in a string or list"
print(len(x))

#splitting
inp = input("this will become a list ")
inp.split()
print(inp)

#replacing strings
inp = input("your input will be changed ")
inp = inp.replace(inp[0:],"this has replaced your input")
print(inp)

#sorting
mylist = ["this", "will", "be", "sorted"]
mylist.sort()
print(mylist)

#equal and not equal to
inp = int(input("Number? "))
if inp == 3:
    print("that is equals to")
elif inp != 5:
    print("that is not equal to")

#data types
data = input("input in any data type: ")
print(type(data))

#unpacking tuples
tuple1 = ("this", "will", "be", "unpacked", "and", "become", "a", "variable")
(it, will, be, assigned, *here) = tuple1
print(it)
print(will)
print(be)
print(assigned)
print(here)

#looping tuples
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

#count instances in a tuple
mytuple = ("things", "in", "here", "will", "be", "repeated", "repeated")
counted = mytuple.count("repeated")
print(counted)

#search for a specific item
thistuple = ("this","has","been","found")
searching = thistuple.index("found")
print(searching)

#sets
set1 = {"this", "is", "a", "set"}
print(set1)

#adding to sets
thisset = {"hello","there","good",}
thisset.add("morning")
print(thisset)

#clearing a set
myset = {"this", "will", "disappear"}
myset.clear()
print(myset)

#merging sets
set2 = {"this", "will"}
set3 = {"be", "merged"}
z = set2.intersection(set3)
print(z)