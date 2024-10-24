#### 1. A table

# We define a table with how many seats it encompasses and we define the object in the `table.py` file

##### 1.1 Seat

# In `table.py`:

# Create a class called `Seat` with two attributes:

# - `free` which is a boolean.
# - `occupant` which is a string.

# and 2 functions : 

# - `set_occupant(name)` which allows the program to assign someone a seat if it's free
# - `remove_occupant()` which  remove someone from a seat and return the name of the person occupying the seat before

class Seat:
    
    """Class representing a seat with two attributes 'free' and 'occupant'"""

    def __init__(self, free, occupant):
        """Constructor"""
        self.free = free
        self.occupant = occupant

    def set_occupant(self, name):
        "function which allows the program to assign someone a seat"
        seats = []
        if self.free == True:
            seats.append(name)
        else:
            return "Sorry, this seat is occupied."
    
    def remove_occupant(self, seats):
        "function which removes someone from a seat and return the name of the person occupying the seat before"
        index_occupant = seats.index(self.occupant)
        seats.remove(self.occupant)
        seat_before = seats[index_occupant-1]
        return seat_before



##### 1.2 Table

# In the same file, create a class `Table` with ? attributes:

# - `capacity` which is an integer
# - `seats` which is a list of `Seat` objects (size = `capacity`)

# and 3 functions : 
# - `has_free_spot()` that returns a boolean (True if a spot is available)
# - `assign_seat(name)` that places someone at the table
# - `left_capacity()` that returns an integer

class Table:
    
    """Class representing a Table with attributes 'capacity' and 'seats'"""

    def __init__(self, capacity, seats):
        """Constructor"""
        self.capacity = capacity
        self.seats = seats

    def has_free_spot(self,spot):
        "function that returns a boolean (True if a spot is available)"
        
        if self.seats[spot] == str:
            return True
        else:
            return False
    
    def left_capacity(self):
        "function that returns capacity"

        capacity = len(self.seats)
        return capacity

