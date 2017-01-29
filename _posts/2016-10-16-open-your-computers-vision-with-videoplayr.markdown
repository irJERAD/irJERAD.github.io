---
layout: post
title: "Open Your Computer's Vision with videoplayR"
date: 2016-10-16 16:10:10 -0700
categories: How-To
tags: [Computer Vision, videoplayR, R, OpenCV, OpenCV3, CRAN, Tutorial]
---

## Work in Progress
As a work in progress this should be _along with quite a few other posts here_ in my \_drafts folder. However, for this one, I remote access to its current state for other project I have going on. (I have no excuse for the myriad of other unfinished drafts in my \_posts directory but I do have _hopes_ that I'll get around to them - It's just that greedy habit of mine to prioritize learning and experience over sharing and teaching. I love 'em all but time only permits about the top 1.5 ~ 2% of the activities swirling around in my head at any moment)

As of the writing of this post, videoplayR is unfortunately **not currently available through [CRAN](https://cran.r-project.org)**. It is currently - as far as my R package creation and management understanding goes - not possible for this to be supported and easily installed through CRAN. This is strictly a result of the package's external dependency on OpenCV - a library that most likely doesn't require introduction for most interested in this post. Written in C++ requires some multi-platform setup to ship OpenCV with the videoplayR package through CRAN which presents a host of issues beyond my current ability to explain (read: _beyong my current understanding_).

**HOWEVER: There is a way** and a _somewhat_ simple one at that!

If you are at all familiar with [Homebrew](Homebrew), CRAN, and installing R packages from Github using the [devtools package][devtools], then please: list any issues and solutions you may have had while tinkering around.  
If you don't know any of this, fret-not, I hope to make this an easy to walk through example of some Computer Vision fun to be had within R.
If you prefer MacPorts as your package manager I will add instructions for Port as well. Note, however, that I personally used and acquired all my hard earned lessons and battle scars managing OpenCV2.3 and OpenCV3 via Homebrew (after installing the OpenCV library **AND** correctly linking all the necessary paths, the R parts were a walk in the park - so maybe that says more about my choice of package management tool than the difficulty of this tutorial)


{% comment sources %}
Sources:

[videoplayR vignette]: <http://rpubs.com/sjmgarnier/videoplayR> "Vignette written by author of videoplayR"
[videoplayR Github]: <https://github.com/swarm-lab/videoplayR> "Github for videoplayR package"

[Homebrew]: <http://brew.sh> "Homebrew homepage"
[devtools]: https://www.rstudio.com/products/rpackages/devtools/ "devtools RStudio about page"
{% endcomment sources %}
