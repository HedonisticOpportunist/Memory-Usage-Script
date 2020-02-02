import psutil
import threading, time
from memory_usage import MemoryUsage

memory = psutil.virtual_memory()
percentage_threshold = 80.0
WAIT_TIME_SECONDS = 15
ticker = threading.Event()
virtual_memory = MemoryUsage(memory, percentage_threshold)

while not ticker.wait(WAIT_TIME_SECONDS) and True:
    virtual_memory.over_threshold()
