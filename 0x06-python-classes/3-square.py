<<<<<<< HEAD
#!/usr/bin/python3

"""Define a class Square."""
=======
 #!/usr/bin/python3

"""Defines a class Square"""
>>>>>>> 33545e5b6d1dc597ff5ae0aca4912665c83c89a8


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
