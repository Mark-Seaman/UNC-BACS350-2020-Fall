# Book Builder - Software Plan

## Requirements

Book Builder is a specialized application that is built inside the Sensei master app.

Sensei is a software application platform that is host to a number of specialized applications.


### Hosted Applications

BookBuilder is a Hosted Application with its own development lifecycle.  
The Requirements, Design, Code, and Test are documented in this doc. 

View the [Sensei Software Plan](Index.md) for more information about the overall Sensei
software platform.


## Design

The Sensei software is built with the Django web framework and uses all of the best 
practices that are recommended by the Django community.

    

## Django Apps

Each Hosted Application is built using a Django app to implement it.  

To use the Book Builder app there are several other apps that it is dependent on.

This is a map of the INSTALLED_APPS used by Book Builder.

    * book     Book Builder
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

