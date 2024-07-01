# Time Complexity : O(1)
# Space Complexity : O(n), where n is the number of unique messages

"""
Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds. All messages will come in chronological order (in increasing timestamp order).
"""
class Logger:

    def __init__(self):
        self.message_timestamp_map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if message not in self.message_timestamp_map or timestamp - self.message_timestamp_map[message] >= 10:
            self.message_timestamp_map[message] = timestamp
            return True
        else:
            return False

# Example usage
logger = Logger()

# Example 1
print(logger.shouldPrintMessage(1, "foo")) # returns True
print(logger.shouldPrintMessage(2, "bar")) # returns True
print(logger.shouldPrintMessage(3, "foo")) # returns False
print(logger.shouldPrintMessage(8, "bar")) # returns False
print(logger.shouldPrintMessage(10, "foo")) # returns False
print(logger.shouldPrintMessage(11, "foo")) # returns True

# Example 2
print(logger.shouldPrintMessage(1, "abc")) # returns True
print(logger.shouldPrintMessage(2, "xyz")) # returns True
print(logger.shouldPrintMessage(9, "abc")) # returns False
print(logger.shouldPrintMessage(12, "abc")) # returns True

# Example 3
print(logger.shouldPrintMessage(1, "test")) # returns True
print(logger.shouldPrintMessage(5, "test")) # returns False
print(logger.shouldPrintMessage(11, "test")) # returns True
print(logger.shouldPrintMessage(21, "test")) # returns True