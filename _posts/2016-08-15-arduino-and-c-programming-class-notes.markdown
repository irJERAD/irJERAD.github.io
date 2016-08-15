---
layout: post
title: "Arduino and C Programming Class Notes"
date: "2016-08-15 04:27:41 -0700"
---

These are notes for [The Arduino Platform and C Programming][This Class].

###Student Peer graded Assignments
####Week 1: Program a blinking LED on an Arduino board


####Week 2: Create a Fibonacci Printing Program
```
/* Write a program in C that computes and prints out the first six digits
in the Fibonacci sequence. You will need to look up the definition of
the Fibonacci sequence if you don't know it.
The first two numbers in the sequence are 0 and 1,
but your program should compute the next four digits.
Your C program must compile in order for it to be tested. */

#include <stdio.h>
int main() {
  /*variable for how many numbers in the sequence should be printed*/
  int seq = 6;

  /*create secquence array*/
  int fib[seq];

  /*the first two outputs are 0 and 1*/
  fib[0] = 0;
  fib[1] = 1;
  printf("Digit #1 of the Fibonacci sequence is %d \n"
         "Digit #2 of the Fibonacci sequence is %d \n", fib[0], fib[1]);

  /*run a loop to collect the remaining seq - 2 numbers in the sequence*/
  for (int i = 2; i < seq; i++) {
    fib[i] = fib[i - 1] + fib[i - 2];
    printf("Digit #%d of the Fibonacci sequence is %d\n", i + 1, fib[i]);
  }

  return 0;
}

```

---  

>! References:
> ¡Left Blank Intentionally!
> below here in the source code are reference links that can be reused throughout the article.
> ###TODO Check if you can use reference links from other posts without reciting them on each page
> ¿can there be 'Global' reference links - or image sources - that can be used on multiple pages?

[This Class]: <https://www.coursera.org/learn/arduino-platform> "The Arduino Platform and C Programming"  

[This Specialization]: <https://www.coursera.org/specializations/iot> "Create You Own Internet of Things (IoT) Device"

[UCI]: <https://uci.edu> "University California Irvine"

[Coursera]: <https://Coursera.org> "Online Classes From Top Universities"
