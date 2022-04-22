import time

class StopWatch:
    def __init__(self, start=True):
        self._current_time = 0.0
        self._start = 0.0
        self._is_working = False
        if start: self.start()

    def start(self, reset=False):
        if reset: self.reset()
        if not self._is_working:
            self._start = time.time()
            self._is_working = True

    def stop(self):
        if self._is_working:
            self._current_time += time.time() - self._start
            self._is_working = False

    def reset(self):
        self._current_time = 0.0
        self._is_working = False

    def prints(self, stop=True):
        if stop: self.stop()
        print(f"time : {self._current_time} seconds.")
