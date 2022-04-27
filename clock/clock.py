MINUTES_PER_DAY = 24*60
class Clock:
    def __init__(self, hour, minute):
        self.minutes = (hour*60 + minute) % MINUTES_PER_DAY
    def __repr__(self):
        h, m = self._parse()
        return f"Clock({h}, {m})"
    def __str__(self):
        h, m = self._parse()
        return f"{h:02}:{m:02}"
    def _parse(self):
        h = self.minutes // 60
        m = self.minutes % 60
        return h, m
        
    def __eq__(self, other):
        return self.minutes == other.minutes
    def __add__(self, minutes):
        return Clock(0, self.minutes + minutes)
    def __sub__(self, minutes):
        return Clock(0, self.minutes - minutes)