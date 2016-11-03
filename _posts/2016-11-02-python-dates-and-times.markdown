---
layout: post
title: "Python Dates and Times"
date: "2016-11-02 18:45:04 -0700"
categories: Data
tags: [Jupyter, Notebook, IPython, Date, Time, Data, Analytics, Coursera]
---


# Python Dates and Times

Dates and times can be stored in many different ways.  
The offset from the **Epoch** is one of the most common nethods for storing dates and time.  
The Epoch is January 1, 1970. The measurements is usually the numer of miliseconds since this date.  

In Python you can get the current time since the epoch using the time module.


```python
import time as tm
```


```python
tm.time()
```




    1478139144.00778



You can create a timestamp using the `fromtimestamp()` function on the datetime object


```python
import datetime as dt
```


```python
dtnow = dt.datetime.fromtimestamp(tm.time())
dtnow
```




    datetime.datetime(2016, 11, 2, 19, 12, 25, 640018)



The datetime object has attributes to get the representative hour, day, seconds, etc

datetime objects allow for simple math using time deltas.  
This allows us to use a date and a time delta to find another date seperated by that delta.

Let's find the date 100 days before today using the `timedelta()` function in the datetime library.  


```python
delta = dt.timedelta(days = 100)
delta
```




    datetime.timedelta(100)




```python
today = dt.date.today()
```


```python
today - delta
```




    datetime.date(2016, 7, 25)



Here we see that 100 days before today - _previously shown at 2016, 11, 2_ - is 2016, 7, 25

We can also use conditionals as expected. Are timestamps equal to greater than less than etc, using are known conditional operators.  
For example: Today is certainly greater than 100 days ago we just computed (when measuring time since the Jan 1 1970 epoch)


```python
today > today-delta
```




    True
