'''
To process huge amounts of data from log files or streams:
 -to monitor system performance;
 -detect errors;
 -analyze user activity.
When working with such large data streams, we often can't load all the data into memory
(like we might with a for loop over a list).
Instead, iterators allow us to process the data piece by piece as it arrives.
To monitor a live log file to detect errors as soon as they occur,
but the file is constantly being written to by the system.
Using iter and next, we can process the file line-by-line without reading the entire file into memory.
1)iter() and next() are Essential:
 • Memory Efficiency: The entire log file is not loaded into memory. Each line is processed as it becomes available.
 • Real-Time Handling: We can process each log as soon as it’s written (using next) and pause if needed.
 • Fine-Grained Control: We control exactly when to fetch the next log and how to handle errors.
2)the for loop can't solve this:
A for loop typically processes the entire iterable or stops when it's exhausted.
It doesn't provide the ability to pause, resume, or handle real-time dynamic inputs in the same way.
For example:
 • we can't stop mid-iteration and decide later when to continue.
 • With a file or generator, the for loop assumes the entire process must run sequentially,
 which isn't ideal for live data.
In conclusion, for processing real-time data streams or handling memory-intensive tasks
weuse iter() and next() - because it's the only way to maintain efficient, responsive, and controlled operations.
'''
import time
import warnings
#1)get logs line-by-line
def log_generator():
    logs = [
        "INFO: Service started",
        "INFO: User logged in",
        "ERROR: Database connection failed",
        "INFO: Retry attempt 1",
    ]
    for log in logs:
        yield log
        time.sleep(1)
#2)make an iterable object
log_stream = iter(log_generator())
#3)process it line-by-line
while True:
    try:
        log_entry = next(log_stream)  # Fetch the next log entry
        print(f"Processing log: {log_entry}") #process the next log entry
        if "ERROR" in log_entry:# React to detected errors immediately
            warnings.warn("ALERT: Immediate action required!")
    except StopIteration:
        print("No more logs to process.")
        break