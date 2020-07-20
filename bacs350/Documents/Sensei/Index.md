# Sensei Digital Classroom - Software Plan

## Requirements

Sensei is a software application platform that is host to a number of specialized applications.


### Hosted Applications

Each of these applications has its own development lifecycle.  These are documented in the
following docs, which detail the Requirements, Design, Code, and Test. Investigate these
docs to learn more about each component.

* [Book Builder](BookBuilder.md)
* Course Builder
* Software Planner
* Blog Builder
* Student Dashboard
* Project Tracker
* Review Manager
* Page Tester
* Hammer Test


## Design

The Sensei software is built with the Django web framework and uses all of the best 
practices that are recommended by the Django community.


### Technology

There are a number of webframeworks out there that are adequate for building production
software.  Django offers the best tradeoff for me and I have deep knowledge in it.

Alternative Technology

Since the selection was made long before I started this project there is no point in
listing the tradeoffs for other technologies.

* Node.JS/React JS/Mongo - MERN
* Angular JS
* ASP
* PHP
* Ruby on Rails


### Technical Platform and Tools

Components & Language

    Python      3.7.4
    Django      3.0.4
    Pillow      6.2.1
    

## Django Apps

Each Hosted Application is built using a Django app to implement it.  
This is a map of the INSTALLED_APPS.

    * book     Book Builder
    * course   Course Builder
    * devplan  Software Planner
    * blog     Blog Builder
    * student  Student Dashboard
    * project  Project Tracker
    * review   Review Manager
    * pagetest Page Tester
    * test     Hammer Test
    * tools    Utilities used by all
    * markdown Document formatter
    * docs     Document file manager
    
    
## Code

The source code for the project is all under source control.

### Github - Mark-Seaman

Private Repos

These repositories are private so that only collaborators can see the content.  They contain
information that could be used for harmful ends if made public.

* [https://github.com/Mark-Seaman/Sensei-2020](https://github.com/Mark-Seaman/Sensei-2020) - private repo.  
This repository contains all of the source code for the Sensei server application.
This include all static file, url routes, templates, views, and models.
* [https://github.com/Mark-Seaman/Documents-2020](https://github.com/Mark-Seaman/Documents-2020) - private repo.  
This repository contains all of the documents that are displayed by
the Sensei server application.



## Test

The primary means of testing the Sensei software is Hammer Test, which is a tool that was
developed by Shrinking World Solutions in 2009.

Hammer tests are executed on both the development servers and the production server to ensure
that all code remains working properly.

