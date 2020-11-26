from .scuba_thrower import ScubaThrower
from utils import terminators_win

class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    implemented = True  # Change to True to view in the GUI
    instantiated = False
    food_cost = 7
    # END 4.3

    def __init__(self, armor=1):
        # BEGIN 4.3
        super().__init__(armor)
        self.is_buffed = True
        if DragonKing.instantiated == False:
            DragonKing.instantiated = True
            self.is_imposter = False
        else:
            self.is_imposter = True
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.

        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        if self.is_imposter == True:
            self.reduce_armor(self.armor)
        else:
            super().action(colony)
            p = self.place
            p = p.exit
            while(p != None):
                if p.dragon != None:
                    if p.dragon.is_container == False and p.dragon.is_buffed == False:
                        p.dragon.damage = 2 * p.dragon.damage
                        p.dragon.is_buffed = True
                    elif p.dragon.is_container == False:
                        pass
                    elif p.dragon.is_buffed == True and p.dragon.contained_dragon == None:
                        pass
                    elif p.dragon.is_buffed == True and p.dragon.contained_dragon.is_buffed == True:
                        pass
                    elif p.dragon.is_buffed == True:
                        p.dragon.contained_dragon.damage *= 2
                        p.dragon.contained_dragon.is_buffed = True
                    else:
                        p.dragon.damage = 2 * p.dragon.damage
                        p.dragon.is_buffed = True
                        if p.dragon.contained_dragon != None and p.dragon.contained_dragon.is_buffed == False:
                            p.dragon.contained_dragon.damage *= 2
                            p.dragon.contained_dragon.is_buffed = True
                p = p.exit
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        super().reduce_armor(amount)
        if self.armor <= 0 and self.is_imposter == False:
            terminators_win()