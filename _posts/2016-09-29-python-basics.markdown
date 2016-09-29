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

> To learn more about the `center()` method in the `str()` function we can use the `help()` function as so:  
```python
help(str.center)
```

Notice again that we do not use parenthesis when talking about functions or methods and not using them.
