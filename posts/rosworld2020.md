---
title: Personal Notes from ROS World 2020
date: 2020-11-12
externalurl: "https://dev.to/luckierdodge/personal-notes-from-ros-world-2020-2e04"
description: "I attended the Robotic Operating System's [ROS World 2020](https://roscon.ros.org/world/2020/) convention today. I quite enjoyed it! To keep myself focused during the event, I tried to write some comprehensive notes. To keep myself entertained, I wrote them as if somebody else would be reading them."
tags: [dev, post, feed]
---

:::{image} https://roscon.ros.org/world/2020/img/ROSWorld2020.png
:width: 80%
:align: center
:::

> _Update: You can find all of the videos from ROS World 2020 [here](https://vimeo.com/showcase/rosworld2020)._

I attended the Robotic Operating System's [ROS World 2020](https://roscon.ros.org/world/2020/) convention today. I quite enjoyed it! To keep myself focused during the event, I tried to write some comprehensive notes. To keep myself entertained, I wrote them as if somebody else would be reading them.

But it occurred to me that someone else might find these useful in some way, especially if they missed the convention or didn't know it was a thing, and this might act as a sort of helpful guide. Or maybe you're just curious about robots and want to see what we're up to. Either way, I hope this is helpful! I'll add links to the videos once they're posted publicly, and will happily answer any questions in the comments.

## 🔑 Keynote & Q&A - Dr. Vivian Chu, co-founder and CTO of Diligent Robotics

* Missed the first couple minutes because the stream was acting up.
* Good advice on robotics startups
* Interesting insight into systemic issues in healthcare and nursing, and how robots might be able to help alleviate that.
* Users don't know what they want
* Spotty network connections, even indoors
* Q & A Bechdel Test: Two women - Katherine Scott, Developer Advocate from Open Robotics, and Dr. Vivian Chu, CTO of Diligent Robotics. Other founder of Diligent is also a woman.

## 👍 Panel: Software Quality in Robotics Content

* Deby Katz - Carnegie Mellon University (Moderator), Allison Thackston - Waymo, Afsoon Afzal Phd Candidate at Carnegie Mellon, Sophia Kolak from Columbia University
* So many women speakers! Awesome.
* Familiar idea for most devs: automated testing is important
* Adversarial situations: robots have to exist in the real world, where things often don't go to plan.
* FIELD TESTING, LOGGING AND PLAYBACK - IMPORTANT
* Not as much Automated Testing currently, because it's hard, but might be helpful to increase
* 3 Main Challenges:
	* Testing in the real world ("Unknown unknowns")
	* She never actually mentioned the other 2
* Sensor noise makes things interesting.
* "Degenerate Input"
* Lots of dichotomization between pure software like the web and these physical computing concepts.
* Documentation for packages are lacking.
* Need to reduce friction for writing documentation.
* Simulation is critical part of software quality assurance
	* Why aren't people using it then?
	* Using "multiple modalities of testing" can improve testing
* Favorite/most interesting bug
	* Someone found simulated case where robot arm intersected robot body, developers didn't believe, sure enough: broke robot
	* Simulators can be wonky: spawn underground, shoot up and collapse in on itself.
	* Robot kicked human tester so hard they were injured during field testing.
* Software testing important for researchers?
	* Yes (implied _duh_)
	* Too many people treat it as an afterthought
	* Need to make it easy to go from rosbag to structured unit test
	* The infrastructure and techniques need robustness
	* First-to-market tends to outweigh safety/quality concerns
		* Maybe need to introduce standard/certification
* Probabalistic Testing, how do we ensure coverage?
	* Better test platform, increase reproducibility, add fuzziness to try and replicate
* Health of the ROS ecosystem
	* Software Quality/Testing is hidden away in the far corners of specialized CS curriculum
		* Need to prioritize teaching these tools
	* Need better tooling
	* AUTOMATE. THOSE. TOOLS!!!
	* Standardized Environments for testing - neat!
* Best practices?
	* Lot of familiar stuff from traditional software engineering
	* How do you style a test environment to do end-to-end testing
	* Lotta roll-your-own right now
	* Documentation for best practices/testing is lacking
	* MOAR TOOLING
	* If you have something that works/you've created, share it with the community!
	* Lots of dependency on a few centralized packages - dangerous
* Hardware in the Loop Testing
	* Need to look into this more.
	* Simulation is great, but some things are hardware-dependent.
	* Different types of tests to get different types of results
	* Log testing gives rare, real results that might never appear in simulation
* __"At the end of the day, you need a reliable system, and a reliable system is well tested."__
* Even if simulation can't catch everything, it's better than nothing.
* Code maintainers and reviewers could be requiring documentation with new pull requests.
* Make documentation/testing a part of community standards.
* No set of well-defined best practices for software quality. How do we fix that?
	* Community standards, again.
	* People look to OSRF for standards, so maybe starting there.
	* Also maintainers of large packages.

## ⚡ Lightning Talks 1

* Cool vis of ROS contributions over time.
	* Needs a legend for the colors.
	* Should've grabbed the link
* For some reason this conference platform keeps tripping the Firefox VR permissions. Do they have a WebXR viewer? Not willing to risk losing the stream again to figure out.
* Ad for EProsima "The Middleware Experts"
	* Discovery server for ROS
	* Shared Memory
* Sidenote: videos are hosted on Vimeo. Good choice, I guess, given the youtube outage 🤷‍♂️
* Robot Dogs!
	* Aibo
	* Had one as a kid, back when they were...not good. Wonder if they've gotten better? Hard to tell from ad.
* Ubuntu advertisement for snap
	* So fast, much snappy.
	* Look at that apt install, sped up to 4x and still trailing. What a scrub.
* Ooh, flashy "ROS Underground" ad
	* DARPA Subterranean Challenge.
	* Interesting, tools provided competition.
	* 11/17/2020
* Daniel Grieneisen, Six River Systems
	* Shipping and warehousing robots
	* Flash backs to working back-end at Walmart *shudders*
	* [6river.com/category/engineering](https://6river.com/category/engineering)
	* Open source Data-processing pipeline, neat
* They weren't kidding about lightning, geez
* These are some high-budget videos, wow.
* Rocos
	* Some sort of ROS robot operations management tool
	* Widgets! Dashboards! Digital Twins! Autonomous missions! Visualizations! Fleets! Complexity! Security!
	* [rocos.io](https://rocos.io)
* ARM ad
	* "5th wave of computing"
	* Buzzwordy buzzwords are buzzwording.

## 🏫 Time for Class
* If anyone wants my notes on Bezier Curves, let me know 😉
* Missed: networking break (meh), "MSeg: Achieving Generality and Robustness in Semantic Segmentation".

## 🌱 Panel: ROS Agriculture

* Stream wasn't loading, so whatever occurred at the beginning is a mystery to me 😒

:::{image} https://dev-to-uploads.s3.amazonaws.com/i/7rthdv3daux0dnu4k58m.gif
:width: 80%
:::

* Got in, 20 minutes late
* Sarah Osentoski (Moderator), SVP Iron OX; Michele Pratusevich, Direcotr of Software Development, Root AI; Lee Redden, Chief Scientist, Blue River Technology; Eitan Babcock, Chief Roboticist/Cofounder, American Robotics
* ...some stuff that I missed...
* Need to couple engineering w/ extant agricultural knowledge from agronomists to achieve superior results
* Robots can replicate grueling PhD research formerly done by hand, but much faster
* Big push in CV using expert annotators - Ag is a good use case
	* Part of the job is to leverage the myopic knowledge of Ag researchers
	* Needs more love for 3D data - LIDAR, point clouds, etc.
	* Also change detection, time
* Is Ag easy, due to minimal human interaction?
	* "Don't know about easy, but different problem set".
	* Advantages: everything's on a grid, more control of certain variables and structure
	* No FDA testing like in medical
	* Fewer size and power, movement constraints
	* Limited ethical constraints (don't know about this one)
	* Hard: no red tape, so stuff needs to work. Farmers have "show me" culture, needs to withstand the elements, operate in variety of potentially adverse conditions.
* How do you deal with FDA requirements for cleaning tools etc?
	* Michele - "Thankfully, haven't had to deal with it yet"
	* As volume scales: might eventually have safety requirements, IP requirements, etc.
	* Learn as we go.
	* Sarah - difference between agriculture (in the field) and manufacturing (on the conveyor)
* Ever had to pivot areas in Ag?
	* Michele - not yet
	* Eitan - small shift from bulk to high-value crops.
	* Lee - pivoted form lawn mowers to tractors to implements; now some phenotyping.
		* Pivot from lettuce to row crops due to market size.
		* So many small subsegments in Ag, value-based priority shift/addition
		* Enabled by technology leap.
* Connectivity issues?
	* Issues in greenhouse due to water content in air
	* Eitan - rely on LTE, problems if not near highway (most farms). Satellite also an option
		* Range on base station: point to point radio, multiple miles
	* Michele - "Once we send robot out into the row, we assume we can't talk to it"
		* Also in greenhouse
		* Get data off robot at some point
		* Costs money and time to move data offsite
		* How do you prioritize data retention?
	* Lee
		* Embed intelligence on the robot
		* If we have connectivity, that's a nice plus
* How do you get buy-in from Farmers
	* Lee - farmers have been quite open and willing, straightforward with what's valuable and what isn't, allow demos and whatnot, constantly trying things and improving. Calculated risks
	* Michele - "part of it is relationship building", building trust slowly over time, can't destroy somebody's crop, demo what's possible. Onsite facility mocked up to demo stuff/use for marketing
	* Eitan - small pilot programs, work up to 6-month growing season.
* Advice for roboticists interested in Ag?
	* Michele - find your niche. Pick a pain point and solve that, not generalized problems
	* Eitan - agreeing noises to michele, communication is important and talk to farmers when they're not in the middle of growing season.
	* Lee - general roboticist? Apply to one of our companies!!

## 🥪 Lunch Break (Technically a Networking Break, but dammit I need to eat).

## ⚡ Lightning Talks 2

* Spinning circle of doom. At least it's better than the black screen from earlier, I guess.
* Welp, someone posted the permalink, so here it is: [https://vimeo.com/478302472](https://vimeo.com/478302472)
* Also, Vimeo needs to leave my VR headset alone for pity's sake.
* Apex.AI ad: self-driving stuff
	* Autonomous is hard, yo
	* ApexOS
* ROS2 in RoboCup
	* Autonomous soccer bots!
	* Adorably janky
	* Lots of different components, really leveraging ROS for this
	* [https://gitlab.com/boldhearts](https://gitlab.com/boldhearts)
* AWS Robotics Ad
	* I'm too poor for your product, Roger.
	* They do have a lot of integrated ROS extensions
	* Big emphasis on simulation and WorldForge stuff
	* Free Robotics Application Development Curriculum - Might be a good alternative to ROS Construct
* 8:02 going to other session, will come back to this later
* ...
* And we're back.
* Fetch Robotics
	* History of ROS montage
	* Robots helping with COVID!
* roscompile ad
	* Hate using CMake? roscompile makes all that nonsense less awful
	* Thankfully, much less of that in ROS2
* ClearPath Robotics
	* Maker of nice rugged all terrain robots of various classifications
	* Love how industrial their mobile robots are
* Rapyuta Robotics ad
	* More warehouse robots

## 🌍 MoveIt World

Lots of different technical sessions at 1:45pm, I chose this one because it's relevant to stuff I want to do in the near future. Might go back and explore the other talks later.

For those who don't know, MoveIt is a tool for motion planning with robotic arms.

* 9(!) presenters, including a number from PickNik (primary contributors to MoveIt).
* World MoveIt day Hackathon
	* Closed many issues and pull requests
	* 80 participants, 55 people signed up on discord
* MoveIt on Discord and Discourse
* MoveIt2 out of beta now
* RoadMap Status Update
	* Already have straight port to ROS 2 94% complete
	* Currently refactoring for Realtime support
		* "Reactive, closed loop control"
		* "Separate global and local planner (hybrid planning)"
		* "Zero Memory Copy Integration"
		* Integrate pilz_industrial_motion
	* Cool motion planning demos
	* Lots of movement here: Google Summer of Code, Hackathons, research interns, and a well coordinator core contributors group. It's an impressive open source org, to be sure.
	* Lots of features around pose-planning, moving the arm in intelligent ways to avoid collisions, stuff like that.
	* Hybrid planning - trying to solve for the different types of problems that an arm might need to solve (writing with chalk versus avoiding a collision with a surprise obstacle, for instance).
	* Definitely worth just digging through these slides/video in their/its entirety - no way I'm gonna be able to summarize this in text form (lot's of good diagrams/visuals).
	* "Chicken egg" problem of hardware integration: need hardware support to drive ROS2 adoption, need ROS2 adoption to drive hardware support
	* micro-ROS - interesting project to work with microcontrollers on ROS, glad to see this getting attached to other projects like MoveIt
	* Next stage: fully leverage ROS 2
		* ROS 2 release every 6 weeks
		* Main branch switching to Rolling Ridley
* Talk about calibrating a robot arm using a camera
	* 2 forms: eye to hand, and eye in hand
		* Really more or less the same problem
	* Lots of transforms and math
	* I'mma need to brush up on my linear algebra
	* AX=XB solvers - there's a bunch of solutions for this problem, including OpenCV
	* Live demo is a simulation, because the robot is broken - classic
	* I will note, RVIZ is a lot less ugly now.
* Robot Assembly Presentation
	* Presenter from Omron
	* World Robot Summit Assembly Challenge
	* Challenge: build component with lots of small parts and fine motor control required
	* Traditional solution: lots of custom jigs and machining, separate everything into simple tasks
	* Very expensive!
	* Omron solution:
		* "Connecting a lot of things together -- ROS helps"
		* "Always strike a balance between prototyping speed and machine control"
		* "Sliding scale of complexity" to existing approaches
		* Really in-depth here, definitely good stuff if you're interested in this kind of repeatable autonomous fine manipulation with end effectors
		* Pretty cool collaboration between two robot arms shown
		* Emphasis on robustness
* Constraint-based Cartesian Planning
	* Task constraints: how tools and such are allowed to move
	* Generally expect cartesian planning to "just work"
	* Number of different options for planning cartesian movement, all with trade-offs
	* OMPL Constraint Planning - Summer of Code project
		* Used to plan NASA's Robonaut 2
		* Need to replace existing "PoseModel" which has issues - joint space jumps and such
		* Lots of high quality gifs
		* Sampling-based motion planning - interesting approach to find valid and invalid poses
* Robonaut 2 from NASA
	* Cool multi-armed robot that moves in zero-gravity on space station
	* Lots of path-planning, control challenges arise when trying to use arms to pull yourself around a tiny space capsule
	* TaskForce - tool to help task-based motion planning
		* Makes MoveIt control easier and more versatile
	* Currently open sourcing both tools
* MoveIt Capabilities Overview
	* Good roll at the end showing all the different use-cases for MoveIt. Honestly, should've led with that.


## ⚡ Lightning Talks 3

Had to come back for this one.

* PlotJuggler 3.0
	* +1 for most interesting man in the world meme.
	* Pretty good stuff from a data vis perspective, nice hooks into the ROS tooling
	* Window system reminds me of Visual Studio
	* Meme dunking on Matlab. Outstanding
	* [plotjuggler.io](https://plotjuggler.io)
* GurumNetworks ad
	* High production quality, low calorie content
	* "Best DDS"
* Intel OPENVINO Toolkit ad
	* Pictures = ton of data
	* Enables "Smart video and visualizations"
	* CV/Deep learning solution
	* Really throwing the kitchen sink of buzzwords
* Microsoft Ad
	* ROS on windows - 100000+ downloads
	* Lots of integrations
	* Ooh, Mixed Reality Toolkit for ROS2 (mispelled in the slide, oops) - that's pretty exciting
* Zebracorns FRC Team 900
	* First Robotics Competition
	* Bringing ROS to FRC
	* Pretty wild output from Highschoolers. Good for them!
* RobotIS
	* Turtlebot3!
	* Lots of fun consumer/industrial robotics showcasing happening here, very quickly.
* Auterion
	* Autonomous Drone Flight Controller
	* Also includes other mobile robots?
	* Skynode
	* Sharp polos
	* Why doesn't this guy have a polo?
* SICK Sensor Intelligence
	* "Industry 4.0" ugh
	* Warehouse robotics solution

## 📕 Closing Remarks - Ryan Gariepy

* Ryan Gariepy, CTO Clearpath/OTTO Motors
* 1.5 Megatons of CO2 saved by being online
* More participants then ever before (maybe because it's free?)
* Lot of US attendees, but also from around the world
* Many thanks to many sponsors
* Roberta Friedman - Founder and CFO of Open Robotics, is retiring
* Videos should be up by weekend
* Survey coming soon
* ROSCon 2021 October 19th-24th, in New Orleans

## ⚡ Lightning Talks 4

* Webots Robot Simulator
	* Lots of premade robots to simulate
	* Graphical Editor
	* ROSin support
* Weekly Robotics
	* Mat Sadowski does a great job with this weekly newsletter! Big fan of this guy's work. Check it out [here](https://weeklyrobotics.com/)
* Technaid S.L.
	* H3 Exoskeleton
	* A ROS compatible exoskeleton? Neat!
	* Definitely makes security seem really important
* ROS Industrial
	* Ben Greenberg
	* ROS is intimidating for newbies - fair
	* Web-based tools for less technical users
	* 3D viewer
	* WebVis interface and terminal emulator
	* Mobile Friendly
* ROS for Robot Swarms
	* Phd Candidate(?) showing off swarm collaboration
	* Swarm Mapping
	* Swarm monitoring
* Greenzie
	* Selfie cam, bold move
	* Lawn maintenance robots
	* Adapt electric lawn mowers to "Autostriping"
	* Lots of familiar tools and tech on here
* ROS for Autonomous Maritime Systems
	* UL Lafayette Engineering
	* The C.R.A.W. Lab - Outstanding pun.
	* Look at that boat go.
	* RoboBoat! Big fan.
	* Even smaller RoboBoat!
* MoveIt
	* Throwback to Omron's presentation from the MoveIt talk.
* Nobleo
	* Is that Sylvan Esso? No, just a similar bass line
	* Autonomous Pallet Jacks (Terrifying, to anyone who's ever taken one to the ankle before).
	* More Digital Twins
