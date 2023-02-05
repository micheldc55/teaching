# How to use logging in Python 🤓📝

The **logging** library in Python allows us to have a more accurate way to store potential incidents and logs that you may be interested in saving. In this notebook we will implement a PlanetarySystem class, and use logging to store important information about the different elements that are created during the process. 

Note that this will be logging to a file. Logging to console can be useful for testing, but in production we generally want to log to a file that we can access later. For that, we can use the "filename" argument and push all logs to a file we want. Note that in this case, the file will get the logs each time we execute the function, so if we run this cell twice, errors will be logged to the file twice.

The logging library in Python is organized by levels. Each level represents a type of log that you want to make, or the "severity" of whatever you are capturing with the log. The explained logging levels can be found [here](https://www.digitalocean.com/community/tutorials/how-to-use-logging-in-python-3): 
- Debugging logs: are used to diagnose problems and show detailed information. They can be used to store intermetiate bariables or states that you want to use for debugging purposes.
- Information logs: are used as a confirmation that things are working as expected. You can even output the result of a correct operation and the attributes/values of a function/class.
- Warning logs: Indicate something unexpected happened, or could happen. The warning doesn't imply code-breaking events, but they are something to look out for.
- Error logs: used to enrich errors or pass the error code directly to the file. You can log current attributes/values/features so that you can get a better understanding of why the error happened.
- Critical logs: Show a serious error, the program may be unable to continue running. This shows a code-breaking input that needs to be fixed.

# Structure of the Python file used

The Python file in this repo implements a class called PlanetarySystem, in which you can create your own solar system and add different Planet classes to it. These classes are used to showcase how the logging library can be used in this context. We will be logging when a planet is created, storing a few key details about the planet and its orbit. We will also log when a new solar system is created, and also save a few key components.

The process also forces two error types so that you can see how logs could be used in that context. The first one provides the "period" of a planet (the time it takes in years to complete an orbit around the star) as an integer instead of a floating point. This is logged as a warning that the integer for forcefully converted to a float. The second error gives us context of as error. It logs some data about the error for our reference.

## The basicConfig function

One thing that I find really valuable about this library is that it allows for global handling of log settings. You can set up the formatting of the logs, the file where they are saved, and the level above which the logs will be stored from a single method called logging.basicConfig(). This is a one-time configuration function that set's up the behavior of the logs in a single execution, so that all your logs behave similarly.

The thing that I find really good about this is that you can set up your classes to log data using the logging.XYZ elements, and then determine the behavior of the logs from the outside setting up the parameters from the basicConfig function. this allows for formatting all the logs using the same schema, and saving them to a file. The good thing about this approach is that you only need to set up the formatting from the basicConfig, instead of doing it from each logging.XYZ instance.
