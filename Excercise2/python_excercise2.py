# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.
length = 92
breadth = 48.8
area = length * breadth
print(round(area))


# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

tpotato = 9
epacket = 1.49
toshopkeeper = 20

totaldollar = tpotato * epacket
shopkeeperreturn = toshopkeeper - totaldollar
print(round(shopkeeperreturn))


# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)
tileslength = 5.5
squaretiles = tileslength ** 2
tilecost = 500
tileslcost = tilecost * squaretiles
print(round(tileslcost))



# 4. Print binary representation of number 17