---
layout: post
title: "Arduino and C Programming Class Notes"
date: "2016-08-15 04:27:41 -0700"
---

These are notes for [The Arduino Platform and C Programming][This Class].
----
###Module Quizzes
####Quiz 2
1. What is the name of the library which contains the printf() function?
stdio.h

2. What does the '\n' character mean?
newline

3. What type of data is surrounded by double quotes in a program?
a string

4. What C type is one byte long?
char

5. Does the following statement evaluate to True or False?
`(10 || (5-2)) && ((6 / 2) - (1 + 2))`
becomes: `(10 || 7) && (3 - 3)` --> (True OR True) AND False

6. What does the following program print to the screen?
```c
int main (){
   int x = 0, y = 1;
   if (x || !y)
  	printf("1");
   else if (y && x)
  	printf("2");
   else
  	printf("3");
}
```

7. What does the following program print to the screen?
```c
int main (){
   int x = 0, z = 2;
   while (x < 3) {
  	printf ("%i ", x);
      x = x + z;
    }
}
```
8. What does the following program print to the screen?
```c
int foo (int q) {
    int x = 1;
    return (q + x);
}
int main (){
   int x = 0;
   while (x < 3) {
  	printf ("%i ", x);
      x = x + foo(x);
    }
}
```

------
###Student Peer graded Assignments
####Week 1: Program a blinking LED on an Arduino board


####Week 2: Create a Fibonacci Printing Program

```c
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


####Week 3: Alternate between Fast and Slow flashing Pin 13 LED
#####5 equidistance blinks over 2.5 seconds followed by 5 equidistance blinks over 10 seconds
> Write a program that causes the built-in LED connected to pin 13 on the Arduino to blink, alternating between fast blinks and slow blinks. The LED should blink 5 times, once every half second, and then it should blink 5 more times, once every two seconds.

```c
/*
 This code used the Blink example that comes with the Arduino IDE
 It was modified to accomidate a University of Irvine class requirement
 as part of the IoT programming certification via Coursera

  modified 17 August 2016
  by Jerad Acosta
 */


// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(13, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  // create loop with 5 blinks at 1 per half second
  // 1/4 second on amd 1/4 second off gives one blink per half second
  for(int i = 0; i < 5; i++) {
    digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(250);              // wait for 1/4 of a second
    digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
    delay(250);              // wait for 1/4 of a second
  }
  // create loop with 5 blinks at 1 per 2 seconds
  // 1 second on and 1 second off gives 1 blink per 2 seconds
  for(int i = 0; i < 5; i++) {
    digitalWrite(13, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(1000);              // wait for 1 second
    digitalWrite(13, LOW);    // turn the LED off by making the voltage LOW
    delay(1000);              // wait for 1 second
  }
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
