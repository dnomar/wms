from dataclasses import dataclass
from datetime import datetime
from time import time

@dataclass
class Event:

    @property
    def occurred_on(self):
        return time()

    @property
    def event_name(self):
        return type(self).__name__