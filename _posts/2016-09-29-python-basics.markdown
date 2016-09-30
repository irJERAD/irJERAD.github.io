---
layout: post
title: "Python Basics"
date: "2016-09-29 16:15:55 -0700"
categories: Learning
tags: [Learn, Python, Basics, Programming, Notes, Treehouse, Class]
---

Every programming language has specific words and rules for using them which we call **syntax**. Some languages also have rules about how the code should look. _Python has both of these!_
### Blocks, Variables and Functions
* Blocks
    * sections of code that are related - such as a function or a loop.
    * Blocks are indented one _extra step_.
    * Each indentation step should be **4 spaces** - but you can usually just hit tab and your code editor will put in the spaces for you. **Silicon Valley Joke or GIF**
    * Blocks start with a colon after the function name

* Variable and Function names
    * All lower cased
    * Use underscore instead of spaces
        * You cannot use spaces or hyphens in variable names

### Launch and use python shell
To start python from the Mac OS terminal shell type `$ python`
This course will be using python 3.4 + and since the native python for Mac is 2.7 + we need to explicitly request python 3 rather than python 2.

In order to start python 3 shell from the Mac Terminal type `$ python3` - _note there is no space between **python** and **3**_ - this will launch a python shell for the latest version of python 3 in your system

> To launch a python 3 terminal session use
```bash
$ python3
```


### Using help() function
When talking about a function and not using them we do not use the parenthesis.
> When talking about a function and not using them - such as searching for them in the `help()` function we do not use parenthesis
```python
help(print)
```
Press 'q' to exit the help screen

When looking for information on a specific method of a function we can use the dot notation.

> To learn more about the `center()` method in the `str()' function we can use the `help()` function as so:
```python
help(str.center)
```

Notice again that we do not use parenthesis when talking about functions or methods and not using them.


### Errors

#### Name Error
A name error happens whenever you try to use something that doesn't exist.
For Example:
```python
>>> 5 + x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
```

#### Operand Error
An operand error occurs when you try to execute an operation that python does not understand
For Example:
```python
>>> 5 + 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

#### Syntax Error
When you've typed something incorrectly that python just not understand you will get a **syntax error**

```python
>>> print("Hello)
  File "<stdin>", line 1
    print("Hello)
                ^
SyntaxError: EOL while scanning string literal
```
In this example of a SyntaxError we are given a pointer to where we are missing a quotation causing this syntax error.

```python
# create new Variable
variable_name = "variable value"
# delete variable
del variable_name
```

### Numbers
Python 2 would return an int when dividing two ints.  
Python 3 always returns a float from a devision.  

```python
# using += and -=
>>> age = 29
>>> age += 5
>>> age
34
>>> age -= 4
>>> age
30
```

```python
# calculate age in weeks
years = 29
# ignoring leap years
days = years * 365
weeks = days / 7
weeks
1512.142857142857
```

### Strings
In python strings are any gropu of characters between quote marks.

ways to use strings in python
```python
# print a basic string
>>> "he's right"
"he's right"

# however when we use the same quotations
# inline we get a SyntaxError
>>> 'he's right'
  File "<stdin>", line 1
    'he's right'
        ^
SyntaxError: invalid syntax

# We can escape the quote that is part of the string
>>> 'he\'s right'
"he's right"

# we can triple quote the outside of the string
>>> '''He's right'''
"He's right"

# We can create a long string
# with 3 double quotes at the beginning and end
>>> long_string = """Here's a new line!
...
... It's right there!"""
>>> print(long_string)
Here's a new line!

It's right there!
```

#### str.format()
You may not know what you want in the string ahead of time
```python
>>> "My {} is {}".format("name", "Jerad")
'My name is Kenneth'
>>> print("We have {} {} using the site right now".format(5, 'dogs'))
We have 5 dogs using the site right now
```

### Lists
Lists are the ultimate bucket. They can hold anything and not care what type of variable it is. Lists are mutable You can change these variables inside the list but the list remains the same list.

```python
>>> my_list = [1, 2, 3]
>>> my_list + 5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate list (not "int") to list

# as the error tells us we can only add a list to a list
>>> my_list + [4, 5]
[1, 2, 3, 4, 5]

# but this didn't change our list
# we can reassign lists
>>> my_list = my_list + [4, 5]
>>> my_list
[1, 2, 3, 4, 5]

# can use += -+ etc with list algebra
>>> my_list += [6, 7]
>>> my_list * 2
[1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7]

# use append() to a list
>>> my_list.append(6)
>>> my_list
[1, 2, 3, 4, 5, 6]

# append() can only add a single item to a list
>>> my_list.append(7, 8)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: append() takes exactly one argument (2 given)

# if we try to add a list we get a list as an item in the list
>>> my_list.append([7, 8])
>>> my_list
[1, 2, 3, 4, 5, 6, [7, 8]]

# We can use extend() in order to add multiple item to a list
>>> my_list = [1, 2, 3]
>>> my_list.extend([4, 5, 6])
>>> my_list
[1, 2, 3, 4, 5, 6]
# append() for 1 extend() for 2 or more

# if we have something in the list we don't want like before
# with remove() we can remove items from a list
>>> list_in_list = [1, 2, 3, [4, 5, 6]]
>>> list_in_list
[1, 2, 3, [4, 5, 6]]
>>> list_in_list.remove([4, 5, 6])
>>> list_in_list
[1, 2, 3]
```
