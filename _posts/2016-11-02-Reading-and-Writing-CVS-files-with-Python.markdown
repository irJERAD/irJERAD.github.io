---
layout: post
title: "Reading and Writing CSV files in Python"
date: "2016-11-02 18:01:36 -0700"
categories: Data
tags: [Jupyter, Notebook, IPython, CSV, Data, Analytics]
---

# Reading and Writing CSV files in Python
Note: This was created in a Jupyter notebook then saved as a markdown file.

## Reading a CSV file
To open and read a CSV file, we will use the CSV package.  
precision set to 2 allows full floating point math while only printing 2 decimal places for legibility.  
Use `open('fileName')` to open **fileName** _from the current directory_.  
Finally, view the first 3 elements of the file we just loaded.


```python
import csv

# set floatpoint precision for printing to 2
%precision 2

with open('mpg.csv') as csvfile:
    mpg = list(csv.DictReader(csvfile))

# view first 3 elements of list created from csv file
mpg[:3]
```




    [{'': '1',
      'class': 'compact',
      'cty': '18',
      'cyl': '4',
      'displ': '1.8',
      'drv': 'f',
      'fl': 'p',
      'hwy': '29',
      'manufacturer': 'audi',
      'model': 'a4',
      'trans': 'auto(l5)',
      'year': '1999'},
     {'': '2',
      'class': 'compact',
      'cty': '21',
      'cyl': '4',
      'displ': '1.8',
      'drv': 'f',
      'fl': 'p',
      'hwy': '29',
      'manufacturer': 'audi',
      'model': 'a4',
      'trans': 'manual(m5)',
      'year': '1999'},
     {'': '3',
      'class': 'compact',
      'cty': '20',
      'cyl': '4',
      'displ': '2',
      'drv': 'f',
      'fl': 'p',
      'hwy': '31',
      'manufacturer': 'audi',
      'model': 'a4',
      'trans': 'manual(m6)',
      'year': '2008'}]



Here we can see each element of this list is a car in a dict form, the keys for the dict corresponds to a column in the csv file.

Lets see how many dicts - or cars - we have in our dataset


```python
len(mpg)
```




    234



We have a dictionary for each of the 234 cars in the dataset.

To extract just the column names, or the keys in each of these dictionaries we can use the `keys()` function on the first element in the mpg dataset since we are assuming each element has the same keys or _row names_


```python
mpg[0].keys()
```




    dict_keys(['', 'manufacturer', 'class', 'year', 'cyl', 'hwy', 'model', 'fl', 'displ', 'cty', 'drv', 'trans'])



Here we can see we have class, model, fuel type, cty, mpg, engine volume, front or rear wheel drive, highway mpg, manufacturer, model, year, and transmission type.

**NOTE:** I happen to know this from working with the same __cars__ dataset in R. This can easily be found on google when looking at the values is not helping.

Now let's try and find the average city MPG across all cars in our CSV file.
To do this we want to sum the value for the 'cty' key for each car in the set and divide by the number of cars used (which we already know the set to contain 234 cars).

So that should look something like:  
sum (each value of cty in dataset mpg) / size (mpg)


```python
sum(float(d['cty']) for d in mpg) / len(mpg)
```




    16.86



Now let's do the same thing for average hwy mpg across all cars in the dataset


```python
sum(float(d['hwy']) for d in mpg) / len(mpg)
```




    23.44



**Note:** the average mpg for highway is significantly better than for city.  
This makes sense, as cars get better gas milage on the highway that in the city.

## Grouping
#### Find the average city mpg grouped by the number of cylinders a car has.

### Sets
**Sets** are lists with no duplicate entries.  
We can see how many unique values - or _Levels_ - for cylinders the cars in this dataset have by defining a `set()` from the entire list of all cyl values.  


```python
cylinders = set(d['cyl'] for d in mpg)
cylinders
```




    {'4', '5', '6', '8'}



Here we see there are 4 unique levels for the cyl key: 4, 5, 6, and 8

Now we can iterate across each of the cylinder levels,  
then iterate over all the dictionaries.  
If the level for the current dictionary matches the current cylinder being calculated,  
add the mpg to that cylinder's level summpg variable and increment the count in order to average the total.  
After doing through each dictionary in the CSV, we can compute the MPG calculation and append it to our list.


```python
# create an empty list to store calculations
CtyMpgByCyl = []

# start with one cylinder level and iterate
for c in cylinders:
    summpg = 0
    cyltypecount = 0

    # though each dictionary checking for an equal level cyl value
    for d in mpg:
        # if a match is found, add cty to the sum and increase the count to compute the average
        if d['cyl'] == c:
            summpg += float(d['cty'])
            cyltypecount += 1
    # after iterating through all the dictionaries, append MPG calculation and go to the next cylinder level
    CtyMpgByCyl.append((c, summpg / cyltypecount))

CtyMpgByCyl.sort(key=lambda x: x[0])
CtyMpgByCyl
```




    [('4', 21.01), ('5', 20.50), ('6', 16.22), ('8', 12.57)]



After sorting the list of calculations we see that as the number of cylinders increases, the city miles per gallon, `'cty'`, decreases.  
This makes sense, as we would expect a car with more cylinders to be larger and have poorer city fuel milage.

#### Find the average highway MPG for the different vehicle classes

First let's look at the different classes of vehicles in the CSV dataset _mpg_


```python
vehicleclass = set(d['class'] for d in mpg)
vehicleclass
```




    {'2seater', 'compact', 'midsize', 'minivan', 'pickup', 'subcompact', 'suv'}



Similarly, we iterate each vehicle class through all the dictionaries.  
Each match will add highway mpg to the sum total and increase the count.
After exhausting all the dictionaries for a given vehicle class, we can computer the average and append it to our list.   


```python
HwyMpgByClass = []

for v in vehicleclass: # iterate over all the vehicle classes
    summpg = 0
    vclasscount = 0
    for d in mpg: # check each dictionary in the mpg dataset
        if d['class'] == v: # to find a match in class
            summpg += float(d['hwy'])
            vclasscount += 1 # increment the count
    HwyMpgByClass.append((v, summpg / vclasscount)) # append the tuple ('vehicle class', 'avg mpg')

HwyMpgByClass.sort(key=lambda x: x[1]) # this time, sort based on MPG - the second element in each tuple
HwyMpgByClass
```




    [('pickup', 16.88),
     ('suv', 18.13),
     ('minivan', 22.36),
     ('2seater', 24.80),
     ('midsize', 27.29),
     ('subcompact', 28.14),
     ('compact', 28.30)]



Here we have found the pickup to have the worst highway MPG while **the compact has the highest highway MPG.**

Do not despair or completely write off Python as an inefficient iterator of data for summarization.  
The **Pandas** library will bring in many of the tools and tricks us R thoroughbreds have come to rely upon for speedy exploration and summarization of a dataset with a few quick key strokes - well maybe a few extra, but much better than this spiraling mess.
