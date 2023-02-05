# How to use logging in Python

The **logging** library in Python allows us to have a more accurate way to store potential incidents and logs that you may be interested in saving. In this notebook we will implement a PlanetarySystem class, and use logging to store important information about the different elements that are created during the process. 

Note that this will be logging to a file. Logging to console can be useful for testing, but in production we generally want to log to a file that we can access later. For that, we can use the "filename" argument and push all logs to a file we want. Note that in this case, the file will get the logs each time we execute the function, so if we run this cell twice, errors will be logged to the file twice.
