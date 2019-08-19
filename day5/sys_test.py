import time
import sys

for i in range(0, 100):
    sys.stdout.write("#")
    time.sleep(0.1)
    sys.stdout.flush()
