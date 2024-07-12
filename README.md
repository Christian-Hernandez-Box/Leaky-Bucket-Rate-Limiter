# Leaky Bucket Rate Limiter

## Overview

This project implements a rate limiter using the Leaky Bucket algorithm. A rate limiter controls the flow of requests in a system, ensuring that it doesn't get overwhelmed by too many requests in a short period. This implementation is designed to handle concurrent requests safely using thread synchronization mechanisms.

## Features

- **Concurrency and Thread Safety**: Uses Python's `threading.Lock` to ensure that the rate limiter can handle multiple concurrent requests safely.
- **Algorithm Implementation**: Implements the Leaky Bucket algorithm to manage request flow.
- **Customizable Parameters**: Allows customization of bucket capacity and time interval for rate limiting.

## How It Works

The Leaky Bucket algorithm is a way to control the flow of data. In this implementation:

1. **Bucket Capacity**: The maximum number of requests that can be handled in a given time interval.
2. **Time Interval**: The period after which the bucket is reset, allowing for new requests.
3. **Thread Safety**: Ensures that multiple threads can safely check and update the request count using a lock.

## Usage

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/leaky-bucket-rate-limiter.git
    cd leaky-bucket-rate-limiter
    ```

### Example Code

```python
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
