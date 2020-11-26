from .bodyguard_dragon import BodyguardDragon


class TankDragon(BodyguardDragon):
    """TankDragon provides both offensive and defensive capabilities."""

    name = 'Tank'
    damage = 1
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 3.3
    implemented = True  # Change to True to view in the GUI
    is_container = True
    food_cost = 6

    def action(self, colony):
        # BEGIN 3.2
        if self.contained_dragon != None:
            self.contained_dragon.action(colony)
        k = self.place
        for target in k.terminators[:]:
            target.reduce_armor(self.damage)
        # END 3.2
