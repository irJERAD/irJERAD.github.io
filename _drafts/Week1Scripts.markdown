## Advanced Python Objects, map()
Question:
Here is a list of faculty teaching this MOOC. Can you write a function and apply it using `map()` to get a list of all the faculty titles and last names (e.g. ['Dr. Brooks', 'Dr. Collins-Thompson,'...])
Starts:
```python
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
  return #Your answer here

list(map("""Your answer here"""))
```

My Answer
```python
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
  p = person.split(' ')
  del p[1]
  return ' '.join(p)

list(map(split_title_and_name, people))
```

The Classes Answer:
```python
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    title = person.split()[0]
    lastname = person.split()[-1]
    return '{} {}'.format(title, lastname)

list(map(split_title_and_name, people))
```

---

## Advanced Python Lambda and List Comprehensions

### Lambda Functions
Example:
Simple Lambda
```python
my_function = lambda a, b, c : a + b
my_function(1, 2, 3)
```
`Output: 3`

Question:
Convert this function into a lambda:
```python
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda person:???))

#option 2
#list(map(split_title_and_name, people)) == list(map(???))
```

Answer:
```python
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_title_and_name(person):
    return person.split()[0] + ' ' + person.split()[-1]

#option 1
for person in people:
    print(split_title_and_name(person) == (lambda x: x.split()[0] + ' ' + x.split()[-1])(person))

#option 2
list(map(split_title_and_name, people)) == list(map(lambda person: person.split()[0] + ' ' + person.split()[-1], people))
```

### List Comprehensions

#### Sequences
**Sequences** are stuctures we can iterate over
* Tupals - tupal()
* Lists - list()
* Dictionaries - dict()
* "and so forth..."

Often we we create tese through loops or by reading in data from a file.
Python has build in suppot for creating these collections using a more abbreviated syntax call **List Comprehensions**

#### List Comprehensions
**List Comprehensions** are a condensed format which may offer readability and performance benefits and you'll often find them being used in data science tutorials or on stack overflow

Example: place all even numbers in a list
```python
# common way
my_list= []
for number in range(0,1000):
    # determine if current number is even
    if number % 2 == 0:
        # add even numbers to list
        my_list.append(number)

my_list
```
`Output:   [0, 2, 4, 6, 8, 10, 12, ..., 1000]  
`  
Write this as a **List Comprehension** by pulling the iteration on one line.
```python
# using a list comprehension
## start the list comprehension with the value we want in the list _number_
## then put in the for-loop, and finally add any conditional clauses
my_list = [number for number in range(0,1000) if number % 2 == 0]
my_list
```

List Comprehensions are:
* Much more compact
* Easier to write
* Easier to read
* tend to run faster as well

Question:
Convert this function into a list comprehension
```python
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == []
```

Answer:
```python
def times_tables():
    lst = []
    for i in range(10):
        for j in range (10):
            lst.append(i*j)
    return lst

times_tables() == [j*i for i in range(10) for j in range(10)]
```

**Question**
Many organizations have user ids which are constrained in some way. Imagine you work at an internet service provider and the user ids are all two letters followed by two numbers (e.g. aa49).  
Write an itialization line as a single list comprehension which creates a list of all possible user ids. Assume the letters are all lower case.
```python
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [???]
correct_answer == answer
```

```python
lowercase = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

answer = [i + j + k + l for i in lowercase for j in lowercase \
    for k in digits for l in digits]
correct_answer == answer
```

---

## Advanced Python Demonstration: The Numerical Pyton Library (NumPy)

TODO: Go through lesson in Jupyter notebook taking md notes and generating a MD output from the .ipnb file.

Question:
What is the correct output for this code?
```python
old = np.array([[1, 1, 1], [1, 1, 1]])

# remember: new and old are different identifiers pointing at the same object
new = old
# so assigning the first item [0]'s elements 0 until but not including 2
## changes the object which both new and old point to
new[0, :2] = 0

print(old)
```
`Output:
    [[0, 0, 1],
     [1, 1, 1]]`

```python
old = np.array([[1, 1, 1],
                [1, 1, 1]])

new = old.copy()
new[:, 0] = 0

print(old)
```

Question:
What is the correct output for this code?
```python
old = np.array([[1, 1, 1],
                [1, 1, 1]])

new = old.copy()
new[:, 0] = 0

print(old)
```
Note: Because `new` is an identifier of a new object which was copied from the old identifiers object - using `old.copy()` - we can change `new` without changing `old`
`Output:
        [[1 1 1]
        [1 1 1]]`
