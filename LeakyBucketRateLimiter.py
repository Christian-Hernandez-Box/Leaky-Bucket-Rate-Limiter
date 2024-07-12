import time
import threading

class LeakyBucket:
    def __init__(self, bucketCapacity, timeInterval):
        self.bucketCapacity = bucketCapacity
        self.timeInterval = timeInterval
        self.currentRequests = 0
        self.timeSinceLastRequest = time.time()
        self.lock = threading.Lock()  # For thread safety

    def allowRequest(self):
        with self.lock:  # Ensure that this block is thread-safe
            currentTime = time.time()
            elapsedTime = currentTime - self.timeSinceLastRequest

            if elapsedTime > self.timeInterval:
                self.currentRequests = 0
                self.timeSinceLastRequest = currentTime

            if self.currentRequests < self.bucketCapacity:
                self.currentRequests += 1
                return True
            else:
                return False

# Example usage
bucket = LeakyBucket(5, 1)

for i in range(15):
    if bucket.allowRequest():
        print(f"Request {i+1} allowed.")
    else:
        print(f"Request {i+1} denied.")
    time.sleep(0.6)
