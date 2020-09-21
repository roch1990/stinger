import threading
from typing import Any, Optional


class ConcurrentCall:

    def __init__(self, name: str, target: Any):
        self.name: str = name
        self.target: Any = target
        self._thread: threading.Thread = None

    def start(self):
        self._thread = threading.Thread(name=self.name, target=self.target)
        self._thread.daemon = True
        self._thread.start()

    def status(self):
        return self._thread.is_alive()
