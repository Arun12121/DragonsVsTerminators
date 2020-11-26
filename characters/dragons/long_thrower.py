from .thrower_dragon import ThrowerDragon


class LongThrower(ThrowerDragon):
    """A ThrowerDragon that only throws stones at Terminators at least 5 places away."""

    name = 'Long'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.1
    implemented = True  # Change to True to view in the GUI
    food_cost = 2
    armor = 1
    min_range = 5
    # END 2.1
