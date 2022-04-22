import time

class StopWatch:
    def __init__(self, start=True):
        self._current_time = 0.0
        if start:
            self._is_working = True
            self._start_time = time.time()
        else:
            self._is_working = False
            self._start_time = 0

    def start(self, reset=True):
        if self._is_working: return
        if reset: self._current_time = 0.0
        self._is_working = True
        self._start_time = time.time()

    def stop(self):
        if not self._is_working: return
        self._current_time += time.time() - self._start_time
        self._is_working = False

    def reset(self):
        self._current_time = 0.0
        self._start_time = 0.0
        self._is_working = False

    def prints(self):
        if self._is_working: self._current_time += time.time() - self._start_time
        print(f"time : {self._current_time} seconds.")
        self._start_time = time.time()
