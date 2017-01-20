---
layout: post
title: "Social Media Scapping with twitteR Rstats and Donald Trump"
date: "2017-01-18 22:08:15 -0800"
tags: [data, mining, twitteR, R, RStudio, RStats,]
---

RtwitteR-Learn
================

Download Libraries and set working directory
--------------------------------------------

``` r
### maybe
## Get RBioing library
# source("https://bioconductor.org/biocLite.R")
# biocLite("RBioinf")

## Supporting tool libraries
#library(tools)
#library("RBioinf")
#library("DBI")
#library("RSQLite")

## twitteR library
# libraries above have are often used with these techniques
# but are not necessary for these examples
library(twitteR)
```

you can check r's current working directory with `getwd()`

``` r
# you can set working directory with
setwd("/home/Path/To/twitteR/exersizes")
```

Get permission for twitter API
------------------------------

    ## [1] "Using direct authentication"

``` r
consumer_key <- "ENTER-CONSUMER-KEY"
consumer_secret <- "ENTER-CONSUMER-SECRET"
access_token <- "ENTER-ACCESS-TOKEN"
access_secret <- "ENTER-ACCESS-SECRET"
# setup OAuth between this app and you twitter app
setup_twitter_oauth(consumer_key,consumer_secret,access_token,access_secret)
```

Get a User's tweets with Timeline
---------------------------------

userTimeline(user = ) can take a first argument of either a twitteR user object or the Twitter users hand - without the '@' symbol.
Here we are looking at \[@realDonaldTrump\](twitter.com/realDonaldTrump)'s account

``` r
# tweets from a user
recentTen <- userTimeline('realDonaldTrump',n=10)
# print 3 most recent tweets
recentTen[1:3]
```

    ## [[1]]
    ## [1] "realDonaldTrump: Thank you for a wonderful evening in Washington, D.C. #Inauguration https://t.co/a6xpFQTHj5"
    ##
    ## [[2]]
    ## [1] "realDonaldTrump: Thank you for joining us at the Lincoln Memorial tonight- a very special evening! Together, we are going to MAKE AM… https://t.co/OSxa3BamHs"
    ##
    ## [[3]]
    ## [1] "realDonaldTrump: Join me at 4pm over at the Lincoln Memorial with my family!\n#Inauguration2017 https://t.co/GQeQpJOgWz"

``` r
# get tweets from your home timeline
myTen <- homeTimeline (n=15)
# print my most recent tweet
myTen[1]
```

    ## [[1]]
    ## [1] "amasoliverdilme: Catalog of visualization tools https://t.co/1hP6fpwKxr https://t.co/Jp0sNaKbSG"

``` r
# get your tweets that were retweeted
myMention <- mentions (n=15)
# my most recent retweet
myMention[1]
```

    ## [[1]]
    ## [1] "tobiasgreener: @irJerad hi, Jerad! Would you be willing to have a look at the first paper planner which links directly to digital calendars?"

``` r
# tweets a user has favorited containing the favorites quote
# ten most recent favorites containing 'r_programming' in this case
favs <- favorites("r_programming", n =10)
# first 2 mentioning 'r_programming'
favs[1:2]
```

    ## [[1]]
    ## [1] "kaggle: Looking for a crash course on deep learning applied to natural language processing? See @aditdeshpande3's overview:… https://t.co/z2VzsiUGEP"
    ##
    ## [[2]]
    ## [1] "zevross: Starting to dig into the new sf (simple features) package for spatial data in #rstats. Very exciting! | https://t.co/e0Rt5gHQn7"

``` r
# get Donald Trump's 20 most recent tweets
D.twenty <- userTimeline('realDonaldTrump', n=20)
# view most recent tweet as a character class without the poster's name
D.twenty[[1]]$text
```

    ## [1] "Thank you for a wonderful evening in Washington, D.C. #Inauguration https://t.co/a6xpFQTHj5"

