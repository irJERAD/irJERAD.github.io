---
layout: post
title: EON Chart Builder | by PubNub
date: jekyll_insert_date
categories: Blog
tags: [IoT, Sensors, Connected Devices]
---

As I've begun to settle down in SF - after a quick 2 years nearly - I have
started to kick my feet up and unpack. In doing so, I've come across my treasured micro controllers, Single-Board-Computers, sensors, and all sorts of IoT and device goodies.  
I quickly dove into a view fun projects then moved into some unknown areas sorta free-styling my way along. Learned a few new platforms and IDEs while still keeping some old favorites close by.

My favorite all around devices are easily the [Raspberry Pi 3](http://amzn.to/2oOHaAM) and [ESP8266](http://amzn.to/2nX0xDS) released by Adafruit as a Huzzah board.

More recently, have spent my time in SF building data driven dashboards as can be seen on my [projects page](http://jerad.xyz).  

So I guess it is only natural I started working on dashboards for IoT dashboards. In my search for such a tool I found the EON project by PubNub. Below is default dashboard so I can see what it looks like when published on my site (currently static single page app hosted on GitHub pages).

Do you have a favorite dashboard for IoT?
Adafruit.io?
freeboard.io?
...?

Please let me know!

I would really love to build my own dashboard in R and have it displayed here; either as an html page built from an Rmarkdown doc or notebook, or even a Shiny app hosted on a [Raspberry Pi 3](http://amzn.to/2oOHaAM) - an IoT dashboard hosted on an IoT device!


<script type="text/javascript" src="https://pubnub.github.io/eon/v/eon/1.0.0/eon.js"></script>
<link type="text/css" rel="stylesheet" href="https://pubnub.github.io/eon/v/eon/1.0.0/eon.css" />
<div id="chart"></div>
<script type="text/javascript">
var __eon_pubnub = new PubNub({
  subscribeKey: "sub-c-bd9ab0d6-6e02-11e5-8d3b-0619f8945a4f"
});
var __eon_cols = ["Austin","New York","San Francisco","Portland"]; 
var __eon_labels = {}; 
chart = eon.chart({
  pubnub: __eon_pubnub,
  channels: ["test-channel-0.7671745544564044"],
  history: false,
  flow: true,
  rate: 1000,
  limit: 5,
  generate: {
    bindto: "#chart",
    data: {
      colors: {"Austin":"#D70060","New York":"#E54028","San Francisco":"#F18D05","Portland":"#113F8C"},
      type: "spline"
    },
    transition: {
      duration: 250
    },
    axis: {
      x: {
        label: ""
      },
      y: {
        label: ""
      }
    },
    grid: {
      x: {
        show: false 
      },
      y: {
        show: false 
      }
    },
    tooltip: {
     show: true
    },
    point: {
      show: true
    }
  },
  transform: function(message) {
    var message = eon.c.flatten(message.eon);
    var o = {};
    for(index in message) {
      if(__eon_cols.indexOf(index) > -1){
        o[__eon_labels[index] || index] = message[index];
      }
    }
    return {
      eon: o
    };
  }
});
</script>