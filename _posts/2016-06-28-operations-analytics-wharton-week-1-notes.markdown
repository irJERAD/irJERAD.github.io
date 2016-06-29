---
layout: post
title: "Operations Analytics Wharton Week 1 Notes"
date: "2016-06-28 23:16:15 -0700"
categories: learning
tags: [learn, business, analytics, Wharton, Coursera, notes]
---

### Operations Analytics Notes for Week 1:
> The descriptive analytics covered this week will provide a strong conceptual basis for predictive and prescriptive analytics in the following three weeks of the course.

### Covered by this Courser
The class will start by going over a number of the most important and familiar problems in operations.
The Newsvendor Problem is one of the fundamental problems in operations. We will also cover a range of related problems such as Resource Allocation, Network Management and Capacity Planning.
By the end of this course, a familiarity with important problems and with operations analytics methods for tackling them.

#### Descriptive Analytics
Descriptive Analytics function to characterize data and to forecast future events.

#### Predictive and Prescriptive Analytics
Predictive and Prescriptive Analytics are employed to evaluate alternatives and to select the best course of action both in low and in high uncertainty environments.

> Operations is about making good decisions in the frequent setting of uncertainty about future events.

## The Newsvendor Problem
The [Newsvendor Problem][NewsVendor Wiki] is about matching demand with supply in uncertain settings.

We need to be able to describe uncertainty in our data.


Week 1 will be spread across four themed sessions - All of which will center on **descriptive analytics**
Session:
1. Operational Decision Problem: Newsvendor Problem  
  - Random Variables
  - Demand Distributions
2. Forecasting with Past Historical Data
  - Moving Averages
  - Exponential Smoothing (advanced materials)
3. Thinking about Trends and Seasonality
  - Forecasting when the data shows trend or seasonality
4. Forecasting for New Products
  - Fitting Demand Distributions

### Newsvendor Problem, problems
The issue with the Newsvendor problem is accurately predicting future demand to properly stock an item of merchandise.
Oversaturated, order too much:
Purchased n-more pieces of merchandise than were sold by anticipating more d-demand than turned up in reality --> loss of n \* (cost per item)  
Unmet demand, did not order enough:
Purchased m-fewer pieces of merchandise than d-demand --> loss of m \* (profit per item) in potential gains.  

![Demand Data][Demand Data]

### Breaking down the Newsvendor Problem
**Characteristics:**
- You have an objective: usually maximize profits, minimize costs, improve market share, etc.
- You have to make one decision: usually, how much to buy, or plan for.
- All this is decided and done before seeing the future demand.
- Demand occurs, and profits and costs are realized

### Case Study: A Business Application at *Time Inc.*
1. Time Magazine Supply Chain:
  - Stores were either selling out inventories (too little inventory :: under estimating demand)
  - or sold only a small fraction of allocation (too much inventory :: over estimating demand)
2. Time Magazine evaluated and adjusted for every issue:
  - National print order (total number of copies printed and shipped).
  - Wholesale allotment structure (How those copies are allotted to wholesalers)
  - Store distribution (Final distribution to stores).
3. Note: above three decisions are made before the actual demand is realized.  
  - Need to analyze past Data
  - Forecast future demand
4. Time Magazine reports saving #3.5M annually from tackling the newsvendor problem.
  - Koschat et al, *Interfaces*, Volume 33, No 3. May-June 2003, pages 72-84.

### Other Newsvendor Problems

>For each of the examples: some forecast of future demand is essential

1. **Governments order flu vaccines** before the flu season begins, and before the extent of the nature of the flu strain is known.
  - How many vaccines to order?
  - This is a *Newsvendor Problem* because you have to know how to make your decision before the demand is known.
2. Smartphone users buy **mobile data plans** before they know their actual future usage
  - What is the right plan for you?
3. Consumers **buy health insurance plans**, before they know their actual health expenditures.
  - How to think about the right plans?


[Coursera]: <https://Coursera.org> "Online Classes From Top Universities"
[Operations Analytics]: <https://www.coursera.org/learn/wharton-operations-analytics> "Transforming Data into Better Decisions"
[Business Analytics]: <https://www.coursera.org/specializations/business-analytics> "Achieve Fluency in Business Data Strategies in Four Discipline-Specific-Courses"
[Wharton]: <https://www.wharton.upenn.edu> "Wharton School"
[Yahoo]: <https://Yahoo.com> "Do you Yahoo?"
[NewsVendor Wiki]: <https://en.wikipedia.org/wiki/Newsvendor_model> "Newsvendor Model"

[Demand Data]: </images/Operations-Analytics/demand-data.png> "Fake Demand Data for Newsvendor Problem"
