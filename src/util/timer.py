import time


class Timer:
    def __init__(self, period, func, *args):
        self.period = period
        self.func = func
        self.args = args

        self.started = False

    def start(self):
        if not self.started:
            self.delay = self.period
            self.starttime = time.time()
            self.started = True

    def stop(self):
        self.delay = None
        self.started = False

    def update(self):
        if self.started:
            self.delay -= time.time() - self.starttime
            self.starttime = time.time()
            if self.delay < 0:
                self.func(*self.args)
                self.stop()
