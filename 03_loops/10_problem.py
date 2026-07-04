#   Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

# wait_time = wait_time * 2 # this is called exponential backoff

import time

wait_time = 1

for retry in range(1, 6):
    print(f"Retry {retry}: Waiting for {wait_time} seconds...")

    time.sleep(wait_time)

    print("Retrying...\n")

    wait_time = wait_time * 2