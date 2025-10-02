import threading
from collections import OrderedDict
import time

"""
concept
    LRU cache stores the limited number of items to add.
    when it reaches the capacity and new item is added 
     -> it removes the least recently used(oldest) item
     -> whenever an item is accessed , it becomes the most recently used
    
    Need to ensure the thread safety so that concurrent thread doesn't interrupt the internal state. 
    
    Modules to use :
     -> threading.lock
     -> ordereddict
"""
    
class ThreadSafeLRUCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive integer")
        self.capacity = capacity
        self.cache = OrderedDict()
        self.lock = threading.Lock() #-> All modifying operations (put, get, popitem) are wrapped in with self.lock
        
    def get(self, key):
        """retrieve the value and mark as recently used."""
        with self.lock:
            if key not in self.cache:
                return None
            self.cache.move_to_end(key) #-> move key to the end (most recently used)
            return self.cache[key]
        
    def put(self, key, value):
        """need to insert or update a key."""
        with self.lock:
            if key in self.cache:
                
        
def worker(cache, tid):
    for i in range(7):
        key = f"{tid}-{i}"
        val = cache.get(key)
        print (f"thread-{tid}-id:{i} : {val}")
        
    
#cache object
cache = ThreadSafeLRUCache(capacity=5)

#thread creation:
threads = [threading.Thread(target=worker, args=(cache, id_)) for id_ in range(4)]
for thread_obj in threads: 
    thread_obj.start()
    
for thread_obj in threads:
    thread_obj.join()
    
print (f"Final cache: {cache}")

    
                
        