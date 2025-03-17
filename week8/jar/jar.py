class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must possitive number.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Exceed capacity")
        self._size += n

    def withdraw(self, n):
        if self._size < n:
            raise ValueError("Not enough cookies in the jar.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
