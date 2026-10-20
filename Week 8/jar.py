class Jar:
    def __init__(self, capacity=12):
        if not type(capacity) is int:
            raise ValueError("Capacity must be an integer")
        elif capacity < 0:
            raise ValueError("Capacity cannot be negative")    
        else:
            self._capacity = capacity
            self.size = 0

    def __str__(self):
        return self._size*"\U0001F36A"

    def deposit(self, n):
        if not type(n) is int:
            raise ValueError("Deposited amount must be an integer")
        elif n < 0:
            raise ValueError("Deposited amount cannot be negative")
        else:
            self.size = self._size + n
           

    def withdraw(self, n):
        if not type(n) is int:
            raise ValueError("Withdrawn amount must be an integer")
        elif n < 0:
            raise ValueError("Withdrawn amount be negative")
        else:
            self.size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if not type(size) is int:
            raise ValueError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size cannot be negative")
        elif size > self._capacity:
            raise ValueError("Size cant be more than capacity")
        else:
            self._size = size