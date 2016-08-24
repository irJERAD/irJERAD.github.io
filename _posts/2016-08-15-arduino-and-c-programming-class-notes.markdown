---
layout: post
title: "Arduino and C Programming Class Notes"
date: "2016-08-15 04:27:41 -0700"
categories: Learning
tags: [Learn, C, Arduino, Programming, Notes, Coursera, Class]
---

These are notes for [The Arduino Platform and C Programming][This Class].  

### Class Reading  
#### Module 3 Reading
Arduino Toolchain and setup
1. [Arduino Build Process](https://www.arduino.cc/en/Hacking/BuildProcess)
2. [setup() Function](https://www.arduino.cc/en/Reference/Setup)
3. [loop() Function](https://www.arduino.cc/en/Reference/Loop)
4. [pinMode() Function](https://www.arduino.cc/en/Reference/PinMode)
5. [digitalWrite() Function](https://www.arduino.cc/en/Reference/DigitalWrite)
6. [digitalRead() Function](https://www.arduino.cc/en/Reference/DigitalRead)
7. [analogRead() Function](https://www.arduino.cc/en/Reference/AnalogRead)


Arduino Toolchain and Upload process:  
* code  
  * Write Code / Program in Arduino IDE  
* Verify  
  1. Combine & Transform (code) -->  
  2. Compile -->  
  3. Link (libraries) -->  
  4. Hex File Creation  
* Upload  
  * (5) Upload .hex file to Arduino board

### Combine and Transform
* All program files are combined into one
* An #include is added to reference basic Arduino libraries
* Function prototypes are added
  * Every function has a prototype that defines things like type for variable inputs and return types
* A main() function is created
  * every C and C++ program needs a main
  * The main is created behind the scenes here based on the setup() and loop()

### Compile and link  
* avr-gcc is invoked to cross-compile the code  
  * Resulting code executes on AVR, not Intel  
* Generates an object file (.o file)  
* Object file is linked to Arduino library functions (that are being used)  

After you have combined the different source files into one you've transformed them adding the `main()` including the libraries, then you cross-compile the code.

**Compilation** is taking the C or C++ code and generating the machine code required to execute the actual program - because the processor only understand machine code and not high level languages we program in.
**Cross-Compilation** is when you compile code on one machine for execution on another machine.
Here we are compiling code on our Intel processor based laptops or desktops that is intended to be executed on AVR processor in the Arduino boards.

Compilation produces an _object file_ (.o file) that is compiled but not complete because it still needs to be **Linked**.

**Linking** is taking the object (.o) files and combining them. This includes object files for libraries.
When functions from other libraries are used in the code, a branch or jump statement needs to be inserted to jumps you to the libraries code. When Compiling you do not know where in the library a function is. *During the linking process* the object files from your code and the libraries code make this more explicit by creating those precise jumps in the executable.

### Hex File Creation and Programming  
* avr-objcopy is invoked to change the format of the executable file  
* A .hex file is generated from the .elf file  

After compiling and linking is finished, you get an _.elf file_ which is an executable file. BUT, the Arduino processor does not accept .elf files.
So **avr-objcopy** is used to change .elf file to another executable file that can be used by the Arduino processor. This is the **.hex file**.  


----
### Module Quizzes  
#### Quiz 2   
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

#### Quiz 3   
1. What is the function of the linking process after compilation?  
It merges the libraries with the application code into a single executable.  
2. What is the role of avrdude?  
It writes the executable into the memory of the Arduino  
3. Why are classes (in C++) useful?  
They improve the organization and understandability of the code  
4. What is one way that a sketch can invoke a function contained inside a class?  
The name of the class can be concatenated with the name of the function, with a period in between.  
5. Which of the following statements is true?  
The `setup()` function is executed once and the `loop()` function is executed iteratively, as long as the Arduino is powered on.  
6. True of False: An analog pin can accept analog inputs and drive analog outputs?  
False; analogRead() uses the Arduino board 10-bit Analog to Digital converter. This enable mapping of input voltage between 0 and 5 volts to integer values between 0 and 1023.
There is no analog output supported by the Arduino in any of its pins including the analog outputs.  
7. If a sketch running on an Arduino UNO executes the following statements, what voltage would be expected on pin 1 afterwards?  
```c
pinMode(1, OUTPUT);
digitalWrite(1, HIGH);
```  
5
8. True or False: The `delay()` function cases program execution to pause for a number of milliseconds?  
True  
------

### Student Peer graded Assignments
#### Week 1: Program a blinking LED on an Arduino board


#### Week 2: Create a Fibonacci Printing Program

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


#### Week 3: Alternate between Fast and Slow flashing Pin 13 LED
##### 5 equidistance blinks over 2.5 seconds followed by 5 equidistance blinks over 10 seconds
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
