"""
    File:               Arena.py
    Associated Files:   Character.py
    Packages Needed:    random, time
    Date Created:       7/15/2020
    Author:             John Lukowski
    Date Modified:      7/16/2020 by John Lukowski
    Modified By:        John Lukowski
    License:            CC-BY-SA-4.0

    Purpose:            Run a simple gladiator style arena between student submitted characters. Used to help teach classes.
"""

# imports
from Character import *
from time import sleep

# Base variables for the arena
nameLength = 0
delay = .2
battles = 0

# Initialize the fighters, One for each student, using their classes
players = [Player("Tux"), Barbarian("Owen"), Rogue("LaVoe"), healer("Demetri"), Assassin('Ryan'), Boss('Big Baddie')]
# nerf some of the fighters if the students got super crazy with the stats, buff them if they are super low
for player in players:
    if not 25 <= player.health <= 100:
        player.health = 45 + rand.randint(-10,10)
    if not 10 <= player.damage <= 25:
        player.damage = 20 + rand.randint(-5,5)
    if len(player.name) > nameLength:
        nameLength = len(player.name)

# Game loop, run while there is more than one player left in the arena
while len(players) > 1:
    battles += 1
    print("\nRound:",battles)

    player = rand.choice(players)       # pick a random player
    while True:
        enemy = rand.choice(players)    # pick a random enemy that isn't player
        if enemy.name != player.name:
            break
    # Have player fight enemy, then enemy fight back if it is alive
    print(player.name, 'vs', enemy.name)
    print(player.name, 'dealt', player.fight(enemy), 'damage to', enemy.name)
    if enemy.isAlive():
        print(enemy.name,'dealt', enemy.fight(player), 'damage to', player.name)

    sleep(delay)

    # Loop through and print out the status of all players
    print()
    for i in range(len(players)-1,-1,-1):
        player = players[i]
        if player.isAlive():
            print(player.name.ljust(nameLength+1,' '), ':', str(player.health), 'health')
        else:
            print(player.name.ljust(nameLength+1,' '), ':', 'has been eliminated!')
            players.remove(player)  # Player is no longer alive, remove it from the list of players in the arena
        sleep(delay)    # Delays, gives a scrolling effect

# Only one player is left, they are the winner
print('\n' + players[0].name + '\'s the winner!')