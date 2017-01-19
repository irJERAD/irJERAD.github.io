---
layout: post
title: "Social Media Scapping with twitteR Rstats and Donald Trump"
date: "2017-01-18 22:08:15 -0800"
---

RtwitteR-Learn
================

``` r
### maybe
## Getting RBioing library
# source("https://bioconductor.org/biocLite.R")
# biocLite("RBioinf")

# twitteR library
library(twitteR)

# Supporting tool libraries
#library(tools)
#library("RBioinf")
#library("DBI")
#library("RSQLite")
```

Get permission for twitter API
------------------------------

``` r
consumer_key <- "7LXhWbwE2IdTuRYRcbSGTbHmA"
consumer_secret <- "bSiSCliPmpCmzy7GYw7yGZx6oiZOwxJ6nx0sUb74uFeDRtDmMG"
access_token <- "430928969-ZSbOAtGD3I10OJt6sTiyKWjz0YsQ9yWp95RRYC0d"
access_secret <- "4VYGGcBOUUnPd64k4uD7x9xghpCIC2X0eJis5wMgi4Y6x"
setup_twitter_oauth(consumer_key,consumer_secret,access_token,access_secret)
```

    ## [1] "Using direct authentication"

Get a User's Timeline tweets
----------------------------

You can include R code in the document as follows:

``` r
# tweets from a user
userTimeline('realDonaldTrump',n=10)
```

    ## [[1]]
    ## [1] "realDonaldTrump: Thank you to our amazing Wounded Warriors for their service. It was an honor to be with them tonight in D.C.… https://t.co/Qj5cpfaykD"
    ##
    ## [[2]]
    ## [1] "realDonaldTrump: Great seeing @TheLeeGreenwood  and Kimberly at this evenings VP dinner! #GodBlessTheUSA https://t.co/SxVmaWvOFT"
    ##
    ## [[3]]
    ## [1] "realDonaldTrump: Looking forward to a speedy recovery for George and Barbara Bush, both hospitalized. Thank you for your wonderful letter!"
    ##
    ## [[4]]
    ## [1] "realDonaldTrump: Writing my inaugural address at the Winter White House, Mar-a-Lago, three weeks ago. Looking forward to Friday.… https://t.co/J0ojOXjrga"
    ##
    ## [[5]]
    ## [1] "realDonaldTrump: .@TheAlabamaBand was great last night in D.C. playing for 147 Diplomats and Ambassadors from countries around the world. Thanks Alabama!"
    ##
    ## [[6]]
    ## [1] "realDonaldTrump: No wonder the Today Show on biased @NBC is doing so badly compared to its glorious past. Little credibility!"
    ##
    ## [[7]]
    ## [1] "realDonaldTrump: \"Bayer AG has pledged to add U.S. jobs and investments after meeting with President-elect Donald Trump, the latest in a string...\" @WSJ"
    ##
    ## [[8]]
    ## [1] "realDonaldTrump: to the U.S., but had nothing to do with TRUMP, is more FAKE NEWS. Ask top CEO's of those companies for real facts. Came back because of me!"
    ##
    ## [[9]]
    ## [1] "realDonaldTrump: Totally biased @NBCNews went out of its way to say that the big announcement from Ford, G.M., Lockheed &amp; others that jobs are coming back..."
    ##
    ## [[10]]
    ## [1] "realDonaldTrump: Will be interviewed by @ainsleyearhardt on @foxandfriends - Enjoy!"

``` r
# get tweets from home timeline
homeTimeline (n=15)
```

    ## [[1]]
    ## [1] "TheEconomist: Despite resistance from dons, it appears the government will get most of what it wants. That would be no bad result https://t.co/fYDIBg592S"
    ##
    ## [[2]]
    ## [1] "rapsody: RT @Jksonlv: Didn't waste no time, had to cop this on sight! https://t.co/x4Ocsp3iFZ"
    ##
    ## [[3]]
    ## [1] "buffer: The 10 most common social media marketing problems and how to effectively solve them: https://t.co/8o1mEYOmLY ✔️ https://t.co/B6kjKEzpfw"
    ##
    ## [[4]]
    ## [1] "BBCWorld: Japan hotelier's Nanjing massacre denial angers China https://t.co/1pPS400Q0b"
    ##
    ## [[5]]
    ## [1] "Inc: What You Need to Know About Video, According to Someone With 6 Million YouTube Subscribers @caseyneistat https://t.co/ip4yQ6wHbS"
    ##
    ## [[6]]
    ## [1] "nytimes: It may not be “Calexit,” but it is turning into what is, for all intents and purposes, a slow-motion secession https://t.co/vWDLZyPxUl"
    ##
    ## [[7]]
    ## [1] "adafruit: Small clamp works like the kant twist #3DPrinting #3DThursday https://t.co/zhzpYiuWjX"
    ##
    ## [[8]]
    ## [1] "SlackHQ: Threads rollout reached your team, and you're all: “Threads?! What the…” Well stop right there! We’ve got your back: https://t.co/ErSSUXINoG"
    ##
    ## [[9]]
    ## [1] "GuyKawasaki: How to find the right therapist https://t.co/0D9J2VKs5o https://t.co/xcdPQqeJmt"
    ##
    ## [[10]]
    ## [1] "FastCompany: Meetings are a skill you can master, and Steve Jobs taught me how https://t.co/cRYLS74cKi (from 2012) https://t.co/aeUhq5H6qK"
    ##
    ## [[11]]
    ## [1] "Atlassian: We surveyed 1,300 customers &amp; 17,000 software dev professionals to learn how they ship software. See what we found:… https://t.co/DLHRsL1WK2"
    ##
    ## [[12]]
    ## [1] "hackaday: Use A Brushless Motor As A Rotary Encoder https://t.co/PEwBiCey3I"
    ##
    ## [[13]]
    ## [1] "KPMG: #WEFLIVE: a unique way to view real-time conversations, trends and stats surrounding #WEF https://t.co/9QK9HYZ2Kp"
    ##
    ## [[14]]
    ## [1] "WSJ: Donald Trump to nominate Sonny Perdue as Agriculture Secretary https://t.co/BM1khmi7Ck"
    ##
    ## [[15]]
    ## [1] "adafruit: From the mail bag… https://t.co/ZaOMrCXPIE"

