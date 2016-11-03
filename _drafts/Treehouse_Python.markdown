### join() and split()

"'what you want between joined items of list'".join(list_name) # default is space
string_name.split('what to split by') # default is space

```python
# join items from list to string
list_in = ["Hello", "There"]
' '.join(list_in)

# split items from string to list
string_name = "Thing1 Thing2"
list_out = string_name.split(' ')
print(list_out))
```


 ---
### del
Delete variables from memory or delete a single item from a list
```python
# delete var_name from memory
var_name = "This can be any type of variable"
del var_name

# delete item # index from list_name
list_name = [item1, item2, item3]
del list_name[index]
```


---
### Shopping list

---
### Shopping list challenge tasks
Inside of the function, I need a for loop that prints each thing in items. But, if the current thing is the string "STOP", break the loop.
```python
def loopy(items):
    # Code goes here
    for item in items:
        if item == 'STOP':
            break
        print(item)
```

Be able to skip items:
Loop through every item in items. If the current item's index 0 is the letter "a", continue to the next one. Otherwise, print out the current member.
```python
def loopy(items):
    # Code goes here
    for item in items:
        if item[0] != 'a':
            print(item)
```

You probably recognize this code. It's pretty much our shopping_list_2.py from before. I want you to help me with a little refactor, though. Refactoring is when we change code to make it better, often by creating new functions.
Create a new function named main that doesn't take any arguments.
Move everything from line 22 (show_help()) and below into your new function. You shouldn't have any code that isn't inside of a function.

```python
def show_help():
    # print out instructions on how to use the app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
""")

def show_list(shopping_list):
    # print out the list
    print("Here's your list:")

    for item in shopping_list:
        print(item)

def add_to_list(shopping_list, new_item):
    # add new items to our list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))
    return shopping_list

def main():
    show_help()

    # make a list to hold onto our items
    shopping_list = []

    while True:
        # ask for new items
        new_item = input("> ")

        # be able to quit the app
        if new_item == 'DONE':
            break
        elif new_item == 'HELP':
            show_help()
            continue
        elif new_item == 'SHOW':
            show_list(shopping_list)
            continue
        add_to_list(shopping_list, new_item)

    show_list(shopping_list)
```

---
### Number Game

---
### Number game challenge tasks
Write a function named even_odd that takes a single argument, a number.
return True if the number is even, or False if the number is odd.
```python
def even_odd(num):
    if num % 2 == 0:
        return True
    else:
        return False
```

Create a new function named just_right that takes a single argument, a string.
If the length of the string is less than five characters, return "Your string is too short".
If the string is longer than five characters, return "Your string is too long".
Otherwise, just return True.
```python
def just_right(string):
    if len(string) < 5:
        return "Your string is too short"
    elif len(string) > 5:
        return "Your string is too long"
    else:
        return True
```


Write a function named squared that takes a single argument.
If the argument can be converted into an integer, convert it and return the square of the number (num ** 2 or num * num).
If the argument cannot be turned into an integer (maybe it's a string of non-numbers?), return the argument multiplied by its length.
```python
# EXAMPLES
# squared(5) would return 25
# squared("2") would return 4
# squared("tim") would return "timtimtim"
def squared(num):
    try:
        num = int(num)
        # if this works, return the square of the input num
        return num ** 2
    except ValueError:
        # if unable to convert num to int, return num multiplied by its length
        return num * len(num)
```

---
### Letter Game

---
### Letter Game challenge tasks

First, import the random library.
Then create a function named random_item that takes a single argument, an iterable. Then use random.randint() to get a random number between 0 and the length of the iterable, minus one. Return the iterable member that's at your random number's index.
```python
# EXAMPLE
# random_item("Treehouse")
# The randomly selected number is 4.
# The return value would be "h"
import random

def random_item(iterable):
    indx = random.randint(0, len(iterable) - 1)
    return iterable[indx]
```

Use input() to ask the user if they want to start the movie.
If they answer anything other than "n" or "N", print "Enjoy the show!". Otherwise, call sys.exit(). You'll need to import the sys library.
```python
import sys

watch = input("Would you like to start the movie? Y/n ").lower()
if watch != 'n':
    print("Enjoy the show!")
else:
    sys.exit()
```

Make a while loop that runs until start is falsey.
Inside the loop, use random.randint(1, 99) to get a random number between 1 and 99.
If that random number is even (use even_odd to find out), print "{} is even", putting the random number in the hole. Otherwise, print "{} is odd", again using the random number.
Finally, decrement start by 1.
```python
import random

start = 5
def even_odd(num):
    # If % 2 is 0, the number is even.
    # Since 0 is falsey, we have to invert it with not.
    return not num % 2

while start:
    rndm_num = random.randint(1, 99)
    if even_odd(rndm_num):
        print("{} is even".format(rndm_num))
    else:
        print("{} is odd".format(rndm_num))
    start -= 1
```
