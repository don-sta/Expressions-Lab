# ETTG 1801
# Donald Stapleton
# Lab02 Expressions
# Date: 09/11/2020
print(' _____________')
print('|   __    __  |')
print('|  |__|  |__| |')
print('\      \/     /')
print(' |_|_|_|_|_|_|')
# This one is supposed to be a skull
print('  _____\n_|_____|_\n ( o.o ) \n  ~| |~\n  _| |_')
# And this is a man in a top hat. Yeah, he looks weird.
maxHealth = int(input("Welcome to the Salty Spitoon, how tough are ya? \n(This value affects your maximum health.) "))
print("Are you alright? That was a nasty fall you just took! "
      "Huh? 2020? Taco Bell Menu Change? Global pandemic? It's still 2019!\nAnyway, on a scale of "
      "0-" + str(maxHealth), "how do you feel?")
currentHealth = int(input('(This value affects your current health.) '))
print("Now how many characters wide is your health bar display?")
barLength = int(input('(This value affects your health bar length. ) '))
healthLength = (currentHealth/maxHealth)*barLength
healthLengthact = int(healthLength)
print('['+'v' * barLength+']')
print('}'+'=' * healthLengthact+' ' * (barLength - healthLengthact)+'{')
print('['+'^' * barLength+']')
input('(Press enter to see percentage.) ')
print('You are at', (currentHealth/maxHealth)*100, 'percent health!')
input('(Press enter to end.) ')
