# Find Cost of Tile to Cover W x H Floor
# Calculate the total cost of tiling it would take to cover a floor plan of width and height, using a cost per tile entered by the user.

# Note: General convention while buying tiles is cost per sq foot, so we will use foot as the standard input unit. Also
# using int for sake of it.


def calcArea(b, l): 
    return b*l

def calcCost(aT, aF, costPerTile):
    return float((aF/aT)*costPerTile)

print("\n\t\tTile Cost Calculator\n")

print("Please enter floor plan details:")
bF = int(input("\n\tEnter breadth of the floor: "))
lF =int(input("\n\tEnter length of the floor: "))

print("\nPlease enter tile details:")
bT = int(input("\n\tEnter breadth of the tile: "))
lT = int(input("\n\tEnter length of the tile: "))
costPerTile = int(input("\n\tEnter cost per tile: INR "))

areaFloor = calcArea(bF, lF)
areaTile = calcArea(bT, lT)

print("\nTotal cost for the tiling a floor of area - "+str(areaFloor)+" sq ft with a tile of area - "+str(areaTile)+" sqft will be = INR "+str(calcCost(areaTile, areaFloor, costPerTile)))
print() # because asthetics!
