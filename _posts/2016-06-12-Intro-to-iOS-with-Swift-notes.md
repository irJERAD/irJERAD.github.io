---
layout: post
title:  "Notes for Intro to iOS Programming with Swift"
date:   2016-06-12 04:00:00 -0400
categories: Learning
tags: [Learn, iOS, App, Application, Development]

---

Here are the notes I created while going through the [Intro to iOS App Development with Swift](https://www.udacity.com/course/intro-to-ios-app-development-with-swift--ud585) course; the first in [Udacity's](https://www.udacity.com) [iOS Developer Nanodegree](https://www.udacity.com/course/ios-developer-nanodegree--nd003). 
<br> As will all of [Udacity's Nanodegree programs](https://www.udacity.com/nanodegree), this is project based. In fact - a student could graduate from a Nanodegree program without having taken a single course, so long as they competently and appropriately finish all the required projects.
<br> Personally, I think this is a much more grounded and applicable way to learn and express one's ability - particularly in the domain of software engineering.

The project tought and built in the Intro to iOS Programming with Swift course is called "**_Pitch Perfect_**."
<br>Pitch Perfect records audio using a devices native hardware, then applies one of a selection of custom sound effects to the recording such as _Chip Monk_ _Parot_ _Echo_ or _Robot_ voice.

To see the code developed while building the project and taking the course, see my [Intro to iOS App Development with Swift GitHub repository](https://github.com/irJERAD/Intro-to-iOS-App-Development-with-Swift)

---

**Lesson 1 - Introduction to Xcode**
***
**Lesson 2 - AutoLayout and Buttons**

Constraints

You need 2 constraints per dimension.

ex1: distance from top + distance from bottom; distance from left + distance from right.

ex1: distance from top + heights; distance from left + width

[Below: UI elements need constraints that maintain a functional meaning in both portrait and landscape viewing modes]

<img src = "/images/iOSwithSwift/objectThatNeedContraints.png">

[Below: with distance from top to object + object to bottom with distance from left to side of object + side to right of screen we can infer both size and precise location of the object]

height = [screen heigh] - [distance(screen top to element top) + distance(object bottom to screen bottom)]

width = [screen widt] - [distance(screen left to object left) + distance(screen right to object right)]

<img src = "/images/iOSwithSwift/2contraintsPerDImension.png">

2 contrains per dimension are required for definite an tons 

However, finite control over an objects height and width is often preferred to finite control of distance between the side of the object and the sides of the screen.

So:

Constraints can be place on two distances, if the object size is known

[Below: With an objects size already known, only a constraint in each dimension is necessary for placement]

<img src = "/images/iOSwithSwift/1constrainPlusObjectSize.png">

Hot Key for simulator size

With simulator open

⌘1 for 100% screen size

⌘2 for 75% screen size

⌘3 for 50% screen size

⌘4 for 33% screen size

⌘5 for 25% screen size

Target Action

Target is the view controller and the action is the action we are about to create

an IBOutlet goes from code to a UIElement

an IBAction is from UIElement to code

A button is used to go from a UIElement into code (to do something). This calls for an IBAction.

Changing the text of a UIElement requires the code to do something to a UIElement (a label in this case). This would be an IBOutlet.

***

**Lesson 3 - ViewController and Multiple Views**

Hot Key for Documentation:

Command+Shift+0 open documentation

Control+Click open brief documentation popup of a selected function

<img src = "/images/iOSwithSwift/ViewControllerLifecycle.png">

In iOS the **Will** functions always get called before the **Did** functions

viewWill always comes before viewDid

viewWillAppear is called before the the viewController and its view is on screen. viewDidAppear will be called right after.

viewWillLoad is called before the viewController and its view are loaded into memory and before viewWillAppear.

a UIViewController and any subclasses have at least one IBOutlet that always goes to a UIView.

Now we have UIElements that we have wired up to code with IBActions. We can reach back to UIElements using UIOutputs.

Next we want to build multiple views so we can go between two different view controllers. No more single view applications. Most iOS apps have multiple view controllers.

**Multiple Views**

The initial View Controller is the root view for the app. This is called the Root View Controller.

The grey arrow indicated the root View Controller

<img src = "/images/iOSwithSwift/InitialViewControllerArrow.png">

You can also inspect the ViewControllers __Attributes inspector__ to see if the "Is Initial View Controller" box is checked.

<img src = "/images/iOSwithSwift/IsInitialViewController.png">

In order to use multiple view controllers we need a tool for navigating between multiple ViewControllers

There are two classes for navigating views: **UINavigation controller** and **UITabController**

Multiple ViewControllers and Navigation

a **Segue** is what takes you from one view to another. In our example, we use the UIButton StopRecordingButton - which already has multiple functions such as changing the text from “Tap To Record” to “Press To Stop Recording” as well as disabling itself and enabling the Record button. Now when you press the Stop button, you still get all the previous functionality with the addition of navigation to a new view. Also notice a back button appears as a default method to return to the previous UIView when none had been created.

***

**Lesson 4 - Delegation and Recording**

Our Pitch Perfect iOS app sits on top of the stack. The actual hardware that records audio - like an iPhones microphone - and plays the audio back - like an iPhones internal speakers - are at the button of the technology stack.

Another piece, that will take our recorded audio and add fun sound effects before we play them back, lives in the middle of the stack.

AVAudioEngine library allows us to easily traverse all these levels in the iOS tech stack without needing in-depth knowledge of the individual components - such as what type of compression or what amount of current to provide a speaker during playback.

<img src = "/images/iOSwithSwift/TechStackiOS.png">

<img src = "/images/iOSwithSwift/TechStackAVAudioEngine.png">

**sharedInstance** - AVAudioSession.sharedInstance()

There can only be a single instance of the AVAudioSession object. That is because there is only a single piece of audio hardware for this session to run. Object like these - usually found in the Cocoa Touch libraries - are called shared instances because you are asking to share the phone’s single instance of this resource.

**Delegation Basics** - Delegation can be thought of just as you would with a manager to a team or a parent to a child. Work is delegated from one object to another.

AVAudioRecorder can access and record with a devices internal audio equipment. AVAudioRecorder does not have an understanding of files, folders and other necessarily frameworks having to do with what to do with a file after something has been recorded. The AVAudioRecorder has no concept for a ViewController and really does not even know about our application (remember: this is a sharedInstance object so it has other core features that have nothing to do with applications and it is only through sharing this single instance that applications are able to reach and use a devices audio hardware).

<img src = "/images/iOSwithSwift/DelegationBasicsWArrow.png">

The Record ViewController will be created such that the AVAudioRecord can Delegate the work of finding a path to an appropriate memory location, storing and retrieving the audio for use by the application.

A class in swift can only inherit from one superclass, but it can conform to as many protocols as you want. They just need to be declared / listed after the inherited class and separated by a comma

<img src = "/images/iOSwithSwift/DeclaringDelegate.png">

Overview from the class:

Delegation allows one class to do the work for another. The class knows what methods will exist in the delegate because they both agree on a contract, the protocol.

<img src = "/images/iOSwithSwift/DelegrateReview.png">

***

**Lesson 5 - Playback and Effects**