``` r
## The new efficient way using twListToDF() twitteR library
# Create a user object for information about the user account
D.User <- getUser('realDonaldTrump')
# scrape 100 most recent tweets from user
timeline <- userTimeline(D.User, n = 100)
# creates a data frame `tl.Frame` with 1 col
tl.Frame <- twListToDF(timeline)

## The old hacker way
# Creates 1 col data frame with each post as a character class row
#D.tweets <- ldply(userTimeline('realDonaldTrump', n=20), statusText)

## Max userTimeline
# max n number of tweets that can be retreived is 3200
Don3200 <- userTimeline(D.User, n = 3200)
# create data frame from twitteR list
t32k.Frame <- twListToDF(Don3200)
```

Original Tweets vs reTweets and replies
---------------------------------------

``` r
# retreive max tweets (including retweets and replies)
Don.Max <- userTimeline(D.User, n = 3200, includeRts = TRUE, excludeReplies = FALSE)

# retreive only original tweets from same length
Don.OG <- userTimeline(D.User, n = 3200, includeRts = FALSE, excludeReplies = FALSE)

# create data frame from each twitteR list
Max.list <- twListToDF(Don.Max)
OG.list <- twListToDF(Don.OG)
```

19.59375% of Donald Trump's tweets are his original material.
The remaining 2573 tweets, or 80.40625% are retweets from other users, or replies to the tweets of other users.

Create Data Frame and Print twitteR list / S4 Object
----------------------------------------------------

``` r
# convert Twitter list, containing S4 object
don.Frame <- twListToDF(D.twenty)

# creat text doc from twitteR list in current directory
# getwd() for current directory
write.table(don.Frame, "don2Jan18.txt", sep="\t")

# create csv with from Data frame in current directory
# default has variable names as column names, and index as row
write.csv(don.Frame, file = "Don18csvJan18.csv")
```

Search Twitter for Topic / Phrase
---------------------------------

``` r
# search recent tweets and return `n` tweets with the defined topic
## Note: can use `"#hashTag"` as search criteria if searching for tags
## Note: add `cainfo="cacert.pem"` to searchTwitter() arguments for windows
tweets <- searchTwitter("Donald Trump", n=100)
```

Create a Word Cloud from User Tweets
------------------------------------

You can also embed plots, for example:

``` r
library(wordcloud)
```

    ## Loading required package: RColorBrewer

``` r
library(tm)
```

    ## Loading required package: NLP

``` r
library(XML)
library(RColorBrewer)

# take recent 100 tweets and extract tweets as characters
tweet.text <- tl.Frame$text
# Create corpus from tl.Frame data frame [1] = text, with tm library
tcorpus <- Corpus(VectorSource(tweet.text))
tcorpus <- Corpus(DataframeSource(tl.Frame[1]))
## Simplify text for exploration
# remove punctuation
doc <- tm_map(tcorpus, removePunctuation)
# remove numbers
doc <- tm_map(doc, removeNumbers)
# lowercase to equaalize words
doc <- tm_map(doc, tolower)
# remove stopwords from text for more insightful results
doc <- tm_map(doc, removeWords, stopwords('english'))

# make plain text document from the corpus, with tm libary
doc <- tm_map(doc, PlainTextDocument)

# ste  the words so alterations like read and reading are counted as the same
doc <- tm_map(doc, stemDocument)

## online examples showed this usage
# sdoc <- stemDocument(doc[[1]])

# but this works from the remove english stop words
wordcloud(doc, max.words = 100, random.order = FALSE)
```

![b&w][b&w]
![b&w](/images/RtwitteR-Learn_files/figure-markdown_github/word-cloud-1.png)

``` r
# with color and changing rot.per setting
pal <- brewer.pal(9,'Reds')
wordcloud(doc, max.words = 100, random.order = FALSE, rot.per=0.2, colors=pal)
```

![color][color]
![color](/images/RtwitteR-Learn_files/figure-markdown_github/word-cloud-2.png)

``` r
# testing if twitter keeps tweets that donald apparently deletes every days
here <- userTimeline(user = D.User, n=5, sinceID="821930600290521089")
```

[b&w]: </images/RtwitteR-Learn_files/figure-markdown_github/word-cloud-1.png>
[color]: </images/RtwitteR-Learn_files/figure-markdown_github/word-cloud-2.png>
[Schematic Symbols]: </images/interfacing-with-arduino/schematic-symbols.png> "Schematic Symbols Cheat Sheet"
TODO
----

-   \[ \] Look into comparison.cloud() in wordcloud library
    -   compares two different documents to create a cloud from the differences
