# Commodity-Project
This purpose of this tool is to produce time-series visualizations that allow the user to identify the extent to which the indistrial revolution affected the price of various commodities across various countries.
Data set courtesy of Robert Allen and Richard Unger and can be found at https://www.kaggle.com/sohier/allenunger-global-commodity-prices (England has a strong dataset)

When run, the user is prompted to provide a local file path to the dataset
They are then provided a list of countries found in the dataset and asked to select one
They are then provided a list of commodities associated with the selected country and asked to select a commodity
A plot is then provided showing the value of the commodity along with the standard value silver at the time recorded

Pretty Simple Right!

Really, the reason I made this project was to build a simple tool that integrated some of the things I've recently learned such as git/github, SQL (sqlite3), jenkins, unittest, nose2, pylint, pychecker, VSCode, debugging,...

I developed this project in python and used VSCode as a text editor. VSCode's built in terminal and python debugger extension really came in handy when testing my code throughout the project. I used git/github as a VCS (obviosuly). I really only had 2 branches, master/develop. I also created a feature branch to simulate issues that may need to be mitigated when working on a shared project as a learning exercise. I also wrote some unittests for one of my modules. The dataset came as a .csv and I used sqlite3 to create a local sql databse where I stored this data while the program was running (it gets detroyed when the system exits). When the user enters a country and commodity, the sql class I built essentially turns this input into a SQL SELECT statement to query the db.  Then I set up a jenkins server on my local host and established up a webhook from my project's github repository that triggers a build on my local jenkins server when any push/pulls/commits were made to the develop branch of the repository. Because I'm running jenkins on my local machine, I had to use ngrok to create a (secure) tunnel from my local machine to a public url. Unfortuatly, this requires I open a new session every 8 hours which generates a new webhook that I have to update in github. Kind of a pain, but it works! The jenkins build I have tied to the project runs a series of shell commands which essentially spins up a virtual environment, installs any dependencies, runs static code analysis via pylinter as well as my unittests with either nose2 or pytest (I can't tell which one I like better yet) and code coverage results. The build results are then pushed to my email. Individaully all the components of this project are failry simple, but together this project provided a opportunity to integrate a bunch of really cool/modern tools and techiniques for developing a python project using continuous integration development practices. 


Next steps:
  Create Release and Hotfix branches
  more Unit Tests/Integration tests
  Upload to Pypi (I have a 0.5dev version that I uploaded as a test (pip install commodity-tool) but that version doesn't do anything)
  Expand my automated testing framework and utilize some test results publishing extensions
  tailor pylinter
  implement useful statistical measures in the tool and score results against other Countries/Commodities in the dataset
  distrbute the tool across multiple platforms and automate my delivery/distribution
