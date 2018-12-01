###############################
'''print('''
DONE command completes your shopping list
SHOW command prints out your current shopping list
HELP command explains all functions''')'''

###################################
def squared(argument):
    try:
        num = int(argument)
    except ValueError:
        return argument * len(argument)
    else:
        return num * num

###################################### 12/1/18
class RaceCar:
    laps = 0

    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.laps = 0
        self.fuel_remaining = fuel_remaining
        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.laps += 1
        self.fuel_remaining -= length * 0.125
        
##########################################