``` r
# get your tweets that were retweeted
mentions (n=15)
```

    ## [[1]]
    ## [1] "tobiasgreener: @irJerad hi, Jerad! Would you be willing to have a look at the first paper planner which links directly to digital calendars?"
    ##
    ## [[2]]
    ## [1] "attdeveloper: @irJerad Shared with the community. We look forward to seeing you at #ATTShape!"
    ##
    ## [[3]]
    ## [1] "LoyaltyManagers: Eli Edri: @irJerad , Learn how to keep your CRM's lead pipline full with Qwory - ... - https://t.co/15ifX1JKue #LoyaltyManagers"
    ##
    ## [[4]]
    ## [1] "_steve2_: @irJerad @ForceDevMeetup @charlieisaacs @salesforce @attdeveloper do any in denver?"
    ##
    ## [[5]]
    ## [1] "LoyaltyManagers: Eli Edri: @irJerad , Learn how to keep your CRM's lead pipline full with Qwory - ... - https://t.co/vj2U5cyEjK #LoyaltyManagers"
    ##
    ## [[6]]
    ## [1] "cafemasonSF: @irJerad Nice! If you could put anything in a crepe, what would it be?"
    ##
    ## [[7]]
    ## [1] "cafemasonSF: @irJerad YUM. Do you prefer sweet or savory crepes, generally?"
    ##
    ## [[8]]
    ## [1] "FredRivett: @irJerad @wecontrast Thanks for being the first to respond to the question, Jerad \xed\xa0\xbd\xed\xb9\x8c"
    ##
    ## [[9]]
    ## [1] "agungw132: RT@redsand74 Sifting the Boulders of #BigData is out! https://t.co/hB0R9uEiun Stories via @GrupoFractalia @SherryTechMktg @irJerad"
    ##
    ## [[10]]
    ## [1] "rjurney: @irJerad @thisismetis thanks!"
    ##
    ## [[11]]
    ## [1] "thisismetis: So glad you enjoyed! @irJerad @rjurney   https://t.co/HgpTKmvpZy"

``` r
# tweets a user has favorited
favs <- favorites("r_programming", n =10)

# get Donald Trump's 20 most recent tweets
D.twenty <- userTimeline('realDonaldTrump', n=20)
# view most recent tweet as a character class without the poster's name
D.twenty[[1]]$text
```

    ## [1] "Thank you to our amazing Wounded Warriors for their service. It was an honor to be with them tonight in D.C.… https://t.co/Qj5cpfaykD"

``` r
## The new efficient way using twListToDF() twitteR library
# Create a user object for information about the user account
D.User <- getUser('realDonaldTrump')
timeline <- userTimeline(D.User, n = 100)
# creates a data frame `tl` with 1 col
tl <- twListToDF(timeline)

## The old hacker way
# Creates 1 col data frame with each post as a character class row
#D.tweets <- ldply(userTimeline('realDonaldTrump', n=20), statusText)
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
#library(ggplot2)

# Create corpus from tl data frame [1] = text, with tm library
tcorpus <- Corpus(DataframeSource(tl[1]))
# make plain text document from the corpus, with tm libary
PLainText.Tweets <- tm_map(tcorpus, PlainTextDocument)

# remove stopwords from text for more insightful results
rmEngStop <- tm_map(PLainText.Tweets, removeWords, stopwords('english'))

# ste  the words so alterations like read and reading are counted as the same
stem.tweets <- tm_map(rmEngStop, stemDocument)

## TODO: doesn't work
# create wordcloud
wordcloud(stem.tweets, max.words = 100, random.order = FALSE)
```

![](RtwitteR-Learn_files/figure-markdown_github/word-cloud-1.png)

``` r
# but this works from the remove english stop words
wordcloud(rmEngStop, max.words = 100, random.order = FALSE)
```

![](RtwitteR-Learn_files/figure-markdown_github/word-cloud-2.png)

``` r
# with color and changing rot.per setting
pal <- brewer.pal(9,'Reds')
wordcloud(stem.tweets, max.words = 100, random.order = FALSE, colors = pal)
```

![](RtwitteR-Learn_files/figure-markdown_github/word-cloud-3.png)

``` r
#          rot.per=0.2, colors='Oranges')
```

TODO
----

-   \[ \] Look into comparison.cloud() in wordcloud library
    -   compares two different documents to create a cloud from the differences
