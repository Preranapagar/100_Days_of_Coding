import logging

# Specify the log file name
log_filename = 'my_function_log.log'

# Configure logging settings
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Define your Python function
def my_function():
    # Your function logic here
    result = "This is the result of my function."
    logging.info("Function result: %s", result)
    return result

# Call the function and capture the result
result = my_function()

# Close the log file
logging.shutdown()

# Display the captured result
print("Function Result:", result)
