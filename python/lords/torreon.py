#!/usr/bin/python
#
# Just a python to make some calculations about an iphone game

class Resource(object):
  def __init__ (self, wood=0, stone=0, ore=0):
    self.wood = wood
    self.stone = stone
    self.ore = ore
  
  def __add__(self, other):
    self.wood  += other.wood
    self.stone += other.stone
    self.ore   += other.ore
    return self

  def __sub__(self, other):
    self.wood  -= other.wood
    self.stone -= other.stone
    self.ore   -= other.ore
    return self

  def __str__(self):
    return "(%d, %d, %d)" % (self.wood, self.stone, self.ore)

  def total(self):
    return self.wood + self.stone + self.ore

class Keep(object):
  def __init__(self):
    self.SCHANGE = 0
    self.COST = 1
   
    self.level = [
      (0, Resource()),
      (90, Resource(48,   38,   9)),
      (85, Resource(94,   77,   19)),
      (80, Resource(180,  152,  39)),
      (75, Resource(336,  292,  76)),
      (70, Resource(612,  547,  143)),
      (65, Resource(1084, 996,  264)),
      (60, Resource(1867, 1764, 471)),
      (56, Resource(3121, 3034, 819)),
      (53, Resource(5063, 5063, 1381)),
      (50, Resource(7963, 8193, 2255))
    ]
    self.current_level = 1

  def resorces2silver(self, resources):
    """ Change the given resources amount to silver. The type of resources 
    doesn't mother because the change is the same to all of them """
    return resources / self.level[self.current_level][0]

  def silver2resources(self, silver):
    """ Given a desired amount of silver, it return the resources it will 
    take to have it """
    return silver * self.level[self.current_level][0]

  def cost(self, target_level):
    """ Returns the cost in resources to go to target_level """
    r = Resource()
    for i in range(self.current_level + 1, target_level + 1):
      r += self.level[i][self.COST]
    
    return r


tsilver = 5000
k = Keep()
levels = range(1, 11)

for i in levels:
  r = k.cost(i)
  k.current_level = i
  print("Level %d: %d" % (i, r.total() + k.silver2resources(tsilver)))
