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

>For each of the examples, some forecast of future demand is an essential.  

A newsvenver problem requires the actor to make their decisions before the demand or consuption is known.

1. **Governments order flu vaccines** before the flu season begins, and before the extent of the nature of the flu strain is known.
	- How many vaccines to order?  
	- This is a *Newsvendor Problem* because you have to know how to make your decision before the demand is known.
2. Smartphone users buy **mobile data plans** before they know their actual future usage
	- What is the right plan for you?
3. Consumers **buy health insurance plans**, before they know their actual health expenditures.
	- How to think about the right plans?


## Forecasting

### Introduction to Forecasting

#### What is Forecasting?
The primary function of **forecasting** is to predict the future.
Predicting the future is appealing because it dictates the kind of decisions we make today. It follows that the quality of these decisions should be directly related to the accuracy of our forecasting.
>If we know something about the future, we can make better decisions today.

There are lots of economic uses for forecasting.  
Typical applications of forecasting can be seen in:
- Forecasting demand for products and demand for services.
- Forecasting inventory needs and forecasting capacity needs
- and so on...

#### Quality of a Forecast
Forecasting is obviously important and valued, but **What makes a good forecast?**
- Timely: a perfect forecast immediately becomes no more valuable than a statement when it is no longer about the future)
- Accuracy: the more accurate a forecast, the more enhanced decisions can become
- Meaningful units: knowing demand for a product will increase is not nearly as valuable as knowing whether it will double or increase tenfold
- The forecasting method should be easy to use and understood in practice

#### The First rule of Forecasting
**The first rule of forecasting is that point forecasts are usually wrong.**

To forecast that the temperature will be 78.2 degrees fahrenheit provides an infinite amount of possibilities to be proven wrong just between 78.3 and 78.4 degrees

We cannot predict future demand with certainty.

We can try to decide what future demand scenarios are possible and for each scenario, estimate the likelihood of its realization.

Trying to leverage the most value from forecasting, and with *the first rule of forecasting in mind*, we combine likelihoods with scenarios to distribute forecast over a probability space. This probability space can then provide us with expected values that act almost as an *average of forecasts*

For example:
If analyzing data lead us to conclude on the following scenarios:
- Likelihood of "high" demand is 20%
- Likelihood of "normal" demand is 70%
- Likelihood of "low" demand is 10%

To simplify things further, let's say there were only these three options and that "normal" was twice as likely as "low" and half as likely as "high"

Assuming this was a complete system we could statistically compute the expected demand as so:
P(demand is 20%) = 2 x P(demand is 70%) = 4 x P(demand is 10%)
And because of our assumption this was a complete system
P(demand is 20%) + P(demand is 70%) + P(demand is 10%) = 1

Substitution gives us:
4 x P(demand is 10%) + 2 x P(demand is 10%) + P(demand is 10%) = 1
OR
7 x P(demand is 10%) = 1 <==> P(demand is 10%) = 1/7

We can then quickly find that
P(demand is 70%) = 2/7
and
P(demand is 20%) = 4/7

Again, due to a gross over simplification for examples sake, we could then conclude an expected value of:
Expected value of Demand = E[demand = 20%] + E[demand = 10%] + E[demand = 70%] = 


[Coursera]: <https://Coursera.org> "Online Classes From Top Universities"
[Operations Analytics]: <https://www.coursera.org/learn/wharton-operations-analytics> "Transforming Data into Better Decisions"
[Business Analytics]: <https://www.coursera.org/specializations/business-analytics> "Achieve Fluency in Business Data Strategies in Four Discipline-Specific-Courses"
[Wharton]: <https://www.wharton.upenn.edu> "Wharton School"
[Yahoo]: <https://Yahoo.com> "Do you Yahoo?"
[NewsVendor Wiki]: <https://en.wikipedia.org/wiki/Newsvendor_model> "Newsvendor Model"

[Demand Data]: </images/Operations-Analytics/demand-data.png> "Fake Demand Data for Newsvendor Problem"
