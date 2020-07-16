"""
    File:               Character.py
    Associated Files:   Arena.py
    Packages Needed:    random, time
    Date Created:       7/15/2020
    Author:             John Lukowski
    Date Modified:      7/16/2020 by John Lukowski
    Modified By:        John Lukowski
    License:            CC-BY-SA-4.0

    Purpose:            Run a simple gladiator style arena between student submitted characters.
                        Used to help teach students classes and reinforce methods/variables.
"""

# imports
import random as rand

"""
    Class:      Character
    Purpose:    Hold base character stats/methods for all fighters
    Methods:    fight, takeDamage, isAlive
"""
class Character:
    def __init__(self, name):
        # Default stats
        self.name = name
        self.health = 25 + rand.randint(0, 10)
        self.damage = 10 + rand.randint(0, 5)

    """
        Function:   fight
        Params:     other (Character)
        Purpose:    default deal damage to the opponent
        Returns:    amount of damage dealt
    """
    def fight(self, other):
        return other.takeDamage(self.damage)

    """
        Function:   takeDamage
        Params:     damage
        Purpose:    default take damage method
        Returns:    damage dealt
    """
    def takeDamage(self, damage):
        self.health -= damage
        return damage

    """
        Function:   isAlive
        Params:     
        Purpose:    default check health method
        Returns:    True if health > 0 else False
    """
    def isAlive(self):
        return self.health > 0
# END OF CHARACTER CLASS

"""
    Class:      Player
    Purpose:    Sample fighter class
    Methods:    takeDamage (Overridden)
"""
class Player(Character):
    def __init__(self, name):
        self.name = name
        self.health = 60 + rand.randint(0, 15)
        self.damage = 15 + rand.randint(0, 2)
        self.defense = rand.randint(2, 10)

    """
        Function:   takeDamage
        Params:     damage
        Purpose:    take damage, with added defense stat
        Returns:    damage dealt
    """
    def takeDamage(self, damage):
        damageTaken = (damage - self.defense)
        if damageTaken < 0:
            damageTaken = 0
        self.health -= damageTaken
        return damageTaken
# END OF PLAYER CLASS

"""
    Class:      Boss
    Purpose:    Sample fighter class
    Methods:    takeDamage (Overridden), fight (Overridden), levelUp
"""
class Boss(Character):
    def __init__(self, name):
        self.name = name
        self.health = 75
        self.hpThreshold = int(self.health/2)
        self.damage = 25 + rand.randint(-5,5)
        self.dodgeChance = rand.randint(20, 70)
        self.critChance = rand.randint(20,70)

    """
        Function:   takeDamage
        Params:     damage
        Purpose:    take damage, with added dodge chance and level up mechanic
        Returns:    damage dealt
    """
    def takeDamage(self, damage):
        if rand.randint(0, 100) < self.dodgeChance:
            print(self.name + " dodged the attack")
            return 0
        self.health -= damage
        if self.health <= self.hpThreshold:
            self.levelUp()
        return damage

    """
        Function:   fight
        Params:     other (Character)
        Purpose:    deal damage, with added critical hit mechanic
        Returns:    amount of damage dealt
    """
    def fight(self, other):
        damage = self.damage
        if rand.randint(0, 100) < self.critChance:
            print(self.name,'dealt a critical hit!')
            damage = self.damage*2
            if other.health <= damage:  # made so crits cannot one-shot
                damage = other.health - 1
        return other.takeDamage(damage)

    """
        Function:   levelUp
        Params:     
        Purpose:    increase stats and reset the level up threshold
        Returns:    
    """
    def levelUp(self):
        print(self.name,'has leveled up')
        self.hpThreshold = int(self.hpThreshold/2)
        self.damage += 5
        self.dodgeChance = rand.randint(20, 70)
        self.critChance = rand.randint(20,70)
        if 0 < self.health < self.hpThreshold:
            self.health = self.hpThreshold
# END OF BOSS CLASS

"""
    All student Character classes should go below this point, some are given as an example.
    They all need a name, health, damage, fight, takeDamage and isAlive. 
    These can either be inherited or overridden. Other functions may be added,
    but the arena code will only use the stats and 3 functions listed. Added
    functions/variables would have to be used within the class like in the Boss example.
    
    Please proofread/balance all student code as there is no error catching implemented
    and or students may try to make something completely overpowered.
"""

class Barbarian(Character):
  def __init__(self, name):
    self.health = 150
    self.damage = 50
    self.name = name

class Rogue(Character):
    def __init__(self, name):
        self.health = 65
        self.damage = 50
        self.name = name
        self.critChance = 15
        self.dodgeChance = 25

    def fight(self, other):
        if rand.randint(1, 101) <= self.critChance:
            damage = other.takeDamage(self.damage * 2)
            print("Crit")
            return damage
        else:
            damage = other.takeDamage(self.damage)
            return damage

    def takeDamage(self, damage):
        if rand.randint(1, 101) <= self.dodgeChance:
            print("Dodged")
            return 0
        else:
            self.health -= damage
            return damage

class healer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.damage = 12
        self.maxHealth = self.health

    def fight(self, other):
        if self.health < self.maxHealth-9:
            self.health += 10
            print(self.name, 'heals 10 hp.')
        return other.takeDamage(self.damage)

class Assassin(Player):
    def fight(self, other):
        if rand.randint(0, 100) <= 28:
            return other.takeDamage(self.damage * 2)
        return other.takeDamage(self.damage)
