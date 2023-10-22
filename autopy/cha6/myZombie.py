import zombiedice

class My_zombie:
    def __init__(self,name) -> None:
        # All zombie must have a name
        self.name = name
    
    def turn(self,gameStart):
        # gameStart is a dict with info about the current state of the game.
        # You can choose to ingnore it in your code

        diceRollResults = zombiedice.roll() # first roll
        """
        roll() returns a dictionary with keys 'brains','shotgun', and 'footstep'
        with how many rolls of each type there were.
        The 'rolls' key is a list of (color, icon) tuples with the exact roll 
        result information.
        Example of a roll() return value:
        {'brains':1, 'footsteps':1, 'shotgun':1 ,'rolls':[('yellow','brains'),('red','footsteps'),
        ('green',''shotgun)]}

        REPALCE THIS ZOMBIE CODE WITH YOUR OWM:
        """

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']

            if brains < 2:
                diceRollResults = zombiedice.roll() #roll again
            else:
                break

zombies = (zombiedice.examples.RandomCoinFlipZombie(name='Random'),
           zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
           zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 shotguns',minShotguns=2),
           zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 shotgun',minShotguns=2),
           My_zombie(name='My Zombie Bot'),
        #    Add any other zombie players here
           )
# Uncomment one of the following lines to run in CLI or web GUI mode:
zombiedice.runTournament(zombies=zombies,numGames=1000)
# zombiedice.runWebGui(zombies=zombies,numGames=1000)