from victor import Victor
import gevent
from gevent import monkey; monkey.patch_all()
import time
def gameloop():
    while True:
        start = time.time()
        # Your code here (e.g., update game state, render, etc.)
        
        
        elapsed = time.time() - start
        sleep_time = max(0, (1/60) - elapsed)
        gevent.sleep(sleep_time)