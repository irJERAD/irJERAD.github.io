---
layout: post
title: "Notebook Basics"
date: "2016-11-09 19:37:42 -0800"
categories: [Cheat Cheat]
tags: [Learn, Python, iPythong, Jupyter, Notebook, Lynda]
---

In my Jupyter and iPython Data adventures I find having access to this information expedites my work and thus belongs somewhere easy to keep.
# What is a Jupyter notebook?

#### Application for creating and sharing documents that contain:
- live code
- equations
- visualizations
- explanatory text

Home page: http://jupyter.org/

# Notebook tutorials
- [Quick Start Guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/)
- [User Documentation](http://jupyter-notebook.readthedocs.io/en/latest/)
- [Examples Documentation](http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/examples_index.html)
- [Cal Tech](http://bebi103.caltech.edu/2015/tutorials/t0b_intro_to_jupyter_notebooks.html)

# Notebook Users
- students, readers, viewers, learners
    - read a digital book
    - interact with a "live" book
- notebook developers
    - create notebooks for students, readers, ...

# Notebooks contain cells
- Code cells
    - execute computer (Python, or many other languages)
- Markdown cells
    - documentation, "narrative" cells
        - guide a reader through a notebook

# Following cells are "live" cells


```python
print ("Hello Jupyter World!; You are helping me learn")
```

    Hello Jupyter World!; You are helping me learn



```python
(5+7)/4
```




    3




```python
import numpy as np
my_first_array = np.arange(11)
print (my_first_array)
```

    [ 0  1  2  3  4  5  6  7  8  9 10]
