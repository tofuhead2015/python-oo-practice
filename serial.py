"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=100):
        """
        constructor function that takes an initial starting number
        """
        self.start = start
        self.current = start

    def __repr__(self):
        return "Serial Number Generator with starting seed = " + str(self.start)

    def __str__(self):
        return "Serial Number Generator with starting seed = " + str(self.start)

    def generate(self):
        """
        generates the next number
        """
        self.current += 1
        return self.current - 1

    def reset(self):
        """
        resets the current number to the start number
        """
        self.current = self.start

serial = SerialGenerator()

print(serial.generate())

print(serial.generate())

print(serial.reset())

print(serial.generate())

print(str(serial))



