import time
class State:
    info = None
    frame = 0
    fps = 0.0
    is_up = False
    target_fps = 16
    _last_time = time.time()