from os import system
import readchar
from random import randint

NUM_OBJECTS = 10
 
POS_X, POS_Y = [3,1]

tail = []
tailLength = 0

obstacles = """\
###     ##########
#              ###
##            ####
#####       ######
#######             
##                
####       #######
###           ####
           #######
           #######
 #####      ######
             #####
###      ##########\
"""

mapObstacles = [ list(row) for row in obstacles.split("\n") ]

MAP_WIDTH = len(mapObstacles[0])
MAP_HEIGHT = len(mapObstacles)

def generateObjects(numObjects):
  mapObjects = []

  while len(mapObjects) < numObjects:
    x = randint(0,MAP_WIDTH - 1)
    y = randint(0,MAP_HEIGHT - 1)
    newObject = [x, y]
    if newObject not in mapObjects + [POS_X, POS_Y] and mapObstacles[y][x] != "#":
      mapObjects.append(newObject)

  return mapObjects


def createMap():
  global tailLength, tail, mapObjects

  print("+" + "-" * MAP_WIDTH * 3 + "+")

  for coordinate_y in range(MAP_HEIGHT):
    print("|", end="")
    for coordinate_x in range(MAP_WIDTH):

      charToDraw = " "
      objectInCell = None
      position = [coordinate_x, coordinate_y]

      try:
        objectInCell = mapObjects.index(position)
        charToDraw = "*"
      except: ""

      if coordinate_x == POS_X and coordinate_y == POS_Y or position in tail:
        charToDraw = "@"

        if objectInCell != None:
          del mapObjects[objectInCell]
          tailLength += 1
          mapObjects += (generateObjects(NUM_OBJECTS - len(mapObjects)))
      
      if mapObstacles[coordinate_y][coordinate_x] == "#":
        charToDraw = "#"

      print(f" {charToDraw} ", end="")

    print("|")

  print("+" + "-" * MAP_WIDTH * 3 + "+")

mapObjects = generateObjects(NUM_OBJECTS)

lasKey = ""

while True:
  system("clear")
    
  createMap()

  print("Press q to exit")

  direction = readchar.readchar()

  def createTail():
    global tail
    tail.insert(0, [POS_X, POS_Y])
    tail = tail[:tailLength]

  if direction == "w" and lasKey != "s":
    createTail()
    POS_Y -= 1
    POS_Y %= MAP_HEIGHT
    lasKey = "w"

  elif direction == "s" and lasKey != "w":
    createTail()
    POS_Y += 1
    POS_Y %= MAP_HEIGHT
    lasKey = "s"

  elif direction == "a" and lasKey != "d":
    createTail()
    POS_X -= 1
    POS_X %= MAP_WIDTH
    lasKey = "a"

  elif direction == "d" and lasKey != "a":
    createTail()
    POS_X += 1
    POS_X %= MAP_WIDTH
    lasKey = "d"

  elif direction == "q":
    break  

  if [POS_X, POS_Y] in tail[1:len(tail)] or mapObstacles[POS_Y][POS_X] == "#":
    print("[ Game Over ]")
    break
  
